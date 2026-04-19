# 我构建了 AI 代理团队用于软件开发 — 5 个真实项目测试

> **原文作者：** Alexey Grigorev  
> **翻译时间：** 2026-04-07  
> **原文链接：** https://alexeyondata.substack.com/p/i-built-an-ai-agent-team-for-software  
> **核心工具：** Claude Code + 代理团队（PM/SWE/QA/On-Call）  
> **测试项目：** 5 个真实软件项目

---

## 📊 文章信息

| 指标 | 数值 |
|------|------|
| **原文作者** | Alexey Grigorev |
| **核心方法** | AI 代理团队（4 角色） |
| **测试项目** | 5 个真实软件项目 |
| **核心工具** | Claude Code 作为编排器 |
| **关键洞察** | 明确规范 + 分配角色 + 定义流程 |

---

## 🎯 核心理念

**传统单代理模式的局限：**
```
单个 Claude Code 会话
  ↓
适合小工具/简单项目
  ↓
但复杂项目有问题：
- 无法验证代理声称任务完成
- 无法测试实现是否符合计划
- 同一代理写代码又判断正确性
```

**代理团队解决方案：**
```
主会话作为编排器
  ↓
指导小型代理团队
  ↓
每个代理有独立角色
  ↓
明确职责分离
```

**关键优势：**
> 这种任务分配避免了同一代理写代码又决定它是否正确的情况。

---

## 🤖 四个代理角色

### 1️⃣ 产品经理（PM）

**职责：**
- 将原始任务转为可实现内容
- 写规范 + 用户故事 + 验收标准 + 测试场景
- 实现和 QA 后从用户视角审查结果
- 决定任务是否真正完成

**GitHub 定义文件：**
```
.claude/agents/product-manager.md
```

---

### 2️⃣ 软件工程师（SWE）

**职责：**
- 实现代码
- 编写测试

**GitHub 定义文件：**
```
.claude/agents/software-engineer.md
```

---

### 3️⃣ 测试员（QA）

**职责：**
- 运行测试
- 检查每个验收标准
- 报告通过/失败 + 证据

**GitHub 定义文件：**
```
.claude/agents/tester.md
```

---

### 4️⃣ 值班工程师（On-Call）

**职责：**
- 代码推送后监控 CI/CD
- 修复管道故障

**GitHub 定义文件：**
```
.claude/agents/oncall-engineer.md
```

---

## 🔄 完整工作流程

### 任务流转

```
我 → 编排器创建任务 → 添加到 backlog
  ↓
PM 拾取并梳理（grooming）
  ↓
SWE 实现
  ↓
QA 验证
  ↓
如果 QA 拒绝 → 返回 SWE 修复
  ↓
如果 QA 接受 → PM 最终验收审查
  ↓
只有 PM 接受后 → 编排器提交代码并关闭任务
```

### 可视化流程

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│   PM    │ →  │   SWE   │ →  │   QA    │ →  │   PM    │
│  梳理    │    │  实现    │    │  验证    │    │  验收    │
└─────────┘    └─────────┘    └─────────┘    └─────────┘
                                         ↓ 拒绝
                                    返回 SWE 修复
                                         ↓ 接受
                                    编排器提交代码
```

**关键洞察：**
> 最终 PM 审查很重要，确保结果与用户故事对齐。这是超越仅通过测试的关键要求。功能从工程角度可能看似完成，但在真实场景中仍可能失败。

---

## 📁 项目结构

```
repository/
├── .claude/agents/           # 角色定义
│   ├── product-manager.md
│   ├── software-engineer.md
│   ├── tester.md
│   └── oncall-engineer.md
├── _docs/
│   └── PROCESS.md            # 开发工作流描述
├── CLAUDE.md                 # 项目级指令
└── .claude/skills/
    └── execute/
        └── SKILL.md          # 启动管道的技能
```

---

## ⚡ 并行处理

**作者通常一次运行两个任务：**
```
批次 1：任务 A + 任务 B 并行
  ↓
完成后
  ↓
编排器从 backlog 拉取下两个
  ↓
批次 2：任务 C + 任务 D 并行
```

**保持循环无需手动干预：**
```
在任务列表中保持循环指令
  ↓
告诉编排器获取下一批次
  ↓
然后添加相同指令
  ↓
过程持续直到 backlog 空
```

---

## 📋 任务追踪

### 方式 1：GitHub Issues

**优势：**
- ✅ 可见协调
- ✅ 代理报告附加到每个任务
- ✅ 透明进度

**示例：**
> https://github.com/AI-Shipping-Labs/website/issues/147（添加评论功能）

---

### 方式 2：基于文件的追踪器

**结构：**
```
tracker/
├── task-name.todo.md        # 待处理
├── task-name.groomed.md     # 已梳理
├── task-name.in-progress.md # 进行中
└── done/
    └── task-name.md         # 已完成
