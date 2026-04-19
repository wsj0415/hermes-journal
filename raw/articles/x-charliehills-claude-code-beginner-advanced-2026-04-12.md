# Charlie Hills — Claude Code 从初学者到高级完整指南

**来源**: https://charliehills.substack.com/p/claude-code-beginner-advanced  
**作者**: Charlie Hills  
**抓取时间**: 2026-04-12 18:34 UTC  
**类型**: Substack 通讯/完整教程  
**标签**: claude-code, beginner-guide, advanced-workflows, claude-md, plan-mode, context-management, skills, mcp-connectors, remotion-video, figma-mcp

---

## 📊 一句话总结

Charlie Hills 分享 Claude Code 从初学者设置到高级工作流的完整指南，涵盖 CLAUDE.md 项目简报/四种模式（Ask Before Edits/Edit Automatically/Bypass Permissions/Plan Mode）/上下文管理/Slash 命令/Skills 技能系统/MCP 连接器/5 个实战案例（Lead 抓取/提案生成器/网站克隆/Remotion 视频/Figma 同步），三层级协作（初学者/中级/机构级）。

---

## 🏷️ 话题标签

#ClaudeCode #初学者指南 #高级工作流 #CLAUDE MD #PlanMode #上下文管理 #Skills #MCP 连接器 #Remotion 视频 #Figma 同步

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：三阶段学习路径图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
Claude Code Beginner to Advanced learning path infographic.

Layout: Vertical 3-stage progression showing skill levels.

