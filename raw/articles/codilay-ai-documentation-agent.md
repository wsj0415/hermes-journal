# CodiLay — 代码库的活文档 AI 代理

> **项目作者：** HarmanPreet Singh (@HarmanPreet-Singh-XYT)  
> **翻译时间：** 2026-04-01  
> **项目链接：** https://github.com/HarmanPreet-Singh-XYT/codilay  
> **PyPI:** https://pypi.org/project/codilay

---

## 📊 项目概览

| 指标 | 信息 |
|------|------|
| **定位** | AI 代码库文档代理 |
| **核心创新** | Wire Model（依赖追踪） |
| **输出** | 活的 Markdown 文档 |
| **界面** | Web UI + Chat + VSCode 扩展 |
| **许可证** | MIT |
| **语言** | Python |

---

## 🎯 核心理念

> **CodiLay 不仅仅是静态文档生成器；它是一个代理文档研究员。**
>
> 它阅读你的代码，通过 Wire Model 理解模块连接，并维护持久的、可搜索的知识库，你可以通过 Web UI 浏览或通过交互式 Chat 与之对话。

---

## 🛠️ 快速开始

### 安装（推荐从 PyPI）

```bash
# 基础安装
pip install codilay

# 安装所有功能（Web UI + Watch 模式）
pip install "codilay[all]"

# 全局 CLI 安装（推荐）
pipx install codilay
```

### 从源码安装

```bash
# 克隆仓库
git clone https://github.com/HarmanPreet-Singh-XYT/codilay.git
cd codilay

# 安装 Web UI 支持
pip install -e ".[serve]"

# 安装 Watch 模式支持
pip install -e ".[watch]"

# 安装全部（Web UI + Watch 模式）
pip install -e ".[all]"
```

### 设置

```bash
# 运行设置向导（安全存储 API 密钥）
codilay setup
```

---

## 🎛️ 交互式控制中心

无参数运行 `codilay` 打开基于终端的高级仪表板：

### 核心功能

| 功能 | 说明 |
|------|------|
| **项目切换器** | 快速跳转已文档化的代码库 |
| **提供者向导** | 配置密钥和模型，实时验证 |
| **实时监控** | 追踪活动扫描和资源使用 |
| **审计控制台** | 从中央菜单启动安全和架构扫描 |
| **历史浏览器** | 查看过去的对话并导出日志 |
| **智能恢复检测** | 选择"文档化代码库"时，CodiLay 会查看现有状态文件，在确认前显示未完成运行的横幅和文件计数 |

### 工具与自动化子菜单（按 9）

| 编号 | 功能 | 说明 |
|------|------|------|
| **[12]** | Commit 文档 | 交互式提示记录最新 commit、特定 hash、最近 N 个 commit、范围或完整仓库历史（可选指标） |
| **[13]** | Git hooks | 安装或移除 post-commit hook，每次 `git commit` 后在后台自动生成 commit 文档 |

---

## 🔌 Wire Model（核心创新）

CodiLay 将每个导入、函数调用和变量引用视为一个 **Wire（线）**。

### Wire 类型

| 类型 | 说明 |
|------|------|
| **Open Wires** | 未解决的引用，代理正在"追踪"寻找 |
| **Closed Wires** | 成功追踪的连接，形成依赖图的片段 |

### 工作流程

```
代码文件 → Wire 提取 → 依赖追踪 → 文档生成
    ↓           ↓           ↓           ↓
  导入/调用   开放 Wire   关闭 Wire   CODEBASE.md
```

---

## ⚡ 智能 Triage（节省 Token）

在消耗 Token 之前，CodiLay 执行高速 **Triage Phase（分类阶段）**。

### 文件分类

| 分类 | 说明 | Token 使用 |
|------|------|-----------|
| **Core** | 完整架构分析和文档 | 100% |
| **Skim** | 仅元数据和签名 | ~20% |
| **Skip** | 忽略样板代码、生成代码、平台特定噪音 | 0% |

---

## 🔄 增量更新（Git 感知）

CodiLay 是仓库感知的。如果你在 500 文件的项目中只改了 2 个文件：

```bash
codilay .
```

**执行流程：**
1. 通过 Git 检测增量
2. 仅使受影响的文档部分失效
3. 重新打开与更改代码相关的 Wire
4. 重新计算局部影响，保持 CODEBASE.md 最新

---

## 💬 Chat 功能

### 核心特性

```bash
codilay chat .
```

