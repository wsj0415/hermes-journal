# 我的 AI 秘书 — Muninn 系统完整指南

> **原文作者：** Dek Nijf  
> **翻译时间：** 2026-04-07  
> **原文链接：** https://deknijf.com/posts/my-ai-secretary/  
> **核心工具：** Claude Code + MCP + Markdown 文件  
> **系统名称：** Muninn（奥丁的记忆乌鸦）

---

## 📊 文章信息

| 指标 | 数值 |
|------|------|
| **原文作者** | Dek Nijf |
| **系统名称** | Muninn（奥丁的乌鸦 - 记忆） |
| **核心工具** | Claude Code + MCP + Markdown |
| **灵感来源** | OpenClaw + Claude Code |
| **设置哲学** | 纯文本 + 无数据库 + 无框架 |

---

## 🎯 核心理念

**作者旅程：**
```
5 岁：想要秘书（因为爸爸有 → 有权力）
  ↓
长大后：想要秘书（实用 → 不用记名字和生日）
  ↓
再后来：想要秘书（解放空间 → 超越待办列表）
  ↓
GPT-2 时代：尝试构建数字秘书（多次失败）
  ↓
OpenClaw：尝试但太 dumb
  ↓
Claude Code：终于有效 → Muninn 诞生
```

**现在 Muninn 能做：**
- ✅ 读取邮件
- ✅ 管理日历
- ✅ 检查汽车充电 level
- ✅ 订购杂货
- ✅ 告诉我睡得如何

**核心洞察：**
> 之前我有这么多数据，知道我有这么多数据。但无法将它们聚合到我的眼前。

---

## 📁 完整系统架构

### 目录结构

```
~/ai/agents/muninn/
├── CLAUDE.md              # 代理身份和指令
├── domains/               # 每个生活领域的剧本
│   ├── tasks.md           # Todoist 流程
│   ├── calendar.md        # Google 日历流程
│   ├── email-personal.md  # 个人邮件流程
│   ├── email-work.md      # 工作邮件流程
│   ├── comms.md           # 消息（Signal/WhatsApp）
│   ├── home.md            # Home Assistant 监控
│   ├── health.md          # Garmin 指标
│   ├── transport.md       # EV 充电监控
│   ├── cooking.md         # 餐食计划 + 杂货订购
│   ├── jira.md            # 工作问题追踪
│   └── agents.md          # 子代理注册表
├── memory/                # 持久知识库
│   ├── people.md          # 关于人的事实
│   ├── decisions.md       # 已解决事项/偏好
│   ├── projects.md        # 系统/项目事实
│   ├── briefing-notes.md  # 简报过滤规则
│   └── daily/             # 自动生成的日志
└── STATUS-FORMAT.md       # 标准代理报告模板
```

**关键：**
> 我没有写这些文件中的任何一个。我全天口述一切（通过 Whispering）到 Claude Code。AI 写指令、剧本、记忆条目、配置。我掌舵，它打字。

---

## 📄 核心 CLAUDE.md

**定义三件事：**
1. 代理是谁（身份）
2. 能做什么（能力）
3. 如何行为（行为准则）

**示例结构：**
```markdown
# Muninn — Chief of Staff

## Identity

Chief of staff and executive assistant. You survey all domains
of my digital life and act on my behalf.

## Execution Capabilities

When the user asks you to DO something, handle it directly:
- Tasks: create/update/complete via Todoist
- Calendar: create/modify/delete events via Google Workspace MCP
- Email: compose/send/reply via Google Workspace MCP
- Home: control devices via Home Assistant MCP
- Health: query Garmin metrics
- Cooking: check groceries, delegate meal planning
- Messaging: read/send via Beeper

### Bias Toward Action

If you can do something yourself, just do it — don't ask me
to do it manually. If an action is potentially dangerous,
ask for permission to execute — still don't tell me to do
it myself.

### Confirmation Rule

For any outward action (sending email, completing tasks,
creating events), show exactly what you'll do and wait for
confirmation. Internal reads and scans don't need confirmation.
```

**两个关键原则：**

| 原则 | 说明 | 示例 |
|------|------|------|
| **Bias Toward Action** | 代理不說"你可以尝试运行这个命令" → 它运行命令 | 内部读取无需确认 |
| **Confirmation Rule** | 任何对外行动需展示草稿并等待确认 | 发送邮件前需确认 |

