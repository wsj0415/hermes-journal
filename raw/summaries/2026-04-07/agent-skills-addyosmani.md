# Agent Skills — 生产级 AI 编码代理工程技能

> **项目作者：** Addy Osmani (@addyosmani)  
> **翻译时间：** 2026-04-07  
> **项目链接：** https://github.com/addyosmani/agent-skills  
> **核心概念：** 19 个生产级工程技能 +7 个斜杠命令 +3 个专家角色  
> **灵感来源：** Google 软件工程实践

---

## 📊 项目概览

| 指标 | 数值 |
|------|------|
| **项目作者** | Addy Osmani (Google) |
| **技能数量** | 19 个核心技能 |
| **斜杠命令** | 7 个开发生命周期命令 |
| **专家角色** | 3 个预配置审查角色 |
| **参考清单** | 4 个补充检查清单 |
| **许可证** | MIT |

---

## 🎯 核心理念

**技能编码工作流、质量门、和最佳实践：**
```
资深工程师构建软件时使用的实践
  ↓
打包为 AI 代理可一致遵循的格式
  ↓
开发每个阶段自动激活
```

**核心问题：**
> AI 编码代理默认走最短路径 → 跳过规范/测试/安全审查/使软件可靠的实践

**解决方案：**
> Agent Skills 给代理结构化工作流，强制执行资深工程师对生产代码的相同纪律。

---

## 🔄 7 个斜杠命令（开发生命周期映射）

```
DEFINE    PLAN      BUILD     VERIFY    REVIEW    SHIP
┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐ ┌──────┐
│ Idea │──▶│ Spec │──▶│ Code │──▶│ Test │──▶│ QA │──▶│ Go │
│Refine│  │ PRD │  │ Impl │  │Debug │  │ Gate │  │Live │
└──────┘ └──────┘ └──────┘ └──────┘ └──────┘ └──────┘
  /spec   /plan    /build    /test    /review   /ship
```

| 你在做什么 | 命令 | 关键原则 |
|------------|------|----------|
| **定义构建什么** | `/spec` | 规范先于代码 |
| **计划如何构建** | `/plan` | 小原子任务 |
| **增量构建** | `/build` | 一次一个切片 |
| **证明有效** | `/test` | 测试是证明 |
| **合并前审查** | `/review` | 改进代码健康 |
| **简化代码** | `/code-simplify` | 清晰胜于聪明 |
| **发布到生产** | `/ship` | 更快更安全 |

**关键：**
> 命令是入口点。底层激活 19 个技能 — 每个都是结构化工作流带步骤/验证门/反合理化表。

---

## 📚 19 个核心技能

### DEFINE 阶段（2 个技能）

#### 1. idea-refine

**功能：** 结构化发散/收敛思维将模糊想法转为具体提案

**何时使用：** 你有需要探索的粗略概念

---

#### 2. spec-driven-development

**功能：** 在代码前写 PRD（目标/命令/结构/代码风格/测试/边界）

**何时使用：** 开始新项目/功能/重大变更

**关键原则：**
> 规范先于代码

---

### PLAN 阶段（1 个技能）

#### 3. planning-and-task-breakdown

**功能：** 将规范分解为小可验证任务带验收标准和依赖排序

**何时使用：** 你有规范需要可实现单元

---

### BUILD 阶段（6 个技能）

#### 4. incremental-implementation

**功能：** 薄垂直切片 — 实现/测试/验证/提交。功能标志/安全默认/可回滚变更

**何时使用：** 任何触及多于一文件的变更

---

#### 5. test-driven-development

**功能：** 红 - 绿 - 重构，测试金字塔（80/15/5），测试规模，DAMP 胜于 DRY，Beyonce 规则，浏览器测试

**何时使用：** 实现逻辑/修复 bug/改变行为

**关键原则：**
> 测试是证明

---

#### 6. context-engineering

**功能：** 在正确时间给代理正确信息 — 规则文件/上下文打包/MCP 集成

**何时使用：** 开始会话/切换任务/输出质量下降时

---

#### 7. frontend-ui-engineering

**功能：** 组件架构/设计系统/状态管理/响应式设计/WCAG 2.1 AA 无障碍

