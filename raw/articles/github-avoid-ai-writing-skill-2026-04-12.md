# Avoid AI Writing — AI 写作模式检测与重写技能

**来源**: https://github.com/conorbronsdon/avoid-ai-writing  
**作者**: Conor Bronsdon  
**抓取时间**: 2026-04-12 06:05 UTC  
**类型**: GitHub 仓库/Skill  
**标签**: ai-writing, content-audit, de-ai-ify, writing-skill, claude-code, openclaw, content-quality, human-writing, prompt-engineering, content-optimization

---

## 📊 一句话总结

这是一个审计和重写内容以去除 AI 写作模式（"AI-isms"）的 Skill，支持重写/检测双模式，涵盖 36 种 AI 模式检测（格式/句子结构/词汇/结构/沟通/元模式），109 词替换表（3 层级），5 种上下文 profile 适配，与 Claude Code/OpenClaw/Hermes 兼容。

---

## 🏷️ 话题标签

#AIWriting #内容审计 #去 AI 味 #写作技能 #ClaudeCode #OpenClaw #内容质量 #人类写作 #PromptEngineering #内容优化

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：AI vs 人类写作对比图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Before/After comparison infographic for "Avoid AI Writing Skill".

Layout: Side-by-side comparison showing AI text vs human rewrite.

