# Nick Spisak — Hermes Agent 完整使用指南

**来源**: https://x.com/nickspisak_/status/2042664522151006664  
**作者**: Nick Spisak (@nickspisak_)  
**抓取时间**: 2026-04-12 18:09 UTC  
**类型**: X 推文线程/完整教程  
**标签**: hermes-agent, nous-research, ai-automation, learning-loop, skill-graph, telegram-bot, mcp-protocol, claude-code-comparison, openclaw-migration, personal-automation

---

## 📊 一句话总结

Nick Spisak 分享 Hermes Agent 的实用设置指南，涵盖 30 秒定义/学习循环原理/与 Claude Code/OpenClaw 区别/7 个真实工作流（每日简报/用户报告审查/竞争监控/多合一代理/LLM Wiki/自动研究/交易自动化），2 个月 50K stars，核心差异是 Hermes 存储可执行程序而非仅记忆偏好，每次任务让它下次更好。

---

## 🏷️ 话题标签

#HermesAgent #NousResearch #AI 自动化 #学习循环 #SkillGraph #TelegramBot #MCP 协议 #ClaudeCode #OpenClaw #个人自动化

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：Hermes vs Claude Code vs OpenClaw 对比图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Technical comparison diagram for "Hermes vs Claude Code vs OpenClaw".

Layout: 3-column comparison showing where each agent lives and what it does.

