# Philipp Schmid — 8 个 Agent Skills 写作技巧

**来源**: https://x.com/_philschmid/status/2043705157850951699  
**作者**: Philipp Schmid (@_philschmid)  
**抓取时间**: 2026-04-14 05:02 UTC  
**类型**: X 推文线程/技能写作指南  
**标签**: agent-skills, skill-writing, claude-skills, agent-development, prompt-engineering, skill-evaluation, capability-skills, preference-skills

---

## 📊 一句话总结

Philipp Schmid 分享 8 个 Agent Skills 写作实战技巧：技能结构（SKILL.md+ 辅助文件）/两类技能（能力型 vs 偏好型）/描述要具体（包含 what+when）/用指令非琐事/示例优先/解释 why/分层加载/描述目标非步骤/触发测试/评估流程，基于大量实战经验。

---

## 🏷️ 话题标签

#AgentSkills #Skill 写作 #ClaudeSkills #Agent 开发 #提示工程 #技能评估 #能力技能 #偏好技能

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1:8 技巧网格图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
8 Agent Skills Writing Tips infographic grid.

Layout: 2x4 grid showing 8 tips with icons.

Color Palette:
- Tips 1-4: Blue gradient
- Tips 5-8: Purple gradient
- Background: Dark gradient

Tip 1 — Skill Structure 🔵:
图标：文件夹结构
"my-skill/"
"├── SKILL.md (required)"
"├── scripts/ (reusable code)"
"├── references/ (docs on demand)"
"└── assets/ (templates/images)"

Tip 2 — 3 Layers 🔵:
图标：分层图
"1. Frontmatter (always loaded)"
"   name + description"
"2. Body (when triggers)"
"   <500 lines markdown"
"3. Assets (on demand)"
"   references/scripts/assets"

Tip 3 — 2 Categories 🔵:
图标：分类图标
"Capability Skills:"
"Do what model can't consistently"
"(e.g., PDF form filling)"
"Preference Skills:"
"Encode your specific workflow"
"(e.g., team code review steps)"

Tip 4 — Description 🔵:
图标：触发器
"Trigger mechanism"
"Be specific: what AND when"
"❌ Too vague: 'Helps with documents'"
"✅ Specific: 'Create, edit, analyze .docx'"
"50% improvement from better description"

Tip 5 — Instructions 🟣:
图标：指令列表
"Use directives:"
"'Always use interactions.create()'"
"Lead with examples:"
"5-line code > 5-paragraph explanation"
"Explain the why:"
"'Model Y deprecated' helps generalize"

Tip 6 — Layered Loading 🟣:
图标：分层加载
"Don't dump everything"
"1. Frontmatter (always)"
"2. Body (when triggers)"
"3. References (on demand)"
"Split by topic (AWS vs GCP)"
"TOC with line hints if >500 lines"

Tip 7 — Goals not Steps 🟣:
图标：目标 vs 步骤
"❌ Step-by-step workflow:"
"  'Step 1: Read. Step 2: Parse...'"
"✅ Describe what to achieve:"
"  'Update database port to user value'"
"Provide constraints, not procedures"
"If exact steps matter → write script"

Tip 8 — Evaluation 🟣:
图标：测试评估
"1. Manual runs (different prompts)"
"2. Define measurable success"
"3. 10-20 test prompts"
"4. 3-5 trials per prompt"
"5. Clean environment per run"
"6. Fix description first"
"7. Run evals without skill"

Bottom Badge:
"Based on extensive real-world use"
"Skills in active use"

Style: Modern tips grid, dark mode with blue/purple gradient
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 8 个技巧的内容，网格图直接展示所有技巧及其要点，比单一架构图更能传达"完整指南"的价值。

---

### 选项 2：技能结构图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Agent Skill Structure diagram showing folder layout and layers.

Layout: Left folder structure, Right 3-layer loading.

