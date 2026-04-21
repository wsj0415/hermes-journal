---
title: Bjork Disuse Theory
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [memory, architecture]
sources: [raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md]
reviewed: false
confidence: high
confidence_reason: SMF 生命周期管理的理论基础
---

## 编译知识

**Bjork 失用新理论 (New Theory of Disuse)** 是 SMF 记忆生命周期管理的心理学基础。

### 核心概念

记忆强度由两个独立量组成：

| 强度类型 | 定义 | 衰减特性 |
|----------|------|----------|
| **Storage strength** | 编码质量（记得多牢） | **不衰减** |
| **Retrieval strength** | 当前可访问性（多容易想起） | **随未使用而衰减** |

### SMF 实现：区域生命周期

```
HOT → WARM → COLD
```

**HOT 区域**：
- 高频访问实体
- 完整索引
- 快速检索通道

**WARM 区域**：
- 中频访问
- 部分索引
- 标准检索

**COLD 区域**：
- 低频访问
- 降级索引
- 需要时恢复

### Gardener Cycle（园丁循环）

类比生物记忆的**突触修剪**：

```python
# 伪代码
for entity in memory:
    if last_accessed > 90_days:
        demote_to_cold()
    if relationship_strength < threshold:
        prune_symlink()  # 删除弱关系
    if confidence < minimum:
        flag_for_review()
```

**关键**：遗忘不是删除，而是**降级优先级**。

### 与生物记忆的类比

| 生物记忆 | SMF 实现 |
|----------|----------|
| 海马体快速编码 | Stage 0-2 快速模型摄取 |
| 新皮层慢速巩固 | Stage 3-5 前沿模型丰富 |
| 突触强化（Hebbian 学习） | 共同访问时创建快捷 symlink |
| 睡眠时突触修剪 | Gardener cycle 修剪弱边 |
| 记忆巩固 | Zone management 区域管理 |

### 为什么记忆系统必须遗忘

> "Unbounded accumulation without relevance decay is not memory. It is hoarding."

**知识库不应该遗忘** — 这是它们的工作。
**记忆系统必须遗忘** — 无限制积累无关信息是囤积，不是记忆。

### 实际应用

对于 Hermes wiki：
- 90 天未更新的页面 → 标记为 stale
- 6 个月未访问的 raw 来源 → 考虑归档
- 被多个新来源矛盾的信息 → 标记 contradiction，降级置信度

---

## 时间线

- 2026-04-15: 初始创建，来源 [[raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md]]
- 2026-04-15: 关联 [[smf-semantic-memory-framework]], [[knowledge-base-vs-memory]]
