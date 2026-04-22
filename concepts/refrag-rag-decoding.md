---
title: REFRAG Rethinking RAG based Decoding
created: 2026-04-22
updated: 2026-04-22
type: summary
tags: [rag, inference, optimization, meta]
sources: [raw/papers/refrag-2509.01092.md]
---

## 编译知识

**REFRAG** 是 Meta Superintelligence Labs 提出的高效 RAG 解码框架，通过利用 RAG 上下文的注意力稀疏性，实现 **30.85× time-to-first-token 加速**（比之前工作提升 3.75×），且无 perplexity 损失。

这一工作与 [[agent-memory-architecture]] 中讨论的检索瓶颈问题直接相关，也验证了 [[knowledge-base-vs-memory]] 中提到的"检索是瓶颈而非存储"的观点。

### 核心洞察

RAG 上下文与通用长文本有本质区别：
1. **信息稀疏**：检索到的 passages 中只有一小部分与 query 直接相关
2. **低语义相似度**：passages 之间因多样性或去重导致语义差异大
3. **块对角注意力模式**：attention patterns 呈现 block-diagonal 结构，不同于标准 LLM 生成任务

基于此，REFRAG 认为 RAG 上下文中大部分计算是不必要的，可以消除而不影响性能。

### 技术方法

REFRAG 框架采用 **compress-sense-expand** 三步策略：
1. **Compress**：压缩 RAG 上下文，减少 KV cache 内存占用
2. **Sense**：感知哪些上下文片段与 query 相关
3. **Expand**：仅扩展相关片段进行完整计算

### 关键结果

| 指标 | 提升 |
|------|------|
| Time-to-First-Token | 30.85× 加速 |
| 上下文窗口扩展 | 16× |
| Perplexity | 无损失 |
| 内存占用 | 显著降低 |

### 应用场景

- RAG 检索增强生成
- 多轮对话
- 长文档摘要

---

## 时间线

- 2026-04-22: 初始创建，来源 arxiv:2509.01092