**何时使用：** 构建或修改用户 facing 界面

---

#### 8. api-and-interface-design

**功能：** 合同优先设计，Hyrum 定律，One-Version 规则，错误语义，边界验证

**何时使用：** 设计 API/模块边界/公共接口

**关键原则：**
> Hyrum 定律：所有公共行为都被依赖

---

### VERIFY 阶段（2 个技能）

#### 9. browser-testing-with-devtools

**功能：** Chrome DevTools MCP 供实时运行时数据 — DOM 检查/控制台日志/网络追踪/性能分析

**何时使用：** 构建或调试任何在浏览器中运行的东西

---

#### 10. debugging-and-error-recovery

**功能：** 五步分诊：重现/定位/简化/修复/防护。停止线规则，安全回退

**何时使用：** 测试失败/构建断裂/行为意外

**五步流程：**
```
1. 重现
2. 定位
3. 简化
4. 修复
5. 防护
```

---

### REVIEW 阶段（4 个技能）

#### 11. code-review-and-quality

**功能：** 五轴审查，变更规模（~100 行），严重性标签（Nit/Optional/FYI），审查速度规范，拆分策略

**何时使用：** 合并任何变更前

**关键原则：**
> 变更规模 ~100 行
> 五轴审查

---

#### 12. code-simplification

**功能：** Chesterton 围栏，500 规则，减少复杂度同时保留精确行为

**何时使用：** 代码工作但比应该的更难读或维护

**关键原则：**
> 清晰胜于聪明
> Chesterton 围栏：理解为什么存在再移除

---

#### 13. security-and-hardening

**功能：** OWASP Top 10 预防，认证模式，秘密管理，依赖审计，三层边界系统

**何时使用：** 处理用户输入/认证/数据存储/外部集成

---

#### 14. performance-optimization

**功能：** 测量优先方法 — Core Web Vitals 目标，分析工作流，捆绑分析，反模式检测

**何时使用：** 存在性能要求或你怀疑回归

**关键原则：**
> 测量优先

---

### SHIP 阶段（4 个技能）

#### 15. git-workflow-and-versioning

**功能：** 主干开发，原子提交，变更规模（~100 行），提交即保存点模式

**何时使用：** 做任何代码变更（总是）

---

#### 16. ci-cd-and-automation

**功能：** 左移，更快更安全，功能标志，质量门管道，失败反馈循环

**何时使用：** 设置或修改构建和部署管道

**关键原则：**
> Shift Left（左移）
> Faster is Safer（更快更安全）

---

#### 17. deprecation-and-migration

**功能：** 代码即负债心态，强制 vs 咨询废弃，迁移模式，僵尸代码移除

**何时使用：** 移除旧系统/迁移用户/淘汰功能

**关键原则：**
> 代码是负债

---

#### 18. documentation-and-adrs

**功能：** 架构决策记录，API 文档，内联文档标准 — 记录为什么

**何时使用：** 做架构决策/改变 API/发布功能

---

#### 19. shipping-and-launch

**功能：** 发布前检查清单，功能标志生命周期，分阶段推出，回滚程序，监控设置

**何时使用：** 准备部署到生产

---

## 🤖 3 个专家角色

**预配置专家角色供目标审查：**

| 角色 | 职责 | 视角 |
|------|------|------|
| **code-reviewer** | 高级员工工程师 | 五轴代码审查带"员工工程师会批准吗？"标准 |
| **test-engineer** | QA 专家 | 测试策略/覆盖分析/Prove-It 模式 |
| **security-auditor** | 安全工程师 | 漏洞检测/威胁建模/OWASP 评估 |

---

## 📋 4 个参考清单

**技能需要时拉取的快速参考材料：**

| 参考 | 覆盖 |
|------|------|
| **testing-patterns.md** | 测试结构/命名/mocking/React/API/E2E 示例/反模式 |
| **security-checklist.md** | 提交前检查/认证/输入验证/headers/CORS/OWASP Top 10 |
| **performance-checklist.md** | Core Web Vitals 目标，前端/后端检查清单，测量命令 |
| **accessibility-checklist.md** | 键盘导航/屏幕阅读器/视觉设计/ARIA/测试工具 |

