---
title: "The Skeleton of Remembering: Why Your Filesystem Is a Brain Waiting to Happen"
author: Ashwin Gopinath
source_url: https://x.com/ashwingop/status/2044085923185602747
published: 2026-04-14
retrieved: 2026-04-15
type: article
tags: [memory, knowledge-base, filesystem, architecture]
---

# The Skeleton of Remembering: Why Your Filesystem Is a Brain Waiting to Happen

**Author**: @ashwingop  
**Date**: 2026-04-14  
**Stats**: 77 Likes, 13 RTs, 5,718 Views, 130 Bookmarks

---

## TL;DR

- A designer sees the Golden Gate Bridge and remembers International Orange. An engineer sees cables. A biologist remembers a whale. Same object, three memories, because memory is not knowledge storage. It is a utility function.

- Karpathy's LLM Wiki and Garry Tan's GBrain are building knowledge bases, structured records of what is true. Memory is something else: it encodes why something matters, to whom, and manages how that changes over time. The difference matters at scale.

- Obsidian wikilinks create a graph, but one you cannot query programmatically, traverse multi-hop, or put access controls on. Flat markdown does not scale.

- SMF is our response: POSIX symlinks are the knowledge graph edges. ls -la reveals the graph. No separate graph database. Native access control. Scales to millions of entities without touching a context window.

- Structure over scale: on LoCoMo, a well-structured filesystem-native memory with BM25 + graph traversal achieves the same strict J-score as a much richer 14+ channel stack, and a 50× model scale increase only buys +0.081 J-score under a dedicated GPT‑4.1 judge. Architecture dominates scale.

- We are open-sourcing the core. Production goes further. https://github.com/dynamis-Labs/SMF

---

## Key Distinctions

### Knowledge Base vs Memory

| System | Type | Characteristics |
|--------|------|-----------------|
| Karpathy LLM Wiki | Knowledge Base | ~100 interlinked markdown articles, Obsidian IDE, auto-maintained index |
| GBrain | Knowledge Base | PostgreSQL + pgvector, 10,000+ files, nightly "dream cycle" |
| Obsidian | Knowledge Base | Wikilinks create graph, no programmatic query, no access control |
| **SMF** | **Memory System** | Symlink graph, native ACL, zone-based forgetting, utility function encoding |

### The Utility Function Problem

Memory depends on the observer's utility function:
- Designer → International Orange
- Engineer → 80,000 miles of cable, 746-foot towers
- Marine biologist → whale passing under

Same object, three different memories. Memory is **purpose-driven compression**.

---

## SMF Architecture

### 8 Entity Types

1. **Actors** — who
2. **Interactions** — what happened
3. **Events** — what happened (temporal)
4. **Decisions** — what was decided
5. **Rationale** — why
6. **VCOs** — what was committed (Verbal Commitment Objects)
7. **Time** — when
8. **Topics** — about what

### Filesystem Structure

```
/memory/actors/alice/
├── content.md
├── meta.json
├── related/
│   ├── collaborated_with/bob -> /memory/actors/bob/
│   ├── decided_at/meeting-123 -> /memory/decisions/meeting-123/
│   └── ...
└── .provenance.jsonl
```

**Key insight**: `ln -s` is a zero-cost relational pointer. `ls -la` reveals the graph.

---

## Benchmark Results (LoCoMo)

### Structure > Scale

| Model | J-Score (strict judge) |
|-------|----------------------|
| 8B | 0.623 |
| 70B | 0.687 |
| Sonnet | 0.704 |

**50× scale increase → +0.081 J-score**

### Retrieval Ablation

| Configuration | J-Score |
|---------------|---------|
| Full 14+ channel stack | 0.704 |
| Baseline (BM25 + graph + temporal only) | 0.704 |

**Baseline matches full stack** — architecture dominates retrieval complexity.

---

## Comparison Against Field

| System | Judge | J-Score |
|--------|-------|---------|
| ByteRover | LLM-as-Judge (lenient) | 0.88-0.96 |
| SMF | Dedicated GPT-4.1 (strict) | 0.704 |
| Other systems | Self-judged | inflated |

SMF's relationships are **explicit and non-parametric** — symlinks exist on disk, survive model changes, traversable without LLM call.

---

## What's Open-Sourced

Repository: https://github.com/dynamis-Labs/SMF

- Full 6-stage pipeline (INGEST → META-REFLECT)
- 8 entity types with Pydantic models
- Parallel retriever with 14+ channels + RRF fusion
- Agentic retriever (ReAct loop, 9 tools, max 5 iterations)
- 7 query modes with per-mode channel routing
- Self-RAG validation hooks
- Lifecycle subsystem (gardener, zone management, Bjork's theory)
- Security & ACL (4 sensitivity levels)
- MCP server (12 tools, 5 resources, 4 prompts)
- Circuit-breaker inference routing

---

## Related Papers

- **SpectralQuant**: https://github.com/Dynamis-Labs/spectralquant
- **The Geometry of Forgetting**: https://arxiv.org/abs/2604.06222
- **The Price of Meaning**: https://arxiv.org/abs/2603.27116

---

## Key Quotes

> "Memory is not about recording what is true. Memory is about encoding what matters, to whom, for what purpose, and managing how that encoding changes over time."

> "A knowledge base answers: 'What do I know?' Memory answers: 'What will I need?'"

> "Architecture dominates scale."

> "Forgetting and false recall are the price of meaning. SMF does not claim to have escaped that tradeoff. It claims to be a principled navigation of the frontier."