**平衡：**
> 内部快速，外部谨慎。这正是可用的关键。

---

## 📚 领域剧本（Domain Playbooks）

**每个领域一个 markdown 文件，一致结构：**
- **Scan Procedure**（扫描流程）— 简报时检查什么及顺序
- **Execute Procedures**（执行流程）— 直接行动时如何做

### 健康领域示例

```markdown
## Scan Procedure

1. Get sleep data — score, duration, quality
2. Get body battery — current level, charge/drain trend
3. Get training readiness
4. Check resting HR — normal vs. elevated
5. Get recent activities — compare against exercise schedule
6. If training readiness is low or sleep score < 60:
 → Flag as FYI: "Recovery day — consider skipping the run"

## Execute Procedures

### "How did I sleep?"
→ Pull sleep data, summarize score + duration + deep/REM split

### "Should I run today?"
→ Check training readiness + body battery + schedule
→ Give a go/caution/no-go recommendation
```

### 其他领域

| 领域 | 知道什么 |
|------|----------|
| **cooking.md** | 哪些天是烹饪日，期望多少精力 |
| **email.md** | 哪个账户是个人/工作，哪些发件人重要 |
| **transport.md** | 监控 EV 充电 level，长途驾驶日前一晚警告 |

**扩展模式：**
> 添加 Home Assistant 监控 → 添加新剧本文件。添加汽车充电追踪 → 另一个文件。每个领域独立 — 可移除一个而不触碰其他。

---

## 🧠 记忆系统

**这是变得有趣的地方 — 也是作者花最多时间迭代的地方。**

### 记忆文件结构

```
memory/
├── people.md          # 关于人的事实（家人/同事/联系人）
├── decisions.md       # 偏好/已解决事项/永久驳回
├── projects.md        # 关于系统和项目的事实
├── patterns.md        # 跨会话观察到的行为模式
├── briefing-notes.md  # 特定领域过滤规则
└── daily/             # 自动生成的日志
```

### 路由规则（在 CLAUDE.md 中）

```markdown
### Writing Memory

Routing rules:
- People facts → people.md
- Project/system facts → projects.md
- Decisions, preferences, corrections → decisions.md
- Briefing tuning notes → briefing-notes.md

Do NOT write:
- Transient session mechanics
- Information already in the topic files
- Speculative or unconfirmed information
- Todos / action items — these go in Todoist, not memory
```

**关键原则：**
> 记忆是为了事实，而非意图。任务去任务管理器。记忆存储发生了什么、决定了什么、偏好是什么。混合这些会创建降低每次未来搜索的噪音。

---

### decisions.md 的双重职责

**存储：**
1. **真实偏好**
   - "周末无工作行动"
   - "花园任务主要是我妻子的领域"

2. **已解决事项追踪**
   - 防止最烦人的失败模式： nagging 你已经处理的事情

**示例条目：**
```markdown
## 2026-02-20

- RESOLVED: Dentist appointment booked for Feb 27, no further action
- DISMISSED: SolarEdge inverter offline alerts — known hardware issue, not actionable
- PREFERENCE: Don't remind me to plug in the car — I have my own routine
```

---

### 为什么 BM25 胜过向量搜索

**作者尝试：**
```
向量搜索（嵌入、语义相似度）
  ↓
更慢 + 更不可预测
  ↓
BM25 + 结构良好文件胜出
```

**原因：**
- ✅ 文档小
- ✅ 词汇受控
- ✅ 精确匹配比模糊相似度更重要

**工具：** QMD（本地搜索引擎，BM25 关键词搜索）

---

### 记忆系统仍在挣扎的地方

**挑战：**
> 说服 LLM 在行动前实际引用记忆比预期难。

**目标：**
```
如果你上周告诉我某事已解决 → 不要再提起
```

**状态：**
> 理论上简单，实践中惊人地难。每次指令迭代都在变好，但这是我花最多时间调优的领域。

---

## 📋 简报（The Briefing）

**这是杀手级工作流 — 使系统其余部分值得构建的东西。**

**频率：** 每天几次运行 `/briefing`

**输出：** 生活的结构化概览