```

**优势：**
- ✅ 更轻量
- ✅ 状态编码在文件名中
- ✅ 简单文件移动

**关键：**
> 工具本身不如周围工作流重要。两种方式都保持相同的 PM→SWE→QA→PM 循环。

---

## 🧪 5 个测试项目

### 项目 1：AI Shipping Labs 社区平台

**GitHub：** https://github.com/AI-Shipping-Labs/website

**背景：**
- 作者和 Valeriia 决定创建新社区
- 收集平台需求
- 录制很多语音消息 + 多次 ChatGPT 会话
- 结论：无现有平台匹配需求 → 构建自己的

**流程：**
```
需求分散在多个源
  ↓
拉到一起 → Claude Code 转规范和任务
  ↓
使用 GitHub Issues 追踪
  ↓
让代理整夜运行
  ↓
早晨：46 个任务中 41 个已完成
```

**成果：**
> 第一次看到这个工作流可处理非平凡项目。

---

### 项目 2：DataTasks（DataTalks.Club 任务追踪器）

**GitHub：** https://github.com/alexeygrigorev/datatasks

**背景：**
- 当前工作分散在 Trello/不同电子表格/Telegram TODO bot
- 有效但创建很多认知负荷
- 计划替换为定制解决方案但无时间

**技术约束：**
- 无服务器
- 运行在 AWS Lambda + DynamoDB

**时间投入：**
```
20 分钟口述需求
  ↓
20 分钟启动 Claude Code 会话
  ↓
20 分钟第二天给反馈
  ↓
DataTasks 诞生
```

**状态：** 暂停（作者无时间适当评估），但作为实验证明方法论可应用于单一项目外。

---

### 项目 3：Merm（纯 Python Mermaid 渲染器）

**GitHub：** https://github.com/alexeygrigorev/merm

**背景：**
- AI Engineering Buildcamp 课程需要在课程中包含图表
- Mermaid 是明显格式
- 尝试从 Python 渲染 Mermaid 到图像遇限制：
  - 无 Python 库直接渲染
  - Node.js 方案底层启动完整浏览器 → 对 Mermaid 这种常见需求过重

**解决方案：**
```
要求 Claude Code 实现纯 Python 渲染器
  ↓
使用文件系统而非 GitHub Issues（不确定项目是否有用）
  ↓
创建文件夹 → 初始化 Git → 任务放 tracker/ 文件夹
  ↓
文件名编码状态（.todo.md → .groomed.md → .in-progress.md → done/）
  ↓
偶尔检查 → 指出不喜欢 → 定义更清晰标准
  ↓
最后要求基准测试（不仅要工作，还要够快）
```

**成果：**
> 结果够好 → 发布为 merm → 现在作者用它生成图表，包括本文中的。

---

### 项目 4：Rustkyll（Jekyll 的 Rust 重写）

**GitHub：** https://github.com/alexeygrigorev/rustkyll

**背景：**
- DataTalks.Club 网站使用 Jekyll（Ruby 静态站点生成器）
- 对小网站是好选择，但网站已增长 5 年+
- 构建耗时超过 1 分钟 → 中断工作流
- 小更改 → 等 1 分钟+ → 检查结果 → 重复
- 添加 Snowplow 赞助商标志提醒积累了多少摩擦

**目标：**
> 用 Rust 重写 Jekyll 使构建更快

**教训（跳过需求步骤的错误）：**
```
指向网站说"用 Rust 和方法论重新实现"
  ↓
第二天检查结果
  ↓
发现结果针对我们网站定制而非通用引擎
  ↓
