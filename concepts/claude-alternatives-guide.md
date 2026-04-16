---
title: Claude 最佳替代方案 — OpenClaw & Hermes 完整指南
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [model-config, provider, best-practice]
sources: [raw/articles/claude-alternatives-guide.md]
reviewed: false
confidence: high
confidence_reason: 基于单一权威来源完整翻译，内容结构忠实原文
---

## 编译知识

本指南发布于 Anthropic 在所有第三方代理工具（包括 OpenClaw 和 Hermes）中禁止订阅 OAuth token 后。核心目的：分享所有优秀替代方案（甚至比 Claude 更划算），提供技巧和提示词让人性化任何模型，让替代模型写出像 Claude 一样的文字。**收藏率 401%**（1,675/417），说明内容极其实用。

**推文数据**：417👍 | 38🔁 | 194K👁️ | 1,675🔖

---

## 时间线

- 2026-04-15: 从 kilroy-cdn 迁移，来源 Meta Alchemist (@meta_alchemist)

---

## 核心背景

**突发变化**：Anthropic 刚刚在所有第三方代理工具（包括 OpenClaw 和 Hermes）中禁止了订阅 OAuth token。

**影响**：
- ❌ 无法再用 Claude 订阅通过 OpenClaw/Hermes
- ❌ 如果尝试用 Claude API，成本会增加 20-30 倍
- ✅ 需要寻找替代方案

**本指南目的**：
1. 分享所有优秀替代方案（甚至比 Claude 更划算）
2. 提供技巧和提示词让人性化任何模型
3. 让替代模型写出像 Claude 一样的文字

---

## 最佳 Claude 替代方案

### 1️⃣ GLM 5.1 ⭐ 最推荐

**优势**：
- ✅ 最佳替代方案之一，superb LLM 模型
- ✅ 比 Claude Plan 便宜 3 倍
- ✅ 公司不会禁止 OpenClaw 或 Hermes
- ✅ GLM 5 免费开源（可本地运行）
- ✅ GLM 5.1 即将开源（目前仅编码计划）

**社区声誉**：
- 在开源和本地 LLM 社区备受尊敬
- 开发者和硬核 LLM 社区喜爱
- X 上可能不那么流行（但值得研究）

**订阅链接**：https://z.ai/subscribe

---

### 2️⃣ Minimax 2.7

**优势**：
- ✅ X 上越来越受欢迎
- ✅ 订阅不仅包含编码 LLM，还有图像/音乐/语音工具
- ✅ Minimax 2.5 免费开源（本地运行）
- ✅ Minimax 2.7 即将开源
- ✅ 支持 OpenClaw 使用
- ✅ 公司增长主要来自 harness 用户（不会禁止）

**基准测试**：
KiloCode 运行了对比 Minimax 2.7 和 Claude Opus 4.6 的基准测试：
- 大量构建/编码/审查相关任务
- 结果"超出预期"
- KiloCode 在基准测试后高度评价 Minimax 2.7
- 成本 vs Claude Opus 4.6 更具优势

**来源**：https://blog.kilo.ai/p/we-tested-minimax-m27-against-claude

**官网**：https://www.minimax.io/

---

### 3️⃣ OpenAI GPT 5.4 (Codex)

**优势**：
- ✅ 大多数事情上已经优于 Opus 4.6
- ✅ OpenAI 收购了 OpenClaw，不用担心 OpenClaw 被禁
- ⚠️ 如果用 Hermes，OpenAI 可能采取和 Claude 相同的禁令路线
- ✅ 后端和编码任务是野兽（目前找不到更好的代理）
- ✅ 比 Claude Opus 4.6 强很多
- ✅ token 性价比高（比 Claude 大方 3-4 倍）
- ✅ 经常重置每周限额作为姿态

**缺点**：
- ❌ 不如 Claude 对话和情感智能
- ❌ UI/UX 设计不如 Claude
- ❌ $20 和 $200 之间没有中间订阅（要么小计划要么大计划）

**作者使用模式**：
> "我 95% 的编码和构建用 Codex，主要选择 Claude 用于对话、编排和 UI/UX 工作。"

---

### 4️⃣ 本地 LLM（如果你有强大 PC/Mac）

**免费开源选项**：
- GLM 5
- Qwen 3.5
- Kimi 2.5
- Minimax 2.5

**即将开源**：
- GLM 5.1
- Minimax 2.7

**建议**：如果你有强大配置，可以仅用电私有运行这些模型。

---

## 让替代模型像 Claude 一样好

### 核心洞察

**Claude 的优势**：
- ✅ 对话和编排 superb
- ✅ 理解优秀 UI/UX 的含义
- ✅ 有品味和个性

**好消息**：所有这些都可复制！如果你想用特定意图进化 OpenClaw 或 Hermes 的代理。

