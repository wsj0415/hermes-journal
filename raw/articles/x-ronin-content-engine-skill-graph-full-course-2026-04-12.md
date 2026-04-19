# Ronin 内容引擎 Skill Graph 完整教程

**来源**: https://x.com/deronin_/status/2042604279077237170  
**作者**: Ronin (@deronin_)  
**抓取时间**: 2026-04-12 17:58 UTC  
**类型**: X 推文线程/完整教程  
**标签**: content-engine, skill-graph, ai-content, social-media-automation, markdown, obsidian, content-repurposing, claude, platform-native, content-system

---

## 📊 一句话总结

Ronin 分享用 17 个互联 Markdown 文件（Skill Graph）+ 一个 AI agent 管理 10 个社交媒体账户的完整系统，涵盖 index.md/平台文件/声音文件/钩子公式/复用链/调度日历，实现一个想法产出 10 个平台原生内容（每个平台重新思考而非简单改写）。

---

## 🏷️ 话题标签

#内容引擎 #SkillGraph #AI 内容 #社交媒体自动化 #Markdown #Obsidian #内容复用 #Claude #平台原生 #内容系统

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：Skill Graph 架构图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Technical architecture diagram for "Content Skill Graph System".

Layout: Central index.md with radiating nodes showing 4 folders and 17 files.

