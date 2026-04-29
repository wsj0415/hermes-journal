---
title: SMF Semantic Memory Framework
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [architecture, agent-architecture, knowledge-base, graph, memory]
sources: [raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md]
reviewed: false
confidence: high
confidence_reason: 来自 SMF 官方开源文档，作者 Ashwin Gopinath
---

## 编译知识

**SMF (Semantic Memory Framework)** 是由 Dynamis Labs 开源的记忆系统架构，核心创新是**使用 POSIX symlink 作为知识图谱的边**，实现原生可扩展、可查询、可访问控制的组织记忆系统。

### 核心架构

```
/memory/actors/alice/
├── content.md          # 规范内容
├── meta.json           # 结构化元数据
├── related/            # symlink 关系图谱
│   ├── collaborated_with/bob -> /memory/actors/bob/
│   ├── decided_at/meeting-123 -> /memory/decisions/meeting-123/
│   └── ...
└── .provenance.jsonl   # 溯源记录
```

**关键洞察**：`ln -s` 是零成本的关系指针，`ls -la` 即可遍历图谱，无需独立图数据库。

### 8 种实体类型

| 类型 | 回答的问题 |
|------|-----------|
| Actors | who（谁） |
| Interactions | what happened（发生了什么互动） |
| Events | what happened（发生了什么事件） |
| Decisions | what was decided（做了什么决定） |
| Rationale | why（为什么） |
| VCOs | what was committed（承诺了什么） |
| Time | when（何时） |
| Topics | about what（关于什么） |

### 14+ 检索通道

- BM25（实体 + 事实）
- 图遍历（symlink）
- 时间索引
- 嵌入搜索（可选）
- RAPTOR 层次摘要（可选）
- 层次/代理检索器（可选）
- 检索反射器（可选）
- Self-RAG 验证（可选）
- 交叉编码器重排序（可选）

**7 种查询模式**：factual, temporal, counting, multi-session, preference, summarisation, contradiction

### 基准测试结果（LoCoMo）

**结构 > 规模**：
- 8B → Sonnet（50× 规模增长）→ J-score 仅 +0.081
- 基线配置（BM25 + symlink + temporal）→ J-score 与完整 14+ 通道相同

**对比**：
- ByteRover（宽松 LLM 自判）：J=0.88-0.96
- SMF（严格 GPT-4.1 独立评判）：J=0.704

### 生命周期管理

基于 **[[bjork-disuse-theory]]** 实现热→温→冷区域：
- **Storage strength**（存储强度）：不衰减
- **Retrieval strength**（检索强度）：随未使用而衰减
- **Gardener cycle**：修剪弱边，降级低置信度事实

### 访问控制

原生 Unix 权限（chmod, chown, ACL）直接应用到实体目录：
- 4 个敏感度级别：public, internal, confidential, restricted
- 基于身份访问
- 段落级编辑

### 开源范围

仓库：https://github.com/dynamis-Labs/SMF

包含：
- 6 阶段流水线（INGEST → META-REFLECT）
- 8 种实体类型 + Pydantic 模型
- 并行检索器 + RRF 融合
- 代理检索器（ReAct 循环，9 工具，最多 5 次迭代）
- 7 种查询模式 + 通道路由
- Self-RAG 验证钩子
- 生命周期子系统（gardener, zone management）
- MCP 服务器（12 工具，5 资源，4 提示词）

---

## 时间线

- 2026-04-15: 初始创建，来源 [[raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 2026-04-15: 关联 [[knowledge-base-vs-memory]], [[filesystem-as-knowledge-graph]], [[bjork-disuse-theory]]