Color Palette:
- Folder: Green (#10B981)
- Layers: Blue (#3B82F6)
- Background: Dark gradient

Left — Folder Structure 🟢:
图标：文件夹树
"my-skill/"
"│"
"├── SKILL.md ← Required"
"│   └── Frontmatter (name+description)"
"│   └── Body (markdown instructions)"
"│"
"├── scripts/ ← Reusable code"
"│   └── Agent can run these"
"│"
"├── references/ ← Docs on demand"
"│   └── Agent reads when needed"
"│"
"└── assets/ ← Templates/images"
    └── Used in output

Right — 3 Loading Layers 🔵:
图标：分层加载
"Layer 1: Always Loaded"
"└── Frontmatter (name + description)"
"    Trigger mechanism"
"    What + When to use"
"│"
"Layer 2: When Skill Triggers"
"└── SKILL.md Body"
"    Markdown instructions"
"    Keep <500 lines"
"│"
"Layer 3: On Demand"
"└── references/ scripts/ assets/"
    Split by topic
    TOC with line hints if long

Bottom Categories:
"Capability Skills: Do what model can't"
"Preference Skills: Your specific workflow"

Style: Clean technical structure, dark mode with folder/layer colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：评估流程图

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 7 modules showing "Skill Evaluation Workflow".

Color Palette:
- Primary: Purple (#8B5CF6)
- Accent: Various eval colors
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (7 Cards):

M1 — Hero:
"Skill 评估流程"
"基于大量实战经验"
Icon: Test tube + Checkmark

M2 — Step 1-2:
"1. Manual runs"
"   Different prompts, watch breaks"
"2. Define success"
"   Measurable: compile? right API?"

M3 — Step 3-4:
"3. 10-20 test prompts"
"   Should handle / Should ignore / Edge cases"
"4. 3-5 trials per prompt"
"   Nondeterministic, look at distribution"

M4 — Step 5-6:
"5. Clean environment"
"   No context bleeding between runs"
"6. Fix description first"
"   Most problems in trigger, not instructions"

M5 — Step 7:
"7. Run evals WITHOUT skill"
"If they pass → model absorbed skill value"
"Retire the skill (especially capability)"

M6 — Key Insight:
"Describe WHAT to achieve"
"Not HOW to get there"
"❌ Step 1: Read. Step 2: Parse..."
"✅ Update database port to user value"

M7 — Description Tips:
"Trigger mechanism"
"Include what AND when"
"50% improvement from better description"
"Be specific, not vague"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## Skill 基础结构

### 文件夹结构

```bash
my-skill/
├── SKILL.md          ← 唯一必需文件
├── scripts/          ← Agent 可运行的可重用代码
├── references/       ← Agent 需要时阅读的文档
└── assets/           ← 输出中使用的模板/图像/文件
```

---

### 3 层结构

| 层 | 内容 | 加载时机 |
|------|------|----------|
| **1. Frontmatter** | name + description | 总是加载（进入每个提示） |
| **2. Body** | SKILL.md 的 Markdown 指令 | 技能触发后加载 |
| **3. Assets** | scripts/ references/ assets/ | 按需加载 |

---

### 两类 Skills

| 类型 | 说明 | 示例 | 持久性 |
|------|------|------|--------|
| **Capability Skills** | 帮助 agent 做基础模型无法一致完成的事 | PDF 表单填写 | 可能随模型改进而不必要 |
| **Preference Skills** | 编码你的特定工作流 | 团队代码审查步骤 | 持久但需与实际流程同步 |

---

## 技巧 1: 描述要具体

> **SKILL.md 中的描述是触发机制。如果模糊，agent 不知道何时激活技能。如果太宽泛，技能在每个请求触发。**

**关键**: **在具体说明技能做什么 AND 何时使用它。描述中包含"what"和"when"。技能主体仅在技能触发后加载。**

---

### 对比示例

| ❌ 太模糊 | ✅ 具体可操作 |
|----------|--------------|
| "Helps with documents" | "Create, edit, and analyze .docx files, use for tracked changes, comments, formatting, or text extraction" |
| "API helper" | "Use when writing code that calls the Gemini API for text generation, multi-turn chat, image generation, or streaming" |

> **我见过仅改进描述就有 50% 的提升。**

---

## 技巧 2: 用指令非琐事

> **Agent 很聪明。你的工作是告诉它它还不知道什么。研究表明更长、更全面、太多上下文实际上损害性能。**

### 最佳实践

| 实践 | 说明 |
|------|------|
| **用指令** | `"Always use interactions.create()"` 而非 `"The Interactions API is the recommended approach."` |
| **示例优先** | 5 行代码片段胜过 5 段解释 |
| **解释 why** | `"Use model X, model Y is deprecated and will return errors"` 帮助 agent 推广而非死记 |
| **不要过拟合** | 避免仅通过三个测试提示的"fiddly"更改。写在数百万次调用中有效的技能 |

---

## 技巧 3: 分层加载

> **不要把一切都倒入一个文件。Agent 分层加载信息。**

### 加载顺序

```
1. Always loaded: Frontmatter of SKILL.md (name + description)
2. Loaded when skill triggers: the SKILL.md body (keep under 500 lines)
3. Loaded on demand: reference files, scripts, assets
```

**提示**: 如果技能覆盖多主题（如 AWS vs GCP 部署），拆分为单独的 reference 文件。Agent 只读它需要的那个。这为实际任务节省上下文。

**技巧**: 如果 reference 文件超过 500 行，在顶部添加带"line hints"的目录，方便 agent 快速找到需要的内容。

---

## 技巧 4: 描述目标非步骤

> **创建技能的常见错误是将技能变成逐步工作流。**

### 对比示例

| ❌ 逐步工作流 | ✅ 描述目标 |
|--------------|------------|
| "Step 1: Read the config file. Step 2: Find the database URL. Step 3: Update the port number. Step 4: Write the file back." | "Update the database port in the config file to the value specified by the user." |
| "Step 1: Create a branch. Step 2: Make the change. Step 3: Run tests. Step 4: Open a PR." | "Always run tests before opening a PR. Never push directly to main." |

**关键洞察**:
- 当你规定每步时，你剥夺了它们适应/从错误恢复/找更好方法的能力
- **提供约束，非程序**
- **如果 exact 步骤重要，写脚本**。如果任务脆弱且 step 3 在 step 2 前做会破坏一切，那不是 skill 问题，是 scripting 问题

---

## 技巧 5: 触发测试

> **考虑技能何时不应触发。像"Use for any coding task"的描述会劫持每个请求。**

### 示例

```
"Use when working with PDF files. 
Do NOT use for general document editing, spreadsheets, or plain text files."
```

**测试"should trigger"和"shouldn't trigger"案例都必不可少**。否则你会单向优化技能。

---

## 技巧 6: 评估流程

> **不要没有评估就发布技能。每次运行可能表现不同，所以单次检查不够。**

### 6 步评估流程

**Step 1: 手动运行**
```
用不同提示手动运行几次。观察在哪里破裂。
- 是否假设依赖存在？
- 是否跳过步骤？
```

**Step 2: 定义可衡量成功**
```
Does the output compile?
Does it use the right API?
Did it follow the steps?
Grade outcomes, not paths.
```

**Step 3: 10-20 个测试提示**
```
混合：
- 技能应处理的提示
- 技能应忽略的提示
- 棘手边缘案例
每个提示应有自己的成功标准
```

**Step 4: 多次试验**
```
Agent 输出是非确定性的。
每提示运行 3-5 次试验。
看分布而非单次 pass/fail。
```

**Step 5: 隔离每次运行**
```
每次测试用干净环境。
运行间上下文 bleeding 掩盖真实失败。
```

**Step 6: 先修复描述**
```
大多数问题在触发器，非指令中。
```

---

### Step 7: 无技能评估

> **运行没有技能的评估。如果它们通过，模型已吸收技能价值，技能不再必要。退役它。**

**这尤其适用于 capability skills**，随模型改进，差距缩小。

---

## 关键数据

| 指标 | 数值 |
|------|------|
| 描述改进提升 | 50% |
| SKILL.md 主体行数上限 | 500 行 |
| 测试提示数量 | 10-20 个 |
| 每提示试验次数 | 3-5 次 |
| 技能类别 | 2 (Capability/Preference) |
| 加载层 | 3 |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "描述是触发机制" | 技能激活关键 |
| "50% improvement from better description" | 描述价值 |
| "Lead with examples: 5-line code > 5-paragraph" | 示例优先 |
| "Describe WHAT to achieve, not HOW" | 目标非步骤 |
| "Most problems are in the trigger, not instructions" | 问题定位 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **技能结构** — SKILL.md+scripts/references/assets
2. **两类技能** — Capability vs Preference 清晰分类
3. **描述具体** — 包含 what+when 触发条件
4. **指令非琐事** — Always use X 而非 X is recommended
5. **分层加载** — Frontmatter/Body/Assets 按需加载
6. **目标非步骤** — 描述目标提供约束
7. **触发测试** — should trigger + shouldn't trigger
8. **评估流程** — 6 步 + 无技能评估

### 可实施
- 为内容创作技能定义清晰结构
- 分类技能为能力型或偏好型
- 改进技能描述包含触发条件
- 用指令格式写技能指令
- 实现分层加载节省上下文
- 描述内容创作目标非步骤
- 测试技能触发和不触发案例
- 建立技能评估流程

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Philipp Schmid 原文 | https://x.com/_philschmid/status/2043705157850951699 |
| 原文发布 | https://www.anthropic.com/news/writing-agent-skills |

---

*原始来源：https://x.com/_philschmid/status/2043705157850951699*