---

### 实施方法

**OpenClaw 有 SOUL.md 系统**，应该用它填补差距。

**3 个技能**：复制粘贴到 OpenClaw & Hermes，将它们变成技能，然后让代理评估如何用这些技能升级自己。

---

## 顶级 UI/UX 技能

### 1️⃣ ui-ux-pro-max-skill ⭐ 必用

**GitHub**：https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

**数据**：
- ⭐ 58k stars
- 🔁 高采用率

**功能**：
- 让任何模型理解优秀 UI/UX
- 提供设计原则和检查清单
- 生成符合人类审美的输出

**安装**：
```bash
# 克隆技能
git clone https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

# 安装到 OpenClaw/Hermes
cp -r ui-ux-pro-max-skill ~/.hermes/skills/
```

---

### 2️⃣ taste-skill

**功能**：
- 培养代理的"品味"
- 理解什么是"好设计"
- 避免 AI 常见的审美错误

**使用**：
```text
# 在 SOUL.md 中添加
skills:
  - taste-skill
```

---

### 3️⃣ human-like-writing-skill

**功能**：
- 让代理写作更像人类
- 避免 AI 常见表达
- 增加个性和情感

**核心提示词**：
```text
写作时遵循：
1. 用短句，避免长句
2. 用具体例子，避免抽象
3. 用主动语态，避免被动
4. 有个性和观点，避免中立
5. 有情感，避免机械
```

---

## 模型对比总结

| 模型 | 编码 | 对话 | UI/UX | 成本 | 推荐度 |
|------|------|------|-------|------|--------|
| **GLM 5.1** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | $ | ⭐⭐⭐⭐⭐ |
| **Minimax 2.7** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | $ | ⭐⭐⭐⭐⭐ |
| **GPT 5.4 (Codex)** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | $$ | ⭐⭐⭐⭐ |
| **本地 LLM** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 免费 | ⭐⭐⭐⭐ |
| **Claude Opus 4.6** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | $$$$ | ⭐⭐⭐ |

**成本说明**：
- $ = 便宜（<$50/月）
- $$ = 中等（$50-100/月）
- $$$ = 贵（$100-200/月）
- $$$$ = 很贵（>$200/月）

---

## 迁移指南

### 从 Claude 迁移到 GLM 5.1

**步骤**：
1. 订阅 GLM 5.1（https://z.ai/subscribe）
2. 获取 API Key
3. 更新 Hermes 配置：
   ```yaml
   model:
     default: glm-5.1
     provider: zai
     base_url: https://open.bigmodel.cn/api/coding/paas/v4
   ```
4. 测试基本功能
5. 调整提示词优化输出

### 从 Claude 迁移到 Minimax 2.7

**步骤**：
1. 订阅 Minimax（https://www.minimax.io/）
2. 获取 API Key
3. 更新 Hermes 配置：
   ```yaml
   model:
     default: minimax-2.7
     provider: minimax
   ```
4. 测试基本功能
5. 安装 UI/UX 技能补偿

### 从 Claude 迁移到 Codex

**步骤**：
1. 订阅 OpenAI（https://openai.com/）
2. 获取 API Key
3. 更新 Hermes 配置：
   ```yaml
   model:
     default: gpt-5.4
     provider: openai
   ```
4. 测试基本功能
5. 注意：Hermes 可能被禁，优先用 OpenClaw

---

## 关键洞察

1. **GLM 5.1 是最佳替代** — 便宜 3 倍，不会被禁
2. **Minimax 2.7 性价比最高** — 包含图像/音乐/语音工具
3. **Codex 编码最强** — 但对话和 UI/UX 不如 Claude
4. **本地 LLM 是终极方案** — 免费、私有、无禁令风险
5. **技能可以补偿差距** — UI/UX、品味、人性化写作技能可让任何模型像 Claude

---

## 行动清单

### 立即行动
- [ ] 订阅 GLM 5.1 或 Minimax 2.7
- [ ] 获取 API Key
- [ ] 更新 Hermes 配置

### 本周
- [ ] 安装 UI/UX 技能
- [ ] 安装品味技能
- [ ] 安装人性化写作技能
- [ ] 测试并调整提示词

### 本月
- [ ] 评估替代模型表现
- [ ] 优化工作流
- [ ] 考虑本地 LLM 设置（如果有强大硬件）

---

## 相关链接

- [[hermes-system-prompt-structure]] - Hermes Agent 系统提示词结构
- [[how-to-make-money-with-claude-code]] - 如何用 Claude Code 赚钱
- [KiloCode 基准测试](https://blog.kilo.ai/p/we-tested-minimax-m27-against-claude)
- [GLM 订阅](https://z.ai/subscribe)
- [Minimax 官网](https://www.minimax.io/)