必须纠正方向 → 要求找其他 Jekyll 网站使实现也支持它们
```

**当前状态：**
- 运行 3 周
- 比预期复杂得多
- 优化目标清晰：最小化 Jekyll 输出和 Rustkyll 输出差异
- backlog 耗尽后代理可比较结果 → 识别不匹配 → 创建新任务
- 对 DataTalks.Club 网站已快很多
- Jekyll 和 Rustkyll 可见差异现在很小

---

### 项目 5：Codehive（编码编排器）

**GitHub：** https://github.com/alexeygrigorev/codehive

**为什么构建 Codehive：**

**重复遇到的问题：**

1. **编排器停止当应继续**
   ```
   问"shall we proceed?"并等数小时
   或报告工作完成即使任务 widget 中仍有项目
   ```

2. **可见性限制**
   ```
   子代理花一小时做某事
   无法看是否在进展还是卡住
   ```

3. **编排器忽略流程**
   ```
   不通过 PM 梳理和 QA 验证
   直接启动 SWE
   必须注意并强制回预期工作流
   ```

4. **Claude Code 使用限制**
   ```
   简单任务也到 100% 会话限制
   想要可在工具间切换的设置
   ```

**Codehive 目标：**
- ✅ 硬编码方法论而非基于提示的纪律
- ✅ 多代理后端（Claude Code/Codex/GitHub Copilot/Z.ai）
- ✅ 非阻塞工作流（一任务等我输入时系统继续其他）
- ✅ 子代理可见性（可检查它们在做什么并在需要时干预）
- ✅ GitHub 集成（新问题自动进入任务池）

**当前状态：**
> 最近开始工作。主要焦点仍在 AI Shipping Labs 网站，但最终想投资更多到此项目并单独写文章。

**成果摘要：**
```
96 issues 完成
~2,195 测试跨后端/web/移动端
```

---

## 💡 核心洞察

### 洞察 1：三要素必不可少

**复杂项目受益于：**
1. **明确规范**
2. **分配代理角色**
3. **定义流程**

**无这三要素：**
```
代理漂移
  ↓
跳过步骤
  ↓
过早宣布完成
```

---

### 洞察 2：职责分离是关键

**为什么 4 角色模式有效：**
```
PM（梳理 + 验收）≠ SWE（实现）≠ QA（验证）
  ↓
同一代理不写代码又判断正确性
  ↓
更难跳过步骤
  ↓
更容易看到哪里出错
```

---

### 洞察 3：最终 PM 验收很重要

**原因：**
> 功能从工程角度可能看似完成，但在真实场景中仍可能失败。

**PM 验收确保：**
- ✅ 结果与用户故事对齐
- ✅ 超越仅通过测试
- ✅ 真实场景可用

---

### 洞察 4：并行处理提升效率

**作者模式：**
```
一次运行两个任务并行
  ↓
完成后拉取下两个
  ↓
循环指令保持过程自动继续
```

**成果：**
> 46 个任务中 41 个整夜完成无需干预。

---

### 洞察 5：文件状态编码轻量有效

**基于文件的追踪器：**
```
.todo.md → .groomed.md → .in-progress.md → done/
```

**优势：**
- ✅ 状态在文件名中清晰
- ✅ 简单文件移动
- ✅ 无需额外工具
- ✅ Git 友好

---

## ⚠️ 已知限制

| 限制 | 说明 | 缓解方法 |
|------|------|----------|
| **编排器停止** | 应继续时停止等输入 | Codehive 硬编码流程 |
| **可见性差** | 无法看子代理进展 | Codehive 子代理检查 |
| **流程被忽略** | 编排器跳过 PM/QA 步骤 | Codehive 强制执行 |
| **使用限制** | Claude Code 会话限制 | Codehive 多后端支持 |
| **需要监督** | 仍需要偶尔检查 | 目标是减少参与 |

---

## 📊 对比：单代理 vs 代理团队

| 维度 | 单代理 | 代理团队 |
|------|--------|----------|
| **职责** | 混合 | 分离（PM/SWE/QA/On-Call） |
| **验证** | 自己判断自己 | QA 独立验证 |
| **流程** | 隐式 | 显式定义 |
| **可见性** | 单会话 | 每角色独立报告 |
| **复杂项目** | 困难 | 适合 |
| **监督需求** | 高 | 中（减少中） |

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **原文** | https://alexeyondata.substack.com/p/i-built-an-ai-agent-team-for-software |
| **AI Shipping Labs** | https://github.com/AI-Shipping-Labs/website |
| **DataTasks** | https://github.com/alexeygrigorev/datatasks |
| **Merm** | https://github.com/alexeygrigorev/merm |
| **Rustkyll** | https://github.com/alexeygrigorev/rustkyll |
| **Codehive** | https://github.com/alexeygrigorev/codehive |
| **代理角色定义** | https://github.com/AI-Shipping-Labs/website/tree/main/.claude/agents |

---

## 📊 翻译信息

| 项目 | 信息 |
|------|------|
| **翻译时间** | 2026-04-07 |
| **原文作者** | Alexey Grigorev |
| **测试项目** | 5 个真实软件项目 |
| **翻译状态** | ✅ 完整翻译 +5 项目详解 |

---

*翻译完成时间：2026-04-07 | 版本：v1.0*