Color Palette:
- Beginner: Blue (#3B82F6)
- Intermediate: Purple (#8B5CF6)
- Advanced: Orange (#F97316)
- Background: Dark gradient

Stage 1 — Beginner (Setup):
图标：终端窗口
"Step 1: Get Claude Pro ($20/month)"
"Step 2: Install Claude Code (2 min)"
"Step 3: Authenticate"
"Step 4: Navigate to project"
"VS Code / Windsurf IDE options"
"CLAUDE.md — Standing brief"

Stage 2 — Intermediate (Workflows):
图标：并行 Agent
"4 Modes: Ask/Edit/Bypass/Plan"
"Context Management"
"Slash Commands (/plan /context /compact)"
"Skills System (.claude/skills/)"
"MCP Connectors (50+ integrations)"

Stage 3 — Advanced (Business):
图标：机构运营
"Lead Scraping Skill"
"Proposal Generator"
"Website Clone from Screenshot"
"Remotion Programmatic Video"
"Figma MCP Sync"

Center Badge:
"3 Levels, One Newsletter"
"Tested Every Workflow"
"Marketer, Not Developer"

Bottom Badge:
"CLAUDE.md = Highest leverage"
"Plan Mode saves 10x rebuild time"
"Context is scarce resource"

Style: Modern learning path, dark mode with stage colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于从初学者到高级的完整学习路径，垂直三阶段图直接展示技能进阶过程，比单一架构图更能传达"循序渐进"的价值。

---

### 选项 2：四种模式对比图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Claude Code 4 Modes comparison diagram.

Layout: 2x2 grid showing each mode with use cases.

Color Palette:
- Ask Before Edits: Green (#10B981)
- Edit Automatically: Blue (#3B82F6)
- Bypass Permissions: Red (#EF4444)
- Plan Mode: Purple (#8B5CF6)
- Background: Dark gradient

Mode 1 — Ask Before Edits (Default) 🟢:
"Claude asks before changing any file"
"Safe, but slow"
"Use: First time with project"
"Switch if asking every edit on complex build"

Mode 2 — Edit Automatically 🔵:
"Auto-accept changes to existing files"
"Asks before creating new ones"
"Good middle ground for most work"
"Use: Regular development"

Mode 3 — Bypass Permissions 🔴:
"Removes all prompts"
"Works without interruption"
"Flag: --dangerously-skip-permissions"
"Use: Non-critical folders only"
"Warning: Real but low risk"

Mode 4 — Plan Mode 🟣:
"Read-only before execution"
"Researches project, reads files"
"Produces plan before touching files"
"Most beginners undervalue"
"1 min planning = 10 min rebuild saved"
"Token economics, not motivation"

Center Insight:
"Plan Mode = Load-bearing, not cosmetic"
"Every hour saved came from 5 min Plan Mode first"

Bottom Badge:
"Switch modes based on task complexity"
"Plan → Bypass → Build"

Style: Clean mode comparison, dark mode with mode colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3:5 实战案例网格

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules showing "5 Claude Code实战案例".

Color Palette:
- Primary: Blue (#3B82F6)
- Accent: Various case colors
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"5 实战案例"
"从技能到业务基础设施"
Icon: Skill + Connector

M2 — Lead Scraping:
"技能 + Google Sheets 连接器"
"输入：行业/地点/数量"
"输出：自动上传表格"
"一行运行整个流程"

M3 — Proposal Generator:
"Plan Mode 构建"
"输入表单 + AI 生成 + 客户视图"
"接受按钮 + 支付链接"
"无 PandaDoc 订阅"

M4 — Website Clone:
"截图 + 内容 → 完整网站"
"3 个布局变体并行"
"Figma MCP 推送设计"
"无模板/无页面构建器"

M5 — Remotion Video:
"React 编程视频"
"每帧是组件/每动画是代码"
"终端创建产品发布视频"
"完全可编辑/可变体"

M6 — Key Insights:
"技能 = 工作流"
"连接器 = 实时数据"
"无连接器 = 本地文件"
"有连接器 = 业务运营"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 什么是 Claude Code

> **命令行工具，安装在终端。本地运行在你的机器上。直接读取/写入/创建/修改文件。调用 API。浏览网页。Spawn 子 agent 并行研究。执行你从未写过的 Python 脚本。**

**比喻**:
> 把它想成住在你电脑里的 AI，与你的工具一起工作，而非围绕它们工作。

**你不必是开发者使用它**。

---

## 初学者设置（4 步）

### Step 1: 获取付费 Claude 计划

| 计划 | 价格 | 适用 |
|------|------|------|
| **Pro** | $20/月 | 最低要求 |
| **Max** | 更高 | 重度工作流 |

---

### Step 2: 安装 Claude Code

**Mac**: 打开 Spotlight 输入"terminal"  
**Windows**: 使用 CMD 或 PowerShell

运行安装命令从 code.claude.com/docs  
**耗时**: 约 2 分钟

---

### Step 3: 认证

在终端输入 `claude`，提示登录 Claude 账户，跟随步骤。

---

### Step 4: 导航到项目文件夹

在终端去任何你想 Claude Code 工作的文件夹，再次输入 `claude`。**你运行了**。

---

### IDE 选项（非终端用户）

如果终端对你陌生，通过 IDE 使用 Claude Code：

| IDE | 说明 | 链接 |
|------|------|------|
| **VS Code** | 免费，来自微软 | code.visualstudio.com |
| **Windsurf** | 更新，更 AI 原生 | — |

**两者让你在右侧图形聊天面板运行 Claude Code，左侧是文件。无需原始终端**。

**添加到 VS Code**:
1. 去 Extensions 标签
2. 搜索"Claude Code"
3. 安装 Anthropic 的那个
4. 点击编辑器面板出现的 Claude 图标

---

### 本地开源模型（零成本）

通过 Ollama 运行 Claude Code 带本地开源模型：

```bash
# 安装 Ollama
# 拉取模型如 qwen3-coder 或 gpt-oss:20b
# 指向 Claude Code 到本地端点
```

| 优势 | 劣势 |
|------|------|
| 无 API 费用 | 输出质量明显低于 Claude 自家模型 |
| 数据不离开机器 | 需要至少 32GB RAM 可用体验 |
| 适合学习界面 | 不足以用于后面多步工作流 |

设置指南：docs.ollama.com/integrations/claude-code

---

## CLAUDE.md — 最高杠杆的事

> **这是你能在 Claude Code 中做的单一最高杠杆的事。**

**什么是 CLAUDE.md**:
- 坐在项目文件夹的文本文件
- Claude Code 在每会话开始自动读取
- 在你输入第一条消息前注入上下文

**比喻**:
> **这是项目的常驻简报。** 告诉 Claude Code 项目用途/如何行为/绝不做的事/使用的工具和惯例/任何此工作的特定约束。

**为什么重要**:
> 每次 Claude Code 会话从冷开始。无上次的记忆。**CLAUDE.md 是让它感觉像了解你工作的工具，而非你每天早上简报的空白画布。**

---

### 生成你的第一个 CLAUDE.md

**自动方式**:
```bash
在任何项目文件夹运行 /init
```
Claude Code 读取你的文件并自动写一个。它分析文件夹里有什么并产生摘要带工作指令。然后你随时间精炼它。

---

### 好 CLAUDE.md 规则

| 规则 | 说明 |
|------|------|
| **1. 最重要约束在顶部** | Claude Code 有首因偏差。它读的第一件事最牢固 |
| **2. 用项目符号和短标题** | 高信息密度胜过散文 |
| **3. 200-500 行最大** | 更长你付 token 成本降低输出质量 |
| **4. 绝不粘贴整个 API 文档** | 给 Claude Code 摘要，让它需要时获取其余 |
| **5. 当 Claude Code 持续犯同样错误时更新** | 如果同一问题绊倒两次，添加规则 |

---

## 四种模式

Claude Code 有四种模式。理解它们改变你如何使用它。

### Mode 1: Ask Before Edits（默认）

| 特征 | 说明 |
|------|------|
| **行为** | Claude Code 改变任何文件前问许可 |
| **优势** | 安全 |
| **劣势** | 慢 |
| **何时切换** | 如果复杂构建中问每个单独编辑批准 |

---

### Mode 2: Edit Automatically

| 特征 | 说明 |
|------|------|
| **行为** | 自动接受对现有文件的改变 |
| **仍问** | 创建新文件前 |
| **适用** | 大多数工作的良好中间地带 |

---

### Mode 3: Bypass Permissions

| 特征 | 说明 |
|------|------|
| **行为** | 移除所有提示。Claude Code 无中断工作 |
| **启用** | `claude --dangerously-skip-permissions` |
| **风险** | 真实但低（如果在非关键文件夹工作） |
| **警告案例** | 有人在 Linux 机器 bypass permissions 丢失数据。命令有效。上下文错误。**用意识使用**。 |

---

### Mode 4: Plan Mode ⭐ 最被低估

> **一分钟规划节省十分钟构建。那不是激励语言。是 token 经济学。**

**实际数学**:
```
无规划构建：
- 构建某物 → 错误 → 重建
- 总成本：构建时间 + 重建时间 + 两次尝试消耗的 token

先规划：
- Claude Code 识别方法问题在碰任何文件前
- 总成本：5 分钟规划 + 一次正确构建
```

**Plan Mode 是只读的**:
- Claude Code 研究你的项目
- 读取你的文件
- 检查文档
- 在执行任何事前产生计划

**计划不是化妆品的。是承重的。**

> **我在复杂构建中节省的每小时来自先花 5 分钟在 Plan Mode。**

---

### 如何使用 Plan Mode

```
1. 点击聊天面板底部权重的"Plan Mode"切换
2. 描述你想构建什么
3. 让 Claude Code 产生计划
4. 读它。如果有问题 push back
5. 当计划看起来对，切换到 Bypass Permissions，让它构建
```

---

## 上下文管理

> **上下文是 Claude Code 中的稀缺资源。** 管理好它是平滑构建和降级构建之间的差异。

---

### 值得知道的 Slash 命令

你不需要 memorize 所有 62 个。这些是最重要的：

| 命令 | 用途 |
|------|------|
| `/plan` | 任何复杂任务前启动 Plan Mode |
| `/context` | 看确切什么消耗你的上下文窗口 |
| `/compact` | 释放上下文（约 50% 时做，非 95%） |
| `/clear` | 切换到新任务时完全重置上下文 |
| `/model` | 会话中切换模型或推理级别 |
| `/init` | 自动生成第一个 CLAUDE.md |
| `/doctor` | 诊断安装和认证问题 |
| `/rewind` | 当 Claude 偏离轨道时撤销（或按 Esc 两次） |
| `/permissions` | 预允许安全命令而非用 bypass 模式 |
| `/btw` | 问侧面问题不中断主任务 |

---

### /context 命令

运行 `/context` 在任何会话看确切什么消耗你的上下文窗口。你会看到：
- 系统提示
- 工具
- MCP 工具
- 记忆文件
- Skills
- 带确切 token 计数的消息

**大多数人惊讶**。在他们输入第一条消息前，他们经常已经从纯系统级开销通过窗口的 15-20%。

---

## Skills 技能系统

> **这是 Claude Code 停止成为生产力工具开始成为业务基础设施层的地方。**

**什么是 Skill**:
- 坐在 `.claude/skills/` 文件夹的 Markdown 文件
- Claude Code 按需读取它
- 跟随它作为逐步工作流
- **定义一次。之后，一行运行整个事。**

---

### 连接器的重要性

> **每个技能在正确连接器激活的时刻变得更有用。**

| 连接器 | 技能效果 |
|--------|----------|
| **Google Sheets** | Lead 抓取技能直接上传结果 |
| **Gmail** | 邮件分类技能读取和标记真实收件箱 |
| **Figma** | 构建的界面落到设计画布作为可编辑帧 |

**无连接器**: 你在本地文件工作  
**有连接器**: 你在你的业务已经依赖的工具中运行运营

---

### 设置连接器

```
去 Settings > Connectors in Claude Desktop
50+ 集成列出
认证一次
每未来会话自动拾取它们
```

---

## 关键 MCP 工具

### Context7

**链接**: https://context7.com/  
**功能**: 获取最新库文档到上下文。**阻止 Claude 幻觉过时的 API**。

---

### Playwright

**链接**: https://github.com/microsoft/playwright-mcp  
**功能**: 给 Claude 浏览器自动化。可实现/测试/验证 UI 功能通过自己导航你的应用。

---

### Excalidraw

**链接**: https://github.com/walidboulanouar/Ay-Skills/tree/main/skills/excalidraw-diagram  
**功能**: 让 Claude 从提示生成架构图和流程图作为手绘草图。

---

### DeepWiki

**链接**: https://docs.devin.ai/work-with-devin/deepwiki-mcp  
**功能**: 为任何 GitHub repo 拉取结构化文档。指向 Claude 到 repo 它获得完整图片无需你粘贴 README 文件到聊天。

---

## 5 个实战案例

### 案例 1: Lead 抓取技能

**技能描述**: 抓取目标行业/分类 leads/丰富联系邮件/上传到 Google Sheet

**构建技能**:
```markdown
Create a Claude Code skill file called lead-scraping.md 
in a .claude/skills/ folder.

The skill should:
1. Scrape business leads for target industry and location using web search
2. Classify each lead with AI (business name, website, phone, category)
3. Enrich a contact email for each lead where publicly available
4. Upload all results to a Google Sheet

Accept three inputs from user:
- Industry (e.g. dentists, accountants, solicitors)
- Location (e.g. Manchester UK, United States)
- Number of leads required

Write as step-by-step Markdown checklist Claude Code follows when invoked.
```

**运行它（一行）**:
```bash
Use the lead-scraping skill.
Industry: dentists
Location: Manchester, UK
Leads required: 20
Upload to this Google Sheet: [YOUR SHEET URL]
```

---

### 案例 2: 提案生成器

**功能**: 完整提案生成器带简短输入表单/AI 生成提案用你的声音/客户视图带接受按钮/支付链接字段。**无 PandaDoc 订阅。无每提案成本。**

**用 Plan Mode 构建**:
```bash
/plan Build a proposal generator web app with:
- Brief input form (client name, industry, scope, budget)
- AI-generated proposal output in my voice using brand-voice.md
- Client-facing view with Accept button
- Payment link field to add manually before sending
- Each proposal saved as Markdown in /proposals folder

Use plain HTML, CSS, JavaScript. No frameworks.
Read all files in this folder before planning.
Ask clarifying questions before starting.
```

**构建后**: 在构建前清除上下文窗口所以规划消耗的 token 不吃构建。Claude Code 然后执行每步不停问许可。

---

### 案例 3: 从截图克隆网站

**功能**: 截图你欣赏的网站。连同你的内容和品牌指南喂给 Claude Code。获得完整可部署网站无需碰模板或页面构建器。

**构建它**:
```bash
拖参考截图到终端，然后粘贴：

I am going to give you a screenshot of a website I like the design of 
and my own content. Build me a complete single-page website using my 
content but matching the visual style and layout of the reference.

My content:
Headline: [YOUR HEADLINE]
Subheadline: [YOUR SUBHEADLINE]  
Key points: [POINT 1], [POINT 2], [POINT 3]
CTA: [YOUR CTA TEXT]
Brand colour: [HEX CODE]

Build as single HTML file with embedded CSS.
Produce three layout variants: version-a.html, version-b.html, version-c.html
Run them in parallel.
```

**推送到 Figma**:
```bash
# 先连接 Figma MCP
claude mcp add --transport http figma https://mcp.figma.com/mcp

# 然后
Start a local server for my app and capture the UI in a new Figma file.
```

Claude Code 打开浏览器，捕获实时界面，发送到 Figma 作为可编辑设计层。在画布上精炼它，推回更新。**设计和代码保持同步无手动交接**。

---

### 案例 4: Remotion 编程视频

**什么是 Remotion**:
- 开源框架让你用 React 编程创建视频
- **每帧是组件。每动画是代码。**
- 你描述想要的，Claude Code 构建它

**不是**: AI 从文本提示生成随机视频  
**是**: Claude Code 写渲染你视频的 React 组件。**你获得完全控制/完全可编辑性/从单模板生成变体的能力**。

---

#### 四步设置

**Step 1**: 创建新 Remotion 项目
```bash
npx create-video@latest
# 选择 Blank 模板
# 对 TailwindCSS 说是
# 对安装 Skills 说是
```

**Step 2**: 导航到文件夹并启动预览服务器
```bash
cd my-video
npm install
npm run dev
```

**Step 3**: 打开第二终端窗口启动 Claude Code
```bash
cd my-video
claude
```

**Step 4**: 描述你想要的视频
- Claude Code 读取你的项目
- 写组件
- localhost:3000 的预览实时更新
- 当你对结果满意，渲染最终 MP4:
```bash
npx remotion render
```

---

#### 输出质量

> **输出质量几乎完全取决于源材料质量。**

| 源材料 | 输出 |
|--------|------|
| 好屏幕录制 | 好视频 |
| 模糊截图 | 通用结果 |

给 Claude Code 锐利高分辨率资产，它处理其他一切。

---

#### 许可检查

**使用前检查商业用途**:
- Remotion 对个人使用和开源项目免费
- **3+ 员工公司需要商业许可为客户渲染视频**
- 检查 remotion.dev/license 在构建客户工作前

---

### 案例 5: Vislo（作者的工具）

**Vislo**: https://www.vislo.ai/  
**功能**: 用纯文本描述想要的，Vislo 几秒生成分享就绪信息图（无需设计技能）  
**价格**: $19/月，前 100 用户锁定那价格

---

## 关键数据

| 指标 | 数值 |
|------|------|
| Claude Pro 价格 | $20/月 |
| 安装时间 | ~2 分钟 |
| CLAUDE.md 最大行数 | 200-500 行 |
| Slash 命令总数 | 62 |
| MCP 连接器 | 50+ |
| Remotion 许可 | 个人免费/商业 3+ 员工需许可 |
| Vislo 价格 | $19/月（前 100 用户） |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "CLAUDE.md = 最高杠杆的事" | 项目简报价值 |
| "一分钟规划节省十分钟构建" | Plan Mode 价值 |
| "计划不是化妆品的。是承重的。" | 规划重要性 |
| "上下文是稀缺资源" | 上下文管理 |
| "技能 = 工作流，连接器 = 实时数据" | 技能 + 连接器价值 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **CLAUDE.md 项目简报** — 自动注入上下文
2. **四种模式切换** — 根据任务复杂度
3. **Plan Mode 优先** — 规划先于执行
4. **上下文管理** — /context /compact /clear
5. **Skills 系统** — 可复用工作流
6. **MCP 连接器** — 实时数据集成

### 可实施
- 为内容项目创建 CLAUDE.md
- 实现模式切换逻辑
- 复杂任务前先规划
- 追踪上下文使用
- 将内容流程编码为 Skills
- 集成外部工具（Google Sheets/Gmail/Figma）

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Charlie Hills 原文 | https://charliehills.substack.com/p/claude-code-beginner-advanced |
| Claude Code 文档 | https://code.claude.com/docs |
| Ollama 集成 | https://docs.ollama.com/integrations/claude-code |
| Context7 | https://context7.com/ |
| Playwright MCP | https://github.com/microsoft/playwright-mcp |
| Remotion | https://remotion.dev |
| Vislo | https://www.vislo.ai/ |

---

*原始来源：https://charliehills.substack.com/p/claude-code-beginner-advanced*
