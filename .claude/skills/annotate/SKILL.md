# Annotate Paper for topo-rosetta

## When to use
When adding a research paper to the topo-rosetta repository. Invoke with `/annotate <paper-identifier>` where the identifier can be an arXiv ID, a link-forge URL, a title, or a file path to a PDF.

## What it does

Produces a full-depth annotation following METHODOLOGY.md, then files it into both the by-domain and by-structure indices.

## Annotation Template

For each paper, produce exactly this structure:

```markdown
## <arXiv ID or DOI> --- <Authors> (<Year>)
**"<Title>"**

**Domain(s)**: <comma-separated list from: TDA, QEC, dynamical systems, neuroscience, information theory, [new domain if needed]>

**Abstract machines instantiated**:
- **Chain complex**: <How this paper constructs or uses boundary operators, homology, cycles/boundaries. Omit if not instantiated.>
- **Parameterized homology**: <How the paper tracks topological invariants as a parameter varies. Omit if not instantiated.>
- **Matching**: <How the paper solves an optimal assignment between features. Omit if not instantiated.>
- **Stability**: <How the paper proves or exploits robustness under perturbation. Omit if not instantiated.>
- **Joint-vs-marginal excess**: <How the paper detects structure in composites absent from components. Omit if not instantiated.>
- **Null hypothesis**: <How the paper constructs a reference by destroying structure. Omit if not instantiated.>

**What is genuinely new (not reducible to shared abstraction)**:
<Bullet points. This is the MOST IMPORTANT field. If everything reduces, say so explicitly. Be precise about what does NOT fit the six machines.>

**Connections the authors acknowledge**: <Do the authors cite or acknowledge parallels to other domains in the Rosetta? Most don't. Note when they do.>

**Vocabulary mapping**:
| Paper term | Rosetta term |
|---|---|
| <domain-specific term> | <corresponding entry from SYNONYMS.md> |
| ... | ... |
```

## Filing Rules

1. Add the annotation to `papers/inbox.md` under a `---` separator
2. Add a reference line to the appropriate `papers/by-domain/<domain>.md` file(s)
3. Add a reference line to the appropriate `papers/by-structure/<structure>.md` file(s)
4. If the paper introduces a new vocabulary mapping, add it to `glossary/SYNONYMS.md`
5. If the paper reveals a genuine divergence, add it to `glossary/ANTISYNONYMS.md`

## Quality Checklist

- [ ] Every machine claimed is justified with a specific mechanism from the paper
- [ ] "Genuine novelty" field is non-empty and specific
- [ ] Vocabulary table maps paper terms to existing Rosetta terms (not the reverse)
- [ ] Domain assignment reflects the community that produced/reads the paper, not just the subject matter
- [ ] Cross-domain awareness is noted --- most papers are siloed; the rare bridges matter

## Sources

Papers can be sourced from:
- **link-forge Neo4j** (`bolt://localhost:7687`, neo4j/link_forge_dev): Query with `MATCH (l:Link) WHERE l.title =~ '(?i).*<keyword>.*' AND l.contentType = 'research-paper' RETURN l.title, l.url, l.content, l.description`
- **arXiv MCP tools**: `mcp__arxiv__search_papers`, `mcp__arxiv__read_paper`
- **Semantic Scholar MCP**: `mcp__semantic-scholar__search_semantic_scholar`
- **Direct PDF read**: Use the Read tool on local PDF files
