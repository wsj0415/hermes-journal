# Claude 最佳替代方案 — OpenClaw & Hermes 完整指南

> **原文作者：** Meta Alchemist (@meta_alchemist)  
> **翻译时间：** 2026-04-05  
> **原文数据：** 417👍 | 38🔁 | 194K👁️ | 1,675🔖  
> **推文链接：** https://x.com/meta_alchemist/status/2040416725775352258

---

## 📊 推文数据

| 指标 | 数值 |
|------|------|
| 浏览量 | 194,680 |
| 点赞数 | 417 |
| 转发数 | 38 |
| 书签数 | 1,675 |
| 发布时间 | 2026-04-04 13:10 UTC |

**超高收藏率：** 1,675/417 = 401%（说明内容极其实用）

---

## 🎯 核心背景

**突发变化：** Anthropic 刚刚在所有第三方代理工具（包括 OpenClaw 和 Hermes）中禁止了订阅 OAuth token。

**影响：**
- ❌ 无法再用 Claude 订阅通过 OpenClaw/Hermes
- ❌ 如果尝试用 Claude API，成本会增加 20-30 倍
- ✅ 需要寻找替代方案

**本指南目的：**
1. 分享所有优秀替代方案（甚至比 Claude 更划算）
2. 提供技巧和提示词让人性化任何模型
3. 让替代模型写出像 Claude 一样的文字

---

## 🏆 最佳 Claude 替代方案

### 1️⃣ GLM 5.1 ⭐ 最推荐

**优势：**
- ✅ 最佳替代方案之一， superb LLM 模型
- ✅ 比 Claude Plan 便宜 3 倍
- ✅ 公司不会禁止 OpenClaw 或 Hermes
- ✅ GLM 5 免费开源（可本地运行）
- ✅ GLM 5.1 即将开源（目前仅编码计划）

**社区声誉：**
- 在开源和本地 LLM 社区备受尊敬
- 开发者和硬核 LLM 社区喜爱
- X 上可能不那么流行（但值得研究）

**订阅链接：** https://z.ai/subscribe

---

### 2️⃣ Minimax 2.7

**优势：**
- ✅ X 上越来越受欢迎
- ✅ 订阅不仅包含编码 LLM，还有图像/音乐/语音工具
- ✅ Minimax 2.5 免费开源（本地运行）
- ✅ Minimax 2.7 即将开源
- ✅ 支持 OpenClaw 使用
- ✅ 公司增长主要来自 harness 用户（不会禁止）

**基准测试：**
KiloCode 运行了对比 Minimax 2.7 和 Claude Opus 4.6 的基准测试：
- 大量构建/编码/审查相关任务
- 结果"超出预期"
- KiloCode 在基准测试后高度评价 Minimax 2.7
- 成本 vs Claude Opus 4.6 更具优势

**来源：** https://blog.kilo.ai/p/we-tested-minimax-m27-against-claude

**官网：** https://www.minimax.io/

---

### 3️⃣ OpenAI GPT 5.4 (Codex)

**优势：**
- ✅ 大多数事情上已经优于 Opus 4.6
- ✅ OpenAI 收购了 OpenClaw，不用担心 OpenClaw 被禁
- ⚠️ 如果用 Hermes，OpenAI 可能采取和 Claude 相同的禁令路线
- ✅ 后端和编码任务是野兽（目前找不到更好的代理）
- ✅ 比 Claude Opus 4.6 强很多
- ✅ token 性价比高（比 Claude 大方 3-4 倍）
- ✅ 经常重置每周限额作为姿态

**缺点：**
- ❌ 不如 Claude 对话和情感智能
- ❌ UI/UX 设计不如 Claude
- ❌ $20 和 $200 之间没有中间订阅（要么小计划要么大计划）

**作者使用模式：**
> "我 95% 的编码和构建用 Codex，主要选择 Claude 用于对话、编排和 UI/UX 工作。"

---

### 4️⃣ 本地 LLM（如果你有强大 PC/Mac）

**免费开源选项：**
- GLM 5
- Qwen 3.5
- Kimi 2.5
- Minimax 2.5

**即将开源：**
- GLM 5.1
- Minimax 2.7

**建议：** 如果你有强大配置，可以仅用电私有运行这些模型。

