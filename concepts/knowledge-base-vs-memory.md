---
title: Knowledge Base vs Memory
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [architecture, knowledge-base, memory]
sources: [raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md]
reviewed: false
confidence: high
confidence_reason: 来自 SMF 官方文档的核心区分
---

## 编译知识

**知识库 ≠ 记忆系统** — 这是当前 AI 领域普遍混淆的关键区别。

### 核心区别

| 维度 | 知识库 | 记忆系统 |
|------|--------|----------|
| 回答的问题 | "我知道什么？" | "我将来需要什么？" |
| 优化目标 | 信息检索准确性 | 效用函数编码 |
| 遗忘机制 | 无（应该无） | 有（基于相关性衰减） |
| 访问控制 | 通常无 | 原生支持 |
| 可扩展性 | 受限于上下文窗口 | 百万级实体 |

### 现有系统分类

#### 知识库系统

**Karpathy LLM Wiki** [[llm-wiki-karpathy]]
- ~100 篇互连 markdown 文章
- Obsidian 作为 IDE
- LLM 自动维护索引和反向链接
- **局限**：无程序化图谱查询，无访问控制，受限于上下文窗口

**GBrain (Garry Tan)**
- PostgreSQL + pgvector
- 10,000+ 文件索引
- 夜间"梦境循环"丰富图谱
- **局限**：依赖外部数据库，关系存储在 PostgreSQL 而非文件系统，无原生访问控制

**Obsidian 图谱系统**
- Wikilinks 创建连接
- 图谱视图可视化
- **局限**：无法程序化查询，无多跳遍历，无类型化关系，无访问控制

#### 记忆系统

**SMF (Semantic Memory Framework)** [[smf-semantic-memory-framework]]
- POSIX symlink 作为图谱边
- 原生访问控制（Unix 权限）
- 基于 [[bjork-disuse-theory]] 的遗忘机制
- 可扩展至百万级实体
- 效用函数编码到存储结构中

### 效用函数问题

记忆依赖于观察者的效用函数：

> 金门大桥例子：
> - 设计师看到它 → 记住 International Orange 颜色
> - 结构工程师看到它 → 记住 80,000 英里电缆，746 英尺塔
> - 海洋生物学家看到它 → 记住上周二从桥下经过的鲸鱼

**同一对象，三种完全不同的记忆** — 不是因为记忆错误，而是因为每个观察者有不同的效用函数。

### 基准测试的隐含问题

所有记忆基准测试都隐含定义了效用函数：
- LoCoMo 测试长对话记忆
- 测试的是检索准确性，而非关系持久性、访问控制、矛盾处理、生命周期管理

**结论**：当比较 SMF 与 ByteRover 等系统时，我们比较的是检索准确性这一个维度，而非完整的记忆质量。

### 设计取舍

| 场景 | 推荐方案 | 原因 |
|------|----------|------|
| 个人工具 | 知识库（Karpathy Wiki） | 需求变化快，重读成本低，无需访问控制 |
| 组织记忆 | 记忆系统（SMF） | 需要合规、审计、问责、多代理访问 |

---

## 时间线

- 2026-04-15: 初始创建，来源 [[raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 2026-04-15: 关联 [[smf-semantic-memory-framework]], [[llm-wiki-karpathy]], [[bjork-disuse-theory]]
