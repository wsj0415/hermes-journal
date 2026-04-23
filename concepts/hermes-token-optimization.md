---
title: Hermes Token 优化策略
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [token-optimization, cost-reduction, openrouter, best-practice]
sources: [raw/articles/startup-ideas-pod-hermes-imran-2026-04.md, raw/articles/ksimback-hermes-beginners-guide-2026-04.md]
reviewed: false
confidence: high
confidence_reason: 来自实际用户的实证数据，90% 成本降低有具体数字支撑
---

## 编译知识

Hermes Agent 的 Token 优化有**两个核心策略**，结合使用可降低约 90% 成本：

### 策略一：使用 OpenRouter

**为什么有效：**
- 清晰的每 token 定价，所有模型一目了然
- 每周轮换免费模型（2026-04 录制时 NVIDIA NemoTron 免费）
- 可以按需选择最便宜的模型执行特定任务

**实施：**
```yaml
# config.yaml 中设置
model:
  provider: openrouter
  model: nvidia/nemotron  # 或其他免费/低价模型
```

### 策略二：将重复任务代码化

**核心逻辑：**
如果每天运行相同任务 → 让 agent 写一次代码 → 之后变成确定性任务 → 不再需要 agent 参与 → 零 token 花费

**案例：**
- 早晨 Gmail 分类 → 第一次用 agent，之后运行生成的脚本
- 费用报告 → agent 生成固定格式处理代码
- 数据抓取 → agent 写好爬虫后定时运行

**成本对比（Imran 实测）：**

| 阶段 | 5 天花费 | 说明 |
|------|----------|------|
| 优化前 | ~$130 | 所有任务都走 agent |
| 优化后 | ~$10 | 重复任务代码化 + OpenRouter |
| 降低 | **90%+** | 能力相同 |

---

## 任务分类策略

| 任务类型 | 推荐模型 | 原因 |
|----------|----------|------|
| Gmail 分类/简单 triage | 免费/超小模型 | 规则明确，不需要强推理 |
| 代码生成/调试 | 中等模型 | 需要理解上下文 |
| 战略决策/复杂分析 | 前沿模型 | 需要强推理能力 |
| 重复性数据抓取 | 代码化 | 一次性生成，之后零成本 |

---

## 子 Agent 模式

Imran 使用子 agent 分配不同模型：
- 便宜任务（如 Gmail triage）→ 小模型子 agent
- 重要任务 → 前沿模型

Cron jobs 用于 recurring tasks，sub-agents 用于模型分层。

---

## 监控建议

1. **OpenRouter Dashboard** — 实时查看每模型花费
2. **Hermes 日志审计** — `hermes logs` 查看高频任务
3. **每周审查** — 识别可代码化的重复任务

---

## 时间线

- **2026-04-20**: Imran 在 The Startup Ideas Podcast 分享 90% 成本降低策略 [[imran-hermes-power-user]]

---

## 相关工作

- [[imran-hermes-power-user]] — Imran 完整使用模式
- [[hermes-best-practices]] — Hermes 最佳实践汇总
- [[openrouter-model-pricing]] — OpenRouter 模型定价对比（待创建）