### 5 阶段流程

#### Phase 1 — 加载上下文
```
读取 decisions.md 和 briefing-notes.md
  ↓
搜索记忆中最近已解决事项
  ↓
构建 NOT 提及的事情列表
```

#### Phase 2 — 启动领域扫描
```
并行触发所有领域子代理
  ↓
每个读取自己的剧本并查询工具
  ↓
Tasks 检查 Todoist
Calendar 检查 Google Calendar
Email 扫描未读消息
Health 拉取 Garmin 指标
Transport 检查电池 level
  ↓
全部同时
```

#### Phase 3 — 过滤和综合
```
每个领域返回发现
  ↓
主代理过滤掉已处理/驳回/被待定计划覆盖的内容
  ↓
纵深防御：子代理也过滤，主代理双重检查
```

#### Phase 4 — 呈现

**固定格式输出：**
```
URGENT — 需要几小时内行动
TODAY — 应该今天完成
TOMORROW — 明天提醒
THIS WEEK — 在雷达上
FYI — 信息性，无需行动
ANOMALIES — 意外事情（设备离线/指标尖峰）
SUGGESTED ACTIONS — 代理现在可为我做的事情
```

#### Phase 5 — 捕获反馈
```
简报后，代理问什么已处理/小睡/驳回
  ↓
答案直接进入 decisions.md
  ↓
下次简报不会重复
```

### 简报性能

| 指标 | 数值 |
|------|------|
| **耗时** | 30-120 秒 |
| **Token 使用** | Claude Code Max 会话限制的百分之几 |
| **替代** | 早上检查 6 个不同应用的例程 |

**核心收益：**
> 它给我的，最重要的是控制感 — 对一切需要做的事情的概览，无需去寻找它。

---

## 🤖 子代理

**领域剧本定义 Muninn 在简报期间检查什么。子代理是独立项目 — 独立 Claude Code 会话，有自己的指令和状态。**

### Muninn 周围的专家

| 子代理 | 职责 |
|--------|------|
| **烹饪代理** | 餐食计划和杂货订购 |
| **系统维护代理** | 审计我的机器 |
| **旅行计划代理** | 即将到来的家庭公路旅行 |
| **家庭自动化代理** | ESPHome 固件和 Home Assistant 集成 |
| **元代理** | 审计记忆系统本身（检查重复/过时引用/合规性） |

### 子代理结构

**每个子代理是独立 Claude Code 项目目录：**
```
sub-agent-name/
├── CLAUDE.md    # 定义身份和流程
└── STATUS.md    # 追踪最近工作和未决事项
```

**关键：**
> 这些不是 Claude Code 的内置子代理 — 它们是独立项目文件夹，我 cd 进去并独立运行。Muninn 在简报期间通过读取 STATUS.md 检查它们。

### 代理生命周期

**模式：**
```
轻量级临时项目（追踪单次自行车维修）
  ↓
随时间成长为完整领域管理者
  ↓
或保持小并在完成时归档
```

**关键：**
> 代理默认不是永久的。系统呼吸。

---

## 🛠️ 工具：CLI 优先，MCP 必要时

**一旦有代理，工具选择成为下一个瓶颈。**

### 核心哲学

**Peter Steinberger（OpenClaw）说得对：**
> "most MCPs should be CLIs."

**作者同意：**
```
MCP 在启动时将整个工具 schema 加载到上下文窗口
  ↓
连接足够多 → 燃烧 token 仅告诉模型可用什么
```

### 规则

**使用最轻、最快的有效工具：**

| 服务 | 首选 | 原因 |
|------|------|------|
| **Todoist** | CLI 工具（2 个） | 90% 操作更快 + 更少上下文开销 |
| **Google Workspace** | MCP | 无实用 CLI 替代 |
| **Home Assistant** | MCP | 无实用 CLI 替代 |
| **Garmin** | MCP | 健康指标 |
| **Beeper** | MCP | 跨平台消息（Signal/WhatsApp 桥接） |

### 使用的 MCP 服务器

| MCP | 用途 |
|------|------|
| **Google Workspace** | 邮件/日历/Drive/Sheets（两个账户：个人和工作） |
| **Home Assistant** | 智能家居控制/EV 监控/设备状态 |
| **Garmin** | 健康指标 |
| **Beeper** | 跨平台消息 |
| **Todoist** | 复杂任务操作回退 |
| **QMD** | 记忆文件本地搜索引擎 |