| 特性 | 说明 |
|------|------|
| **RAG + Deep Search** | 使用文档快速回答，可"升级"到阅读源代码获取实现细节 |
| **记忆** | 代理记住你的偏好和代码库事实，跨会话保持 |
| **Promote to Doc** | 在 chat 中找到好的解释？使用 `/promote` 将 AI 答案变成文档永久部分 |

---

### 分支对话系统

**对话是树，不是列表。** 每条消息是一个节点；编辑过去的消息会从该点创建新分支，同时完全保留原始线程。

```
msg_001 "支付服务如何工作？"
msg_002 "支付服务处理..."
msg_003 "重试呢？"
 │
 ├── 主分支（原始）
 │ msg_004 "重试使用指数退避..."
 │ msg_005 "延迟多长？"
 │
 └── Webhooks 分支（通过编辑 msg_003 创建）
    msg_006 "重试与 webhooks 分开..."
    msg_007 "Webhooks 在哪里处理？"
```

**关键特性：**
- 每个分支的 LLM 上下文仅包含其自己的祖先
- 兄弟分支的编辑不可见
- 旧对话在首次读取时自动迁移

---

### 对话可见性

| 可见性 | 谁可以看到 |
|--------|-----------|
| **private** | 仅对话所有者 |
| **team** | 所有团队成员 |

**Web UI 历史侧边栏**将对话分为 Private 和 Team 部分。设置一次用户名（存储在浏览器中），过滤器自动应用。

---

## 🌐 Web UI

```bash
codilay serve .
```

### 四层架构

| 层 | 功能 |
|----|------|
| **Layer 1: The Reader** | 高保真渲染你的部分和图 |
| **Layer 2: The Chatbot** | 从文档上下文快速问答 — 分支感知历史（仅活动分支消息发送到 LLM） |
| **Layer 3: The Deep Agent** | 深入源代码验证事实 |
| **Layer 4: Audit Lab** | 浏览过去的审计报告，直接从 Web 界面运行新审计 |

### Commits 标签

- 浏览所有 commit 文档
- 生成新文档（可选上下文和指标）
- 阅读完整文档，带视觉质量评分条

### 分支导航

- **Edit 按钮**：悬停在过去任何用户消息上出现 — 点击打开内联文本框；提交创建新分支
- **分支指示器按钮**：聊天工具栏显示活动分支名称和总数；点击打开切换器在分支间跳转
- **历史下拉菜单**：按 Private 和 Team 分组对话，显示每个对话的分支计数，可设置/更改用户名

---

## 👁️ Watch 模式（实时文档）

后台运行 CodiLay，文件更改时自动更新文档。

```bash
# Watch 当前目录，保存时自动更新
codilay watch .

# 自定义防抖延迟（5 秒）
codilay watch . --debounce 5

# 详细输出用于调试
codilay watch . -v
```

### 核心特性

| 特性 | 说明 |
|------|------|
| **防抖 Watcher** | 使用文件系统事件（通过 watchdog）保存时自动更新 |
| **实时进度显示** | 文件处理、triage 和 LLM 调用的高分辨率进度条 |
| **Eager Resolution** | Wire 在文件处理的瞬间关闭，给你即时图反馈 |

---

## 📦 VSCode 扩展

在编辑文件时内联显示文档的 VSCode 扩展。需要运行 `codilay serve .` 服务器。

### 侧边板（Activity Bar）

| 面板 | 功能 |
|------|------|
| **Documentation Sections** | 所有文档部分的树视图；点击任何部分打开 |
| **Dependencies** | 当前活动文件的 wire，切换文件时自动更新 |
| **Team Knowledge** | 从团队记忆折叠的事实/决策/约定 |

### 状态栏

```
📚 N sections · N open wires
```
右下角，每 60 秒刷新。

### 命令（命令面板）

| 命令 | 功能 |
|------|------|
| **CodiLay: Show Documentation Panel** | 在侧面板打开完整 CODEBASE.md |
| **CodiLay: Show Documentation for Current File** | 显示活动文件的文档部分 |
| **CodiLay: Ask a Question About This Code** | 与 CodiLay 聊天 — 后续继续同一对话 |
| **CodiLay: New Conversation** | 重置聊天会话 |
| **CodiLay: Search Past Conversations** | 跨聊天历史全文搜索 |
| **CodiLay: Show Documentation Diff** | 自上次运行后文档的变化 |
| **CodiLay: Browse Commit Docs** | 从 QuickPick 列表选择 commit 并阅读其文档 |
| **CodiLay: Show Dependency Graph** | 节点/边摘要（完整图在 Web UI） |
| **CodiLay: Add Team Fact** | 添加事实到团队记忆，带类别选择器 |
| **CodiLay: Run Audit** | 选择审计类型 + 深度，内联运行并阅读报告 |
| **CodiLay: Open Web UI in Browser** | 在默认浏览器打开 `codilay serve` |
| **CodiLay: Refresh Documentation** | 重新加载所有侧面板和状态栏 |

