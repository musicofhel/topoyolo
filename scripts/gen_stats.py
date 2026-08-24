#!/usr/bin/env python3
"""Derive atlas statistics from papers/annotations/*.md (stdlib only).

Parses each per-paper annotation for its Domain(s) line and the machine
bullets under "Abstract machines instantiated", then:

  * prints headline numbers (papers, cells, min cell, deep cells)
  * rewrites diagrams/coverage-matrix.md from the derived data

This is the single source of truth for coverage counts. check_structure.py
--check recomputes the same numbers and fails if any claimed stat drifts.

Run from anywhere: paths resolve relative to the repo root.
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ANNOTATION_DIR = ROOT / "papers/annotations"
MATRIX_PATH = ROOT / "diagrams/coverage-matrix.md"

# Canonical domains, in matrix row order.
DOMAINS = ["TDA", "QEC", "Dynamics", "Neuro", "InfoTheo"]

# Prose -> canonical domain. First token of each comma/slash-separated
# Domain(s) entry, lowercased, must match a key here; anything else is
# reported as unrecognized and ignored.
DOMAIN_ALIASES = {
    "tda": "TDA",
    "qec": "QEC",
    "quantum": "QEC",
    "dynamical": "Dynamics",
    "neuroscience": "Neuro",
    "information": "InfoTheo",
}

# Canonical machines, in matrix column order, with the bullet-label prefix
# each maps to. Qualifiers like "(weak)"/"(inverted direction)" are stripped
# before matching.
MACHINES = [
    ("Chain complex", "Chain complex"),
    ("Parameterized homology", "Parameterized homology"),
    ("Matching", "Matching"),
    ("Stability", "Stability"),
    ("Joint-vs-marginal excess", "Joint-vs-marginal"),
    ("Null hypothesis", "Null hypothesis"),
]

MATRIX_HEADER = """# Coverage Matrix — 6 Machines × 5 Domains

Updated: {updated} (derived by scripts/gen_stats.py from papers/annotations/)

## Paper Counts

"""
MATRIX_FOOTER = """
## Legend

- **Bold/green cells** (≥10): Deep coverage — multiple independent instantiations documented
- All other cells: Adequate coverage (<10)

Counts cover papers with full annotations under `papers/annotations/`
(one file per paper). Index stubs without a full annotation are not counted.
Regenerate with `python3 scripts/gen_stats.py`; `check_structure.py --check`
fails if these numbers drift from the claims in README.md / docs/index.html.
"""


def normalize_domain(raw):
    """First word of a domain mention -> canonical name or None."""
    word = re.split(r"[^A-Za-z]", raw.strip(), maxsplit=1)[0].lower()
    return DOMAIN_ALIASES.get(word)


def split_domains(line):
    """Split '**Domain(s)**: TDA, dynamical systems' into canonical names."""
    _, _, rest = line.partition("**:")
    out = set()
    unknown = []
    for part in re.split(r"[,/]| \(|\)|;", rest):
        d = normalize_domain(part)
        if d:
            out.add(d)
        elif part.strip():
            unknown.append(part.strip())
    return out, unknown


def parse_machines(lines):
    """Collect canonical machine names from the 'Abstract machines
    instantiated' bullet block of one annotation."""
    out = set()
    in_block = False
    for line in lines:
        if not in_block:
            if "abstract machines instantiated" in line.lower():
                in_block = True
            continue
        if not line.strip():
            continue  # blank lines occur inside the bullet block
        if not line.startswith("- "):
            break  # end of bullet block
        m = re.match(r"^-\s+\*\*([^*]+)\*\*", line)
        if m:
            label = re.sub(r"\s*\([^)]*\)", "", m.group(1)).strip().lower()
            for canon, _disp in MACHINES:
                if label == canon.lower():
                    out.add(canon)
    return out


