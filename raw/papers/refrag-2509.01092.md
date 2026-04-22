# REFRAG: Rethinking RAG based Decoding

**Authors:** Xiaoqiang Lin, Aritra Ghosh, Bryan Kian Hsiang Low, Anshumali Shrivastava, Vijai Mohan  
**Affiliation:** Meta Superintelligence Labs, National University of Singapore, Rice University  
**Date:** October 14, 2025  
**arXiv:** 2509.01092  
**Code:** https://github.com/facebookresearch/refrag (待发布)

---

## Abstract

Large Language Models (LLMs) have demonstrated remarkable capabilities in leveraging extensive external knowledge to enhance responses in multi-turn and agentic applications, such as retrieval-augmented generation (RAG). However, processing long-context inputs introduces significant system latency and demands substantial memory for the key-value cache, resulting in reduced throughput and a fundamental trade-off between knowledge enrichment and system efficiency.

While minimizing latency for long-context inputs is a primary objective for LLMs, we contend that RAG systems require specialized consideration.

In RAG, much of the LLM context consists of concatenated passages from retrieval, with only a small subset directly relevant to the query. These passages often exhibit low semantic similarity due to diversity or deduplication during re-ranking, leading to block-diagonal attention patterns that differ from those in standard LLM generation tasks. Based on this observation, we argue that most computations over the RAG context during decoding are unnecessary and can be eliminated with minimal impact on performance.

To this end, we propose **REFRAG**, an efficient decoding framework that compresses, senses, and expands to improve latency in RAG applications. By exploiting this attention sparsity structure, we demonstrate:

- **30.85× time-to-first-token acceleration** (3.75× improvement to previous work) without loss in perplexity
- **16× context window extension** capability
- Rigorous validation across diverse long-context tasks including RAG, multi-turn conversations, and long document summarization

---

## Key Insights

### 1. Inefficient Token Allocation in RAG

RAG contexts contain sparse information — many retrieved passages are uninformative. Treating RAG TTFT as a generic LLM inference problem overlooks this key aspect.

### 2. Block-Diagonal Attention Patterns

RAG passages exhibit low semantic similarity, leading to block-diagonal attention patterns that differ from standard LLM generation tasks.

### 3. Specialized Optimization Required

Existing long-context optimization methods (sparse attention, context sparsification) target generic LLM tasks. RAG requires specialized techniques exploiting its unique structure.

---

## REFRAG Framework

### Compress-Sense-Expand Strategy

1. **Compress**: Compress RAG context to reduce KV cache memory
2. **Sense**: Identify which context segments are relevant to the query
3. **Expand**: Expand only relevant segments for full computation

---

## Results Summary

| Metric | Improvement |
|--------|-------------|
| Time-to-First-Token | 30.85× speedup |
| Context Window | 16× extension |
| Perplexity | No loss |
| Memory | Significantly reduced |

---

## Applications

- Retrieval-Augmented Generation (RAG)
- Multi-turn Conversations
- Long Document Summarization

---

*Full paper text truncated. See arXiv for complete version.*