**推荐阅读：** 作者覆盖了各种用例的免费开源 LLM（图像生成/视频/语音/通用/编码等）及所需配置。

---

## 🎨 让替代模型像 Claude 一样好

### 核心洞察

**Claude 的优势：**
- ✅ 对话和编排 superb
- ✅ 理解优秀 UI/UX 的含义
- ✅ 有品味和个性

**好消息：** 所有这些都可复制！如果你想用特定意图进化 OpenClaw 或 Hermes 的代理。

---

### 实施方法

**OpenClaw 有 SOUL.md 系统**，应该用它填补差距。

**3 个技能：** 复制粘贴到 OpenClaw & Hermes，将它们变成技能，然后让代理评估如何用这些技能升级自己。

---

## 🎯 顶级 UI/UX 技能

### 1️⃣ ui-ux-pro-max-skill ⭐ 必用

**GitHub：** https://github.com/nextlevelbuilder/ui-ux-pro-max-skill

**数据：**
- ⭐ 58k stars
- 🍴 5.7k forks
- GitHub 上最流行的 UI/UX 技能

**建议：** 至少使用这个选项，你希望新 LLM 的 UI/UX 技能开箱即用就很棒。

---

### 2️⃣ Anthropic/Claude 官方技能库

**GitHub：** https://github.com/anthropics/skills

**说明：** Anthropic/Claude 自己的技能库，甚至可以在其他 harness 中使用。特别推荐 UI/UX 相关技能。

---

### 3️⃣ Vercel 技能库

**GitHub：** https://github.com/vercel-labs/agent-skills

**推荐技能：**
- Vercel Web Design Guidelines
- Vercel React Best Practices
- Vercel Composition Patterns
- Vercel React Native Skills

**说明：** Vercel 的技能库备受尊敬。

---

## 🧠 Harness 工作原理

### OpenClaw 人格系统

**系统提示构建：** 每次轮次连接 5 个 markdown 文件

| 槽位 | 文件 | 用途 |
|------|------|------|
| **Slot 1** | SOUL.md | 个性、哲学、声音 |
| **Slot 2** | IDENTITY.md | 名称、表情符号、展示元数据 |
| **Slot 3** | USER.md | 用户上下文、偏好、时区 |
| **Slot 4** | AGENTS.md | 操作规则、路由、安全 |
| **Slot 5** | TOOLS.md | 能力描述、工具策略 |

---

### 关键规则

| 规则 | 说明 |
|------|------|
| **SOUL.md 是槽位 #1** | 塑造下游一切。三个"人性化"技能放在这里 |
| **AGENTS.md 用于操作** | 不要放个性规则。不要跨文件复制 SOUL.md 内容（浪费 token 且产生矛盾） |
| **位置** | `~/.openclaw/workspaces/[agent-name]/SOUL.md` |
| **最大文件大小** | 20,000 字符（由 `agents.defaults.bootstrapMaxChars` 控制） |
| **总 bootstrap 上限** | 150,000 字符（所有文件） |
| **缺失文件** | 注入短标记。空 SOUL.md 回退到默认个性 |
| **子代理** | 仅注入 AGENTS.md 和 TOOLS.md。如需要子代理个性，用 `agent:bootstrap` 钩子注入 SOUL.md |
| **验证** | 用 `/context list` 或 `/context detail` 验证注入和 token 消耗 |

---

### Hermes Agent 人格系统

**位置：** `~/.hermes/SOUL.md`（或 `$HERMES_HOME/SOUL.md`）

**关键区别：**

| 特性 | 说明 |
|------|------|
| **SOUL.md** | 持久身份，系统提示槽位 #1 |
| **/personality [name]** | 会话级覆盖（临时） |
| **config.yaml** | `agent.personalities` 下的命名个性预设 |
| **Profiles** | 完全隔离实例，独立 SOUL.md 文件 |

---

### 关键规则