Color Palette:
- Hermes: Purple (#8B5CF6)
- Claude Code: Blue (#3B82F6)
- OpenClaw: Green (#10B981)
- Background: Dark gradient

Column 1 — Claude Code:
图标：代码仓库
"lives in your repo"
"Reads codebase, writes code, runs tests"
"Best for: software development"
❌ "No server"
❌ "No Telegram"
❌ "No recurring jobs"

Column 2 — OpenClaw:
图标：服务器
"lives on your server"
"Personal agent with messaging/scheduling"
"Best for: personal automation"
❌ "No learning loop"
❌ "No auto-skill writing"

Column 3 — Hermes:
图标：服务器 + 大脑
"lives on your server + learning loop"
"Every task makes it marginally better"
"Best for: everything except coding"
✅ "Telegram/Discord/Slack/WhatsApp"
✅ "Auto-learns skills"
✅ "Recurring jobs while you sleep"

Bottom — Architecture:
"Run BOTH: Claude Code for code, Hermes for everything else"
"Same MCP protocol → tools work in both"
"One infrastructure, two agents, zero duplication"

Badge:
"50K stars in 2 months" | "Learning Loop" | "Executable Procedures"

Style: Clean technical comparison, dark mode with neon column colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 Hermes 与 Claude Code/OpenClaw 对比的内容，三列对比图直接展示每个 agent 的定位和差异，比单一架构图更精准传达"为什么同时运行两者"的核心信息。

---

### 选项 2:7 工作流全景图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
7 Hermes Workflows infographic showing real use cases.

Layout: Grid of 7 workflow cards with icons and outcomes.

Color Palette:
- Each workflow: Unique color
- Background: Dark gradient

7 Workflows:

1. Daily Briefing 🌅 (Blue)
"Monitor email/calendar/topics"
"Telegram summary every morning"
"Day 30 learns your preferences"

2. User Report Review ✅ (Green)
"Read reports, check metadata"
"Apply valid fixes, log changes"
"Replaced manual review entirely"

3. Competitor Monitoring 📊 (Purple)
"Camoufox stealth browser"
"Track pricing/jobs/news"
"Diff of what changed overnight"

4. Unified Agent 🎯 (Yellow)
"One Hermes for marketing/outreach/community"
"Claude Code for codebase"
"Unified memory = compounding context"

5. LLM Wiki 🧠 (Red)
"Karpathy pattern built-in"
"Raw sources → wiki pages"
"Auto-maintained, cross-referenced"

6. Auto Research 🔬 (Cyan)
"Change → Test → Keep winner → Repeat"
"Email rates, conversion, response time"
"Gets better at predicting what works"

7. Trading Automation 💰 (Orange)
"Brokerage API + 4 strategies"
"Live account, real money"
"Define goal + constraints, Hermes experiments"

Bottom Badge:
"2 min install" | "15 tool calls → new skill" | "Day 30 ≠ Day 1"

Style: Modern workflow grid, dark mode with rainbow workflow colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：学习循环流程图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Hermes Learning Loop flowchart showing how skills are created.

Layout: Circular flow showing task → reflection → skill creation.

Color Palette:
- Task: Blue (#3B82F6)
- Reflection: Purple (#8B5CF6)
- Skill: Green (#10B981)
- Background: Dark gradient

Learning Loop (circular):

Step 1 — Task Execution:
"Give Hermes a job"
"Research, monitor, automate"
"~15 tool calls"

Step 2 — Pause & Reflect:
"Every 15 tool calls, Hermes pauses"
"What worked?"
"What failed?"
"What took too long?"

Step 3 — Skill Creation:
"Write skill → ~/.hermes/skills/"
"Markdown file, human readable"
"Reusable workflow saved"

Step 4 — Next Task:
"Day 1: generic summary"
"Day 30: tighter, relevant, your format"
"Learned from watching you"

Center Badge:
"Claude Code stores facts"
"Hermes stores executable procedures"
"Doesn't remember you like bullets"
"Remembers entire workflow that produces bullets"

Bottom — Comparison:
"Day 1 ≠ Day 30" | "Compounding capability" | "Editable skills"

Style: Modern circular flowchart, dark mode with neon step colors
Aspect ratio: 9:16 portrait
```

---

## Hermes Agent 是什么（30 秒）

**定义**: Hermes 是个人自动化 agent，住在服务器（或笔记本）上，通过消息应用（或 CLI）与你对话。

**核心特点**:
- 始终在线系统
- 处理重复性工作
- 监控你关心的事
- 自动学习
- 创建可复用技能

**安装**（2 分钟）:
```bash
# 1. curl 安装脚本
curl ... | bash

# 2. 选择模型
hermes model

# 3. 连接 Telegram
hermes gateway setup
```

**完成**。你有 agent 了。

---

## 学习循环如何工作

### 核心机制

```
每~15 个工具调用 → Hermes 暂停 → 反思 → 写技能
```

**反思内容**:
- 什么有效
- 什么失败
- 什么花太长时间

**输出**:
- Markdown 技能文件保存到 `~/.hermes/skills/`
- 将学到的转为可复用工作流
- **人类可读/可编辑/可删除**

---

### Day 1 vs Day 30

| 时间 | 输出质量 | 原因 |
|------|----------|------|
| **Day 1** | 通用总结 | 还没学过你偏好 |
| **Day 30** | 更紧凑/更相关/你的格式 | 从你回应/忽略的内容学习 |

**关键差异**:
- Claude Code 记忆存储**关于你偏好的事实**
- Hermes 记忆存储**可执行程序**

> 它不只记得你喜欢项目符号。它记得产生你想要的项目符号的整个研究 - 过滤 - 格式工作流。

---

## Hermes vs Claude Code vs OpenClaw

### 定位对比

| Agent | 住在哪里 | 做什么 | 最佳用途 | 缺少什么 |
|-------|----------|--------|----------|----------|
| **Claude Code** | 你的仓库 | 读代码/写代码/跑测试/提交 | 软件开发 | 服务器/Telegram/重复工作 |
| **OpenClaw** | 你的服务器 | 消息/调度/工具访问 | 个人自动化 | 学习循环/自动写技能 |
| **Hermes** | 你的服务器 + 学习循环 | 每次任务让它下次更好 | 除编码外的一切 | 无（专为非编码设计） |

---

### 为什么同时运行两者

**架构**:
```
Claude Code → 软件开发
Hermes → 研究/简报/监控/自动化

Same MCP protocol → 你的工具在两者都工作
One infrastructure → Two agents → Zero duplication
```

**建议**: 停止比较它们。为软件开发运行 Claude Code，为其他一切运行 Hermes。

---

## 7 个真实工作流

### 1. 每日简报（Daily Briefing）

**设置**:
```bash
hermes gateway setup  # 连接 Telegram
# 告诉它监控：邮件/日历/2-3 个主题
# 设为重复任务
```

**输出**: 每天早上一条 Telegram 消息，包含摘要

**复合收益**:
- 两周后，Hermes 学会：
  - 你回应哪些邮件发送者
  - 你为哪些会议准备
  - 哪些主题让你问后续问题
- 技能文件自我更新
- Day 30 的简报看起来和 Day 1 完全不同

**支持平台**: Telegram/Discord/Slack/WhatsApp/Signal/Email/Home Assistant（15+）

---

### 2. 用户报告审查（User Report Review）

**用例**: 实时网站审查传入用户报告，决定是否应更正元数据

**流程**:
```
读取报告 → 检查现有数据 → 应用有效修复 → 记录更改
```

**结果**: 完全替换手动审查流程

---

### 3. 竞争监控（Competitor Monitoring）

**工具**:
- **Camoufox**: 隐身浏览器，不像普通自动化工具那样被指纹识别
- **Firecrawl**: 结构化提取

**设置**:
```
指向：竞争对手定价页面/招聘网站/新闻来源/产品列表
Hermes 处理：提取/变更追踪/知道什么是新的 vs 昨天已展示
```

**收益**: 停止每天早上手动检查 10 个标签，开始获得夜间实际变更的差异报告

---

### 4. 多合一代理（Unified Agent）

**案例**: 零员工 fintech 初创公司

**失败尝试**:
```
5 个专用 AI agent:
- Marketing
- Sales development
- Engineering
- Community
- Daily briefings

结果：48 小时内失败
- Agent 无法共享上下文
- 技能跨系统重复
- 品牌声音在不同渠道不一致
```

**成功方案**:
```
1 个 Hermes 实例：
- Marketing
- Outreach
- Community management
- Daily briefings

Claude Code: 处理代码库
```

**收益**: 统一记忆意味着每个功能将上下文注入其他功能。当工作跨 5 个断开工具分割时，这种复合不会发生。

---

### 5. LLM Wiki（Karpathy 模式）

**内置**: Hermes 内置 Karpathy 的 LLM Wiki 模式作为内置技能

**设置**:
```
告诉它创建 wiki → 指向来源 → 它组织为互联 Markdown 文件
```

**三层结构**:
1. **Raw sources**: 放入且从不修改
2. **Wiki pages**: agent 编写和维护
3. **Schema file**: 定义规则保持一致性

**Hermes 特定优势**: 学习循环意味着 wiki 自动维护
- 添加新来源 → agent 不只归档它
- 检查现有页面
- 更新任何变更
- 添加交叉引用
- 标记矛盾

**结果**: 一个月常规使用后，你有合成一切输入的复合知识库

**社区技能**: 643 个社区技能在 Skills Hub 可用，用 `/skills` 浏览

---

### 6. 自动研究（Auto Research）

**模式**:
```
AI agent 小改变 → 测试是否有效 → 保留赢家 → 再试
自动重复
```

**适用**:
- 邮件打开率
- 落地页转化
- 潜在客户响应时间

**Hermes 优势**: 学习循环意味着它不只随机测试。基于已尝试内容，它变得更擅长预测哪些变化有效。

**案例**:
- Builder 给 Hermes 经纪 API key，构建 4 个自动化交易策略
- 部署到真实账户
- 另一人在 Solana 上运行自动化 token 操作

**这些不是演示，是处理真金的生产系统**。

---

### 7. MCP 协议兼容

**v0.8.0**: 原生 MCP 客户端支持

**MCP**: 与 Claude Code 相同的工具集成协议

**收益**:
- 为 Claude Code 构建/安装的每个 MCP 服务器与 Hermes 一起工作
- Google Workspace 连接器/数据库工具/自定义 API
- Hermes 自动发现它们
- 无需重建/无需重新配置

**作者设置**:
```
Claude Code → 写代码/管理仓库
Hermes → 研究/简报/监控/自动化（使用已配置的相同 MCP 服务器）
```

---

## 模型选择（关键！）

### #1 错误：错误模型选择

**问题**: 人们责怪框架，实际是模型在工具调用上失败

**案例**:
- Builder 在 v0.8.0 更新后连续跑 Hermes 近 3 小时 — 但仅在切换到 frontier 模型后
- 其他人尝试大开源模型 → agent 幻觉不存在的工具调用

**推荐**:
| 用途 | 模型 |
|------|------|
| **本地实验** | Gemma 4 26B via Ollama（最佳当前选项） |
| **生产工作流** | Frontier model API（Nous Portal/OpenRouter/OpenAI/自有端点） |

**切换模型**:
```bash
hermes model  # 无代码变更/无锁定
```

**诊断**:
```bash
hermes doctor  # 在花费数小时猜测前诊断配置问题
```

---

## OpenClaw 迁移

**从 OpenClaw 来**？一个命令导入一切：
```bash
hermes claw migrate
```

**导入内容**:
- Persona
- Memories
- Skills
- API keys
- Messaging settings

**5 分钟完成**。

---

## 关键数据

| 指标 | 数值 |
|------|------|
| GitHub Stars | 50K（2 个月） |
| 安装时间 | 2 分钟 |
| 技能创建频率 | 每~15 工具调用 |
| 支持消息平台 | 15+ |
| 社区技能 | 643 |
| 版本 | v0.8.0 |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Claude Code 记忆存储事实，Hermes 记忆存储可执行程序" | 核心差异 |
| "Day 30 版本才值得评估" | 学习循环价值 |
| "停止比较它们，运行两者" | 架构建议 |
| "统一记忆 = 复合上下文" | 多合一代理优势 |
| "每次任务让它下次更好" | 复合能力 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **学习循环** — 每~15 工具调用后反思写技能
2. **可执行程序记忆** — 非仅事实，是整个工作流
3. **技能文件人类可读** — 可打开/阅读/编辑/删除
4. **MCP 协议兼容** — 工具在多个 agent 间共享
5. **复合知识** — Day 1 ≠ Day 30
6. **多消息平台支持** — Telegram/Discord/Slack 等

### 可实施
- 实现技能自动创建机制
- 存储可执行工作流而非仅偏好
- 使技能文件人类可读可编辑
- 支持多消息平台
- 实施定期反思循环
- 追踪 Day 1 vs Day 30 输出质量差异

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Hermes Agent GitHub | https://github.com/NousResearch/Hermes |
| Nick Spisak 原文 | https://x.com/nickspisak_/status/2042664522151006664 |
| LLM Wiki 指南 | https://x.com/NickSpisak_/status/...（文中提及） |
| Auto Research 指南 | https://x.com/NickSpisak_/status/...（文中提及） |

---

*原始来源：https://x.com/nickspisak_/status/2042664522151006664*