Color Palette:
- AI Text: Red tones (#EF4444)
- Human Text: Green tones (#10B981)
- Background: Dark gradient

Left — AI-Generated Text (Before):
红色高亮标记 AI 模式：
"Certainly!"
"vibrant startup nestled"
"watershed moment"
"serves as, featuring, boasting"
"Experts believe"
"Moreover"
"The future looks bright"
"Only time will tell"
"Feel free to reach out"

标注：15+ AI tells in one paragraph

Right — Human Rewrite (After):
绿色干净文本：
"Acme Analytics raised $40M Series B"
"Boulder-based startup"
"runs queries in under a second"
"380 companies are paying"
"They'll use money to hire"

标注：Direct. Specific. Human.

Bottom — 36 Patterns Detected:
6 类别：
Formatting | Sentence | Words | Structure | Communication | Meta

Badge:
"901 Stars" | "MIT License" | "2 Modes: Rewrite/Detect"

Style: Clean technical comparison, dark mode with red/green contrast
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 AI 写作检测与重写的内容，前后对比图直接展示技能效果，比抽象 infographic 更直观传达"去 AI 味"价值。

---

### 选项 2:36 模式分类架构图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
36 AI writing patterns categorized diagram.

Layout: 6 category boxes with pattern counts.

Color Palette:
- Content: Blue (#3B82F6)
- Language: Purple (#8B5CF6)
- Structure: Green (#10B981)
- Communication: Yellow (#FBBF24)
- Meta: Orange (#F97316)
- Background: Dark gradient

6 Categories:

Content (7 patterns):
Significance inflation | Notability name-dropping
Superficial -ing | Promotional language
Vague attributions | Formulaic challenges | Novelty inflation

Language (7 patterns):
Word replacements (3 tiers) | Copula avoidance
Synonym cycling | Template phrases | Filler phrases
False ranges | Parenthetical hedging

Structure (9 patterns):
Formatting | Sentence structure | Structural issues
Transition phrases | Inline-header lists | Title case headings
Numbered list inflation | False concession | Rhetorical questions

Communication (8 patterns):
Chatbot artifacts | "Let's" constructions | Cutoff disclaimers
Generic conclusions | Emotional flatline | Reasoning chain artifacts
Sycophantic tone | Acknowledgment loops

Meta (5 patterns):
Excessive structure | Rhythm/uniformity | Over-polishing
Rewrite-vs-patch threshold | Confidence calibration

Bottom Badge:
"109 Word Replacements" | "3 Tiers" | "5 Context Profiles"
"Rewrite Mode | Detect Mode"

Style: Modern categorized grid, dark mode with neon category colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3:3 层词汇表可视化

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
3-Tier vocabulary replacement table visualization.

Layout: Vertical 3-tier pyramid showing flagging strictness.

Color Palette:
- Tier 1: Red (#EF4444)
- Tier 2: Yellow (#FBBF24)
- Tier 3: Green (#10B981)
- Background: Dark gradient

Tier 1 (Top — Always Flag):
"5-20x more often in AI text"
delve | landscape | tapestry | realm | paradigm | embark
beacon | testament | robust | comprehensive | cutting-edge
leverage | pivotal | underscores | meticulous | seamless
game-changer | utilize | watershed | nestled | vibrant
thriving | showcasing | deep dive | unpack | bustling
intricate | complexities | ever-evolving | holistic | actionable
...

Tier 2 (Middle — Flag 2+ in paragraph):
harness | navigate | foster | elevate | unleash | streamline
empower | bolster | spearhead | resonate | revolutionize
facilitate | underpin | nuanced | crucial | multifaceted
ecosystem | myriad | plethora | encompass | catalyze
...

Tier 3 (Bottom — Flag at high density):
significant | innovative | effective | dynamic | scalable
compelling | unprecedented | exceptional | remarkable
sophisticated | instrumental | world-class | state-of-the-art

Bottom Badge:
"109 Words" | "3 Tiers" | "Reduces false positives"
"Cluster detection" | "Density-based flagging"

Style: Technical pyramid diagram, dark mode with tier colors
Aspect ratio: 9:16 portrait
```

---

## 核心功能

### 双模式操作

| 模式 | 功能 | 触发词 | 输出 |
|------|------|--------|------|
| **Rewrite** (默认) | 标记 AI 模式并重写修复 | 默认 | Issues found → Rewritten version → What changed → Second-pass audit |
| **Detect** | 仅标记 AI 模式不重写 | "detect"/"flag only"/"audit only"/"just flag"/"scan" | Issues found (P0/P1/P2) → Assessment |

---

### 36 种 AI 写作模式检测

#### Content Patterns (7 种)

| # | 模式 | Before | After |
|---|------|--------|-------|
| 1 | **Significance inflation** | "marking a pivotal moment in the evolution of..." | "was founded in 2019 to solve X" |
| 2 | **Notability name-dropping** | "cited in NYT, BBC, and Wired" | "In a 2024 NYT interview, she argued..." |
| 3 | **Superficial -ing analyses** | "symbolizing... reflecting... showcasing..." | Replace with specific facts or cut |
| 4 | **Promotional language** | "nestled within the breathtaking region" | "is a town in the Gonder region" |
| 5 | **Vague attributions** | "Experts believe it plays a crucial role" | "according to a 2019 survey by Gartner" |
| 6 | **Formulaic challenges** | "Despite challenges... continues to thrive" | Name the challenge and the response |
| 7 | **Novelty inflation** | "He introduced a term I hadn't heard before" | "He walked through how X works in practice" |

---

#### Language Patterns (7 种)

| # | 模式 | Before | After |
|---|------|--------|-------|
| 8 | **Word/phrase replacements (3 tiers)** | "leverage... robust... seamless... utilize" | "use... reliable... smooth... use" |
| 9 | **Copula avoidance** | "serves as... features... boasts" | "is... has" |
| 10 | **Synonym cycling** | "developers... engineers... practitioners... builders" | "developers" (repeat the clear word) |
| 11 | **Template phrases** | "a [adj] step towards [adj] infrastructure" | Describe the specific capability |
| 12 | **Filler phrases** | "In order to," "Due to the fact that" | "To," "Because" |
| 13 | **False ranges** | "from the Big Bang to dark matter" | List the actual topics |
| 14 | **Parenthetical hedging** | "tools (like X and Y)" | Name them directly or cut |

---

#### Structure Patterns (9 种)

| # | 模式 | Before | After |
|---|------|--------|-------|
| 15 | **Formatting** | Em dashes (— and --), bold overuse, emoji headers | Commas/periods, prose paragraphs |
| 16 | **Sentence structure** | "It's not X, it's Y" + hollow intensifiers | Direct positive statements |
| 17 | **Structural issues** | Uniform paragraphs, formulaic openings | Varied length, lead with the point |
| 18 | **Transition phrases** | "Moreover," "Furthermore," "In today's [X]" | "and," "also," or restructure |
| 19 | **Inline-header lists** | "**Speed:** Speed improved by..." | Write the point directly |
| 20 | **Title case headings** | "Strategic Negotiations And Partnerships" | "Strategic negotiations and partnerships" |
| 21 | **Numbered list inflation** | "Here are 7 reasons why..." | Cut to the 2-3 that matter |
| 22 | **False concession** | "While X has limitations, it's still remarkable" | State the real tradeoff |
| 23 | **Rhetorical question openers** | "What if there were a better way to...?" | Lead with the claim |

---

#### Communication Patterns (8 种)

| # | 模式 | Before | After |
|---|------|--------|-------|
| 24 | **Chatbot artifacts** | "I hope this helps! Let me know if..." | Remove entirely |
| 25 | **"Let's" constructions** | "Let's explore," "Let's break this down" | Just start with the point |
| 26 | **Cutoff disclaimers** | "While details are limited in available sources..." | Find sources or remove |
| 27 | **Generic conclusions** | "The future looks bright," "Only time will tell" | Specific closing thought or cut |
| 28 | **Emotional flatline** | "What surprised me most," "I was fascinated" | Earn the emotion or cut the claim |
| 29 | **Reasoning chain artifacts** | "Let me think step by step," "Breaking this down" | State conclusion, then evidence |
| 30 | **Sycophantic tone** | "Great question!", "You're absolutely right!" | Remove entirely |
| 31 | **Acknowledgment loops** | "You're asking about," "To answer your question" | Just answer directly |
| 32 | **Confidence calibration** | "It's worth noting," "Interestingly," "Surprisingly" | Let the fact speak for itself |

---

#### Meta Patterns (5 种)

| # | 模式 | Before | After |
|---|------|--------|-------|
| 33 | **Excessive structure** | 5 headers in 200 words, "Overview:", "Key Points:" | Merge sections, use specific headers |
| 34 | **Rhythm and uniformity** | All sentences 15–25 words, all paragraphs same length | Mix short/long, fragments, questions |
| 35 | **Over-polishing** | Every irregularity sanded away, perfectly uniform | Keep natural disfluency, varied rhythm |
| 36 | **Rewrite-vs-patch threshold** | 5+ vocabulary flags + 3+ pattern categories + uniform rhythm | Advise full rewrite, not patching |

---

### 109 词替换表（3 层级）

#### Tier 1 — Always Flag (总是标记)

这些词在 AI 文本中出现频率比人类文本高 5-20 倍：

| Replace | With |
|---------|------|
| delve / delve into | explore, dig into, look at |
| landscape (metaphor) | field, space, industry, world |
| tapestry | (describe the actual complexity) |
| realm | area, field, domain |
| paradigm | model, approach, framework |
| embark | start, begin |
| beacon | (rewrite entirely) |
| testament to | shows, proves, demonstrates |
| robust | strong, reliable, solid |
| comprehensive | thorough, complete, full |
| cutting-edge | latest, newest, advanced |
| leverage (verb) | use |
| pivotal | important, key, critical |
| underscores | highlights, shows |
| meticulous / meticulously | careful, detailed, precise |
| seamless / seamlessly | smooth, easy, without friction |
| game-changer / game-changing | describe what specifically changed |
| utilize | use |
| watershed moment | turning point, shift |
| nestled | is located, sits, is in |
| vibrant | (describe what makes it active, or cut) |
| thriving | growing, active (or cite a number) |
| showcasing | showing, demonstrating (or cut the clause) |
| deep dive / dive into | look at, examine, explore |
| unpack / unpacking | explain, break down, walk through |
| intricate / intricacies | complex, detailed |
| complexities | (name the actual complexities) |
| ever-evolving | changing, growing |
| holistic / holistically | complete, full, whole |
| actionable | practical, useful, concrete |
| learnings | lessons, findings, takeaways |
| at its core | (cut — just state the thing) |
| in order to | to |
| due to the fact that | because |
| serves as | is |
| features (verb) | has, includes |
| boasts | has |
| commence | start, begin |
| ascertain | find out, determine |
| endeavor | effort, attempt, try |

---

#### Tier 2 — Flag when 2+ in paragraph (段落中出现 2+ 时标记)

这些词单独出现没问题，但同一段落出现 2 个以上是强 AI 信号：

| Replace | With |
|---------|------|
| harness | use, take advantage of |
| navigate / navigating | work through, handle, deal with |
| foster | encourage, support, build |
| elevate | improve, raise, strengthen |
| unleash | release, enable, unlock |
| streamline | simplify, speed up |
| empower | enable, let, allow |
| bolster | support, strengthen, back up |
| spearhead | lead, drive, run |
| resonate / resonates with | connect with, appeal to, matter to |
| revolutionize | change, transform, reshape |
| facilitate / facilitates | enable, help, allow, run |
| underpin | support, form the basis of |
| nuanced | specific, subtle, detailed |
| crucial | important, key, necessary |
| multifaceted | (describe the actual facets, or cut) |
| ecosystem (metaphor) | system, community, network, market |
| myriad | many, numerous (or give a number) |
| plethora | many, a lot of (or give a number) |
| encompass | include, cover, span |
| catalyze | start, trigger, accelerate |
| reimagine | rethink, redesign, rebuild |
| galvanize | motivate, rally, push |
| augment | add to, expand, supplement |
| cultivate | build, develop, grow |
| illuminate | clarify, explain, show |
| elucidate | explain, clarify, spell out |
| juxtapose | compare, contrast, set side by side |
| cornerstone | foundation, basis, key part |
| paramount | most important, top priority |
| poised (to) | ready, set, about to |
| burgeoning | growing, emerging |
| nascent | new, early-stage, emerging |
| quintessential | typical, classic, defining |
| overarching | main, central, broad |

---

#### Tier 3 — Flag only at high density (高密度时标记)

这些是正常词汇，仅当文本饱和时标记（约占总词数 3%+）：

| Word | What to do |
|------|------------|
| significant / significantly | Replace some with specifics: numbers, comparisons, examples |
| innovative / innovation | Describe what's actually new |
| effective / effectively | Say how or cite a metric |
| dynamic / dynamics | Name the actual forces or changes |
| scalable / scalability | Describe what scales and to what |
| compelling | Say why it compels |
| unprecedented | Name the precedent it breaks (or cut) |
| exceptional / exceptionally | Cite what makes it an exception |
| remarkable / remarkably | Say what's worth remarking on |
| sophisticated | Describe the sophistication |
| instrumental | Say what role it played |
| world-class / state-of-the-art / best-in-class | Cite a benchmark or comparison |

---

### 5 种上下文 Profile

| Profile | 适用场景 | 严格度 |
|---------|----------|--------|
| **linkedin** | 短社交内容 | 宽松（bold/emoji/列表可用） |
| **blog** | 默认长文 | 全部规则全强度 |
| **technical-blog** | 技术博客 | 技术词汇豁免 |
| **investor-email** | 投资者邮件 | 最严格（promotional language 额外严格） |
| **docs** | 文档/README | 清晰优先于声音 |
| **casual** | Slack/内部笔记 | 仅捕获最严重问题 |

---

### 严重性分级

| 级别 | 含义 | 示例 |
|------|------|------|
| **P0** | 可信度杀手（立即修复） | Cutoff disclaimers / Chatbot artifacts / Vague attributions |
| **P1** | 明显 AI 味（发布前修复） | Word-list violations / Template phrases / "Let's" openers / Em dashes >1/1000 字 |
| **P2** | 风格润色（有时间时修复） | Generic conclusions / Rule of three / Uniform paragraph length / Transition phrases |

---

## 安装与使用

### Claude Code

**选项 1: Clone 到 skills 目录**
```bash
git clone https://github.com/conorbronsdon/avoid-ai-writing ~/.claude/skills/avoid-ai-writing
```

**选项 2: 直接复制文件**
```bash
# 下载 SKILL.md 放到任何 Claude Code 可读目录
# 在 CLAUDE.md 中引用
- Editing for AI patterns → read `path/to/avoid-ai-writing/SKILL.md`
```

**选项 3: 用作 slash command**
```bash
# 创建命令文件 ~/.claude/commands/clean-ai-writing.md
---
description: Audit and rewrite content to remove AI writing patterns
---

$ARGUMENTS

Read and follow the instructions in ~/.claude/skills/avoid-ai-writing/SKILL.md
```

然后用 `/clean-ai-writing <your text>`

---

### OpenClaw

**选项 1: 从 ClawHub 安装**
```bash
clawhub install avoid-ai-writing
```

**选项 2: Clone 到 skills 目录**
```bash
git clone https://github.com/conorbronsdon/avoid-ai-writing ~/.openclaw/skills/avoid-ai-writing
```

---

### 触发技能

安装后，让助手清理 AI 写作：
- "Remove AI-isms from this post"
- "Audit this draft for AI tells"
- "Make this sound less like AI"
- "Clean up AI writing in this paragraph"

---

## 完整示例

### Before (AI-generated)

> Certainly! Here's a comprehensive overview of Acme's Series B.
>
> Acme Analytics, a vibrant startup nestled in the heart of Boulder's thriving tech ecosystem, has secured $40M in Series B funding — marking a watershed moment for the company and the observability landscape at large. The round was led by Sequoia, with participation from Andreessen Horowitz, Y Combinator, and Index Ventures, underscoring the robust investor confidence in Acme's vision.
>
> The platform serves as a unified hub for engineering teams, featuring real-time dashboards, boasting sub-second query performance, and presenting a seamless integration layer. It's not just another monitoring tool — it's a paradigm shift in how organizations navigate complex distributed systems. Experts believe Acme is poised to disrupt the $15B observability market. Studies show that companies utilizing comprehensive monitoring solutions can ascertain issues 40% faster.
>
> - 🚀 **Performance:** The platform streamlines incident response, empowering engineers to resolve issues faster.
> - 💡 **Scale:** Acme fosters collaboration across teams, from frontend developers to SRE practitioners to platform builders to infrastructure engineers.
> - ✅ **Adoption:** Customer adoption continues to accelerate, reflecting broader industry trends.
>
> Moreover, Acme's approach showcases the potential of modern observability — symbolizing a shift toward proactive monitoring, reflecting years of R&D investment, and highlighting the intricate interplay between data collection and actionable intelligence. Despite challenges common in the crowded monitoring space, Acme continues to thrive. In order to fully capitalize on this momentum, the company plans to expand its go-to-market endeavors.
>
> In conclusion, the future looks bright for Acme Analytics. Only time will tell how this game-changer will reshape the observability paradigm. Feel free to reach out if you'd like more details!

---

### After (cleaned up)

> Acme Analytics raised a $40M Series B led by Sequoia. The Boulder-based startup makes an observability platform that runs queries in under a second and plugs into existing monitoring stacks without custom integration work.
>
> The pitch is speed. Their median time-to-resolution is 12 minutes, compared to the 45-minute industry average that Datadog reported in 2024. That gap is why 380 companies are paying for it.
>
> They'll use the money to hire sales reps in EMEA and add log management. The monitoring market is crowded, but Acme's bet is that most teams still stitch together three or four tools and lose time switching between them.

---

### 捕获的 AI 模式

35+ AI tells:
- Chatbot artifacts (Certainly!, Feel free to reach out)
- 3 em dashes
- Promotional language (vibrant, nestled, thriving)
- Significance inflation (watershed moment)
- Copula avoidance (serves as, featuring, boasting, presenting)
- 10 word replacements (landscape, robust, seamless, paradigm, streamline, empower, foster, utilize, ascertain, endeavor)
- Synonym cycling (developers/practitioners/builders/engineers)
- Negative parallelism (It's not just X, it's Y)
- Notability name-dropping (Sequoia, a16z, YC, Index stacked)
- Vague attributions (Experts believe, Studies show)
- Filler phrases (In order to, Moreover)
- Inline-header list with emoji
- Superficial -ing analysis (symbolizing... reflecting... highlighting...)
- Formulaic challenges (Despite challenges... continues to thrive)
- Generic conclusion (the future looks bright, only time will tell)

---

## 关键数据

| 指标 | 数值 |
|------|------|
| GitHub Stars | 901 |
| Forks | 98 |
| Commits | 55 |
| AI 模式检测 | 36 种 |
| 词汇替换表 | 109 词 |
| 词汇层级 | 3 层 |
| 上下文 Profile | 5 种 |
| 严重性分级 | 3 级 (P0/P1/P2) |
| 许可证 | MIT |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Structure is the #1 detection signal" | 结构是首要检测信号 |
| "AI text is metronomic; human text has varied rhythm" | AI 文本是机械的，人类文本有变化节奏 |
| "Don't sand away all personality" | 不要磨掉所有个性 |
| "If the thing is genuinely surprising, the reader should feel that from the content" | 如果内容真的令人惊讶，读者应该从内容感受到 |
| "State the core point in one sentence, then rebuild" | 用一句话陈述核心观点，然后重建 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **36 模式检测** — 全面的 AI 写作模式库
2. **3 层词汇表** — 减少误报的分级标记
3. **双模式操作** — Rewrite/Detect 灵活使用
4. **上下文 Profile** — 不同场景不同严格度
5. **Second-pass audit** — 二次审计捕获残留模式
6. **严重性分级** — P0/P1/P2 优先级修复

### 可实施
- 建立内容审计技能检测 AI 模式
- 实现 3 层词汇表减少误报
- 添加 Detect 模式供用户选择
- 根据平台适配严格度（微头条/小红书/B 站）
- 实现二次审计确保干净输出
- 优先修复 P0/P1 问题

---

## 相关资源

| 资源 | 链接 |
|------|------|
| GitHub 仓库 | https://github.com/conorbronsdon/avoid-ai-writing |
| Web App | https://avoid-ai-writing-app.vercel.app/ |
| DexScreener | https://dexscreener.com/solana/4b5mprekzapcwybrsbbaiewtk4amck62rpcznjcxz69m |
| 研究来源 | Pangram Labs / Wikipedia / blader/humanizer / brandonwise/humanizer |

---

*原始来源：https://github.com/conorbronsdon/avoid-ai-writing*