| 规则 | 说明 |
|------|------|
| **SOUL.md 占据槽位 #1** | 替换硬编码默认身份 |
| **SOUL.md 仅从 HERMES_HOME 加载** | 不从当前工作目录加载（防止项目间意外个性变化） |
| **空或不可读 SOUL.md** | 回退到："You are Hermes Agent, an intelligent AI assistant created by Nous Research..." |
| **SOUL.md 扫描** | 注入前扫描提示注入模式 |
| **/personality concise** | 会话覆盖，修改当前会话行为但不改变 SOUL.md |
| **命名预设** | config.yaml 支持字符串格式和字典格式（含 description/system_prompt/tone/style 键） |
| **Profiles** | `hermes profile create [name]` 创建完全隔离环境（独立 config/SOUL.md/memory/sessions/skills） |
| **多组网关** | config.yaml 中的 `topic_configs` 允许每聊天个性覆盖 |

---

### 其他 Harness

**适用于：** Cline、Cursor、OpenCode 或任何接受系统提示的工具

**方法：**
- 将三个技能组合粘贴为系统提示或自定义指令字段
- 一些工具有字符限制
- 如截断，优先 Skill 1（Voice）— 每 token 影响最高

---

## 🧬 三个 LAYER（人性化技能）

### 科学原理

AI 检测研究显示 LLM 文本在三个可测量维度上失败：

#### 1. 低 perplexity（困惑度）

**问题：** AI 做最可预测的词选择。

**人类特征：**
- 选择意外词汇
- 使用俚语
- 做统计上不太可能的刻意风格选择

**Skill 1 解决：** 禁止 50+ 最可预测 AI 短语，强制执行结构变化。

---

#### 2. 低 burstiness（爆发度）

**问题：** AI 产生统一长度和节奏的句子。

**人类特征：**
- 长复合句和两词片段之间剧烈交替
-  deliberate 节奏变化

**Skill 1 强制执行：** deliberate 节奏变化。

---

#### 3. 缺乏情感校准

**问题：** 人类在对话中自动镜像情感状态（镜像神经元系统）。AI 要么忽略情感上下文，要么用感觉表演性而非真诚的脚本共情短语回应。

**Skill 2 实现：** 基于认知共情（观点采择）和情感共情（情感共鸣）的状态检测和响应协议。

---

#### 4. 缺乏心智理论

**问题：** 人类建模对话者的心理状态并相应调整沟通。AI 同样对待每条消息，无视发送者的知识水平/情感状态/意图。

**Skill 2 元规则 + Skill 3 决策框架：** 实现基础心智理论。

---

#### 5. 无持久角色

**问题：** 人类个性在上下文中稳定。同一人在每次对话中使用相似习语/推理模式/幽默。AI 个性每次会话重置（或会话内漂移）。

**Skill 3：** 通过 SOUL.md 每次重新注入创建稳定角色，具有特定可识别模式。

---

### LAYER 1：人性化作家

**功能：** 在语法层面重写模型的语言 DNA。

**目标：**
- 消除使 AI 文本可检测的模式
- 替换为产生具有自然 perplexity 和 burstiness 散文的规则

---

### LAYER 2：情商层

**功能：** 教导模型检测并适当响应 7 种情感状态，不表演。

**问题：** 大多数开源模型要么完全忽略情感上下文，要么用脚本治疗语言回应。

**解决：** 这个技能创造真正的响应能力。

---

### LAYER 3：个性引擎

**功能：** 不是让你填写的模板。是问你问题然后基于答案构建代理个性的系统。

**输出：** 对你独特的定制 SOUL.md 个性部分。

**使用方式：**
- 作为 OpenClaw/Hermes 技能安装：作为互动对话运行
- 手动使用：回答下方问题，然后将生成输出粘贴到 SOUL.md（Layer 1 和 2 之后）

---

## 📝 实施清单

### 步骤 1：选择替代方案

- [ ] 评估 GLM 5.1（最推荐）
- [ ] 评估 Minimax 2.7
- [ ] 评估 Codex（后端/编码最强）
- [ ] 或准备本地运行（GLM 5/Qwen 3.5/Kimi 2.5/Minimax 2.5）

### 步骤 2：安装 UI/UX 技能

- [ ] 安装 ui-ux-pro-max-skill（必用）
- [ ] 可选：Anthropic 官方技能库
- [ ] 可选：Vercel 技能库

### 步骤 3：实施三个 LAYER

- [ ] LAYER 1：人性化作家
- [ ] LAYER 2：情商层
- [ ] LAYER 3：个性引擎

