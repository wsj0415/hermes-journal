---
title: Hermes 最佳实践汇总
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [best-practice, workflow, automation, hermes-power-user]
sources: [raw/articles/startup-ideas-pod-hermes-imran-2026-04.md, raw/articles/ksimback-hermes-beginners-guide-2026-04.md]
reviewed: false
confidence: high
confidence_reason: 综合官方指南和深度用户实证经验
---

## 编译知识

基于 Kevin Simback（Hermes Atlas 维护者）的官方指南和 Imran（基金从业者，深度用户）的实证经验，汇总 Hermes 最佳实践。

---

## 快速入门（第一个周末）

### 1. 安装（2 分钟）

```bash
# Mac 首次安装开发工具
xcode-select --install

# 一行安装 Hermes
# 参考官方文档最新命令
```

### 2. 选择模型

```bash
hermes model
# 查看所有可用 provider 和 model
```

**推荐起点：**
- **CLI coder** → 用 Claude/GPT-5.4
- **自动化操作** → 用 OpenRouter + 中等模型
- **Telegram 用户** → 用 GLM-5.1/MiniMax（性价比高）

### 3. 第一个工作流

**从个人问题开始**（Imran 模式）：
- 不要一上来就搞复杂的工作自动化
- 先解决一个让你烦恼的小问题
- 学会范式比完成大项目更重要

**Imran 的第一个突破：** 晚餐食谱
- 录 8 分钟 Telegram 语音描述 pantry 食材
- Agent 每天根据现有食材 + 健身目标发 3 个食谱
- 小问题，大心理负担减轻

---

## 三种用户类型

| 类型 | 特征 | 先用什么 | 暂时忽略 |
|------|------|----------|----------|
| **CLI Coder** | 住终端里，用 Claude Code/Cursor | CLI, skills, memory | Telegram, cron, multi-agent |
| **自动化操作** | 不一定要写代码，想要 recurring jobs | cron, messaging, memory | code execution, multi-agent |
| **Telegram 用户** | 手机随时访问 | messaging gateway, voice, skills | local CLI usage |

---

## 核心架构理解

### Harness Engineering

Nous 的核心赌注：**2026 年的解锁不是更聪明的模型，是更聪明的 wrapper**。

Hermes 在 LLM 周围投入五层：
1. **Instructions** — 系统提示词
2. **Constraints** — 边界和限制
3. **Feedback** — 执行结果反馈
4. **Memory** — 持久化记忆
5. **Orchestration** — 任务编排

模型可以换：今天用前沿，明天用本地，后年用别的。

### 学习循环（The Learning Loop）

每几次工具调用，Hermes 自问：
> *what just happened, what worked, what failed, should this become a skill?*

如果答案是 yes → 写入 `~/.hermes/skills/` → 以后复用。

**这是最重要的功能。**

---

## Token 优化（90% 成本降低）

### 策略一：OpenRouter
- 清晰定价，所有模型一目了然
- 每周轮换免费模型

### 策略二：代码化重复任务
- 每天运行的任务 → agent 写代码 → 之后零 token

**Imran 的数字：** $130/5 天 → $10/5 天

详见 [[hermes-token-optimization]]

---

## 部署模式

### 1. Bare Metal（推荐）
- Imran 在用
- 每日更新
- 性能最好

### 2. Docker 容器
- 与文件隔离
- 更安全

### 3. Modal（Serverless）
- 按需运行
- 零运维

### 4. Android（进阶）
- Termux + Termux API
- 常开、低功耗、真实设备
- 解锁 SMS、传感器、不限流发布

详见 [[hermes-android-deployment]]

---

## 安全设置

### 自审命令
```bash
hermes "Is this secure? Tell me why or why not."
```

它会检查：
- 明文密钥
- 弱防火墙配置
- 暴露的 secrets

### 非谈判项（Imran）

1. **每晚更新** — 还是 beta，9 天不更新落后 535 commits
2. **锁定访问** — Telegram/WhatsApp + Tailscale 组网

---

## 每日 Meta-Prompts

Imran 每天结束时间 agent：

1. What have I been procrastinating on?
2. What's the most important thing to work on today?
3. What tasks am I doing every day that I should automate?
4. What's one tool you can build me tonight that would make my life easier tomorrow?
5. Is there anything important today that I missed?

> 这些读起来很明显。但大多数人从不问。

---

## 推荐 Skills

| Skill | 用途 | 来源 |
|-------|------|------|
| **Obsidian** | 即使不用 CLI，markdown 组织很有用 | 内置 |
| **G-Stack** | YC 创业流程 bolt 到 agent | Gary Tan（免费） |
| **Honcho dev memory** | 小 context 帮助记忆限制 | 社区 |
| **自定义** | 银行、财务、健身 | 自己建 |

---

## 7 天采用曲线

Imran 的经验：

| 天数 | 状态 |
|------|------|
| **Day 1** | 安装，跑第一个任务 |
| **Day 3** | 开始理解学习循环 |
| **Day 7** | 大部分效果达成 |
| **Day 20** | Agent 自己搭建 Obsidian dashboard |
| **Day 30** | 它是 *你的* assistant，不是通用 assistant |

---

## 一个 vs 多个 Agent

**Imran：** 跑 4 个，但认为 1-2 个足够（1 个人 +1 工作）

**原因：** Fortune 500 不会让你在工作机器上运行装满私人数据的个人 agent。分开保持干净。

---

## 心态调整

> 学习使用个人 agent 不是技能。它正在变成**必需能力**。

> 重点不是工具。是工具帮你从盘子里清掉什么。

> 定制 agent 不是技能。用它完成工作才是。

> Hermes 就像 90 年代 tuner car culture。找零件、装上、变成你的。但记住你在优化什么——不是车，是你开车要去的地方。

---

## 时间线

- **2026-04-20**: Kevin Simback 发布官方新手指南 [[raw/articles/ksimback-hermes-beginners-guide-2026-04]]
- **2026-04-20**: Imran 在 The Startup Ideas Podcast 分享实证经验 [[raw/articles/startup-ideas-pod-hermes-imran-2026-04]]
- **2026-04-23**: 本页面创建，综合两来源

---

## 相关工作

- [[imran-hermes-power-user]] — Imran 深度使用案例
- [[hermes-token-optimization]] — Token 优化策略
- [[hermes-android-deployment]] — Android 部署模式
- [[llm-wiki-karpathy]] — Karpathy 知识库模式（Hermes 灵感来源）