---

## 🏗️ 技能结构

**每个技能遵循一致解剖：**

```
┌─────────────────────────────────────────┐
│ SKILL.md                                │
│                                         │
│ ┌─ Frontmatter ─────────────────────────┐ │
│ │ name: lowercase-hyphen-name           │ │
│ │ description: Use when [trigger]       │ │
│ └───────────────────────────────────────┘ │
│                                         │
│ Overview → 这技能做什么                  │
│ When to Use → 触发条件                   │
│ Process → 逐步工作流                     │
│ Rationalizations → 借口 + 反驳           │
│ Red Flags → 某事错误的信号               │
│ Verification → 证据要求                  │
└─────────────────────────────────────────┘
```

### 关键设计选择

| 选择 | 说明 |
|------|------|
| **流程，非散文** | 技能是代理遵循的工作流，非参考文档。每有步骤/检查点/退出标准。 |
| **反合理化** | 每技能包含代理跳过步骤常用借口表（如"I'll add tests later"）带记录反驳。 |
| **验证不可协商** | 每技能结束带证据要求 — 测试通过/构建输出/运行时数据。"Seems right"永不足够。 |
| **渐进披露** | SKILL.md 是入口点。支持参考仅需要时加载，保持 token 使用最小。 |

---

## 📁 项目结构

```
agent-skills/
├── skills/                      # 19 个核心技能（每目录 SKILL.md）
│   ├── idea-refine/             # DEFINE
│   ├── spec-driven-development/ # DEFINE
│   ├── planning-and-task-breakdown/ # PLAN
│   ├── incremental-implementation/ # BUILD
│   ├── context-engineering/     # BUILD
│   ├── frontend-ui-engineering/ # BUILD
│   ├── test-driven-development/ # BUILD
│   ├── api-and-interface-design/ # BUILD
│   ├── browser-testing-with-devtools/ # VERIFY
│   ├── debugging-and-error-recovery/ # VERIFY
│   ├── code-review-and-quality/ # REVIEW
│   ├── code-simplification/     # REVIEW
│   ├── security-and-hardening/  # REVIEW
│   ├── performance-optimization/ # REVIEW
│   ├── git-workflow-and-versioning/ # SHIP
│   ├── ci-cd-and-automation/    # SHIP
│   ├── deprecation-and-migration/ # SHIP
│   ├── documentation-and-adrs/  # SHIP
│   ├── shipping-and-launch/     # SHIP
│   └── using-agent-skills/      # Meta：如何使用这包
├── agents/                      # 3 个专家角色
├── references/                  # 4 个补充清单
├── hooks/                       # 会话生命周期钩子
├── .claude/commands/            # 7 个斜杠命令
└── docs/                        # 每工具设置指南
```

---

## 🚀 安装方式

### Claude Code（推荐）

**市场安装：**
```bash
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills
```

**本地/开发：**
```bash
git clone https://github.com/addyosmani/agent-skills.git
claude --plugin-dir /path/to/agent-skills
```

---

### Cursor

**复制任何 SKILL.md 到 `.cursor/rules/`，或引用完整 skills/ 目录。**

**文档：** docs/cursor-setup.md

---

### Gemini CLI

**安装为原生技能供自动发现，或添加到 GEMINI.md 供持久上下文。**

```bash
gemini skills install https://github.com/addyosmani/agent-skills.git
```

**文档：** docs/gemini-cli-setup.md

---

### Windsurf

**添加技能内容到 Windsurf 规则配置。**

**文档：** docs/windsurf-setup.md

---

### GitHub Copilot

**用 agents/ 中代理定义作为 Copilot 角色和 .github/copilot-instructions.md 中技能内容。**

**文档：** docs/copilot-setup.md

---

### Codex / 其他代理

**技能是普通 Markdown — 它们与任何接受系统提示或指令文件的代理工作。**

**文档：** docs/getting-started.md

---

## 💡 核心洞察

### 洞察 1：技能是工作流，非提示

