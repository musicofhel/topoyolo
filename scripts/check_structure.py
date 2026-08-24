#!/usr/bin/env python3
"""Structure lint for topo-rosetta (stdlib only).

Checks:
  1. every full annotation in papers/inbox.md / inbox-archive.md is
     referenced in >=1 papers/by-domain/ file AND >=1 papers/by-structure/ file
  2. every relative markdown link in the repo resolves to an existing file
  3. claimed counts (papers / cells) agree across README.md, docs/index.html,
     diagrams/coverage-matrix.md (exact agreement with the real corpus count
     is a warning, not an error)
  4. no annotation header appears twice

Errors -> exit 1. Warnings are printed but do not fail the run.
Run from anywhere: paths are resolved relative to the repo root.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

INBOX_FILES = [ROOT / "papers/inbox.md", ROOT / "papers/inbox-archive.md"]
DOMAIN_DIR = ROOT / "papers/by-domain"
STRUCTURE_DIR = ROOT / "papers/by-structure"
COUNT_FILES = [
    ROOT / "README.md",
    ROOT / "docs/index.html",
    ROOT / "diagrams/coverage-matrix.md",
]

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
    """Parse annotation headers out of the two inbox files."""
    annotations = []          # (loc, body, hard_key, soft_key)
    seen_headers = {}         # normalized header -> first location
    for path in INBOX_FILES:
        if not path.exists():
            v.warn(f"inbox file missing: {path.relative_to(ROOT)}")
            continue
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


def check_counts(n_ann, v):
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
                    detail = ", ".join(f"{k}: {sorted(v)}" for k, v in vals.items())
                    v.err(f"{metric} count disagreement across sources -> {detail}")

    # corpus truth vs claims (warning only)
    claimed = set().union(*[c["papers"] for c in per_file.values()]) if per_file else set()
    for c in sorted(claimed):
        if c != n_ann:
            v.warn(
                f"claimed count {c} papers != {n_ann} annotation headers found in "
                f"inbox.md + inbox-archive.md"
            )


def main():
    v = Violations()

    annotations = collect_annotations(v)
    texts = index_texts()
    n_ann = check_coverage(annotations, texts, v)
    n_md, n_broken = check_links(v)
    check_counts(n_ann, v)

    print(f"topo-rosetta structure lint")
    print(f"  annotations parsed : {n_ann}")
    print(f"  index files scanned: {len(texts)}")
    print(f"  markdown files     : {n_md}")
    print()
    for w in v.warnings:
        print(f"WARN  {w}")
    for e in v.errors:
        print(f"ERROR {e}")
    print()
    print(f"{len(v.errors)} errors, {len(v.warnings)} warnings")
    return 1 if v.errors else 0


if __name__ == "__main__":
    sys.exit(main())
