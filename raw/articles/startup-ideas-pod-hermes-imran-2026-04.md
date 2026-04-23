# The Hermes Agent clearly explained (how to use it)

**来源**: The Startup Ideas Podcast (SIP) @startupideaspod  
**发布日期**: 2026-04-20  
**链接**: https://x.com/startupideaspod/status/2046310040207016342  
**数据**: 117K 浏览，345 点赞，955 收藏  
**主角**: Imran (@imranye) — Hermes 深度用户，在基金工作

---

## 为什么离开 OpenClaw

三个问题叠加：

1. **没有内置记忆** — 他不得不反复告诉 agent 同样的事情
2. **网关需要重启** — 有一天每小时重启一次
3. **Token 花费无透明度** — 完全不知道什么在烧钱

他先试了 Nebula。适合 AI 同事，但不适合需要随时间学习的个性化工作流。然后转向 Hermes。

---

## Hermes 的核心优势

| 特性 | 说明 |
|------|------|
| **内置记忆** | 每个成功完成的任务都会写入记忆，越用越好用 |
| **可搜索历史** | 标准 SQLite 数据库，忘记保存的东西（如 API key）可以搜日志找回 |
| **稳定性** | Imran 超过一周没重启过 |
| **40+ 预装工具** | 浏览器、网页搜索、cron jobs、图像生成、Home Assistant |
| **预装 Skills** | MacBook 上包括 Apple Notes、Reminders、Find My、iMessage |

---

## 如何降低 90% Token 花费

**两个动作：**

1. **用 OpenRouter** — 清晰的每 token 定价，每周轮换免费模型（录制时 NVIDIA NemoTron 免费）
2. **把重复任务转为代码** — 每天运行的任务让 agent 写一次代码，之后变成确定性任务，不再需要 agent 参与

**他的数字：**
- 之前：~$130 / 5 天
- 之后：~$10 / 5 天
- 能力相同

---

## 安全设置

可以让 Hermes 自审：*"Is this secure? Tell me why or why not."*

它会检查：
- 明文密钥
- 弱防火墙配置
- 暴露的 secrets

**三种运行模式：**
1. Bare metal（Imran 在用，每日更新）
2. Docker 容器（与文件隔离）
3. Modal（serverless）

---

## Android 安装（重点）

**需要两个额外应用：**
- Termux（Android 内的终端）
- Termux API（F-Droid 下载，提供传感器访问：电池、Wi-Fi、音量、相机、亮度、振动）

**为什么重要：**
便宜的 Android 手机 + SIM 卡 = 常开、低功耗的专用 agent 设备。不需要抢购 Mac Mini。

**解锁能力：**
- 从真实设备发社交媒体（不用被限流的调度 API）
- 直接读 SMS
- 自动化 2FA 验证码

Imran 在 Solana Seeker Android 手机上跑，命名为 "Cookie Monster"（他的 agent 都以 Muppets 命名）。

---

## 实际使用模式

**Imran 的模式：先解决个人问题**

第一个突破点是晚餐。他用 Telegram 语音备忘录录了 8 分钟，描述 pantry 里所有食材。现在 agent 根据现有食材和健身目标，每天发他 3 个食谱。

**小问题，大心理负担减轻。**

**其他已运行的自动化：**
- 早晨 Gmail 分类（删除垃圾、取消无用订阅、返回重要摘要）
- 费用报告
- Obsidian vault（agent 自己整理）

**关于 Obsidian：**
他之前不是用户。现在是他的 home dashboard。Markdown 文件每天早晨被 agent 操作：今日任务、本周优先级、即将到来的旅行、工作、个人事务。

**这不是他设计的。agent 用了约 20 天自己搭建的。**

Imran 认为 **7 天持续使用** 就能达到大部分效果。

---

## 他对自己跑的 Prompts

每天结束时 meta-prompt agent：

1. What have I been procrastinating on?
2. What's the most important thing to work on today?
3. What tasks am I doing every day that I should automate?
4. What's one tool you can build me tonight that would make my life easier tomorrow?
5. Is there anything important today that I missed?

> 这些读起来很明显。但大多数人从不问。

---

## 一个 vs 多个 Agent

Imran 跑 4 个。他是 tinkerer。他认为真正答案是 1-2 个：一个个人，一个工作。

**原因：** 如果在 Fortune 500 工作，公司不会让你在工作机器上运行装满私人数据的个人 agent。分开保持干净，就像 to-do app 分开个人和工作列表。

**Cron jobs vs Sub-agents：**
- 他运行 recurring tasks 作为 cron jobs，不是 sub-agents
- Sub-agents 可以让便宜任务用便宜模型（如 Gmail triage 可以用小模型）
- 两种都可行，领域还在探索

---

## 推荐安装的 Skills

1. **Obsidian skill**（即使不用 Obsidian CLI）
2. **G-Stack by Gary Tan** — 原本为 Cloud Code 构建，把 YC 创业流程（每周迭代、正确问题、代码级决策）bolt 到 agent 上，免费
3. **Honcho dev memory skill** — 帮助因为 Hermes 有记忆限制，小 context 有帮助
4. **你自己的** — 银行账单、个人财务、健身。为你已经付费的东西构建。

---

## 两个非谈判项

1. **每晚更新** — 还是 beta。Imran 九天没更新后落后 535 commits
2. **锁定安全** — 设置 Telegram 或 WhatsApp 访问，安装 Tailscale 让手机和电脑在同一虚拟网络，然后从任何地方 SSH 进入

---

## 更大的想法

> 学习使用个人 agent 不是技能。它正在变成**必需能力**。

Imran 在基金工作。因为 agent 处理后台工作，他能多和 20-30% 的创始人交流。更好的信号、更好的 deal flow、更好的回报。

> 重点不是工具。是工具帮你从盘子里清掉什么。

> 定制 agent 不是技能。用它完成工作才是。

---

## 结语

> Hermes Agent 就像 90 年代的 tuner car culture。找零件、装上、变成你的。

> 但记住你在优化什么。不是车。是你开车要去的地方。

---

**Follow Imran**: @imranye
