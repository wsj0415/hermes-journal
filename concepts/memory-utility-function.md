---
title: Memory Utility Function
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [memory, architecture]
sources: [raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md]
reviewed: false
confidence: high
confidence_reason: SMF 核心理论框架
---

## 编译知识

**记忆是效用函数的编码** — 这是理解记忆系统设计的核心洞察。

### 金门大桥思想实验

同一座桥，三个观察者：

| 观察者 | 记住的内容 | 原因 |
|--------|-----------|------|
| 设计师 | International Orange 颜色 | 与色彩理论、环境协调相关 |
| 结构工程师 | 80,000 英里电缆，746 英尺塔，894,500 吨钢 | 与结构分析相关 |
| 海洋生物学家 | 上周二从桥下经过的鲸鱼 | 与研究观察相关 |

**同一对象，三种完全不同的记忆** — 不是因为记忆错误，而是因为每个观察者有不同的效用函数。

### 效用函数定义

> "Memory is purpose-driven compression."

效用函数回答：**"我将来需要记住什么？"**

### 对记忆系统设计的启示

| 范围 | 效用函数 | 实现难度 |
|------|----------|----------|
| 组织记忆 | 谁负责、做了什么决定、承诺了什么、理由是什么 | **较易**（约束明确） |
| 个人记忆 | 个人生活的所有方面 | 较难（需求变化快） |
| 通用 AI 代理 | 用户可能问的任何事 | **最难**（效用函数几乎无边界） |

### 编码方式对比

| 系统 | 效用函数编码位置 |
|------|-----------------|
| Karpathy Wiki | LLM 在查询时决定 |
| GBrain | LLM 在查询时决定 |
| Obsidian | LLM 在查询时决定 |
| **SMF** | **存储结构本身**（8 实体类型、symlink schema、置信度评分、区域管理） |

### 设计取舍

**动态效用函数（LLM 查询时决定）**：
- ✅ 更灵活，适应新问题
- ✅ 适合个人工具（需求变化快，重读成本低）
- ❌ 关系不持久，依赖模型

**结构化效用函数（编码到存储中）**：
- ✅ 关系持久，独立于模型
- ✅ 适合组织记忆（合规、审计、问责、多代理访问）
- ❌ 灵活性较低

### 对基准测试的影响

所有记忆基准测试都隐含定义了效用函数：
- LoCoMo 测试长对话 → 隐含效用函数是"对话检索"
- 测试组织记忆的系统（如 SMF）在对话基准上可能表现不佳
- 测试个人记忆的系统在组织基准上可能表现不佳

**结论**：比较记忆系统时，必须考虑效用函数对齐度，而非单一分数。

### SMF 的组织效用函数

SMF 为组织记忆设计，编码了以下问题类型：
- **Who** → Actors 实体
- **What happened** → Interactions, Events 实体
- **What was decided** → Decisions 实体
- **Why** → Rationale 实体
- **What was committed** → VCOs 实体
- **When** → Time 实体
- **About what** → Topics 实体

> "An organisation that cannot remember what it committed to is an organisation that cannot be held accountable."

---

## 时间线

- 2026-04-15: 初始创建，来源 [[raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14]]
- 2026-04-15: 关联 [[knowledge-base-vs-memory]], [[smf-semantic-memory-framework]], [[bjork-disuse-theory]]