def derive():
    """-> (papers, matrix, per_file_notes). papers: int; matrix[domain][machine] = count."""
    matrix = {d: defaultdict(int) for d in DOMAINS}
    papers = 0
    notes = []
    for path in sorted(ANNOTATION_DIR.glob("*.md")):
        lines = path.read_text().splitlines()
        dom_line = next((l for l in lines
                         if l.startswith("**Domain(s)**") or l.startswith("**Domain**:")), None)
        if dom_line is None:
            notes.append(f"{path.name}: no '**Domain(s)**' line — skipped")
            continue
        domains, unknown = split_domains(dom_line)
        if unknown:
            notes.append(f"{path.name}: unrecognized domain(s): {', '.join(unknown)}")
        machines = parse_machines(lines)
        if not machines:
            notes.append(f"{path.name}: no recognizable machine bullets — domain counts skipped")
            continue
        papers += 1
        for d in domains:
            for mch in machines:
                matrix[d][mch] += 1
    return papers, matrix, notes


def cell_label(n, deep=False):
    return f"**{n}**" if deep else str(n)


def render_matrix(papers, matrix, updated="2026-08-24"):
    cols = [disp for _, disp in MACHINES]
    short = ["ChainCmplx", "ParamHom", "Matching", "Stability",
             "JointMarg", "NullHyp"]
    width = max(len(s) for s in short) + 2
    n_deep = sum(1 for d in DOMAINS for c, _ in MACHINES if matrix[d][c] >= 10)
    min_cell = min(matrix[d][c] for d in DOMAINS for c, _ in MACHINES)

    out = MATRIX_HEADER.format(updated=updated)
    out += "```\n"
    out += f"{'':14}" + "".join(f"{s:>{width}}" for s in short) + "\n"
    out += "─" * (14 + width * len(short)) + "\n"
    for d in DOMAINS:
        row = f"{d:14}"
        for c, _ in MACHINES:
            n = matrix[d][c]
            row += f"{('*' + str(n) + '*' if n >= 10 else str(n)):>{width}}"
        out += row + "\n"
    out += "```\n"
    out += "\n(`*n*` marks deep cells ≥10.)\n"

    out += "\n## Mermaid Heatmap\n\n```mermaid\n"
    out += "%%{init: {'theme': 'base', 'themeVariables': {'fontSize': '14px'}}}%%\nblock-beta\n  columns 7\n\n  space:1 "
    ids = ["CC", "PH", "MA", "ST", "JM", "NH"]
    out += " ".join(f'{i}["{l.replace(chr(10), chr(92) + "n")}"]'
                    for i, l in zip(ids, short)) + "\n\n"
    for d in DOMAINS:
        did = {"TDA": "TDA", "QEC": "QEC", "Dynamics": "DYN",
               "Neuro": "NEU", "InfoTheo": "IT"}[d]
        cells = []
        for i, (c, _) in enumerate(MACHINES):
            cells.append(f'{did}_{ids[i]}["{matrix[d][c]}"]')
        out += f'  {did}["{d}"] ' + " ".join(cells) + "\n"
    for d in DOMAINS:
        did = {"TDA": "TDA", "QEC": "QEC", "Dynamics": "DYN",
               "Neuro": "NEU", "InfoTheo": "IT"}[d]
        for i, (c, _) in enumerate(MACHINES):
            if matrix[d][c] >= 10:
                out += f"  style {did}_{ids[i]} fill:#9f9,stroke:#333\n"
    out += "```\n"
    out += MATRIX_FOOTER
    out += (f"\n## Coverage Status\n\n{papers} fully annotated papers. "
            f"{n_deep} of 30 cells ≥10 (deep); min cell = {min_cell}.\n")
    return out


def main():
    papers, matrix, notes = derive()
    cols = [c for c, _ in MACHINES]
    min_cell = min(matrix[d][c] for d in DOMAINS for c in cols)
    n_deep = sum(1 for d in DOMAINS for c in cols if matrix[d][c] >= 10)

    print("topo-rosetta derived stats (source: papers/annotations/*.md)")
    print(f"  fully annotated papers : {papers}")
    print(f"  cells                  : 30 (6 machines x 5 domains)")
    print(f"  min cell               : {min_cell}")
    print(f"  cells >=10 (deep)      : {n_deep}")
    for note in notes:
        print(f"  note: {note}")

    rendered = render_matrix(papers, matrix)
    old = MATRIX_PATH.read_text() if MATRIX_PATH.exists() else ""
    if old != rendered:
        MATRIX_PATH.write_text(rendered)
        print(f"  wrote {MATRIX_PATH.relative_to(ROOT)}")
    else:
        print(f"  {MATRIX_PATH.relative_to(ROOT)} already up to date")
    return 0


if __name__ == "__main__":
    sys.exit(main())
