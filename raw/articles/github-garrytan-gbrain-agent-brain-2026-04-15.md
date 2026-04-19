# Garry Tan — GBrain: YC CEO 的 OpenClaw/Hermes Agent 大脑

**来源**: https://github.com/garrytan/gbrain  
**作者**: Garry Tan (YC President & CEO)  
**抓取时间**: 2026-04-15 14:39 UTC  
**类型**: GitHub 仓库/开源项目  
**标签**: gbrain, agent-brain, openclaw, hermes-agent, knowledge-management, skill-system, pgvector, mcp-server, thin-harness-fat-skills

---

## 📊 一句话总结

YC CEO Garry Tan 开源的个人 AI Agent 大脑系统，12 天构建 17,888 页知识库（4,383 人/723 公司），25 个技能文件，21 个 cron 作业自主运行，PGLite/Supabase 双引擎，30 分钟安装，让 agent 在你睡觉时摄入会议/邮件/推文/语音并 enrichment 实体，醒来大脑更聪明。

---

## 🏷️ 话题标签

#GBrain #AgentBrain #OpenClaw #HermesAgent #知识管理 #技能系统 #PGVector #MCP 服务器 #ThinHarnessFatSkills

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1:GBrain 架构图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
GBrain Architecture diagram showing Brain Repo + GBrain + AI Agent interaction.

Layout: Horizontal 3-component flow.