**关键区别：**
```
提示：模糊建议（"写测试"）
  ↓
技能：结构化工作流（红 - 绿 - 重构，80/15/5 金字塔，DAMP 胜于 DRY）
```

**为什么重要：**
> 技能编码硬获得工程判断：何时写规范/测试什么/如何审查/何时发布。

---

### 洞察 2：反合理化表

**常见借口 + 反驳：**

| 借口 | 反驳 |
|------|------|
| "我稍后加测试" | "测试是证明。无测试 = 无证明。" |
| "这很简单无需规范" | "简单现在 = 复杂稍后。规范捕获隐性假设。" |
| "我会手动测试" | "手动测试不可重复。自动化测试是资产。" |
| "这变更很小" | "小变更引入大 bug。规模 ~100 行供可审查性。" |

**为什么有效：**
> 代理像人类一样合理化跳过步骤。反合理化表预编码反驳。

---

### 洞察 3：验证不可协商

**每技能结束带证据要求：**
```
❌ "Seems right"
✅ 测试通过
✅ 构建输出
✅ 运行时数据
✅ 具体引用
```

**为什么重要：**
> "Seems right"是原型质量。证据要求是生产质量。

---

### 洞察 4：Google 工程实践嵌入

**技能烘焙最佳实践来自 Google 软件工程文化：**

| 概念 | 来源 | 技能 |
|------|------|------|
| **Hyrum 定律** | Software Engineering at Google | api-and-interface-design |
| **Beyonce 规则** | Google 工程实践 | test-driven-development |
| **测试金字塔** | Google 工程实践 | test-driven-development |
| **变更规模** | Google 代码审查 | code-review-and-quality |
| **Chesterton 围栏** | 软件工程智慧 | code-simplification |
| **主干开发** | Google Git 工作流 | git-workflow-and-versioning |
| **左移** | DevOps 实践 | ci-cd-and-automation |
| **代码即负债** | 软件工程智慧 | deprecation-and-migration |

**关键：**
> 这些非抽象原则 — 它们直接嵌入代理遵循的逐步工作流。

---

### 洞察 5：渐进披露保持 Token 高效

**设计：**
```
SKILL.md（入口点）
  ↓
仅需要时加载参考
  ↓
最小 token 使用
```

**为什么有效：**
> 技能具体（可操作步骤，非模糊建议），可验证（清晰退出标准带证据要求），实战测试（基于真实工作流），最小（仅需要指导代理的内容）。

---

## ⚠️ 已知限制

| 限制 | 说明 | 缓解方法 |
|------|------|----------|
| **需要代理支持** | 技能需要代理接受 Markdown 指令 | 用兼容代理（Claude Code/Cursor 等） |
| **初始设置时间** | 需要安装和配置 | 一次性投资，市场安装 2 分钟 |
| **学习曲线** | 19 技能需时间掌握 | 从 7 斜杠命令开始，随舒适添加 |
| **Token 开销** | 技能激活用 token | 渐进披露保持最小 |

---

## 📊 对比：通用提示 vs Agent Skills

| 维度 | 通用提示 | Agent Skills |
|------|----------|-------------|
| **结构** | 模糊建议 | 逐步工作流 |
| **验证** | 无或可选 | 不可协商带证据 |
| **反合理化** | 无 | 预编码反驳表 |
| **来源** | 通用最佳实践 | Google 工程实践 |
| **质量** | 原型质量 | 生产质量 |
| **可重复** | 依赖代理心情 | 一致激活 |

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **项目仓库** | https://github.com/addyosmani/agent-skills |
| **Software Engineering at Google** | https://abseil.io/resources/swe-book |
| **Google 工程实践** | https://google.github.io/eng-practices/ |
| **技能解剖** | docs/skill-anatomy.md |
| **贡献指南** | CONTRIBUTING.md |

---

## 📊 翻译信息

| 项目 | 信息 |
|------|------|
| **翻译时间** | 2026-04-07 |
| **项目作者** | Addy Osmani |
| **技能数量** | 19 个核心技能 |
| **翻译状态** | ✅ 完整翻译 +19 技能详解 |

---

*翻译完成时间：2026-04-07 | 版本：v1.0*
