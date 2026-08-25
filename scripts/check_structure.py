#!/usr/bin/env python3
"""Structure lint for topo-rosetta (stdlib only).

Checks:
  1. every full annotation in papers/annotations/*.md, papers/inbox.md and
     papers/inbox-archive.md is referenced in >=1 papers/by-domain/ file AND
     >=1 papers/by-structure/ file
  2. every relative markdown link in the repo resolves to an existing file
  3. claimed counts (papers / cells) agree across README.md, docs/index.html,
     diagrams/coverage-matrix.md (exact agreement with the real corpus count
     is a warning, not an error)
  4. no annotation header appears twice
  5. per-paper layout (A3): each file in papers/annotations/ holds exactly one
     "<id> --- <authors>" annotation header at the top of its body

Errors -> exit 1. Warnings are printed but do not fail the run.

  --check   also derive stats via scripts/gen_stats.py and FAIL if
            diagrams/coverage-matrix.md or the headline counts in
            README.md / docs/index.html drift from the annotations.

Run from anywhere: paths are resolved relative to the repo root.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

INBOX_FILES = [ROOT / "papers/inbox.md", ROOT / "papers/inbox-archive.md"]
ANNOTATION_DIR = ROOT / "papers/annotations"
DOMAIN_DIR = ROOT / "papers/by-domain"
STRUCTURE_DIR = ROOT / "papers/by-structure"
COUNT_FILES = [
    ROOT / "README.md",
    ROOT / "docs/index.html",
]
MATRIX_FILE = ROOT / "diagrams/coverage-matrix.md"

# Annotation header: "## <id> --- <authors>" (inbox) or "## <id> — <authors>"
# (archive). Either dash style separates id from authors.
HEADER_RE = re.compile(r"^##(?!#)\s*(.+?)\s*(?:---|—)\s+(.+)$")
H2_RE = re.compile(r"^##(?!#)\s*(.+)$")
WAVE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}|^Wave\b", re.IGNORECASE)
MODERN_ARXIV_RE = re.compile(r"\b(\d{4}\.\d{4,5})\b")
OLD_ARXIV_RE = re.compile(r"\b((?:[a-z]+-)?[a-z]+/\d{7})\b")
DOI_RE = re.compile(r"\bDOI:?\s*([^\s(—-]+)", re.IGNORECASE)
YEAR_RE = re.compile(r"\((\d{4})(?:/\d{4})?\)")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
MD_LINK_RE = re.compile(r"\]\(([a-zA-Z0-9_./-]+)(#[^)]*)?\)")


class Violations:
    def __init__(self):
        self.errors = []
        self.warnings = []

    def err(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warnings.append(msg)


def paper_key(header_text):
    """Extract a machine-matchable key from an annotation header line.

    Preference order: arXiv id (new or legacy), bare identifier token
    (DOI / publisher slug with no internal whitespace, e.g. "10.1371/
    journal.pcbi.1002581", "s42005-021-00605-4", "eLife.03476"),
    first-author surname + year. Anything else is unmatchable and is
    surfaced as a warning by the caller.
    """
    m = MODERN_ARXIV_RE.search(header_text)
    if m:
        return ("id", m.group(1))
    m = OLD_ARXIV_RE.search(header_text)
    if m:
        return ("id", m.group(1))
    ident = re.split(r"\s*(?:---|—)\s*", header_text)[0].strip()
    for prefix in ("arXiv:", "arXiv ", "DOI:", "DOI ", "doi:"):
        if ident.lower().startswith(prefix.lower()):
            ident = ident[len(prefix):].strip()
    if ident and not re.search(r"\s", ident):
        return ("id", ident.rstrip(".,;"))
    # No explicit id: fall back to first capitalized word + year, e.g.
    # "## Rosas, Mediano, ... (2020)". Fragile by design — flagged below.
    return None  # no explicit identifier anywhere in the header


def collect_annotations(v):
    """Parse annotation headers out of the per-paper files + the two inboxes."""
    annotations = []          # (loc, body, hard_key, soft_key)
    seen_headers = {}         # normalized header -> first location
    per_paper = sorted(ANNOTATION_DIR.glob("*.md")) if ANNOTATION_DIR.exists() else []
    for path in per_paper + INBOX_FILES:
        if not path.exists():
            v.warn(f"inbox file missing: {path.relative_to(ROOT)}")
            continue
        n_here = 0
        for i, line in enumerate(path.read_text().splitlines(), 1):
            s = line.rstrip()
            if not s.startswith("##"):
                continue
            body = s.lstrip("#").strip()
            m = HEADER_RE.match(s)
            if not m:
                # Not a "<id> --- <authors>" header. Wave/section headings are
                # expected; a paper-looking h2 without a separator is debt.
                hm = H2_RE.match(s)
                if hm and not WAVE_RE.match(hm.group(1)):
                    if MODERN_ARXIV_RE.search(body) or OLD_ARXIV_RE.search(body):
                        v.warn(
                            f"{path.relative_to(ROOT)}:{i}: ## heading looks like "
                            f"a paper but lacks the '<id> --- <authors>' separator: {body[:70]}"
                        )
                continue
            if WAVE_RE.match(m.group(1)) or WAVE_RE.match(m.group(2)):
                continue  # wave/section heading, not an annotation
            norm = re.sub(r"\s+", " ", m.group(1)).lower()
            loc = f"{path.relative_to(ROOT)}:{i}"
            if norm in seen_headers:
                v.err(
                    f"duplicate annotation header '{m.group(1)[:60]}' at {loc} "
                    f"(first seen at {seen_headers[norm]})"
                )
            else:
                seen_headers[norm] = loc
            hard = paper_key(m.group(1))
            annotations.append((loc, body, hard or ("none", ""), soft_key(m.group(2) or "")))
            n_here += 1
        if path in per_paper:
            rel = path.relative_to(ROOT)
            if n_here == 0:
                v.err(f"{rel}: per-paper annotation file has no '<id> --- <authors>' header")
            elif n_here > 1:
                v.err(f"{rel}: per-paper annotation file holds {n_here} annotations (expected 1)")
    return annotations


def index_texts():
    texts = {}
    for d in (DOMAIN_DIR, STRUCTURE_DIR):
        if not d.exists():
            continue
        for p in sorted(d.glob("*.md")):
            texts[p] = p.read_text()
    return texts


def check_coverage(annotations, texts, v):
    """annotations: list of (loc, body, hard_key, soft_key).

    hard_key is an explicit identifier (arXiv/DOI/slug); soft_key is the
    first-author-surname+year fallback, because index entries frequently cite
    papers by prose ("Full annotation: inbox.md", "**Author (year)**") rather
    than by id. A paper counts as referenced if EITHER matches; matching on
    the soft key alone is noted so exact-id crossrefs can be tightened later.
    """
    domain_blobs = {p: t for p, t in texts.items() if DOMAIN_DIR in p.parents}
    struct_blobs = {p: t for p, t in texts.items() if STRUCTURE_DIR in p.parents}

    def find(key, blobs):
        kind, val = key
        for p, t in blobs.items():
            if kind == "nameyear":
                # val is (list_of_candidate_surnames, year): match if any
                # candidate surname co-occurs with the year in one file.
                names, year = val
                if any(n in t for n in names) and year in t:
                    return p.name
            elif val.lower() in t.lower():
                return p.name
        return None

    n_loose = 0
    for loc, body, hard, soft in annotations:
        for side, blobs in (("by-domain/", domain_blobs), ("by-structure/", struct_blobs)):
            hit = find(hard, blobs)
            tier = "id"
            if hit is None and soft[0] != "none":
                hit = find(soft, blobs)
                tier = "author-year"
            if hit is None:
                v.err(f"{loc}: annotation NOT referenced in any {side} file "
                      f"(looked for id={hard[1]}, author-year={soft[1]})")
            elif tier == "author-year":
                n_loose += 1
    if n_loose:
        v.warn(f"{n_loose} annotation<->index references matched only by author-year "
               f"prose, not by a shared id (crossref debt)")
    return len(annotations)


def soft_key(header_text):
    words = re.findall(r"\b[A-Z][a-z’']{2,}", header_text)
    y = YEAR_RE.search(header_text)
    if words and y:
        return ("nameyear", (words, y.group(1)))
    return ("none", "")


def check_links(v):
    md_files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    broken = 0
    for p in md_files:
        rel = p.relative_to(ROOT)
        for i, line in enumerate(p.read_text().splitlines(), 1):
            for target, _anchor in MD_LINK_RE.findall(line):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                # Skip prose false positives like `K[g](w)` — only path-like
                # targets (containing a slash or dot) count as links.
                if "/" not in target and "." not in target:
                    continue
                resolved = (p.parent / target).resolve()
                if not resolved.exists():
                    v.err(f"{rel}:{i}: broken markdown link -> {target}")
                    broken += 1
    return len(md_files), broken


def extract_counts(text):
    """Return {'papers': {...}, 'ge4': {...}, 'ge10': {...}} claim sets."""
    claims = {"papers": set(), "ge4": set(), "ge10": set()}
    for m in re.finditer(r"~?(\d{2,4})\+?(?:\s+(?:annotated\s+|unique\s+))?papers", text):
        claims["papers"].add(int(m.group(1)))
    for m in re.finditer(r"(\d+)\+?\s*cells?[^\n.]{0,25}?≥\s*(\d+)", text):
        n, k = int(m.group(1)), int(m.group(2))
        if k == 4:
            claims["ge4"].add(n)
        elif k == 10:
            claims["ge10"].add(n)
    return claims


def check_counts(v):
    """Cross-file agreement of the headline paper-count claims (README vs
    docs/index.html). The corpus-truth comparison lives in
    check_stats_drift, which derives the real number from the annotations."""
    per_file = {}
    for p in COUNT_FILES:
        if not p.exists():
            v.warn(f"count source missing: {p.relative_to(ROOT)}")
            continue
        per_file[p.relative_to(ROOT)] = extract_counts(p.read_text())

    for metric in ("papers", "ge4", "ge10"):
        vals = {}
        for fname, claims in per_file.items():
            if claims[metric]:
                vals[fname] = claims[metric]
        if len(vals) < 2:
            continue  # only one source makes the claim; nothing to disagree with
        names = list(vals)
        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                if vals[names[i]] != vals[names[j]]:
                    detail = ", ".join(f"{k}: {sorted(x)}" for k, x in vals.items())
                    v.err(f"{metric} count disagreement across sources -> {detail}")
    return per_file


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def derived_stats():
    """Import gen_stats (scripts/, stdlib only) and derive corpus truth."""
    sys.path.insert(0, str(ROOT / "scripts"))
    from gen_stats import derive, render_matrix

    papers, matrix, notes = derive()
    machines = sorted(next(iter(matrix.values())).keys()) if matrix else []
    min_cell = min(matrix[d][c] for d in matrix for c in machines) if matrix else 0
    n_deep = sum(1 for d in matrix for c in machines if matrix[d][c] >= 10)
    return papers, n_deep, min_cell, render_matrix(papers, matrix), notes


def check_stats_drift(v):
    """A4: claimed stats must equal the numbers derived from
    papers/annotations/ by scripts/gen_stats.py."""
    try:
        papers, n_deep, min_cell, rendered, notes = derived_stats()
    except ImportError as e:
        v.warn(f"cannot import scripts/gen_stats.py — stats drift unchecked ({e})")
        return None
    for note in notes:
        v.warn(f"gen_stats: {note}")

    if MATRIX_FILE.exists():
        current = MATRIX_FILE.read_text()
        if current.strip() != rendered.strip():
            v.err("diagrams/coverage-matrix.md is out of date with "
                  "papers/annotations/ — run: python3 scripts/gen_stats.py")
    else:
        v.err("diagrams/coverage-matrix.md missing (gen_stats.py should emit it)")

    # each prose surface must carry the derived headline paper count
    for p in COUNT_FILES:
        txt = strip_tags(p.read_text())
        if not re.search(rf"\b{papers}\b\s+fully annotated papers|\b{papers}\s+papers\b", txt):
            v.err(f"{p.relative_to(ROOT)}: does not state the derived count "
                  f"({papers} fully annotated papers)")
    return papers, n_deep, min_cell


LAYOUT_CONTRACT = ROOT / "papers/README.md"


def check_papers_layout(v):
    """A5 layout contract: every entry directly under papers/ must be named
    in papers/README.md (backtick-quoted), so no file can become
    undocumented."""
    if not LAYOUT_CONTRACT.exists():
        v.warn("papers/README.md missing — papers/ layout contract unchecked")
        return 0
    readme = LAYOUT_CONTRACT.read_text()
    n = 0
    for entry in sorted((ROOT / "papers").iterdir()):
        name = entry.name
        if name.startswith(".") or entry == LAYOUT_CONTRACT:
            continue  # the contract documents itself by existing
        # directories may be documented with or without the trailing slash
        if f"`{name}`" not in readme and f"`{name}/`" not in readme:
            v.err(f"papers/{name} is not documented in papers/README.md "
                  f"(papers/ layout contract)")
        else:
            n += 1
    return n


def check_inbox_empty(v):
    """A3 layout: inbox files are pointer-lists only — zero full annotations."""
    n_total = 0
    for p in INBOX_FILES:
        if not p.exists():
            continue
        n = 0
        for i, line in enumerate(p.read_text().splitlines(), 1):
            m = HEADER_RE.match(line)
            if m and not WAVE_RE.match(m.group(1)) and not WAVE_RE.match(m.group(2)):
                n += 1
                if n == 1:
                    v.err(f"{p.relative_to(ROOT)}:{i}: full annotation still in inbox "
                          f"(migrate to papers/annotations/): {line.lstrip('# ')[:60]}")
        n_total += n
    return n_total


def main(argv):
    check = "--check" in argv
    v = Violations()

    annotations = collect_annotations(v)
    n_layout = check_papers_layout(v)
    n_inbox = check_inbox_empty(v)
    texts = index_texts()
    n_ann = check_coverage(annotations, texts, v)
    n_md, n_broken = check_links(v)
    check_counts(v)
    stats = check_stats_drift(v) if check else None

    print(f"topo-rosetta structure lint")
    print(f"  annotations parsed : {n_ann}")
    print(f"  papers/ entries    : {n_layout} documented in layout contract")
    print(f"  index files scanned: {len(texts)}")
    print(f"  markdown files     : {n_md}")
    if stats:
        papers, n_deep, min_cell = stats
        print(f"  derived stats      : {papers} papers, {n_deep}/30 cells >=10, "
              f"min cell {min_cell} (--check)")
    print()
    for w in v.warnings:
        print(f"WARN  {w}")
    for e in v.errors:
        print(f"ERROR {e}")
    print()
    print(f"{len(v.errors)} errors, {len(v.warnings)} warnings")
    return 1 if v.errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