### 右键菜单

- **Explorer 上下文菜单** 和 **编辑器上下文菜单** 都显示 "CodiLay: Annotate This File"
- 从编辑器触发时，如果选择了文本，自动捕获行范围

### 内联提示

第 1 行的微妙斜体装饰显示活动文件的部分标题（用 `codilay.inlineHints` 设置切换）。

### 安装

```bash
cd vscode-extension/
npm install && npm run compile
```

---

## 📤 导出功能

以精确、Token 高效的格式导出文档，专为 LLM 上下文窗口定制。

### 交互式导出

```bash
# 启动对话界面定义导出规格
codilay export . --interactive
```

代理将你的需求翻译成规格，估算 Token，在提交前显示计划。

### CLI 直接导出

```bash
# 仅文件结构和连接
codilay export . --query "file structure and linkage only" -o structure.md

# API 端点和模式
codilay export . --query "just the API endpoints and their schemas" -o api.md
```

### 预设模板

```bash
# 列出可用预设（structure, api-surface, onboarding 等）
codilay export . --list-presets

# 使用 'architecture' 预设
codilay export . --preset architecture -o context.md
```

### 实现细节剥离

使用交互式或查询模式时，CodiLay 可自动剥离实现细节（函数体、内部逻辑），同时保留签名和文档头，大幅减少 Token 使用而不丢失架构上下文。

---

## 📊 Diff 功能

### Diff-Doc（文档内容对比）

```bash
# 显示自上次运行后文档的变化
codilay diff-doc .

# 输出为 JSON 用于编程使用
codilay diff-doc . --json-output
```

**与 `codilay diff` 区别：**
- `codilay diff`：显示 Git 级文件变化
- `codilay diff-doc`：比较实际文档内容

**自动快照：** 每次 `codilay` 运行后自动保存快照，diff 始终可用。

---

### Diff-Run（增量文档）

为自特定边界以来的代码更改生成聚焦文档，而非分析整个代码库。非常适合功能分支、PR 和增量更新。

#### 边界类型

| 类型 | 语法 | 示例 |
|------|------|------|
| **Commit hash** | `--since abc123f` | `--since abc123f` |
| **Git tag** | `--since v2.1.0` | `--since v2.1.0` |
| **Date** | `--since 2024-03-01` | `--since 2024-03-01` |
| **Branch** | `--since-branch main` | `--since-branch main` |

#### 使用示例

```bash
# 记录自特定 commit 以来的变化
codilay diff-run . --since abc123f

# 记录自发布 tag 以来的所有变化
codilay diff-run . --since v2.1.0

# 记录自上个月以来的变化
codilay diff-run . --since 2024-03-01

# 记录功能分支的变化（vs main）
codilay diff-run . --since-branch main

# 用变化分析更新 CODEBASE.md
codilay diff-run . --since-branch main --update-doc
```

#### 输出内容

| 部分 | 说明 |
|------|------|
| **Change Summary** | AI 生成的变化概述及重要性 |
| **Added/Modified/Deleted Files** | 每个变化的详细影响分析 |
| **Wire Impact Report** | 引入、满足或破坏的依赖 |
| **Affected Documentation Sections** | 哪些现有文档可能需要更新 |
| **Commit Context** | diff 中包含的所有 commit 供参考 |

**报告保存为：** `CHANGES_{boundary_type}_{timestamp}.md` 在 codilay 输出目录中，便于跟踪文档变化与代码变化。

---

## 🎯 Triage 反馈系统

标记不正确的 triage 决策以改进未来运行。更正按项目存储，并在后续运行的 triage 阶段自动应用。

```bash
# 标记被 skim 但应该是 core 的文件
codilay triage-feedback add . src/auth/handler.py skim core -r "包含关键认证逻辑"

# 标记模式（基于 glob）
codilay triage-feedback add . "tests/**" core skip --pattern -r "测试应该被跳过"

# 列出所有存储的反馈
codilay triage-feedback list .

# 为项目类型设置提示
codilay triage-feedback hint . react "将所有 hooks/ 文件视为 core"

# 移除特定文件的反馈
codilay triage-feedback remove . src/auth/handler.py

# 清除所有反馈
codilay triage-feedback clear . --yes
```

---