Color Palette:
- Brain Repo: Green (#10B981)
- GBrain: Blue (#3B82F6)
- AI Agent: Purple (#8B5CF6)
- Background: Dark gradient

Left — Brain Repo (git) 🟢:
图标：Markdown 文件
"Source of Truth"
"17,888 pages"
"4,383 people"
"723 companies"
"Human can read & edit"
"Markdown files = truth"

Center — GBrain (retrieval) 🔵:
图标：Postgres + pgvector
"Postgres + pgvector"
"Hybrid search"
"Vector + Keyword + RRF"
"PGLite (embedded)"
"Supabase (cloud)"
"Multi-query expansion"
"4-layer dedup"

Right — AI Agent (read/write) 🟣:
图标：25 skills
"25 Skills"
"RESOLVER.md routes intent"
"Read/Write through both"
"Signal detector"
"Brain ops"
"Enrichment tiers"

Bottom Data Flow:
"Signal (meeting/email/tweet/link)"
"→ Signal detector captures ideas + entities"
"→ Brain-ops: check brain first"
"→ Respond with full context"
"→ Write: update pages + citations"
"→ Sync: index changes"

Style: Clean technical architecture, dark mode with component colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 GBrain 架构的内容，三组件流程图直接展示 Brain Repo/GBrain/AI Agent 如何协同工作，比单一架构图更能传达"检索层"的价值。

---

### 选项 2:25 技能分类网格

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
25 GBrain Skills categorized grid showing 5 categories.

Layout: 5 category boxes with skill counts.

Color Palette:
- Always-on: Blue (#3B82F6)
- Content Ingestion: Green (#10B981)
- Brain Ops: Purple (#8B5CF6)
- Operational: Orange (#F97316)
- Identity: Yellow (#FBBF24)
- Background: Dark gradient

Category 1 — Always-on (2 skills) 🔵:
"signal-detector: Fires on every message"
"brain-ops: Brain-first lookup"

Category 2 — Content Ingestion (4 skills) 🟢:
"ingest: Thin router"
"idea-ingest: Links/articles/tweets"
"media-ingest: Video/audio/PDF/repos"
"meeting-ingestion: Transcripts to pages"

Category 3 — Brain Operations (8 skills) 🟣:
"enrich: Tiered enrichment (1/2/3)"
"query: 3-layer search with synthesis"
"maintain: Periodic health checks"
"citation-fixer: Fix missing citations"
"repo-architecture: File organization"
"publish: Password-protected HTML"
"data-research: Structured extraction"
"cross-modal-review: Quality gate"

Category 4 — Operational (8 skills) 🟠:
"daily-task-manager: P0-P3 priorities"
"daily-task-prep: Morning prep"
"cron-scheduler: Staggering + quiet hours"
"reports: Timestamped reports"
"webhook-transforms: External events"
"testing: Skill conformance validation"
"skill-creator: Create new skills"
"briefing: Daily briefing"

Category 5 — Identity (3 skills) 🟡:
"soul-audit: 6-phase interview"
"setup: Auto-provision DB"
"migrate: Universal migration"

Center Badge:
"25 Skills"
"12 days to build"
"30 min install"
"Thin harness, fat skills"

Bottom Insight:
"Skill files are code"
"Encode entire workflows"
"Agent reads and executes"

Style: Modern skills grid, dark mode with category colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：知识模型编译真相 + 时间线图

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules showing "GBrain Knowledge Model".

Color Palette:
- Primary: Blue (#3B82F6)
- Accent: Various knowledge colors
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"GBrain Knowledge Model"
"Compiled Truth + Timeline"
Icon: Brain + Timeline

M2 — Compiled Truth:
"Above the ---"
"Current best understanding"
"Gets rewritten with new evidence"
"Example: 'Do Things That Don't Scale'"
"PG's argument about unscalable effort"

M3 — Timeline:
"Below the ---"
"Append-only evidence trail"
"Never edited, only added"
"- 2013-07-01: Published on paulgraham.com"
"- 2024-11-15: Referenced in W25 kickoff"

M4 — Entity Enrichment:
"Tier 3: 1 mention → stub page"
"Tier 2: 3+ mentions → web + social"
"Tier 1: Meeting/8+ mentions → full pipeline"
"Brain learns who matters"

M5 — Hybrid Search:
"Vector + Keyword + RRF fusion"
"Multi-query expansion"
"4-layer dedup"
"Compiled truth boost"
"P@k, Recall@k, MRR, nDCG@k"

M6 — Daily Cycle:
"Agent runs while you sleep"
"Scans conversations"
"Enriches missing entities"
"Fixes broken citations"
"Wake up smarter"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心洞察

### GBrain 是什么

> **你的 AI agent 很聪明但健忘。GBrain 给它一个大脑。**

**由 YC President & CEO Garry Tan 构建**，用于运行他的实际 AI agents。这是他 OpenClaw 和 Hermes 部署的生产大脑：

| 指标 | 数值 |
|------|------|
| **知识库页数** | 17,888 |
| **人物页面** | 4,383 |
| **公司页面** | 723 |
| **Cron 作业** | 21 个自主运行 |
| **构建时间** | 12 天 |
| **技能文件** | 25 |
| **安装时间** | ~30 分钟 |

---

### 核心功能

> **Agent 在你睡觉时摄入会议/邮件/推文/语音和原创想法。它 enrichment 遇到的每个人和公司。它夜间修复引用并整合记忆。你醒来大脑比睡前更聪明。**

---

## 安装方式

### 方式 1: 在 Agent 平台上（推荐）

**适用平台**:
- **[OpenClaw](https://openclaw.ai/)** — Deploy AlphaClaw on Render (一键，8GB+ RAM)
- **[Hermes Agent](https://github.com/NousResearch/hermes-agent)** — Deploy on Railway (一键)

**粘贴给你的 agent**:
```
Retrieve and follow the instructions at:
https://raw.githubusercontent.com/garrytan/gbrain/master/INSTALL_FOR_AGENTS.md
```

**效果**: Agent 克隆 repo/安装 GBrain/设置大脑/加载 25 技能/配置循环作业。你回答几个 API key 问题。~30 分钟。

---

### 方式 2: 独立 CLI（无 agent）

```bash
git clone https://github.com/garrytan/gbrain.git && cd gbrain && bun install && bun link
gbrain init                     # local brain, ready in 2 seconds
gbrain import ~/notes/          # index your markdown
gbrain query "what themes show up across my notes?"
```

**示例输出**:
```
3 results (hybrid search, 0.12s):

1. concepts/do-things-that-dont-scale (score: 0.94)
   PG's argument that unscalable effort teaches you what users want.
   [Source: paulgraham.com, 2013-07-01]

2. originals/founder-mode-observation (score: 0.87)
   Deep involvement isn't micromanagement if it expands the team's thinking.

3. concepts/build-something-people-want (score: 0.81)
   The YC motto. Connected to 12 other brain pages.
```

---

### 方式 3: MCP 服务器（Claude Code/Cursor/Windsurf）

GBrain 通过 stdio 暴露 30+ MCP 工具：

```json
{
  "mcpServers": {
    "gbrain": { "command": "gbrain", "args": ["serve"] }
  }
}
```

添加到：
- `~/.claude/server.json` (Claude Code)
- Settings > MCP Servers (Cursor)
- 或客户端的 MCP 配置

---

### 方式 4: 远程 MCP（Claude Desktop/Cowork/Perplexity）

```bash
ngrok http 8787 --url your-brain.ngrok.app
bun run src/commands/auth.ts create "claude-desktop"
claude mcp add gbrain -t http https://your-brain.ngrok.app/mcp -H "Authorization: Bearer TOKEN"
```

---

## 25 个技能文件

GBrain 随 25 个技能，按 `skills/RESOLVER.md` 组织。**Resolver 告诉 agent 任何任务读哪个技能。**

> **技能文件是代码。** 它们是完成知识工作最强大的方式。技能文件是 fat markdown 文档，编码整个工作流：何时触发/检查什么/如何与其他技能链/执行什么质量条。Agent 读技能并执行。

**Thin harness, fat skills**: 智能存在于技能中，非 runtime。

---

### Always-on（2 技能）

| 技能 | 功能 |
|------|------|
| **signal-detector** | 每条消息触发。并行 spawn 便宜模型捕获原创思考和实体提及。大脑自动复合。 |
| **brain-ops** | 大脑优先查找在任何外部 API 前。read-enrich-write 循环让每次响应更聪明。 |

---

### Content Ingestion（4 技能）

| 技能 | 功能 |
|------|------|
| **ingest** | 薄路由器。检测输入类型并委托给正确的摄入技能。 |
| **idea-ingest** | 链接/文章/推文变成带分析/作者人物页面/交叉链接的大脑页。 |
| **media-ingest** | 视频/音频/PDF/书籍/截图/GitHub repos。转录/实体提取/反向链接传播。 |
| **meeting-ingestion** | 转录变成大脑页。每个参会者被 enrichment。每个公司获得时间线条目。 |

---

### Brain Operations（8 技能）

| 技能 | 功能 |
|------|------|
| **enrich** | 分层 enrichment（Tier 1/2/3）。创建和更新人物/公司页带编译真相和时间线。 |
| **query** | 3 层搜索带合成和引用。说"大脑没有 X 信息"而非幻觉。 |
| **maintain** | 定期健康：陈旧页/孤立页/死链接/引用审计/反向链接执行/标签一致性。 |
| **citation-fixer** | 扫描页缺失或格式错误引用。修复格式匹配标准。 |
| **repo-architecture** | 新大脑文件去哪。决策协议：主主题决定目录，非格式。 |
| **publish** | 分享大脑页为密码保护 HTML。零 LLM 调用。 |
| **data-research** | 结构化数据研究带参数化 YAML 配方。从邮件提取投资者更新/费用/公司指标。 |
| **cross-modal-review** | 第二模型的质量门。拒绝路由：如果一个模型拒绝，静默切换。 |

---

### Operational（8 技能）

| 技能 | 功能 |
|------|------|
| **daily-task-manager** | 任务生命周期带优先级（P0-P3）。存储为可搜索大脑页。 |
| **daily-task-prep** | 晨间准备：日历前瞻带每个参会者的大脑上下文/开放线程/任务审查。 |
| **cron-scheduler** | 调度交错（5 分钟偏移）/安静时间（时区感知带唤醒覆盖）/幂等性。 |
| **reports** | 时间戳报告带关键词路由。"最新简报是什么？"瞬间找到。 |
| **webhook-transforms** | 外部事件（SMS/会议/社交提及）转换为带实体提取的大脑页。 |
| **testing** | 验证每个技能有 SKILL.md 带 frontmatter/manifest 覆盖/resolver 覆盖。 |
| **skill-creator** | 创建新技能遵循一致性标准。对现有技能 MECE 检查。 |
| **briefing** | 每日简报带会议上下文/活跃交易/引用追踪。 |

---

### Identity and Setup（3 技能）

| 技能 | 功能 |
|------|------|
| **soul-audit** | 6 阶段访谈生成 SOUL.md（agent 身份）/USER.md（用户 profile）/ACCESS_POLICY.md（4 层隐私）/HEARTBEAT.md（运营节奏）。 |
| **setup** | 自动配置 PGLite 或 Supabase。首次导入。GStack 检测。 |
| **migrate** | 从 Obsidian/Notion/Logseq/markdown/CSV/JSON/Roam 通用迁移。 |

---

## 工作原理

```
Signal 到达（会议/邮件/推文/链接）
  → Signal detector 捕获想法 + 实体（并行，永不阻塞）
  → Brain-ops: 先检查大脑（gbrain search, gbrain get）
  → 用完整上下文响应
  → Write: 用新信息 + 引用更新大脑页
  → Sync: gbrain 索引更改供下次查询
```

**每次循环添加知识**。Agent 在会议后 enrichment 人物页。下次那人被提起，agent 已有上下文。**区别每日复合。**

---

### 系统自动变聪明

**Entity enrichment 自动升级**:
- **Tier 3**: 提及 1 次 → stub 页
- **Tier 2**: 跨不同来源 3 次提及 → web + social enrichment
- **Tier 1**: 会议或 8+ 次提及 → 完整 pipeline

> **大脑学会谁重要无需被告知。**

**确定性分类器随时间改进**通过 fail-improve 循环记录每次 LLM fallback 并从失败生成更好 regex 模式。

`gbrain doctor` 显示轨迹：
> "intent classifier: 87% deterministic, up from 40% in week 1."

---

## 数据摄入配方

GBrain 随集成配方，你的 agent 为你设置。每个配方告诉 agent 问什么凭证/如何验证/注册什么 cron。

| 配方 | 需要 | 功能 |
|------|------|------|
| **Public Tunnel** | — | MCP + 语音固定 URL（ngrok Hobby $8/mo） |
| **Credential Gateway** | — | Gmail + Calendar 访问 |
| **Voice-to-Brain** | ngrok-tunnel | 电话到大脑页（Twilio + OpenAI Realtime） |
| **Email-to-Brain** | credential-gateway | Gmail 到实体页 |
| **X-to-Brain** | — | Twitter 时间线 + 提及 + 删除 |
| **Calendar-to-Brain** | credential-gateway | Google Calendar 到可搜索每日页 |
| **Meeting Sync** | — | Circleback 转录到大脑页带参会者 |

**数据研究配方**从邮件提取结构化数据到追踪大脑页。内置配方用于投资者更新（MRR/ARR/runway/headcount）/费用追踪/公司指标。用 `gbrain research init` 创建自己的。

运行 `gbrain integrations` 看状态。

---

## GBrain + GStack

[GStack](https://github.com/garrytan/gstack) 是引擎。GBrain 是 mod。

| 组件 | 功能 |
|------|------|
| **GStack** | 编码技能（ship/review/QA/investigate/office-hours/retro）。70,000+ stars，30,000 开发者/天。当 agent 编码自己时用 GStack。 |
| **GBrain** | 其他技能（大脑操作/信号检测/摄入/enrichment/cron/报告/身份）。当 agent 记忆/思考/运营时用 GBrain。 |
| **`hosts/gbrain.ts`** | 桥梁。告诉 GStack 的编码技能在编码前检查大脑。 |

`gbrain init` 检测 GStack 是否安装并报告 mod 状态。如果 GStack 不在，它告诉你如何获取。

---

## 架构

```
┌──────────────────┐    ┌───────────────┐    ┌──────────────────┐
│   Brain Repo     │    │    GBrain     │    │    AI Agent      │
│   (git)          │    │  (retrieval)  │    │  (read/write)    │
│                  │    │               │    │                  │
│  markdown files  │───>│  Postgres +   │<──>│  25 skills       │
│  = source of     │    │  pgvector     │    │  define HOW to   │
│    truth         │    │               │    │  use the brain   │
│                  │<───│  hybrid       │    │                  │
│  human can       │    │  search       │    │  RESOLVER.md     │
│  always read     │    │  (vector +    │    │  routes intent   │
│  & edit          │    │   keyword +   │    │  to skill        │
│                  │    │   RRF)        │    │                  │
└──────────────────┘    └───────────────┘    └──────────────────┘
```

**Repo 是记录系统。GBrain 是检索层。Agent 通过两者读写。人类总是赢**... 编辑任何 markdown 文件，`gbrain sync` 拾取更改。

---

## 知识模型

每页遵循 **编译真相 + 时间线** 模式：

```md
---
type: concept
title: Do Things That Don't Scale
tags: [startups, growth, pg-essay]
---

Paul Graham's argument that startups should do unscalable things early on.
The key insight: the unscalable effort teaches you what users actually
want, which you can't learn any other way.

---

- 2013-07-01: Published on paulgraham.com
- 2024-11-15: Referenced in batch W25 kickoff talk
```

**`---` 之上**: **编译真相**。你当前最佳理解。当新证据改变图景时被重写。

**`---` 之下**: **时间线**。仅追加证据 trail。永不编辑，仅添加。

---

## 搜索

**混合搜索**: vector + keyword + RRF fusion + multi-query expansion + 4-layer dedup。

```
Query
  → Intent classifier (entity? temporal? event? general?)
  → Multi-query expansion (Claude Haiku)
  → Vector search (HNSW cosine) + Keyword search (tsvector)
  → RRF fusion: score = sum(1/(60 + rank))
  → Cosine re-scoring + compiled truth boost
  → 4-layer dedup + compiled truth guarantee
  → Results
```

**单独关键词错过概念匹配。单独向量错过精确短语。RRF 得两者。**

搜索质量是 benchmarked 和 reproducible：
```bash
gbrain eval --qrels queries.json
```
测量 P@k / Recall@k / MRR / nDCG@k。部署前 A/B 测试配置更改。

---

## 语音

**打电话号。你的 AI 接听。它知道谁打来，从大脑拉完整上下文，响应像真正了解你世界的人。**

通话结束后，大脑页出现带转录/实体检测/交叉引用。

[语音配方随 GBrain](https://github.com/garrytan/gbrain/blob/master/recipes/twilio-voice-brain.md)。WebRTC 在浏览器 tab 工作零设置。真实电话号码可选。

---

## 引擎架构

```
CLI / MCP Server
     (thin wrappers, identical operations)
              |
      BrainEngine interface (pluggable)
              |
     +--------+--------+
     |                  |
PGLiteEngine       PostgresEngine
  (default)          (Supabase)
     |                  |
~/.gbrain/           Supabase Pro ($25/mo)
brain.pglite         Postgres + pgvector
embedded PG 17.5

     gbrain migrate --to supabase|pglite
         (bidirectional migration)
```

**PGLite**: 嵌入式 Postgres，无服务器，零配置。当大脑超过本地（1000+ 文件，多设备），`gbrain migrate --to supabase` 移动一切。

---

## 文件存储

大脑 repo 累积二进制文件。GBrain 有三阶段迁移：

```bash
gbrain files mirror <dir>       # copy to cloud, local untouched
gbrain files redirect <dir>     # replace local with .redirect pointers
gbrain files clean <dir>        # remove pointers, cloud only
gbrain files restore <dir>      # download everything back (undo)
```

**存储后端**: S3-compatible（AWS/R2/Minio）/ Supabase Storage / 本地。

---

## 命令参考

### SETUP
```bash
gbrain init [--supabase|--url]        # Create brain (PGLite default)
gbrain migrate --to supabase|pglite   # Bidirectional engine migration
gbrain upgrade                          # Self-update with feature discovery
```

### PAGES
```bash
gbrain get <slug>                     # Read a page (fuzzy slug matching)
gbrain put <slug> [< file.md]         # Write/update (auto-versions)
gbrain delete <slug>                  # Delete a page
gbrain list [--type T] [--tag T]      # List with filters
```

### SEARCH
```bash
gbrain search <query>                 # Keyword search (tsvector)
gbrain query <question>               # Hybrid search (vector + keyword + RRF)
```

### IMPORT
```bash
gbrain import <dir> [--no-embed]      # Import markdown (idempotent)
gbrain sync [--repo <path>]           # Git-to-brain incremental sync
gbrain export [--dir ./out/]          # Export to markdown
```

### FILES
```bash
gbrain files list|upload|sync|verify  # File storage operations
```

### EMBEDDINGS
```bash
gbrain embed [<slug>|--all|--stale]   # Generate/refresh embeddings
```

### LINKS + GRAPH
```bash
gbrain link|unlink|backlinks|graph    # Cross-reference management
```

### ADMIN
```bash
gbrain doctor [--json] [--fast]       # Health checks (resolver, skills, DB, embeddings)
gbrain doctor --fix                   # Auto-fix resolver issues
gbrain stats                          # Brain statistics
gbrain serve                          # MCP server (stdio)
gbrain integrations                   # Integration recipe dashboard
gbrain check-backlinks check|fix      # Back-link enforcement
gbrain lint [--fix]                   # LLM artifact detection
gbrain transcribe <audio>             # Transcribe audio (Groq Whisper)
gbrain research init <name>           # Scaffold a data-research recipe
gbrain research list                  # Show available recipes
```

运行 `gbrain --help` 获取完整参考。

---

## 起源故事

> **我在设置 OpenClaw agent 并启动 markdown 大脑 repo。每人一页，每公司一页，编译真相在上，时间线在下。一周内：10,000+ 文件，3,000+ 人，13 年日历数据，280+ 会议转录，300+ 捕获想法。**

> **Agent 在我睡觉时运行。梦循环扫描每次对话，enriches 缺失实体，修复损坏引用，整合记忆。我醒来大脑比睡前更聪明。**

> **这 repo 的技能是那些模式，通用化。手工 11 天构建的作为 mod 你 30 分钟安装。**

---

## 关键数据

| 指标 | 数值 |
|------|------|
| 知识库页数 | 17,888 |
| 人物页面 | 4,383 |
| 公司页面 | 723 |
| Cron 作业 | 21 自主运行 |
| 技能文件 | 25 |
| 构建时间 | 12 天 |
| 安装时间 | ~30 分钟 |
| GitHub Stars | 8.2k |
| Forks | 904 |
| 语言 | TypeScript 98.6% |
| 许可证 | MIT |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Your AI agent is smart but forgetful. GBrain gives it a brain." | 核心价值 |
| "Thin harness, fat skills" | 架构哲学 |
| "Wake up smarter than when you went to bed" | 每日复合 |
| "Skill files are code" | 技能本质 |
| "Brain learns who matters without being told" | 自动 enrichment |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **Thin harness, fat skills** — 智能在技能非 runtime
2. **编译真相 + 时间线** — 知识组织模式
3. **25 技能系统** — 覆盖全工作流
4. **RESOLVER.md** — 技能分发器
5. **混合搜索** — vector + keyword + RRF
6. **Tiered enrichment** — 自动升级实体
7. **Brain-first lookup** — 查大脑先于外部 API
8. **每日复合循环** — 睡觉时摄入醒来更聪明

### 可实施
- 采用 Thin harness, fat skills 架构
- 用编译真相 + 时间线组织内容知识
- 建立技能系统覆盖内容创作全工作流
- 实现 RESOLVER.md 路由意图到技能
- 用混合搜索提升内容检索
- 实现 tiered enrichment 自动升级实体
- Brain-first 查找先于外部 API
- 建立每日复合循环

---

## 相关资源

| 资源 | 链接 |
|------|------|
| GBrain GitHub | https://github.com/garrytan/gbrain |
| GStack | https://github.com/garrytan/gstack |
| OpenClaw | https://openclaw.ai/ |
| Hermes Agent | https://github.com/NousResearch/hermes-agent |
| 语音演示 | https://x.com/garrytan/status/2043022208512172263 |

---

*原始来源：https://github.com/garrytan/gbrain*
