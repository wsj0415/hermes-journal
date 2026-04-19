# Peter Pang — 为什么你的"AI-First"策略可能是错的

**来源**: https://x.com/intuitiveml/status/2043545596699750791  
**作者**: Peter Pang (@intuitiveml) — CREAO 联合创始人  
**抓取时间**: 2026-04-15 00:03 UTC  
**类型**: X 推文线程/深度文章  
**标签**: ai-first, harness-engineering, agent-platform, engineering-workflow, self-healing-loop, monorepo, ci-cd, ai-code-review

---

## 📊 一句话总结

CREAO 用 25 人团队（10 工程师）实现每日 3-8 次生产部署，通过重构整个工程流程围绕 AI：单体仓库让 AI 看见一切、6 阶段 CI/CD 管道、3 层 AI 代码审查、自愈合反馈循环，从 6 周发布周期压缩到当天发布当天验证。

---

## 🏷️ 话题标签

#AI-First #HarnessEngineering #Agent 平台 #工程工作流 #自愈合循环 #单体仓库 #CI-CD #AI 代码审查

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：AI-First vs AI-Assisted 对比图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
AI-First vs AI-Assisted Engineering comparison diagram.

Layout: Side-by-side comparison showing two approaches.

Color Palette:
- AI-Assisted: Yellow/Orange (#F97316)
- AI-First: Green/Blue (#10B981)
- Background: Dark gradient

Left — AI-Assisted (Traditional) 🟠:
图标：AI 附加到现有流程
"Add Copilot to IDE"
"PM drafts specs with ChatGPT"
"QA experiments with AI test generation"
"Same sprint cycles, Jira boards, standups"
"Efficiency +10-20%"
"Nothing structurally changes"
"Workflow stays the same"

Right — AI-First (CREAO Model) 🟢:
图标：流程围绕 AI 重构
"Redesign process around AI as primary builder"
"AI does the building, engineers provide direction"
"Monorepo so AI can see everything"
"6-phase CI/CD pipeline"
"3 parallel AI review passes"
"Self-healing feedback loop"
"3-8 deployments per day"

Center Metrics:
"Old: 6 weeks per release"
"New: Same day ship + A/B test + kill"
"25 employees, 10 engineers"
"Competitors had 100x more people"

Bottom Insight:
"AI-Assisted: Add AI to loop"
"AI-First: Redesign the loop"
"Vibe coding → Production system"

Style: Clean technical comparison, dark mode with approach colors
Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 AI-First vs AI-Assisted 对比的内容，并排对比图直接展示两种方法的根本差异，比单一架构图更能传达"重构流程"的价值。

---

### 选项 2：自愈合反馈循环流程图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11257 (Infographic Style)  
**示例图**: https://cms-assets.youmind.com/media/1772433527626_7jezbj_HCW2O1lX0AEnqu0.jpg

```prompt
Self-Healing Feedback Loop flowchart for CREAO engineering workflow.

Layout: Circular flow showing daily cycle.

Color Palette:
- Morning: Blue (#3B82F6)
- Triage: Orange (#F97316)
- Fix: Green (#10B981)
- Deploy: Purple (#8B5CF6)
- Background: Dark gradient

9:00 AM — Health Workflow 🔵:
"Claude Sonnet queries CloudWatch"
"Analyzes error patterns across services"
"Executive health summary → Microsoft Teams"
"Nobody had to ask for it"

10:00 AM — Triage Engine 🟠:
"Cluster errors from CloudWatch + Sentry"
"Score across 9 severity dimensions"
"Auto-generate Linear tickets"
"Include: sample logs, affected users, endpoints"
"Deduplicate: update open or reopen closed"

Engineer Fix 🟢:
"Engineer investigates (AI did diagnosis)"
"Validates and pushes fix"
"3 Claude review passes evaluate PR"
"CI validates"

6-Phase Deploy 🟣:
"Dev → Test Dev → Prod → Test Prod → Release"
"Triage re-checks CloudWatch"
"If resolved → Linear ticket auto-closes"

Center Badge:
"Daily cycle creates self-healing loop"
"Errors detected → triaged → fixed → verified"
"Minimal manual intervention"

Bottom Stack:
"AWS + CloudWatch + GitHub Actions + Claude + Statsig + Graphite + Sentry + Linear"

Style: Modern circular flowchart, dark mode with phase colors
Aspect ratio: 9:16 portrait
```

---

### 选项 3：工程栈组件网格

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 8 modules showing "CREAO Engineering Stack".

Color Palette:
- Primary: Blue (#3B82F6)
- Accent: Various tool colors
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (8 Cards):

M1 — Hero:
"CREAO 工程栈"
"25 人=100x 竞争对手产出"
Icon: Stack + AI

M2 — Infrastructure:
"AWS + auto-scaling"
"Circuit-breaker rollback"
"CloudWatch: 25+ alarms"
"Structured logging"

M3 — CI/CD:
"GitHub Actions 6-phase:"
"Verify→Build→Test Dev→Deploy→Test Prod→Release"
"No manual overrides"
"Deterministic pipeline"

M4 — AI Code Review:
"Claude Opus 4.6"
"Pass 1: Code quality"
"Pass 2: Security"
"Pass 3: Dependency scan"
"Review gates, not suggestions"

M5 — Feature Flags:
"Statsig"
"Every feature behind gate"
"Team → % rollout → full/kill"
"Kill switch: no deploy needed"

M6 — PR Management:
"Graphite"
"Merge queues rebase→CI→merge"
"Stacked PRs for high throughput"

M7 — Error Tracking:
"Sentry + CloudWatch"
"Merged by triage engine"
"Cross-tool context"

M8 — Ticketing:
"Linear"
"Auto-created with severity"
"Sample logs + investigation paths"
"Auto-closes on resolution"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心洞察

### AI-Assisted vs AI-First

> **大多数公司将 AI  bolt 到现有流程上。工程师打开 Cursor。PM 用 ChatGPT 起草规范。QA 实验 AI 测试生成。工作流保持不变。效率提升 10-20%。没有结构性变化。**

**那是 AI-Assisted。**

> **AI-First 意味着你围绕 AI 是主要构建者的假设重新设计你的流程、架构和组织。你停止问"AI 如何帮助我们的工程师？"开始问"我们如何重构一切让 AI 做构建，工程师提供方向和判断？"**

**区别是乘数效应。**

---

### CREAO 成果

| 指标 | 数值 |
|------|------|
| **团队规模** | 25 员工，10 工程师 |
| **竞争对手** | 100x 更多人 |
| **部署频率** | 每日 3-8 次生产部署 |
| **旧模型** | 两周无一次发布 |
| **发布周期** | 6 周 → 当天 |
| **用户参与** | 上升 |
| **支付转化** | 上升 |

---

## 三大瓶颈及解决方案

### 瓶颈 1: 产品管理

**问题**:
- PMs 花数周研究/设计/规范功能
- Agent 两小时可实现功能
- 构建时间从数月压缩到两小时，数周规划周期成约束

**解决方案**:
> **PMs 需演变为产品思维架构师，以迭代速度工作，或退出构建循环。设计通过快速原型 - 发布 - 测试 - 迭代循环发生，非委员会审查的规范文档。**

---

### 瓶颈 2: QA

**问题**:
- Agent 发布功能后，QA 团队花数天测试边界情况
- **构建时间：2 小时。测试时间：3 天。**

**解决方案**:
> **用 AI 构建的测试平台替换手动 QA，测试 AI 编写的代码。验证必须与实现同速移动。否则你在旧瓶颈下游十英尺处建了新瓶颈。**

---

### 瓶颈 3: 人数

**问题**:
- 竞争对手有 100x 更多人做可比工作
- CREAO 只有 25 人

**解决方案**:
> **无法通过雇佣达到平等。必须通过重新设计达到。**

**三个系统需 AI 贯穿**:
1. 如何设计产品
2. 如何实现产品
3. 如何测试产品

> **如果任何一个保持手动，它约束整个管道。**

---

## 代码库重构

### 问题

> **旧架构分散在多个独立系统中。单次更改可能需触碰三四个仓库。从人类工程师角度可管理。从 AI agent 角度不透明。Agent 看不见全貌。无法推理跨服务影响。无法本地运行集成测试。**

---

### 解决方案：单体仓库

> **必须统一所有代码到单一单体仓库。一个原因：让 AI 能看见一切。**

**Harness 工程原则实践**:
> **你将系统拉入 agent 可检查/验证/修改的形式越多，你获得杠杆越大。碎片化代码库对 agent 不可见。统一的可见。**

**时间**:
- 1 周设计新系统（规划/实现/测试/集成测试阶段）
- 1 周用 agent 重构整个代码库

> **CREAO 是 agent 平台。我们用自己的 agent 重建运行 agent 的平台。如果产品能自建它，就有效。**

---

## 完整工程栈

### Infrastructure: AWS

| 组件 | 功能 |
|------|------|
| **Auto-scaling** | 容器服务自动扩展 |
| **Circuit-breaker** | 部署后指标降级自动回滚 |
| **CloudWatch** | 中枢神经系统，结构化日志跨所有服务，25+ 警报，自定义指标 |

> **如果 AI 无法读取日志，它无法诊断问题。**

---

### CI/CD: GitHub Actions

**6 阶段管道**:
```
Verify CI → Build and Deploy Dev → Test Dev → Deploy Prod → Test Prod → Release
```

**CI 门每 PR 执行**:
- 类型检查
- Linting
- 单元测试 + 集成测试
- Docker 构建
- Playwright 端到端测试
- 环境奇偶检查

> **无阶段可选。无手动覆盖。管道是确定性的，所以 agent 可预测结果并推理失败。**

---

### AI 代码审查：Claude

**每 PR 触发 3 个并行审查**（Claude Opus 4.6）:

| Pass | 检查内容 |
|------|----------|
| **Pass 1** | 代码质量：逻辑错误/性能问题/可维护性 |
| **Pass 2** | 安全：漏洞扫描/认证边界检查/注入风险 |
| **Pass 3** | 依赖：供应链风险/版本冲突/许可证问题 |

> **这些是审查门，非建议。它们与人工审查并行运行，捕获人在海量下错过的。当你每天部署 8 次，无人工审查者能持续注意每 PR。**

**工程师也可在 GitHub issue/PR 中@Claude** 获取实现计划/调试会话/代码分析。Agent 看见整个单体仓库。上下文跨对话携带。

---

## 自愈合反馈循环

> **这是核心。**

### 每日循环

**9:00 AM UTC — 健康工作流**:
```
Claude Sonnet 4.6 查询 CloudWatch
→ 分析所有服务的错误模式
→ 生成执行健康摘要
→ 通过 Microsoft Teams 交付团队
→ 没人需要请求它
```

**10:00 AM UTC — 分类引擎**:
```
集群 CloudWatch + Sentry 的生产错误
→ 跨 9 个严重维度评分每个集群
→ 自动生成 Linear 调查票据
→ 每票据包含：样本日志/受影响用户/端点/建议调查路径
→ 去重：如果开放 issue 覆盖相同错误模式则更新
→ 如果之前关闭 issue 复发则检测回归并重新打开
```

**工程师修复**:
```
工程师调查（AI 已完成诊断）
→ 验证并推送修复
→ 3 个 Claude 审查评估 PR
→ CI 验证
→ 6 阶段部署管道通过 dev 和 prod，每阶段测试
→ 部署后分类引擎重新检查 CloudWatch
→ 如果原始错误解决，Linear 票据自动关闭
```

---

### 工具栈

| 工具 | 用途 |
|------|------|
| **Statsig** | 功能标志，每功能在门后发布 |
| **Graphite** | PR 分支管理，合并队列 rebase→CI→merge |
| **Sentry** | 结构化异常报告，与 CloudWatch 合并 |
| **Linear** | 人界面层，自动创建票据带严重性评分 |

---

## 发布路径

### 新功能路径

```
1. 架构师定义任务为结构化提示（代码库上下文/目标/约束）
2. Agent 分解任务，规划实现，编写代码，生成自己的测试
3. PR 打开。3 个 Claude 审查评估。人工审查者检查战略风险，非逐行正确性
4. CI 验证：类型检查/lint/单元测试/集成测试/端到端测试
5. Graphite 合并队列 rebase→重新运行 CI→如果 green 则合并
6. 6 阶段部署管道通过 dev 和 prod，每阶段测试
7. 功能标志为团队开启。逐步百分比发布。监控指标
8. Kill switch 可用如果任何降级。严重问题自动回滚
```

---

### Bug 修复路径

```
1. CloudWatch 和 Sentry 检测错误
2. Claude 分类引擎评分严重性，创建带完整调查上下文的 Linear issue
3. 工程师调查。AI 已完成诊断。工程师验证并推送修复
4. 相同审查/CI/部署/监控管道
5. 分类引擎重新验证。如果解决，票据自动关闭
```

> **两条路径用相同管道。一个系统。一个标准。**

---

## 两种工程师类型

### The Architect（架构师）

**1-2 人**。他们：
- 设计教 AI 如何工作的标准操作程序
- 构建测试基础设施/集成系统/分类系统
- 决定架构和系统边界
- 定义 agent 的"好"看起来像什么

**需要深度批判性思维**:
> **你批评 AI。你不跟随它。当 agent 提出计划，架构师找漏洞。它错过了什么失败模式？它跨了什么安全边界？它在积累什么技术债务？**

> **我有物理学博士学位。我博士最有用的事是教我如何质疑假设/压力测试论证/找缺失的东西。批评 AI 的能力将比生产代码的能力更有价值。**

**这也是最难填充的角色。**

---

### The Operator（操作员）

**其他人**。工作重要。结构不同。

```
AI 分配任务给人。
分类系统找 bug→创建票据→浮现诊断→分配给正确的人。
人调查/验证/批准修复。
AI 创建 PR。
人审查是否有风险。
```

**任务**: Bug 调查/UI 精炼/CSS 改进/PR 审查/验证  
**需要**: 技能和注意力  
**不需要**: 旧模型要求的架构推理

---

### 谁适应最快

> **初级工程师比高级工程师适应更快。**

| 群体 | 适应速度 | 原因 |
|------|----------|------|
| **初级工程师** | 快 | 更少传统实践感觉被赋能，可放大影响的工具，无十年习惯需改 |
| **高级工程师** | 慢 | 强传统实践，两月工作可被 AI 一小时完成，难接受多年建立的稀有技能集 |

> **在这转型中，适应性比积累技能更重要。**

---

## 管理崩溃

### CTO 时间分配变化

| 活动 | 之前 | 现在 |
|------|------|------|
| **管理人** | 60% | <10% |
| **构建** | 少 | 9 AM - 3 AM 多数天 |

> **传统 CTO 模型说赋能团队做架构工作/培训他们/委托。但如果系统只需 1-2 个架构师，我需要先自己做。我从管理转向构建。我设计 SOP 和系统架构。我维护 harness。**

> **更有压力。但我享受构建，非对齐。**

---

### 关系改善

> **之前与团队多数互动是对齐会议。讨论权衡。辩论优先级。对技术决策分歧。那些对话在传统模型中必要。也耗尽。**

> **现在我仍与团队交谈。我们谈其他事。非工作话题。休闲对话。离线旅行。我们相处更好因为我们停止争论我们系统可轻松完成的工作。**

---

## 不确定性是真实的

> **我不会假装每个人都开心。**

**问题**:
- 当 CTO 停止每天与人交谈，一些团队成员感觉不确定
- "CTO 不跟我说话意味着什么？"
- "我在这新世界价值是什么？"
- 合理担忧

**原则**:
> **我们不因工程师引入生产 bug 而解雇。我们改进审查流程。我们加强测试。我们添加护栏。同样适用于 AI。如果 AI 犯错，我们建更好验证/更清晰约束/更强可观察性。**

---

## 全公司 AI-Native

> **如果工程以小时发布功能但营销需一周宣布它们，营销是瓶颈。如果产品团队仍运行月度规划周期，规划是瓶颈。**

**CREAO 推 AI-Native 操作到每个功能**:

| 功能 | AI-Native 实现 |
|------|---------------|
| **产品发布说明** | 从 changelog 和功能描述 AI 生成 |
| **功能介绍视频** | AI 生成动态图形 |
| **社交媒体每日帖子** | AI 编排和自动发布 |
| **健康报告和摘要** | 从 CloudWatch 和生产数据库 AI 生成 |

> **工程/产品/营销/增长在一个 AI-Native 工作流运行。如果一个功能以 agent 速度运行另一个以人速度运行，人速度功能约束一切。**

---

## 对工程师的建议

> **你的价值正从代码输出转向决策质量。快速编写代码的能力每月贬值。评估/批评/指导 AI 的能力增值更多。**

**产品感或品味重要**:
- 你能看生成的 UI 在用户告诉你前知道它错吗？
- 你能看架构提案看见 agent 错过的失败模式吗？

> **告诉 19 岁实习生：训练批判性思维。学会评估论证/找差距/质疑假设。学好设计看起来像。那些技能复合。**

---

## 对 CTO 和创始人的建议

| 建议 | 说明 |
|------|------|
| **如果 PM 流程长于构建时间，从那里开始** | 先解决最长瓶颈 |
| **在扩展 agent 前建测试 harness** | 快 AI 无快验证=快移动技术债务 |
| **从一个架构师开始** | 一人建系统并证明有效 |
| **系统运行后将他人纳入操作员角色** | 渐进扩展 |
| **推 AI-Native 到每个功能** | 全公司 AI-Native |
| **预期阻力** | 一些人会推回 |

---

## 对行业的影响

> **OpenAI/Anthropic/多个独立团队收敛于相同原则：结构化上下文/专业 agent/持久记忆/执行循环。Harness 工程正成标准。**

**模型能力是驱动这个的时钟**:
> **我将 CREAO 整个转变归因于过去两月。Opus 4.5 做不到 Opus 4.6 做的。下代模型将进一步加速。**

> **我相信一人公司将变普遍。如果一个架构师带 agent 可做 100 人的工作，许多公司不需要第二个员工。**

> **我 talk 的大多数创始人和工程师仍以传统方式运营。一些人考虑转变。很少人已完成。**

> **记者朋友说她谈了约五人这个话题。她说我们比任何人都远："我认为没人像你那样完全重建整个工作流。"**

> **工具存在让任何团队做这个。我们栈中无专有东西。**

> **竞争优势是决定围绕这些工具重构一切，和吸收成本的意愿。成本是真实的：员工不确定性/CTO 工作 18 小时天/高级工程师质疑价值/旧系统消失新系统未证明的两周。**

> **我们吸收了那成本。两月后，数字说话。**

> **我们建 agent 平台。我们用 agent 建它。**

---

## 关键数据

| 指标 | 数值 |
|------|------|
| 团队规模 | 25 员工，10 工程师 |
| 竞争对手人数 | 100x 更多 |
| 每日部署 | 3-8 次 |
| 旧发布周期 | 6 周 |
| 新发布周期 | 当天 |
| CTO 管理时间 | 60% → <10% |
| AI 审查 passes | 3 并行 |
| CI/CD 阶段 | 6 |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "AI-Assisted: Add AI to loop" | 传统方法 |
| "AI-First: Redesign the loop" | 重构方法 |
| "Monorepo so AI can see everything" | 代码库统一 |
| "Fast AI without fast validation = fast-moving technical debt" | 测试 harness 重要性 |
| "Criticise AI. Don't follow it." | 架构师角色 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **AI-First 思维** — 重构流程非附加 AI
2. **单体仓库** — 让 AI 看见一切
3. **多阶段 CI/CD** — 确定性管道
4. **并行 AI 审查** — 捕获人错过的
5. **自愈合循环** — 检测→分类→修复→验证
6. **功能标志** — 快速发布/快速回滚
7. **架构师 vs 操作员** — 角色分离
8. **全公司 AI-Native** — 避免瓶颈

### 可实施
- 统一内容仓库让 AI 访问全部
- 建立多阶段内容审查管道
- 实施并行 AI 内容审查
- 创建自愈合内容监控循环
- 用功能标志测试内容变体
- 分离内容架构师和操作员角色
- 推 AI-Native 到所有功能

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Peter Pang 原文 | https://x.com/intuitiveml/status/2043545596699750791 |
| CREAO | Agent 平台 |
| OpenAI Harness Engineering | 2026 年 2 月概念 |

---

*原始来源：https://x.com/intuitiveml/status/2043545596699750791*