## 🔍 图过滤

按 wire 类型、文件层、模块或连接数过滤依赖图。对大仓库减少噪音至关重要。

```bash
# 仅显示 import 类型 wire
codilay graph . --wire-type import

# 过滤到特定目录层
codilay graph . --layer src/api

# 仅显示 3+ 连接的节点，仅出边
codilay graph . --min-connections 3 --direction outgoing

# 组合过滤器，排除测试
codilay graph . -w import -l src/core -x "tests/**"

# 列出项目的可用过滤值
codilay graph . --list-filters

# 输出为 JSON
codilay graph . --json-output
```

---

## 👥 团队协作

团队在同一项目上工作的共享知识库。记录事实、架构决策、编码约定和文件注释 — 全部按项目存储，并在文档和 chat 期间在 AI 期间展示。

### 用户管理

```bash
# 添加团队成员
codilay team add-user . alice --display-name "Alice Chen"
```

### 事实管理

```bash
# 记录事实
codilay team add-fact . "我们使用 Celery 进行异步任务" -c architecture -a alice -t backend -t infra

# 投票事实
codilay team vote . <fact-id> up

# 列出所有事实
codilay team facts .              # 所有事实
codilay team facts . -c architecture  # 按类别的事实
```

### 架构决策

```bash
# 记录架构决策
codilay team add-decision . "使用 PostgreSQL 而非 MySQL" "更好的 JSON 支持，我们的模式需要" -a alice -f src/db/

# 列出决策
codilay team decisions .          # 所有决策
codilay team decisions . -s active  # 仅活动决策
```

### 编码约定

```bash
# 添加编码约定
codilay team add-convention . "Error Handling" "所有 API 端点必须返回结构化错误响应" -e '{"error": "message", "code": 400}' -a alice

# 列出约定
codilay team conventions .
```

### 文件注释

```bash
# 注释特定文件
codilay team annotate . src/api/routes.py "这个文件太大了，计划按领域拆分" -a alice -l 1-50

# 列出注释
codilay team annotations .           # 所有注释
codilay team annotations . -f src/api/routes.py  # 每文件
```

### 团队成员

```bash
# 列出所有成员
codilay team users .
```

---

## 📊 架构总结

```
┌─────────────────────────────────────────┐
│           CodiLay 架构                  │
├─────────────────────────────────────────┤
│  输入层                                  │
│  ├── 代码库文件                          │
│  ├── Git 历史                            │
│  └── 团队知识                            │
├─────────────────────────────────────────┤
│  处理层                                  │
│  ├── Wire Model（依赖追踪）              │
│  ├── Triage（文件分类）                  │
│  ├── 增量更新（Git 感知）                │
│  └── LLM 集成                            │
├─────────────────────────────────────────┤
│  输出层                                  │
│  ├── CODEBASE.md（活文档）               │
│  ├── Web UI（4 层架构）                  │
│  ├── Chat（分支对话）                    │
│  ├── VSCode 扩展                         │
│  └── 导出功能（Token 高效）              │
└─────────────────────────────────────────┘
```

---

## 💡 关键洞察

### 1. Wire Model 创新

**传统文档生成器：** 静态分析 → 生成文档

**CodiLay：** 提取 Wire → 追踪依赖 → 活文档 → 可聊天

### 2. Token 效率

通过 **Triage + 增量更新 + 实现剥离**，CodiLay 显著减少 Token 使用：
- Triage：仅 Core 文件完整分析（~20% 文件）
- 增量：只重新处理更改文件
- 导出：剥离实现，保留签名

### 3. 分支对话

**独特功能：** 编辑过去消息创建新分支，保留原始线程。

**价值：** 探索多个方向而不丢失原始对话。

### 4. 团队协作

**团队知识：** 事实/决策/约定/注释按项目存储，AI 在文档和 chat 中自动使用。

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **GitHub 仓库** | https://github.com/HarmanPreet-Singh-XYT/codilay |
| **PyPI** | https://pypi.org/project/codilay |
| **演示视频** | https://www.youtube.com/watch?v=DKwydVqjrJw |
| **贡献指南** | [CONTRIBUTING.md](CONTRIBUTING.md) |

---

## 📝 翻译信息

| 项目 | 信息 |
|------|------|
| **翻译时间** | 2026-04-01 |
| **项目作者** | HarmanPreet Singh (@HarmanPreet-Singh-XYT) |
| **项目平台** | GitHub |
| **翻译状态** | ✅ 完整翻译 + 功能详解 |

---

*翻译完成时间：2026-04-01 | 版本：v1.0*
