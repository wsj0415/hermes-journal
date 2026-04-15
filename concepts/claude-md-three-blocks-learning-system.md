---
title: Claude MD 三模块学习系统
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [knowledge-base, best-practice, workflow]
sources: [raw/articles/claude-md-three-blocks-learning-system.md]
reviewed: false
confidence: high
confidence_reason: 基于单一权威来源完整翻译，内容结构忠实原文
---

## 编译知识

Claude MD 三模块学习系统是一个让 Claude 每次会话都变得更聪明的框架。通过三个模块（知识架构、决策日志、质量门）和一个维护计划，实现跨会话学习和持续改进。核心洞察：**没有反思的记忆只是存储**。

**成果**：作者在一个月后，Claude 应用了 24 条它自己编写的项目特定规则——这些规则用户从未提示过，是从数十次会话的模式中提取的。

---

## 时间线

- 2026-04-15: 从 kilroy-cdn 迁移，来源 Paweł Huryn (@PawelHuryn)
- 推文数据：321👍 | 32🔁 | 65K👁️ | 1,123🔖（收藏率 350%）

---

## 问题：没有反思的记忆

**Claude 记得一切，但它不学习。**

### 典型场景

```
会话 1：捕获定价测试显示 40% 流失率
会话 2：捕获竞争对手取消了免费层级
会话 3：捕获 onboarding 用户流失较少

三个独立的观察，三个独立的会话 — Claude 从未将它们连接起来。
```

**没有反思的记忆只是存储。**

大多数 CLAUDE.md 设置正是如此 — 一个不断增长的纠正日志，从不提升模式，从不测试自己的假设，从不评估工作是否真的符合你的标准。

---

## 解决方案：三个模块 + 一个维护计划

### 模块 1：知识架构 — 学习循环

#### 失败模式

Claude 捕获观察但从不重新审视它们。上周的洞察不告知本周的工作。没有机制来测试模式是否成立、在成立时提升它、或在不成立时丢弃它。

#### 核心原则

**强制主动检索** — 在每个任务之前：
1. Claude 在提出建议前读取现有知识
2. 任务后，提取学到的内容
3. 存储在具有清晰层次结构的领域特定文件夹中

#### 知识层次

```
knowledge/
├── observations/        # 原始观察
├── hypotheses/          # 需要更多数据的假设
└── rules/               # 默认应用的确认规则
```

#### 提升循环

```
观察 → 假设 → (多次确认) → 规则
                         ↓
                    (新数据矛盾)
                         ↓
                    降级回假设
```

#### 实施示例

**每次会话结束提示**：
```
Based on this session, extract:
1. New observations about the project/users/domain
2. Any hypotheses that should be tested
3. Any patterns that should become rules

Store each in the appropriate knowledge/ subfolder.
```

---

### 模块 2：决策日志 — 避免重新辩论

#### 失败模式

```
会话 5：决定使用 PostgreSQL 因为事务需求
会话 12：新 Claude 会话，建议改用 MongoDB
会话 12：花费 30 分钟重新辩论已决定的事
```

#### 核心原则

**记录每个重要决策及完整推理**，包括：
- 决策内容
- 考虑过的替代方案
- 为什么选择这个
- 什么条件下会重新考虑

#### 决策日志格式

```markdown
## Decision: Use PostgreSQL for primary database

**Date:** 2026-03-15
**Context:** User management system with financial transactions

**Alternatives considered:**
- MongoDB (rejected: no ACID transactions)
- SQLite (rejected: can't scale for concurrent writes)

**Rationale:**
- Need ACID compliance for financial data
- Team has PostgreSQL experience
- Can use JSONB for flexible schema needs

**Revisit conditions:**
- If team loses PostgreSQL expertise
- If scale requirements change dramatically
```

#### 实施示例

**每次重大决策后**：
```
Log this decision to decisions.md with:
- What was decided
- Alternatives considered
- Why this choice
- When to revisit
```

---

### 模块 3：质量门 — 客观评估标准

#### 失败模式

**代理无法客观判断自己的工作。**

```
Claude: "我完成了 API 端点"
用户：*审查发现缺少错误处理、无日志、无速率限制*
```