Color Palette:
- index.md: Purple (#8B5CF6)
- platforms/: Blue (#3B82F6)
- voice/: Green (#10B981)
- engine/: Yellow (#FBBF24)
- audience/: Red (#EF4444)
- Background: Dark gradient

Center — index.md:
"Command Center"
"Identity + Node Map + Execution"
图标：大脑/指挥中心

4 Folders (环绕):

platforms/ (8 files):
x | linkedin | instagram | tiktok
youtube | threads | facebook | newsletter

voice/ (2 files):
brand-voice | platform-tone

engine/ (4 files):
hooks | repurpose | scheduling | content-types

audience/ (2 files):
builders | casual

Bottom — Workflow:
1 Topic → Read index.md → Follow wikilinks
→ Read relevant nodes → Write 8 platform-native posts
→ Each RETHOUGHT not reformatted

Badge:
"17 Files" | "4 Folders" | "10 Platforms"
"0 Manual Writing"

Style: Clean technical architecture, dark mode with neon folder colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 Skill Graph 系统架构的内容，架构图直接展示 17 文件 4 文件夹的互联结构，比通用 infographic 更精准传达"知识图谱"概念。

---

### 选项 2：内容复用链流程图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
Content repurposing chain flowchart for "1 Idea → 10 Platforms".

Layout: Horizontal 8-step chain showing transformation.

Color Palette:
- Each platform: Unique color
- Arrows: Gradient flow
- Background: Dark gradient

8-Step Chain:

Step 1 — X (Blue):
"Write First"
"280-2,000 chars"
"Find core idea + sharpest hook"

↓

Step 2 — LinkedIn (Purple):
"Expand with Narrative"
"1,300-2,000 chars"
"Add personal story + deeper analysis"

↓

Step 3 — Instagram (Pink):
"Make it Visual"
"7-10 slide carousel"
"Slide 1 = bold hook"

↓

Step 4 — TikTok (Black):
"Make it Raw"
"45-60 sec script"
"Hook in first 2 seconds"

↓

Step 5 — YouTube (Red):
"Make it Deep"
"8-12 min tutorial"
"SEO title + chapters"

↓

Step 6 — Newsletter (Yellow):
"Make it Personal"
"1,000-2,000 words"
"Behind-the-scenes"

↓

Step 7 — Threads (Blue):
"Make it Conversational"
"Under 500 chars"
"Relaxed opinion"

↓

Step 8 — Facebook (Blue):
"Make it Community"
"300-800 chars"
"Add discussion question"

Bottom — Litmus Test:
"If someone followed on ALL platforms,
would they be annoyed seeing same thing?"
NO = Rethought | YES = Reformatted (wrong)

Badge:
"Same Topic, Different Angle"
"10 Platform-Native Posts"

Style: Modern flowchart, dark mode with rainbow platform colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3:Obsidian 图谱可视化风格

**来源**: nano-banana-pro / App / Web Design  
**参考 ID**: 187 (Obsidian Graph View)  
**示例图**: https://cms-assets.youmind.com/media/1772519704561_8123cd_HCbTh8EXEAArOpM.jpg

```prompt
Obsidian graph view screenshot style for "Content Skill Graph".

Style: Dark mode Obsidian interface, neural network visualization showing connected nodes.

Center view:
Network of 17 nodes connected by lines
Central node: index.md (largest, brightest)
Cluster 1: platforms/ (8 nodes, blue)
Cluster 2: voice/ (2 nodes, green)
Cluster 3: engine/ (4 nodes, yellow)
Cluster 4: audience/ (2 nodes, red)

Sidebar:
File tree showing folder structure
/content-skill-graph
├── index.md
├── platforms/
├── voice/
├── engine/
└── audience/

Bottom status:
"17 files" | "4 folders" | "32 wikilinks"
"Neural Network of Your Content System"

Window title: "Content Skill Graph — Obsidian"

Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 教程明确推荐 Obsidian 并提到"图谱视图像看内容系统的神经网络"，Obsidian 风格直接展示作者推荐的工作环境和可视化效果。

---

## 核心问题：为什么大多数人的 AI 内容失败

### 错误用法

```
1. 打开 Claude
2. 输入"给我写一篇关于生产力的 LinkedIn 帖子"
3. 得到像公司实习生写的通用帖子
4. 花 20 分钟让它不那么像机器人写的
5. 然后为每个平台重复整个过程
```

**这不是系统，是额外步骤的杂务**。

---

### 根本问题

不是 AI 的问题，是你给了它：
- ❌ 零品牌上下文
- ❌ 零受众了解
- ❌ 零声音定义
- ❌ 零平台策略
- ❌ 零连接逻辑

**就像每次都雇佣一个失忆的天才**。

---

## 解决方案：Skill Graph（技能图谱）

### 什么是 Skill Graph

**技术定义**: 一个互联 Markdown 文件夹，每个文件是一个"知识节点"，用 `[[wikilinks]]`（双括号链接）引用其他节点。

**比喻**: 不是把新员工扔进深水区希望他们成功，而是给他们一本完整的剧本，解释你是谁、如何操作、跟谁说话、什么是好输出。

---

### 核心差异

| 方式 | 比喻 | 结果 |
|------|------|------|
| **单个提示** | 雇佣没有简报/品牌指南/受众知识的自由职业者 | 通用内容 |
| **Skill Graph** | 雇佣读过完整剧本、知道每个平台如何运作的全职内容团队 | 平台原生内容 |
| **单个.md 文件** | 给你一个工具（简单参考文档） | 有限效果 |
| **图谱** | 给你一个团队（每个平台/钩子/声音/受众的子系统专家） | 系统智能 |

---

### 为什么有效

当 AI agent 指向这个文件夹并给一个主题时，它：
1. 不只看一个文件
2. 跟随链接
3. 阅读连接节点
4. 在写第一个字之前建立对品牌/声音/受众/平台规则/钩子公式/复用逻辑的完整理解

**连接创造智能，单个提示无法匹配**。

---

## 工具选择

### 编辑器（2 选 1）

| 工具 | 优点 | 推荐度 |
|------|------|--------|
| **Obsidian** | 免费 Markdown 编辑器，原生支持 `[[wikilinks]]`，精美图谱视图，像看内容系统神经网络，调试直观 | ⭐⭐⭐⭐⭐ 推荐 |
| **普通文件夹** | 无需新工具，AI 不关心编辑器，VS Code/Notion 导出/记事本都可以 | ⭐⭐⭐⭐ 备选 |

---

### AI 工具（3 选 1）

| 工具 | 用法 | 推荐度 |
|------|------|--------|
| **Claude Projects** | 上传所有.md 文件作为持久上下文，每个对话都有完整图谱访问 | ⭐⭐⭐⭐⭐ 首选 |
| **ChatGPT** | Custom GPTs 或粘贴关键文件到对话 | ⭐⭐⭐⭐ 备选 |
| **Cursor/Claude Code** | 技术用户，agent 直接从本地文件系统读取文件 | ⭐⭐⭐⭐⭐ 最强大 |

---

## 完整文件结构（17 文件 4 文件夹）

```
/content-skill-graph
├── index.md                    # 指挥中心（最重要）
├── platforms/                  # 平台规则（8 文件）
│   ├── x.md
│   ├── linkedin.md
│   ├── instagram.md
│   ├── tiktok.md
│   ├── youtube.md
│   ├── threads.md
│   ├── facebook.md
│   └── newsletter.md
├── voice/                      # 声音定义（2 文件）
│   ├── brand-voice.md
│   └── platform-tone.md
├── engine/                     # 运营引擎（4 文件）
│   ├── hooks.md
│   ├── repurpose.md
│   ├── scheduling.md
│   └── content-types.md
└── audience/                   # 受众定义（2 文件）
    ├── builders.md
    └── casual.md
```

**17 文件。4 文件夹。这就是你的整个内容生产机器**。

---

## 核心文件详解

### 1. index.md（指挥中心）⭐ 最重要

**作用**: 每次给 AI 主题时首先阅读的文件，是整个内容系统的 CEO，看到全局并委托给专家。

**三要素**:

```markdown
# Content Skill Graph — Command Center

## 1. Identity

Content production system for [YOUR BRAND/NAME].
Manages 10 social media accounts from one idea input.

Brand: [YOUR NAME / BRAND]
Niche: [YOUR NICHE — e.g. "AI automation, SaaS building, and
monetizing tech skills"]
Mission: Turn one topic into 10 platform-native posts that each
think about the topic differently

## 2. Node Map

Every node below is a knowledge file. Read the relevant ones before
executing any task. The [[wikilinks]] are clickable, follow them.

### Platforms
- [[x]] — short-form, hook-driven, 280 chars max, casual lowercase.
  post 5x/week minimum. contrarian takes and step-by-step threads
- [[linkedin]] — long-form narrative, professional tone, 1500+ words.
  post 3x/week. personal stories with business insights
- [[instagram]] — visual-first. 7-slide carousels with bold claim
  on slide 1. post 4x/week. reels for short-form video
- [[tiktok]] — raw, unpolished, 45-60 second screen recordings or
  talking head. post 5x/week. hook in first 2 seconds
- [[youtube]] — SEO-optimized titles, structured outlines, 8-12
  minute format. post 2x/week. evergreen content focus
- [[threads]] — conversational, opinion-driven, casual. post 3x/week.
  think "X but more relaxed"
- [[facebook]] — community-focused, longer captions, group engagement.
  post 3x/week
- [[newsletter]] — deep-dive format, 1000-2000 words, actionable
  frameworks. send 1x/week

### Voice
- [[brand-voice]] — the core personality, values, tone markers, and
  vocabulary that define how we sound across ALL platforms
- [[platform-tone]] — how the core voice adapts per platform. same
  person, different room

### Engine
- [[hooks]] — scroll-stopping opener formulas. categorized by type:
  contrarian, proof, discovery, replacement, playbook. updated
  weekly based on performance
- [[repurpose]] — the repurposing chain: 1 idea → 10 outputs. defines
  which platform gets written first, the adaptation order, and what
  changes between each version
- [[scheduling]] — posting calendar, best times per platform,
  frequency rules, and batch workflow
- [[content-types]] — format definitions: threads, carousels, reels,
  long-form articles, short takes, video scripts, newsletters

### Audience
- [[builders]] — primary audience. indie hackers, AI engineers,
  SaaS founders, freelancers monetizing tech skills. they want
  actionable playbooks, real numbers, and tools they can use today
- [[casual]] — secondary audience. curious about AI/tech but not
  building yet. they want inspiration, simplified explanations,
  and "wow I can do this too" moments

## 3. Execution Instructions

When given a topic:

1. Check if the topic aligns with our niche. If not, reject it
2. Read [[brand-voice]] for core personality
3. Read [[hooks]] and select the best hook formula for the topic
4. Read [[repurpose]] for the production chain order
5. Write for the FIRST platform in the chain (usually [[x]])
6. For each subsequent platform, read that platform's node and
   [[platform-tone]] to adapt. don't just reformat, RETHINK the
   angle, structure, hook, and format for that specific platform
7. Apply [[scheduling]] rules for timing and frequency
8. Output one native post per platform, each post ready to publish

CRITICAL RULE: The output is NOT 10 copies of the same text
reformatted for each platform. It's 10 pieces that each THINK
about the topic differently. Same topic, different angle, hook,
voice, structure, and format per platform.
```

**关键设计**:
- Identity 部分不是填充物，AI 用它校准一切
- Node Map 给每个链接带上下文，不仅"[[x]] — Twitter"而是"[[x]] — short-form, hook-driven, 280 chars max..."
- 额外上下文帮助 agent 做决策无需打开每个文件，节省 token

---

### 2. platforms/ 文件夹（8 文件）

每个平台文件是该平台的完整剧本。以 x.md 为例：

```markdown
# X / Twitter

## Platform DNA
- Character limit: 280 per tweet, long-form tweets up to 25,000
  (but sweet spot is 1,000-2,000 characters)
- Vibe: fast, casual, opinion-driven. lowercase is default.
  people scroll fast here, you have maybe 0.5 seconds to stop them
- Audience here: more technical, more builder-oriented. skews
  toward [[builders]] over [[casual]]

## Content Rules
- Write this platform FIRST in the [[repurpose]] chain. X forces
  you to be concise which makes everything else easier to expand
- Use [[hooks]] — contrarian hooks and proof hooks perform best here
- Match [[brand-voice]] but make it more casual. see [[platform-tone]]
  for X-specific adjustments
- Line breaks between every thought. never write dense paragraphs
- No hashtags. ever. they look spammy on X
- Emojis only at the very end as a signoff (heart, or none at all)
- Links go in a reply to your own post, never in the main tweet.
  the algorithm penalizes external links in the main tweet

## Formats That Work
1. The Step-by-Step Thread — "Here's [N] steps to [outcome]:"
   followed by numbered steps. most reliable format for engagement
2. The Short Take — 2-4 lines. bold claim + one-line context +
   punchline. best for contrarian hooks
3. The Proof Post — "[Metric] → [metric] in [timeframe]" followed
   by the breakdown. people can't resist real numbers
4. The Resource Drop — "I just found [thing] — [why it matters]."
   short, high value. always add a personal take
5. The Long-Form Tweet — 1,000-2,000 characters. deep breakdown
   of one idea. use sparingly, 1-2x/week max

## Posting Strategy
- Frequency: 5-7x/week minimum (1-2 posts per day)
- Best times: 8-9am, 12-1pm, 5-6pm (audience timezone)
- Engage in replies for 30 min after posting (algo hack honestly)
- See [[scheduling]] for the full calendar

## Audience on X
- Primary: [[builders]] — indie hackers, AI engineers, SaaS founders
- They want: actionable content, real numbers, tools, playbooks
- They dont want: fluff, motivational quotes without substance,
  generic "AI is changing the world" takes
- Address them as "you" — direct, coaching energy

## Repurposing Notes
- X is the STARTING POINT of the [[repurpose]] chain
- After writing for X, expand for [[linkedin]] (add narrative
  and professional framing)
- Condense the hook for [[tiktok]] (first 2 seconds of video)
- Turn threads into [[instagram]] carousel slides
- See [[repurpose]] for the full chain
```

**其他平台文件遵循相同结构**，只需替换具体细节（字符限制/语气/格式/发布策略等）。

---

### 3. voice/ 文件夹（2 文件）

#### brand-voice.md（品牌声音）

```markdown
# Brand Voice

This file defines the core personality behind all content.
Every platform node ([[x]], [[linkedin]], [[instagram]], etc.)
references this and adapts it to their context.
See [[platform-tone]] for platform-specific adjustments.

## Core Personality

[Write 3-5 sentences describing your brand's personality.
be specific. heres an example for a builder/AI niche:]

We're a builder who teaches while building. casual authority —
we know our stuff but never talk down to anyone. we share real
numbers, real mistakes, real systems. we talk to our audience
like friends who are building alongside us. direct, practical,
allergic to fluff.

## Tone Markers

- Casual but credible — we use "imo", "btw", "lol" naturally
  but back everything with real data and experience
- Direct and personal — we say "I" a lot, address the reader
  as "you", we're coaching not lecturing
- Raw honesty over polish — "the biggest mistake is skipping
  validation" not "one common pitfall is insufficient market
  validation processes"
- Coaching energy — every piece should feel like we're walking
  them through something step by step
- Numbers and proof — include specific metrics whenever possible.
  "$4k MRR", "200 leads/week", "10 accounts". specifics = trust

## Vocabulary

Words we use: build, ship, automate, system, playbook, stack,
workflow, scale, compound, iterate

Words we NEVER use: moreover, furthermore, in conclusion,
it's worth noting, delve, synergy, circle back, holistic

Phrases we use:
- "here's what actually works"
- "most people get this wrong"
- "the real reason is..."
- "study this."
- "hope you loved it."

Phrases we never use:
- "In today's fast-paced world..."
- "It goes without saying..."
- "Without further ado..."
- any corporate buzzword soup

## Formatting Rules
- Lowercase by default for body text
- Title case or ALL CAPS only for hooks/headlines
- Bullet points with - prefix
- Line breaks between every thought, never dense paragraphs
- No hashtags (except Instagram where they actually help)
- Minimal emojis, only as signoffs
```

---

#### platform-tone.md（平台语气适配）

```markdown
# Platform Tone Adaptations

Core voice defined in [[brand-voice]]. This file defines
how that voice ADAPTS per platform.

Like how you talk differently at a house party vs a business
dinner vs a podcast interview (same person, different energy):

## X / Twitter
- Most casual version of the voice
- Lowercase everything
- Short sentences. punchy. no filler
- "lol", "imo", "btw" used freely
- Sarcasm and irony welcome
- Example: "you don't need 10 tools. you need 10 markdown files.
  study this."

## LinkedIn
- Professional but still human. not corporate
- "I" used extensively but framed as lessons/insights
- Longer sentences ok. more narrative structure
- Replace "lol" with thoughtful observations
- Example: "I spent 3 months building a content system that now
  runs 10 accounts for me. Here's exactly what I built."

## Instagram
- Simplest language. visual-first, text supports the visuals
- Carousel text: bold, short, one idea per slide. max 8 words on slide 1
- Caption: more detailed but still scannable
- Aspirational energy, "you can do this too"
- Example: "I run 10 accounts with zero manual writing.
  Swipe to see the exact system."

## TikTok
- Most energetic version of the voice
- Spoken, not written. write how you actually talk
- Fast-paced, no filler, hook immediately
- "This is insane" energy is allowed here
- Example: "You're still writing content manually?
  Let me show you what I use instead."

## YouTube
- Most structured and educational
- Longer, more detailed, more step-by-step
- Authority voice — you're the expert teaching a class
- Still casual but with depth
- Example: "Today I'm showing you step by step how to build
  a content system using nothing but markdown files and AI."

## Newsletter
- Most personal and intimate
- Like writing a letter to a smart friend
- Can be vulnerable, reflective, behind-the-scenes
- Longest-form version of any thought

## Threads
- Similar to X but even more relaxed
- More opinion, less structure
- "shower thought" energy
- Example: "hot take: a folder of markdown files is more
  powerful than any content marketing tool on the market"

## Facebook
- Warmest and most community-oriented
- Ask questions. invite discussion
- More personal stories, less tactical playbooks

## The Rule

When adapting across platforms: CHANGE the tone first.
Then change the format. Then change the hook. The voice stays
the same — only the delivery changes.
```

---

### 4. engine/ 文件夹（4 文件）

#### hooks.md（钩子公式）

```markdown
# Hook Formulas

Use these to open every post. Match hook type to platform and topic.
See [[platform-tone]] for delivery adjustments.

## The Playbook Hook
"Here's [N] steps to [desirable outcome]:"
- Best on: X, LinkedIn, YouTube titles
- Examples:
  - "Here's 7 steps to automate your content production:"
  - "Here's how I run 10 accounts without writing manually:"

## The Proof Hook
"[Before metric] → [after metric] in [timeframe]"
- Best on: X, LinkedIn
- Examples:
  - "0 → 10 accounts managed in 30 days using markdown files"
  - "$8k/mo content spend → $0 after building one system"

## The Contrarian Hook
"You don't need [conventional thing]. You need [this instead]."
- Best on: X, Threads
- Examples:
  - "You don't need a content team. You need a skill graph."
  - "You don't need 15 tools. You need 15 markdown files."

## The Replacement Hook
"I replaced [expensive/complex thing] with [simple thing]"
- Best on: X, TikTok, Instagram slide 1
- Examples:
  - "I replaced my $8k/mo content team with a folder of .md files"
  - "I replaced 5 content tools with 30 wikilinked markdown files"

## The Discovery Hook
"I just found [valuable thing]"
- Best on: X
- Examples:
  - "I just found a way to make AI write differently per platform"

## The Behind-the-Scenes Hook
"I run [impressive thing] and [surprising method]"
- Best on: X, LinkedIn, YouTube titles
- Examples:
  - "I run 10 social media accounts and don't write a single post"

## Rules
- Test 2-3 hooks per topic before publishing
- Track which types get the most engagement PER PLATFORM
- Update this weekly. remove underperformers, add new winners
- Hook for [[x]] is almost never the same as hook for [[linkedin]]
```

---

#### repurpose.md（复用链）⭐ 核心引擎

```markdown
# Repurposing Chain

One idea enters. Ten platform-native posts come out. Each one
THINKS about the topic differently — this is NOT reformatting.

## The Chain Order

Write in this order. Each step builds on the previous but adapts.

### Step 1: [[x]] (Write First)
X forces brevity. starting here makes you find the core idea
and the sharpest hook. everything else expands from this.
- Output: one tweet or long-form tweet (280-2,000 chars)

### Step 2: [[linkedin]] (Expand with Narrative)
Take the X post, add personal story and deeper analysis.
Don't just add more words — add a DIFFERENT ANGLE.
- X says: "I replaced my content team with .md files"
- LinkedIn says: "3 months ago I was spending $8k/mo on content.
  Here's what happened when I built a system with markdown and Claude"
- Output: long-form post (1,300-2,000 chars)

### Step 3: [[instagram]] (Make it Visual)
Extract key points and turn into carousel slides. angle shifts
to visual-first, scannable, aspirational.
- Output: 7-10 slide carousel + caption
- Slide 1 = bold hook
- Each slide = one idea, max 30 words

### Step 4: [[tiktok]] (Make it Raw)
Condense to a 45-60 second script. the angle is SHOWING not telling.
- Output: video script with timestamps
- Hook in first 2 seconds
- Show the system in action if possible

### Step 5: [[youtube]] (Make it Deep)
Combine everything into a structured tutorial. the viewer should
be able to REPLICATE what you're showing.
- Output: full video outline (8-12 min)
- SEO title + description
- Timestamps for chapters

### Step 6: [[newsletter]] (Make it Personal)
Deepest, most personal take. behind-the-scenes context, lessons,
exclusive insights not shared on social.
- Output: 1,000-2,000 word email

### Step 7: [[threads]] (Make it Conversational)
Adapt X version with more relaxed, opinion-driven angle.
- Output: 1-3 short posts (under 500 chars each)

### Step 8: [[facebook]] (Make it Community)
Add a discussion question. frame as invitation to share, not
just consume.
- Output: post with a question at the end

## The Litmus Test

Each platform version should pass this test:

"If someone followed me on ALL platforms, would they be
annoyed seeing the same thing everywhere?"

If yes → you're reformatting, not rethinking. go back
If no → you've made 8 unique pieces from one idea. thats the goal

## What Actually Changes Between Platforms

| Element | How It Adapts |
|---------|--------------|
| Angle | Different entry point into the same topic |
| Hook | Rewritten per platform |
| Tone | Adjusted per [[platform-tone]] |
| Format | Thread vs carousel vs video vs long-form |
| Length | 280 chars → 2,000 words |
| Depth | Surface insight → deep tutorial |

## Batch Workflow

1. Write ALL platform versions in one session, not across days
2. Follow the chain order — each step feeds the next
3. Review all 8 outputs together before publishing any
4. Schedule using [[scheduling]] to stagger across the week
```

---

#### scheduling.md（调度日历）

```markdown
# Scheduling & Posting Calendar

## Weekly Frequency
| Platform | Posts/Week | Best Days |
|----------|-----------|-----------|
| X | 7-10 | Daily |
| LinkedIn | 3-5 | Mon-Thu |
| Instagram | 4-5 | Mon, Wed, Fri, Sat |
| TikTok | 5-7 | Daily |
| YouTube | 1-2 | Tue, Thu or Sat |
| Newsletter | 1 | Tue or Thu morning |
| Threads | 3-5 | whenever posting to X |
| Facebook | 3 | Tue, Thu, Sat |

## Peak Posting Times
| Platform | Best Times |
|----------|-----------|
| X | 8-9am, 12-1pm, 5-6pm |
| LinkedIn | 7-8am, 12pm, 5-6pm |
| Instagram | 11am-1pm, 7-9pm |
| TikTok | 7-9am, 12-3pm, 7-10pm |
| YouTube | 2-4pm day before (indexes overnight) |
| Newsletter | 8-10am |

## Batch Workflow

Weekly Batch (Sunday or Monday):
1. Choose 2-3 topics for the week
2. Run the full [[repurpose]] chain for each
3. This gives you 16-24 posts for the whole week in one sitting
4. Schedule everything (Buffer, Hypefury, Later, or native schedulers)

Daily (15 min):
1. Check engagement
2. Reply to comments in the first hour
3. Note what hooks/formats performed

Weekly Review (Friday):
1. What topics performed best? → more of those
2. What hook types drove engagement? → update [[hooks]]
3. Which platform growing fastest? → double down
4. Any new content ideas from comments/DMs?
```

---

#### content-types.md（内容类型）

```markdown
# Content Types & Formats

## Thread / Multi-Part Post
- Platforms: X (thread), LinkedIn (multi-paragraph), Threads
- When: step-by-step guides, listicles, breakdowns
- Structure: hook → numbered steps → conclusion + CTA

## Carousel / Slide Post
- Platforms: Instagram, LinkedIn (document posts)
- When: visual guides, processes, comparisons
- Structure: slide 1 = hook, slides 2-9 = content, last = CTA

## Short-Form Video
- Platforms: TikTok, Instagram Reels, YouTube Shorts
- When: quick tips, demos, reactions, behind-the-scenes
- Structure: hook (2 sec) → content (30-50 sec) → CTA (5 sec)

## Long-Form Video
- Platforms: YouTube
- When: tutorials, deep dives, system walkthroughs
- Structure: hook (30 sec) → context (90 sec) → main (6-8 min) → recap

## Long-Form Text
- Platforms: Newsletter, LinkedIn articles, blog
- When: deep analysis, personal stories, comprehensive guides
- Length: 1,000-3,000 words

## Short Take
- Platforms: X, Threads, Facebook
- When: hot takes, observations, single insights
- Length: under 280 chars (X) or 500 chars (Threads)
```

---

### 5. audience/ 文件夹（2 文件）

#### builders.md（构建者受众）

```markdown
# Audience: Builders

## Who They Are
Indie hackers, solo founders, AI engineers, SaaS builders,
freelancers, agency owners. already building something or
actively planning to. technical enough to implement what you teach.
revenue range $0-$50k/mo, aspiring to scale

## What They Want
- Actionable playbooks, not theory. steps they can follow TODAY
- Real numbers. revenue, metrics, costs, time saved
- Tool recommendations with context, not just "use this tool"
  but "heres when and why"
- Systems thinking — how pieces connect, not just individual tactics

## How to Talk to Them
- Direct and specific. "Here's 5 steps" not "consider exploring"
- Show your work. real screenshots, real numbers, real process
- Peer energy — building alongside them, not above them
- Challenge them: "if you're not doing this, you're leaving
  money on the table"
```

---

#### casual.md（休闲受众）

```markdown
# Audience: Casual

## Who They Are
Curious about AI/tech but not deeply technical. might be
professionals in non-tech roles thinking about AI. early in
their journey, consuming more than creating. aspirational —
they want to be builders but havent started yet

## What They Want
- Simplified explanations of complex topics
- Inspiration and "I can do this too" energy
- Entry points — where to start, what to learn first
- Results that seem achievable, not intimidating

## How to Talk to Them
- Simpler language. explain acronyms. define terms
- More encouraging, less challenging
- "Here's the easiest way to start" energy
- Analogies and comparisons to things they already understand
```

---

## 三种使用方法

### 方法 1：Claude Projects（推荐）

```
1. 在 Claude 创建新项目叫"Content Skill Graph"
2. 上传所有 17 个文件到项目知识库
3. 开始新对话并给主题：

   Topic: How I use markdown files to run 10 social media accounts
   without writing anything manually

   Follow the execution instructions in index.md. Produce one
   native post for each platform in the repurpose chain order.
   Each post should think about the topic differently — not
   reformatted, RETHOUGHT for each platform.

4. Claude 阅读 index.md，跟随 wikilinks，阅读平台文件/声音文件/钩子/复用链，输出 8 个平台原生帖子
5. 审查。调度。发布。去做别的事
```

---

### 方法 2：粘贴上下文（最简单，适用于任何工具）

```
1. 复制 index.md 内容
2. 粘贴到任何 AI 聊天（Claude 免费/ChatGPT/任何工具）
3. 添加："Here's my content system. When I give you a topic
   follow the execution instructions. For each platform write
   a native post that rethinks the topic for that platform,
   not reformatted, completely rethought"
4. 给主题

更好效果：同时粘贴 brand-voice.md 和你正在生产的平台文件。更多上下文 = 更好输出。总是。
```

---

### 方法 3：Cursor / Claude Code（最强大，最技术）

```
1. 保持 skill graph 文件夹在本地机器上
2. 指向 Cursor 或 Claude Code 到文件夹
3. Agent 直接从文件系统读取文件
4. 它还可以更新文件 — 添加新钩子到 hooks.md，基于表现优化 platform-tone.md

这是完全自主版本，图谱随时间自我进化。就像给系统复合记忆。
```

---

## 实战示例："重新思考而非改写"

**主题**: "How I use AI to manage 10 social media accounts"

### X（对立线程，小写随意，逐步）
```
you don't need a content team. you need 30 markdown files.
here's how i run 10 accounts without writing a single post manually:
[10 步线程]
```

### LinkedIn（个人叙事，专业语气，~1500 字）
```
6 months ago, I was spending $8,000 a month on content production
across 10 platforms. Today I spend $0. Here's exactly what changed.
[个人故事 + 商业洞察]
```

### Instagram（7 幻灯片轮播，视觉优先，幻灯片 1 大胆声明）
```
幻灯片 1: "I Run 10 Accounts And Don't Write Anything."
幻灯片 2-7: 系统分解为视觉步骤
幻灯片 8: "Save this. Follow for more"
```

### TikTok（45 秒原始屏幕录制脚本）
```
"You're still writing content manually for every single platform?
Let me show you what I use instead."
[显示文件夹结构/Obsidian 图谱视图/Claude 输出帖子]
```

### YouTube（SEO 标题 + 结构化大纲，8 分钟格式）
```
标题："How to Run 10 Social Media Accounts with AI
(Complete System Walkthrough)"
[完整教程带屏幕录制]
```

### Newsletter（1500 字深度）
```
"This week I want to pull back the curtain on something
I've been building quietly for months..."
[幕后上下文 + 独家洞察]
```

### Threads（热门观点，对话式）
```
"hot take: the future of content isn't AI that writes for you.
it's AI that thinks like 10 different people for you"
```

### Facebook（社区讨论）
```
"Has anyone else tried building a system to manage multiple
social accounts at once? Here's what I've been experimenting
with — curious what you all think"
```

**同一主题。八个完全不同内容。每个平台原生。每个对在所有平台关注的人都有价值**。

---

## 实施步骤（本周末完成）

### 第 1 步：创建文件夹（2 分钟）
```
1. 打开 Obsidian 或在桌面创建文件夹
2. 创建 4 个子文件夹（platforms/voice/engine/audience）
3. 创建 17 个空.md 文件
4. 然后回来填充每个文件
```

### 第 2 步：先填充 index.md 和 brand-voice.md
```
这两个文件定义一切。如果你不知道你是谁/系统做什么，
其他文件不重要。
```

### 第 3 步：填充前 3 个平台文件
```
不需要第一天全部 8 个平台。从最活跃的 3 个开始。
之后添加其余。
```

### 第 4 步：填充 hooks.md 和 repurpose.md
```
这些是引擎。如何开始帖子和如何倍增它们。
```

### 第 5 步：上传到 Claude Projects
```
（或粘贴到你使用的任何 AI 工具）
```

### 第 6 步：给主题并测试
```
看输出什么。基于输出调整文件。
第一版不会完美，没关系，随时间优化节点会更好。
```

### 第 7 步：每周迭代
```
- 更新 hooks.md 与表现好的内容
- 优化 platform-tone.md 基于学到的
- 准备好时添加新平台文件
```

**Skill Graph 设计为增长**。从小开始，添加节点，优化连接。每周它变得更聪明因为你将学到的编码到文件本身。

**就像复利，但是为你的内容系统**。

---

## 关键数据

| 指标 | 数值 |
|------|------|
| 总文件数 | 17 |
| 文件夹数 | 4 |
| 平台覆盖 | 10 |
| 手动写作 | 0 |
| 每周批次时间 | ~2-3 小时 |
| 产出帖子/周 | 16-24 |
| 替代成本 | $5k/mo 内容团队 |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "不是重新格式化，是重新思考" | 核心理念 |
| "同一主题，不同角度" | 平台原生定义 |
| "连接创造智能" | Skill Graph 价值 |
| "就像复利但为内容系统" | 复合效应 |
| "一个文件夹。17 文件。1 AI。10 平台。0 手动写作" | 系统总结 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **Skill Graph 架构** — 互联 Markdown 文件作为知识库
2. **平台原生思维** — 每个平台重新思考而非改写
3. **复用链设计** — X→LinkedIn→Instagram→TikTok→YouTube→Newsletter
4. **钩子公式库** — 6 类钩子按平台匹配
5. **声音适配** — 核心声音 + 平台语气变化
6. **受众细分** — builders vs casual 不同沟通方式

### 可实施
- 为内容创作建立 Skill Graph
- 实现平台原生内容生成（非简单改写）
- 建立钩子公式库并每周更新
- 定义品牌声音和平台语气适配
- 细分受众并针对性沟通
- 实施每周批次工作流

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Ronin 原文 | https://x.com/deronin_/status/2042604279077237170 |
| Obsidian | https://obsidian.md |
| Claude Projects | https://claude.ai |

---

*原始来源：https://x.com/deronin_/status/2042604279077237170*
