# 网页分析：Patina — Markdown 中的第二大脑

**来源**: gabos.vercel.app  
**链接**: https://gabos.vercel.app/index.html  
**类型**: 产品落地页  
**抓取时间**: 2026-04-09 05:57 UTC

---

## 📊 核心洞察

**一句话总结**: Patina 是一个将用户现有应用（Gmail、日历、消息、健康等）自动同步为本地 Markdown 文件的第二大脑系统，通过 AI（Claude）读取文件、回答问题、保持更新，实现隐私优先、用户完全控制、可完全定制的生活操作系统。

---

## 🎯 完整翻译与分析

### 主页标语

**你的生活，轻松组织**

将你已经在用的应用变成一个自动更新的个人 Wiki。

[开始使用](https://gabos.vercel.app/setup.html)

---

### 支持的应用

连接你已经使用的工具：邮件、日历、消息、健康、财务。Patina 从所有这些地方拉取数据。

- Gmail
- Google Calendar
- Beeper
- Apple Health
- +20 其他应用

---

### 核心工作流程

#### 1. 连接你的应用
链接你已经使用的工具：邮件、日历、消息、健康、财务。Patina 从所有这些地方拉取数据。

#### 2. 一切变成 Markdown
你的数据同步到你电脑上的一个纯文本文件文件夹中。

```
your-folder/
├── identity.md          # 身份档案
├── people/
│   ├── friend.md        # 人物文件
│   └── colleague.md
├── briefings/
│   └── morning-2026-04-09.md  # 早间简报
├── digests/
│   └── digest-2026-04-08.md   # 每日摘要
└── weekly/
    └── weekly-2026-W15.md     # 每周检查
```

#### 3. AI 为你行动
Claude 读取你的文件，回答问题，并保持一切更新。

---

### 核心功能

#### 📄 Identity Profile（身份档案）
一个反映你的信念、价值观和内心冲突的活文档，同时塑造系统如何与你对话。

**文件**: `identity.md`

**用途**: 
- 记录个人信念和价值观
- 追踪内心冲突和成长
- 定义 AI 与用户的交互方式

---

#### 👥 People Files（人物文件）
为你互动的每个人自动创建档案，帮助你随时间理解你的关系。

**文件**: `people/[name].md`

**用途**:
- 自动更新的关系档案
- 追踪互动历史
- 理解关系模式

---

#### 🌅 Morning Briefing（早间简报）
天气、日程、开放循环和需要回复的消息。与你已经处理的内容交叉引用。

**文件**: `briefings/morning-YYYY-MM-DD.md`

**内容**:
- 天气预报
- 当日日程
- 待处理事项
- 需要回复的消息
- 已处理事项交叉引用

[了解更多](https://gabos.vercel.app/skills/morning.html)

---

#### 🌙 End-of-Day Digest（每日摘要）
一天中的每次对话、会议和任务在一个文件中。验证开放循环，附带检查日志。

**文件**: `digests/digest-YYYY-MM-DD.md`

**内容**:
- 当日所有对话记录
- 会议摘要
- 完成任务列表
- 开放循环验证
- 检查日志

[了解更多](https://gabos.vercel.app/skills/digest.html)

---

#### 📅 Weekly Check-in（每周检查）
周日晚上展望，包含完整周日程、目标进度和最近摘要中延续的开放线程。

**文件**: `weekly/weekly-YYYY-Www.md`

**内容**:
- 下周完整日程
- 目标进度追踪
- 延续的开放线程
- 周度反思

[了解更多](https://gabos.vercel.app/skills/weekly.html)

---

### 设计原则

#### 🔒 Private by Design（隐私优先设计）
你所有的数据作为纯文本文件存在于你的电脑上，其他人无法访问。

**关键特点**:
- 本地存储
- 无云端同步
- 纯文本格式
- 用户完全控制

---

#### 🎛️ You're Always in Control（你始终掌控）
它只读写你的本地文件，从不自发送消息或自行采取行动。

**关键特点**:
- 只读/写本地文件
- 无自主行动
- 用户审批所有操作

---

#### 🔧 Fully Customizable（完全可定制）
都是纯文本和 Markdown，所以你可以让 Claude 改变任何关于它如何工作的方式。

**关键特点**:
- 纯文本可编辑
- AI 可修改系统行为
- 无黑盒逻辑

---

### 配套应用

#### 📱 Sumi
从手机提交你的想法、创建新任务并与你的数据聊天的最快方式。

**用途**:
- 快速捕获想法
- 创建任务
- 与数据对话
- 移动端优先

---

#### 🔍 Recall
找到你档案中的空白，一次问一个问题来填补它们。你的答案直接进入你的文件。

**用途**:
- 发现档案空白
- 引导式问题填充
- 自动更新文件

---

#### 💻 Patina for Mac
从 Mac 菜单栏自动调度简报、摘要和同步。

**用途**:
- 自动调度
- 菜单栏快捷访问
- 后台同步

---

## 📐 系统架构

```
┌─────────────────────────────────────────────────────┐
│              数据源（20+ 应用）                        │
│  Gmail  │ Calendar │ Beeper │ Health │ Finances │... │
└─────────────────────────────────────────────────────┘
                        ↓ 同步
┌─────────────────────────────────────────────────────┐
│           本地 Markdown 文件夹（用户电脑）               │
│  identity.md                                         │
│  people/                                             │
│  briefings/                                          │
│  digests/                                            │
│  weekly/                                             │
└─────────────────────────────────────────────────────┘
                        ↓ 读取
┌─────────────────────────────────────────────────────┐
│              AI 层（Claude）                          │
│  - 回答问题                                          │
│  - 生成简报/摘要                                      │
│  - 保持更新                                          │
│  - 不自主行动                                        │
└─────────────────────────────────────────────────────┘
                        ↓ 输出
┌─────────────────────────────────────────────────────┐
│              用户界面                                 │
│  Sumi (移动端) │ Patina for Mac (菜单栏) │ Web      │
└─────────────────────────────────────────────────────┘
```

---

## 💡 与类似系统对比

| 系统 | 数据源 | 存储格式 | AI 角色 | 隐私 | 自动化 |
|------|--------|----------|--------|------|--------|
| **Patina** | 20+ 应用 | 本地 Markdown | 读取 + 回答 + 更新 | ⭐⭐⭐⭐⭐ 本地 | 自动同步 |
| **Stella (Ryan)** | Gmail/Calendar/Todoist | 本地 Markdown | 读取 + 简报 + 追踪 | ⭐⭐⭐⭐⭐ 本地 | 自动同步 |
| **Muninn (Dek)** | 11 领域剧本 | 本地 Markdown | 读取 + 简报 | ⭐⭐⭐⭐⭐ 本地 | 自动调度 |
| **Karpathy 风格** | 手动剪贴 | raw/wiki/outputs | 编译 + 回答 | ⭐⭐⭐⭐⭐ 本地 | 手动/脚本 |
| **当前 KilroyContentBot** | X/YouTube/网页 | 本地 Markdown | 抓取 + 分析 + 归档 | ⭐⭐⭐⭐⭐ 本地 | 自动推送 |

---

## 🔧 可实施建议

### 对 KilroyContentBot 的启示

#### 短期（1-2 周）
1. **增强记忆结构**
   - 添加 `people/` 文件夹追踪关系
   - 添加 `identity.md` 记录用户偏好
   - 心跳时自动更新

2. **简报系统升级**
   - 早间简报：热点 + 日程 + 待处理
   - 每日摘要：当天分析内容汇总
   - 每周检查：周度内容数据分析

3. **移动端支持**
   - 评估 Sumi 类快速捕获工具
   - Telegram Bot 已支持快速输入

#### 中期（1 月）
1. **多数据源集成**
   - Gmail 阅读（如用户授权）
   - Calendar 同步
   - 自动人物档案生成

2. **Recall 模式**
   - 定期询问用户偏好
   - 填补 MEMORY.md 空白
   - 引导式档案完善

---

## 📈 产品亮点分析

| 亮点 | 说明 | 可借鉴度 |
|------|------|----------|
| **隐私优先** | 纯文本本地存储，无云端 | ⭐⭐⭐⭐⭐ 已实现 |
| **应用集成** | 20+ 应用自动同步 | ⭐⭐⭐⭐ 可选择实现 |
| **身份档案** | 活文档反映信念价值观 | ⭐⭐⭐⭐ 可添加 |
| **人物文件** | 自动关系档案 | ⭐⭐⭐⭐ 可添加 |
| **三层简报** | 早/日/周完整体系 | ⭐⭐⭐⭐⭐ 强烈推荐 |
| **移动端 Sumi** | 快速捕获想法 | ⭐⭐⭐ Telegram 可替代 |
| **Recall 填补** | 引导式档案完善 | ⭐⭐⭐⭐ 可添加 |

---

## 🎨 封面图提示词（使用 nano-banana-pro）

### 选项 1：系统架构图 — 技术蓝图风格 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考**: Technical Blueprint Drawing Prompt (ID: 11211)  
**示例图**: https://cms-assets.youmind.com/media/1772433511864_no5yz9_HCU_ufcacAAZMH2.jpg

```prompt
Patina Second Brain system architecture, technical blueprint drawing, orthographic view, vertical flow diagram showing 3 layers (Apps → Markdown Folder → AI), white vector line art, thin construction lines, precise measurements, annotation labels, dimension arrows, grid background, deep blue background, minimal design, engineering schematic style, high detail, aspect ratio 9:16 portrait

Layer 1 (Top): 20+ app icons (Gmail, Calendar, Beeper, Health, Finance) with sync arrows pointing down
Layer 2 (Middle): Markdown folder structure with files (identity.md, people/, briefings/, digests/, weekly/)
Layer 3 (Bottom): AI layer (Claude) with read/write arrows

Labels: "Connect Apps" → "Everything becomes .md" → "AI acts on it"
Badge: "Private by Design" "Local Storage" "Full Control"
```

---

### 选项 2：Bento Grid 信息图风格

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考**: Premium liquid glass Bento grid (ID: 6847)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Input Variable: Patina Second Brain
Language: Chinese

System Instruction:
Create an image of premium liquid glass Bento grid infographic with 6 modules for Patina Second Brain system.

1) Color Palette:
→ Hero color: Soft blue (#3B82F6)
→ Accents: Muted blue (30-40% saturation)
→ Icons, borders: Whisper-thin borders, never black

2) Visual Style:
→ Cards: Apple liquid glass (85-90% transparent)
→ Background: Ethereal abstract glow, light caustics
→ Asymmetric Bento grid, 9:16 portrait
→ Hero card: 28-30% | Info modules: 70-72%

3) Module Content (6 Cards):
M1 — Hero: "Patina 第二大脑" title + Markdown folder icon
M2 — Data Sources: 20+ apps (Gmail, Calendar, Beeper, Health)
M3 — Storage: Local .md files, privacy badge
M4 — AI Layer: Claude reads & answers
M5 — Briefings: Morning/Daily/Weekly icons
M6 — Output: Sumi mobile + Mac menu bar

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

### 选项 3：爆炸视图风格

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考**: Exploded View Infographic (ID: 11270)  
**示例图**: https://cms-assets.youmind.com/media/1772519703684_klovml_HCbTfBgXQAAtlhh.jpg

```prompt
product design, Patina Second Brain system, exploded view diagram, white background, three-dimensional, highly detailed components showing data flow from apps to markdown files to AI layer, studio lighting, product photography, best quality, aspect ratio 9:16

Top layer: App icons floating with sync arrows
Middle layer: Markdown folder with visible files (identity.md, people/, briefings/)
Bottom layer: AI (Claude) with read/write indicators

Style: Clean technical illustration, minimal labels, professional educational infographic
```

---

**适用场景**: 小红书、抖音、技术社区、GitHub

---

## 🔧 实施检查清单

### 对 KilroyContentBot 的改进

- [ ] 创建 `people/` 文件夹追踪关系
- [ ] 创建 `identity.md` 记录用户偏好
- [ ] 添加早间简报（热点 + 待处理）
- [ ] 添加每日摘要（当天分析汇总）
- [ ] 添加每周检查（周度数据 + 目标）
- [ ] 实施 Recall 模式（定期询问偏好）
- [ ] 评估多数据源集成（Gmail/Calendar）

---

*分析完成 | 下一步：推送到 GitHub*