#### 核心原则

**给 Claude 具体的评估标准**，让它能在提交前自我审查。

#### 质量门示例

**代码审查清单**：
```markdown
## Code Quality Gate

Before marking a task complete, verify:

**Functionality:**
- [ ] All requirements met
- [ ] Edge cases handled
- [ ] Error messages are clear

**Code Quality:**
- [ ] Follows project conventions
- [ ] No hardcoded values
- [ ] Functions are <50 lines
- [ ] Each function has single responsibility

**Testing:**
- [ ] Unit tests pass
- [ ] Integration tests added
- [ ] Manual testing completed

**Documentation:**
- [ ] README updated if needed
- [ ] Complex logic commented
- [ ] API changes documented
```

**写作质量门**：
```markdown
## Content Quality Gate

Before submitting content, verify:

**Clarity:**
- [ ] Main point in first paragraph
- [ ] No jargon without explanation
- [ ] Each paragraph has one idea

**Engagement:**
- [ ] Hook in first sentence
- [ ] Examples for abstract concepts
- [ ] Call-to-action at end

**SEO:**
- [ ] Target keyword in title
- [ ] Meta description written
- [ ] Internal links added
```

#### 实施示例

**为每类工作定义质量门**：
```
Create quality gates for:
- Code reviews
- Content creation
- Research tasks
- Testing

Make them specific and actionable.
```

---

### 维护计划 — 保持系统不过时

#### 失败模式

```
系统运行 3 个月 → 规则过时但仍在应用
               → 假设从未测试
               → 决策日志变成被忽视的 blob
```

#### 核心原则

**定期修剪和更新**，防止系统腐化。

#### 维护任务

| 频率 | 任务 | 说明 |
|------|------|------|
| **每周** | 审查新规则 | 确认新提升的规则仍然有效 |
| **每月** | 测试假设 | 对 pending 假设收集更多数据 |
| **每季度** | 清理决策日志 | 标记已过时的决策 |
| **每季度** | 更新质量门 | 根据新最佳实践更新清单 |

#### 维护提示

**每周维护**：
```
Review rules added this week:
- Are they still valid?
- Any contradictions with existing rules?
- Should any be demoted to hypotheses?
```

**每月维护**：
```
For each hypothesis:
- What data have we collected?
- Should it be promoted to rule?
- Should it be discarded?
- What additional tests are needed?
```

---

## 实施路线图

### 第 1 周：基础设置

1. 创建文件夹结构：
   ```
   knowledge/
   ├── observations/
   ├── hypotheses/
   └── rules/
   ```
2. 创建 `decisions.md` 文件
3. 为最常见任务类型定义 1-2 个质量门

### 第 2-3 周：习惯养成

1. 每次会话结束提取学到的内容
2. 每个重大决策后记录
3. 提交前使用质量门

### 第 4 周：第一次维护

1. 审查所有新规则
2. 清理过时的决策
3. 更新质量门

### 第 2-3 个月：优化

1. 根据使用情况调整结构
2. 添加更多质量门
3. 开始测试假设

---

## 预期成果

### 1 个月后

- 10-20 条观察
- 5-10 个假设
- 3-5 条规则
- Claude 开始应用模式而非仅遵循指令

### 3 个月后

- 50+ 观察
- 20+ 假设（10+ 已测试）
- 15-20 条规则
- Claude 主动识别模式并提出改进建议

### 6 个月后

- 系统成为团队知识库
- 新成员通过阅读知识库快速上手
- Claude 成为真正的"团队记忆"

---

## 关键洞察

1. **记忆 ≠ 学习** — 学习需要主动反思和模式提取
2. **决策必须记录推理** — 否则会被重新辩论
3. **质量门让代理自我审查** — 减少返工
4. **维护是必须的** — 否则系统会腐化

---

## 相关链接

- [[12-agentic-harness-patterns]] - 12 个 Agentic Harness 模式
- [[second-brain-karpathy-style]] - Karpathy 风格第二大脑
- [原文推文](https://x.com/pawelhuryn/status/2039095189843706022)
- [完整系统](https://www.productcompass.pm/p/claude-md-snippets)