### 步骤 4：更新 SOUL.md

- [ ] 将三个 LAYER 放入 SOUL.md（槽位 #1）
- [ ] 确保 AGENTS.md 仅用于操作规则
- [ ] 用 `/context list` 验证注入

### 步骤 5：测试和优化

- [ ] 测试对话质量
- [ ] 测试 UI/UX 输出
- [ ] 根据反馈调整

---

## 💡 关键洞察

### 洞察 1：替代方案成熟度

| 模型 | 编码能力 | 对话能力 | UI/UX | 成本优势 | 开放性 |
|------|----------|----------|-------|----------|--------|
| **GLM 5.1** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | 3x 便宜 | 即将开源 |
| **Minimax 2.7** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 性价比高 | 即将开源 |
| **Codex** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | 3-4x 大方 | 闭源 |
| **本地 LLM** | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ | 仅电费 | 免费开源 |

---

### 洞察 2：技能优先级

| 优先级 | 技能 | 影响 |
|--------|------|------|
| **必须** | ui-ux-pro-max-skill | UI/UX 质量开箱即用 |
| **高** | LAYER 1（人性化作家） | 文本不可检测性 |
| **高** | LAYER 2（情商） | 情感响应质量 |
| **中** | LAYER 3（个性） | 持久角色 |
| **可选** | Anthropic/Vercel 技能 | 额外增强 |

---

### 洞察 3：SOUL.md 关键性

**SOUL.md 是槽位 #1** — 塑造下游一切。

**常见错误：**
- ❌ 将个性规则放入 AGENTS.md
- ❌ 跨文件复制 SOUL.md 内容
- ❌ 浪费 token 且产生矛盾

**正确做法：**
- ✅ 三个 LAYER 放入 SOUL.md
- ✅ AGENTS.md 仅用于操作
- ✅ 不重复内容

---

### 洞察 4：Harness 选择策略

| 情况 | 推荐 | 原因 |
|------|------|------|
| **用 OpenClaw** | GLM 5.1 / Minimax 2.7 | 不会禁止，成本低 |
| **用 Hermes** | GLM 5.1 / Minimax 2.7 | OpenAI 可能禁令 |
| **主要编码** | Codex | 后端/编码野兽 |
| **主要对话** | GLM 5.1 + 三个 LAYER | 对话 + 情商最佳 |
| **有强大 PC** | 本地 LLM | 私有 + 免费 |

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **GLM 订阅** | https://z.ai/subscribe |
| **Minimax** | https://www.minimax.io/ |
| **KiloCode 基准** | https://blog.kilo.ai/p/we-tested-minimax-m27-against-claude |
| **ui-ux-pro-max-skill** | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill |
| **Anthropic 技能库** | https://github.com/anthropics/skills |
| **Vercel 技能库** | https://github.com/vercel-labs/agent-skills |
| **原文推文** | https://x.com/meta_alchemist/status/2040416725775352258 |

---

## 📊 翻译信息

| 项目 | 信息 |
|------|------|
| **翻译时间** | 2026-04-05 |
| **原文作者** | Meta Alchemist (@meta_alchemist) |
| **原文平台** | X (Twitter) |
| **原文数据** | 417👍 38🔁 194K👁️ 1,675🔖 |
| **翻译状态** | ✅ 完整翻译 + 实施指南 |

---

## 🎯 TL;DR 总结

| 要点 | 核心信息 |
|------|----------|
| **背景** | Anthropic 禁止第三方工具 OAuth，需替代方案 |
| **最佳替代** | GLM 5.1（3x 便宜）/ Minimax 2.7 / Codex（编码最强） |
| **UI/UX 技能** | ui-ux-pro-max-skill（58k stars）必用 |
| **人性化 LAYER** | 3 层：作家/情商/个性，放入 SOUL.md |
| **SOUL.md 位置** | 槽位 #1，塑造一切，不重复到 AGENTS.md |
| **本地选项** | GLM 5/Qwen 3.5/Kimi 2.5/Minimax 2.5 免费开源 |

**总成果：** 即使离开 Claude，也能用替代方案 + 技能获得同样优秀体验。

---

*翻译完成时间：2026-04-05 | 版本：v1.0*