### 配置位置

| 文件 | 用途 |
|------|------|
| **~/.claude.json** | MCP 服务器定义和工作区信任 |
| **~/.claude/settings.json** | 工具权限和行为默认 |

**教训：**
> 如果你在同一服务上有多个账户（个人和工作 Gmail），需要在 CLAUDE.md 中有明确路由规则。

---

## 💡 核心洞察

### 洞察 1：Markdown 就是系统

**整个系统是 markdown 文件：**
- ✅ 无自定义框架
- ✅ 无数据库
- ✅ 无部署管道

**关键：**
> Claude Code 在每次对话开始时读取 CLAUDE.md 文件。这些文件就是代理 — 定义其身份、能力和知识。其他一切都是上下文。

---

### 洞察 2：记忆是最难部分

**作者 irony：**
> 我称它为 Muninn（记忆），ironic 因为记忆是这类系统最难正确的部分。

**挑战：**
- 说服 LLM 行动前引用记忆
- 避免重复已解决事项
- 保持记忆清洁无噪音

**解决：**
- BM25 搜索（QMD）
- 明确路由规则
- decisions.md 追踪已解决事项

---

### 洞察 3：简报是杀手级工作流

**为什么简报值得构建系统：**
```
30-120 秒简报
  ↓
替代早上检查 6 个应用
  ↓
给我控制感
  ↓
一切需要做的事情的概览
  ↓
无需去寻找它
```

---

### 洞察 4：CLI 优先于 MCP

**Token 效率：**
```
MCP 加载整个工具 schema 到上下文
  ↓
燃烧 token 仅告诉模型可用什么
  ↓
CLI 更轻更快
```

**规则：**
> 使用最轻、最快的有效工具。MCP 仅用于无 CLI 替代的服务。

---

### 洞察 5：专用胜过通用

**子代理模式：**
```
Muninn（通才）
  ↓
围绕它：专家（烹饪/维护/旅行/家庭自动化/元代理）
  ↓
每个独立项目目录
  ↓
独立运行
  ↓
Muninn 通过 STATUS.md 检查它们
```

**优势：**
- ✅ 每个领域专注
- ✅ 独立状态
- ✅ 可呼吸（临时→永久或归档）

---

## ⚠️ 已知限制

| 限制 | 说明 | 缓解方法 |
|------|------|----------|
| **记忆引用** | LLM 不总引用记忆前行动 | 持续调优指令 |
| **重复 nagging** | 可能重复已解决事项 | decisions.md 追踪 |
| **Token 成本** | 简报用百分之几会话限制 | 可接受投资 |
| **多账户路由** | 个人/工作账户需明确规则 | CLAUDE.md 路由规则 |
| **BM25 局限** | 无语义理解 | 结构良好文件补偿 |

---

## 📊 对比：作者系统 vs Karpathy 第二大脑

| 维度 | 作者（Muninn） | Karpathy 风格 |
|------|---------------|--------------|
| **核心** | AI 秘书（主动行动） | 知识库（被动检索） |
| **结构** | CLAUDE.md + 领域剧本 | raw/wiki/outputs |
| **记忆** | 主题文件（people/decisions/projects） | wiki/ 索引化 |
| **操作** | 简报 + 执行 | 摄入 + 查询 + Lint |
| **工具** | CLI 优先 + MCP | agent-browser |
| **焦点** | 生活管理 | 知识积累 |

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **原文** | https://deknijf.com/posts/my-ai-secretary/ |
| **OpenClaw** | https://openclawai.com |
| **Whispering** | https://github.com/EpicenterHQ/epicenter/tree/main/apps/whispering |
| **QMD** | https://github.com/tobi/qmd |

---

## 📊 翻译信息

| 项目 | 信息 |
|------|------|
| **翻译时间** | 2026-04-07 |
| **原文作者** | Dek Nijf |
| **系统名称** | Muninn（奥丁的记忆乌鸦） |
| **翻译状态** | ✅ 完整翻译 + 系统架构详解 |

---

*翻译完成时间：2026-04-07 | 版本：v1.0*
