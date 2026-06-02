# Research Cycle — Autonomous Research Loop for topo-rosetta

## When to use

Invoke with `/research-cycle` to run a full autonomous iteration of the research pipeline. The cycle searches for papers, annotates them, consolidates findings, and identifies what to search next. Designed to run unattended with auto-commit/push.

To resume after a handoff (previous session hit context limits), just invoke `/research-cycle` — it reads pipeline state and picks up where it left off.

## Operating Mode

- **Fully autonomous**: no user approval needed between phases
- **Auto-commit**: commit after every annotated paper and after each phase
- **Auto-push**: push to `origin` after every commit
- **Handoff-safe**: all state persists in `pipeline/` files; any session can resume

## The Loop

```
DETERMINE STATE:
  Read pipeline/queue.md
  IF queue has papers waiting → skip to PHASE 3 (annotate)
  IF queue is empty → start from PHASE 1 (gaps)

PHASE 1 — GAP ANALYSIS
  Read pipeline/coverage_matrix.md
  Read glossary/ANTISYNONYMS.md
  Read glossary/SYNONYMS.md (for vocabulary holes)
  Read pipeline/coverage_matrix.md bridges section
  
  Identify and rank gaps:
    1. Bridge gaps (domain pairs with 0 cross-domain papers)
    2. Empty coverage cells (0 papers)
    3. Sparse cells (1 paper) in under-represented domains
    4. Under-evidenced divergences in ANTISYNONYMS.md
  
  Pick top 3 gaps as this iteration's focus.
  Write focus to pipeline/iteration_history.md.

PHASE 2 — SEARCH
  For each focus gap:
    Extract domain + structure keywords from glossary/SYNONYMS.md
    Generate 3-5 search queries combining domain + structure vocabulary
    Check pipeline/search_log.md — skip queries already run
    
    Execute queries using available MCP tools:
      - Use ToolSearch to discover actual tool names for arxiv, semantic-scholar, paper-search servers
      - Semantic Scholar: paper search + citation-based discovery (get_recommendations, get_paper_references)
      - arXiv: keyword search + download for full-text reading
      - paper-search: PubMed, bioRxiv, medRxiv for neuroscience/biology gaps
      - WebSearch: fallback for any source without MCP coverage
    
    For each result:
      Grep papers/ directory for title or arXiv ID — skip if already annotated
      Grep pipeline/queue.md — skip if already queued
    
    Classify new finds:
      High priority: spans 2+ Rosetta domains (cross-domain bridge)
      Medium priority: fills an empty or sparse coverage cell
      Low priority: single-domain, well-covered area
    
    Add to pipeline/queue.md under appropriate section
    Log queries to pipeline/search_log.md
  
  git add pipeline/queue.md pipeline/search_log.md
  git commit -m "research-cycle: search — <N> papers queued for <focus areas>"
  git push -u origin claude/paper-research-pipeline-9h98k

PHASE 3 — ANNOTATE
  Read pipeline/queue.md. Process papers in priority order (High → Medium → Low).
  
  For each paper:
    1. Retrieve the paper:
       - If arXiv ID: use arXiv MCP to download and read
       - If DOI/URL: use WebFetch to retrieve
       - If in link-forge: query Neo4j at bolt://localhost:7687
    
    2. Produce full annotation following the template in .claude/skills/annotate/SKILL.md:
       - Citation, Domain(s), Abstract machines (with justification)
       - What is genuinely new
       - Connections authors acknowledge
       - Vocabulary mapping table
    
    3. File the annotation:
       - Add to papers/inbox.md under --- separator
       - Add reference to papers/by-domain/<domain>.md
       - Add reference to papers/by-structure/<structure>.md
       - If cross-domain bridge: add to papers/cross_domain_bridges.md
    
    4. Remove from pipeline/queue.md
    
    5. Commit and push:
       git add papers/ pipeline/queue.md
       git commit -m "research-cycle: annotate <arXiv-ID-or-short-title> [<domain>]"
       git push -u origin claude/paper-research-pipeline-9h98k
    
    AFTER EVERY 5 PAPERS — check if this is a good handoff point:
      If the conversation has been running for a long time and you've annotated
      a substantial batch (5+ papers), proceed to PHASE 4 to digest and hand off.
      The remaining queue will be picked up by the next session.

PHASE 4 — DIGEST
  Read all papers annotated during this cycle (from git log or by comparing
  pipeline/queue.md changes).
  
  Update pipeline/coverage_matrix.md:
    Re-scan papers/by-domain/*.md and papers/by-structure/*.md
    Recount all cells
    Update gaps list
    Update bridges table
  
  Vocabulary audit:
    For each new annotation's vocabulary table, check glossary/SYNONYMS.md
    Add any new terms to the appropriate layer/cell
  
  Divergence audit:
    For each new annotation's "genuinely new" section, check glossary/ANTISYNONYMS.md
    Add new divergences if found
  
  Atlas update:
    For each machine instantiated by new papers, update atlas/<MACHINE>.md
    with the new citation under the appropriate domain section
  
  git add glossary/ atlas/ pipeline/coverage_matrix.md
  git commit -m "research-cycle: digest — update matrix, glossary, atlas"
  git push -u origin claude/paper-research-pipeline-9h98k

PHASE 5 — RECORD & HANDOFF
  Determine iteration number from pipeline/iteration_history.md (count existing iterations + 1).
  
  Write iteration summary to pipeline/iteration_history.md:
    ## Iteration <N> — <date>
    **Focus**: <what gaps this iteration targeted>
    **Queries run**: <count>
    **Papers found**: <count>
    **Papers annotated**: <count>
    **New vocabulary**: <terms added to SYNONYMS.md, or "none">
    **New divergences**: <entries added to ANTISYNONYMS.md, or "none">
    **Gaps closed**: <domain-structure pairs that gained sufficient coverage>
    **Gaps remaining**: <top 3 gaps for next iteration>
    **Queue remaining**: <count of papers still in queue.md>
    **Next focus**: <recommended search direction>
  
  git add pipeline/iteration_history.md
  git commit -m "research-cycle: iteration <N> complete"
  git push -u origin claude/paper-research-pipeline-9h98k
  
  DECISION: continue or hand off?
    IF pipeline/queue.md still has papers AND conversation is still fresh:
      → GOTO PHASE 3 (keep annotating)
    IF pipeline/queue.md is empty AND conversation is still fresh:
      → GOTO PHASE 1 (start next iteration)
    OTHERWISE:
      → Output handoff message and STOP
  
  HANDOFF MESSAGE FORMAT:
    ## Handoff — Iteration <N> complete
    
    **This session**: Annotated <X> papers, closed <Y> gaps, found <Z> new papers
    **Queue remaining**: <W> papers in pipeline/queue.md
    **Coverage**: <brief matrix summary — which cells improved>
    **Next focus**: <top 3 gaps>
    
    **To resume**: run `/research-cycle` — it will read pipeline state and continue.
```

## Git Protocol

- Branch: `claude/paper-research-pipeline-9h98k`
- Commit after: every paper annotation, every phase completion
- Push after: every commit
- Push retry: up to 4 attempts with 2s/4s/8s/16s exponential backoff on network failure
- Never amend — always new commits

## MCP Tool Discovery

The actual MCP tool names depend on how the servers register. At the start of each session:
- Use ToolSearch to find available tools matching "arxiv", "semantic", "paper", "pubmed", "biorxiv"
- Use whatever tool names are actually registered
- If an MCP server is unavailable, fall back to WebSearch with domain-filtered queries

## Resilience

- All state is in `pipeline/` markdown files — nothing is held only in memory
- Every paper annotation is committed individually — partial progress is never lost
- Queue is updated as papers are processed — no double-annotation risk
- Any session running `/research-cycle` reads current state and continues from there
