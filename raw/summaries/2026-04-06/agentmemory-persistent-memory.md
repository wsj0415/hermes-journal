# AgentMemory — AI 编码代理的持久记忆系统

> **项目作者：** Rohit G00 (@rohitg00)  
> **翻译时间：** 2026-04-06  
> **项目链接：** https://github.com/rohitg00/agentmemory  
> **核心技术：** iii-engine  
> **测试覆盖：** 581 个测试

---

## 📊 项目概览

| 指标 | 数值 |
|------|------|
| **定位** | AI 编码代理持久记忆 |
| **核心技术** | iii-engine |
| **测试数量** | 581 个测试 |
| **外部依赖** | 零外部数据库依赖 |
| **MCP 工具** | 41 个工具 |
| **REST API** | 100 个端点 |
| **支持代理** | Claude Code/Cursor/Codex/Windsurf/任何 MCP 客户端 |

---

## 🎯 核心问题

**每个 AI 编码代理都有同样的盲点：**

```
会话结束 → 记忆消失
↓
你重新解释架构
你重新发现 bug
你重新教授偏好
```

**内置记忆文件（CLAUDE.md、.cursorrules）的局限：**
- 200 行便利贴
- 会溢出
- 会过时

**agentmemory 的解决方案：**
- 可搜索、版本化、跨代理数据库
- 41 个 MCP 工具
- 三流检索（BM25 + 向量 + 知识图谱）
- 4 层记忆巩固
- 来源追踪引用
- 级联过时机制（退休事实不再污染上下文）

---

## 📈 可衡量成果

**基于 240 个真实观察、30 个会话、20 个标记查询的评估：**

| 系统 | Recall@10 | NDCG@10 | MRR | 每查询 Token |
|------|-----------|---------|-----|-------------|
| **内置（grep 全部到上下文）** | 55.8% | 80.3% | 82.5% | 19,462 |
| **agentmemory BM25** | 55.9% | 82.7% | 95.5% | 1,571 |
| **agentmemory + Xenova 嵌入** | 64.1% | 94.9% | 100.0% | 1,571 |

**关键成果：**
- ✅ **92% token 节省**（19,462 → 1,571）
- ✅ **Recall@10 提升 8pp**（55.8% → 64.1%）
- ✅ **MRR 完美**（100%）
- ✅ **语义搜索**：搜索"数据库性能优化"能找到 3 周前的"N+1 查询修复"（关键词 grep 字面上做不到）

---

## 🔄 工作原理

### 会话流程

```
会话 1："给 API 添加认证"
  ↓
代理编写代码、运行测试、修复 bug
  ↓
agentmemory 静默捕获每个工具使用
  ↓
会话结束 → 观察压缩为结构化记忆

会话 2："现在添加速率限制"
  ↓
agentmemory 注入会话 1 的上下文：
  - 认证使用 src/middleware/auth.ts 中的 JWT 中间件
  - test/auth.test.ts 中的测试覆盖 token 验证
  - 决策：选择 jose 而非 jsonwebtoken（为了 Edge 兼容）
  ↓
代理带着完整项目意识开始
```

**无需手动笔记。无需复制粘贴。代理就是知道。**

---

## 🛠️ 核心能力

| 能力 | 说明 |
|------|------|
| **自动捕获** | 通过钩子静默记录每个工具使用、文件编辑、测试运行、错误 |
| **LLM 压缩** | 原始观察压缩为结构化事实、概念、叙事 |
| **上下文注入** | 会话开始时注入过去知识（可配置 token 预算） |
| **语义搜索** | 混合 BM25 + 向量搜索，即使措辞不同也能找到相关记忆 |
| **记忆进化** | 记忆随时间版本化、相互替代、形成关系图 |
| **项目档案** | 每项目聚合智能：顶级概念、文件、约定、常见错误 |
| **自动遗忘** | TTL 过期、矛盾检测、基于重要性的驱逐保持记忆清洁 |
| **隐私优先** | API 密钥、秘密、<private>标签在存储前被剥离 |
| **自愈** | 断路器、提供者回退链、自纠正 LLM 输出、健康监控 |
| **Claude Code 桥接** | 与 ~/.claude/projects/*/memory/MEMORY.md 双向同步 |
| **跨代理 MCP** | 独立 MCP 服务器（Cursor、Codex、Gemini CLI、Windsurf、任何 MCP 客户端） |
| **引用来源** | JIT 验证将任何记忆追溯回源观察和会话 |
| **级联过时** | 被替代的记忆自动标记相关图节点、边、兄弟节点为过时 |
| **知识图谱** | 实体提取 + BFS 遍历文件、函数、概念、错误 |
| **4 层记忆** | 工作→情景→语义→程序巩固（强度衰减） |
| **团队记忆** | 跨团队成员命名空间共享 + 私有记忆 |
| **治理** | 编辑、删除、批量删除、所有记忆操作审计追踪 |
| **Git 快照** | 通过 git 提交版本化、回滚、diff 记忆状态 |

---

## 📊 对比：内置记忆 vs agentmemory

| 能力 | 内置（CLAUDE.md、.cursorrules） | agentmemory |
|------|--------------------------------|-------------|
| **规模** | 200 行上限（MEMORY.md） | 无限制 |
| **搜索** | 全部加载到上下文 | BM25 + 向量 + 图谱（仅返回 top-K） |
| **Token 成本** | 240 观察时 22K+ token | ~1,900 token（节省 92%） |
| **1K 观察时** | 80% 记忆不可见 | 100% 可搜索 |
| **5K 观察时** | 超出上下文窗口 | 仍约 2K token |
| **跨会话回忆** | 仅在线内上限内 | 完整语料库搜索 |
| **跨代理** | 每代理文件（无共享） | MCP + REST API（任何代理） |
| **多代理协调** | 不可能 | 租约、信号、行动、例行 |
| **跨代理同步** | 无 | P2P 网格（7 范围：记忆、行动、语义、程序、关系、图谱） |
| **记忆信任** | 无验证 | 引用链追溯回源观察 + 置信度评分 |
| **语义搜索** | 无（关键词 grep） | 是（Recall@10：64% vs grep 56%） |
| **记忆生命周期** | 手动修剪 | 艾宾浩斯衰减 + 分层驱逐 |
| **知识图谱** | 无 | 实体提取 + 时间版本化 |
| **可观测性** | 手动读取文件 | 实时查看器（:3113 端口） |

---

## 🤖 支持的代理

### 原生钩子支持

这些代理原生支持钩子。agentmemory 通过 12 个钩子自动捕获工具使用。

| 代理 | 集成 | 设置 |
|------|------|------|
| **Claude Code** | 12 个钩子（所有类型） | `/plugin install agentmemory` 或手动钩子配置 |
| **Claude Code SDK** | Agent SDK 提供者 | 内置 AgentSDKProvider 使用你的 Claude 订阅 |

---

### MCP 客户端

任何连接 MCP 服务器的代理都可以使用 agentmemory 的 41 个工具、6 个资源、3 个提示。

| 代理 | 如何连接 |
|------|----------|
| **Claude Desktop** | 添加到 claude_desktop_config.json MCP 服务器 |
| **Cursor** | 在设置中添加 MCP 服务器 |
| **Windsurf** | MCP 服务器配置 |
| **Cline / Continue** | MCP 服务器配置 |
| **任何 MCP 客户端** | 指向 http://localhost:3111/agentmemory/mcp/* |

---

### REST API

没有钩子或 MCP 的代理可以直接通过 100 个 REST 端点集成。

```bash
# 捕获代理做了什么
POST /agentmemory/observe

# 查找相关记忆
POST /agentmemory/smart-search

# 获取注入上下文
POST /agentmemory/context

# 获取丰富上下文（文件 + 记忆 + bug）
POST /agentmemory/enrich

# 保存长期记忆
POST /agentmemory/remember

# 获取项目智能
GET /agentmemory/profile
```

---

### 使用场景

| 你的情况 | 使用 |
|----------|------|
| Claude Code 用户 | 插件安装（钩子 + MCP + 技能） |
| 用 Claude SDK 构建自定义代理 | AgentSDKProvider（零配置） |
| 使用 Cursor、Windsurf 或任何 MCP 客户端 | MCP 服务器（41 工具 + 6 资源 + 3 提示） |
| 构建自己的代理框架 | REST API（100 端点） |
| 跨多个代理共享记忆 | 所有代理指向同一个 iii-engine 实例 |

---

## 🚀 快速开始

### 方式 1：Claude Code 插件

```bash
# 添加到插件市场
/plugin marketplace add rohitg00/agentmemory

# 安装
/plugin install agentmemory
```

所有 12 个钩子、4 个技能、MCP 服务器自动注册。

---

### 方式 2：一键启动

```bash
npx @agentmemory/agentmemory
```

自动安装 iii-engine（如缺失）、启动、运行 worker。一条命令。

---

### 方式 3：源码安装

```bash
git clone https://github.com/rohitg00/agentmemory.git && cd agentmemory
npm install && npm run build && npm start
```

---

### 健康检查

```bash
curl http://localhost:3111/agentmemory/health
```

**响应示例：**
```json
{
  "status": "healthy",
  "service": "agentmemory",
  "version": "0.7.1",
  "health": {
    "memory": { "heapUsed": 42000000, "heapTotal": 67000000 },
    "cpu": { "percent": 2.1 },
    "eventLoopLagMs": 1.2,
    "status": "healthy"
  },
  "circuitBreaker": { "state": "closed", "failures": 0 }
}
```

---

### 实时查看器

```bash
# 实时查看器（自动启动于 3113 端口）
open http://localhost:3113
```

---

### 手动钩子配置

如不想用插件，可直接添加钩子到 `~/.claude/settings.json`：

```json
{
  "hooks": {
    "SessionStart": [{ "type": "command", "command": "node ~/agentmemory/dist/hooks/session-start.mjs" }],
    "UserPromptSubmit": [{ "type": "command", "command": "node ~/agentmemory/dist/hooks/prompt-submit.mjs" }],
    "PreToolUse": [{ "type": "command", "command": "node ~/agentmemory/dist/hooks/pre-tool-use.mjs" }],
    "PostToolUse": [{ "type": "command", "command": "node ~/agentmemory/dist/hooks/post-tool-use.mjs" }],
    "PostToolUseFailure": [{ "type": "command", "command": "node ~/agentmemory/dist/hooks/post-tool-failure.mjs" }],
    "PreCompact": [{ "type": "command", "command": "node ~/agentmemory/dist/hooks/pre-compact.mjs" }],
    "SubagentStart": [{ "type": "command", "command": "node ~/agentmemory/dist/hooks/subagent-start.mjs" }],
    "SubagentStop": [{ "type": "command", "command": "node ~/agentmemory/dist/hooks/subagent-stop.mjs" }],
    "Notification": [{ "type": "command", "command": "node ~/agentmemory/dist/hooks/notification.mjs" }],
    "TaskCompleted": [{ "type": "command", "command": "node ~/agentmemory/dist/hooks/task-completed.mjs" }],
    "Stop": [{ "type": "command", "command": "node ~/agentmemory/dist/hooks/stop.mjs" }],
    "SessionEnd": [{ "type": "command", "command": "node ~/agentmemory/dist/hooks/session-end.mjs" }]
  }
}
```

---

## 🔧 钩子详解

### 钩子流程

```
PostToolUse 钩子触发
  ↓
去重检查 SHA-256 哈希（5 分钟窗口，无重复）
  ↓
mem::privacy 剥离秘密、API 密钥、<private>标签
  ↓
mem::observe 存储原始观察，推送到实时流
  ↓
mem::compress LLM 提取：类型、事实、叙事、概念、文件
  - 用 Zod 验证
  - 质量评分（0-100）
  - 验证失败自纠正（1 次重试）
  - 生成向量嵌入用于语义搜索

SessionStart 钩子触发
  ↓
mem::context 加载该项目最近会话
  - 跨观察混合搜索（BM25 + 向量）
  - 注入项目档案（顶级概念、文件、模式）
  - 应用 token 预算（默认：2000 token）
  ↓
stdout 代理在对话中接收上下文
```

---

### 12 个钩子

| 钩子 | 捕获内容 |
|------|----------|
| **SessionStart** | 项目路径、会话 ID、工作目录 |
| **UserPromptSubmit** | 用户提示（隐私过滤） |
| **PreToolUse** | 文件访问模式 + 丰富上下文注入（Read、Write、Edit、Glob、Grep） |
| **PostToolUse** | 工具名称、输入、输出 |
| **PostToolUseFailure** | 失败工具调用 + 错误上下文 |
| **PreCompact** | 上下文压缩前重新注入记忆上下文 |
| **SubagentStart/Stop** | 子代理生命周期事件 |
| **Notification** | 系统通知 |
| **TaskCompleted** | 任务完成事件 |
| **Stop** | 触发会话结束总结 |
| **SessionEnd** | 标记会话完成 |

---

## 🔍 搜索：三流检索

agentmemory 使用三流检索组合三个信号实现最大召回率。

| 流 | 说明 | 何时 |
|----|------|------|
| **BM25** | 带同义词扩展和二分搜索前缀匹配的干关键词匹配 | 始终开启 |
| **向量** | 稠密嵌入上的余弦相似度（Xenova、OpenAI、Gemini、Voyage、Cohere、OpenRouter） | 配置任何嵌入提供者 |
| **图谱** | 通过实体匹配和共现边的知识图谱遍历 | 查询中检测到实体 |

**融合：** 所有三流用互逆秩融合（RRF，k=60）融合，会话多样化（每会话最多 3 结果）最大化覆盖。

---

### BM25 增强（v0.6.0）

- **Porter 词干提取器** 规范化词形（"authentication" ↔ "authenticating"）
- **编码领域同义词** 扩展查询（"db" ↔ "database"、"perf" ↔ "performance"）
- **二分搜索前缀匹配** 替换 O(n) 扫描

---

### 嵌入提供者

agentmemory 自动检测使用哪个提供者。最佳结果安装本地嵌入（无需 API 密钥）：

```bash
npm install @xenova/transformers
```

| 提供者 | 模型 | 维度 | 环境变量 | 说明 |
|--------|------|------|----------|------|
| **本地（推荐）** | all-MiniLM-L6-v2 | 384 | `EMBEDDING_PROVIDER=local` | 免费、离线、比仅 BM25 +8pp 召回 |
| **Gemini** | text-embedding-004 | 768 | `GEMINI_API_KEY` | 免费层（1500 RPM） |
| **OpenAI** | text-embedding-3-small | 1536 | `OPENAI_API_KEY` | $0.02/1M token |
| **Voyage AI** | voyage-code-3 | 1024 | `VOYAGE_API_KEY` | 为代码优化 |
| **Cohere** | embed-english-v3.0 | 1024 | `COHERE_API_KEY` | 免费试用可用 |
| **OpenRouter** | 任何嵌入模型 | 可变 | `OPENROUTER_API_KEY` | 多模型代理 |

**无嵌入提供者？** 仅 BM25 模式（带词干和同义词）仍优于内置记忆。

---

### 智能搜索

智能搜索首先返回紧凑结果（标题、类型、评分、时间戳）节省 token。扩展特定 ID 获取完整观察详情。

```bash
# 紧凑结果（每个 50-100 token）
curl -X POST http://localhost:3111/agentmemory/smart-search \
  -d '{"query": "database migration"}'

# 扩展特定
curl -X POST http://localhost:3111/agentmemory/observe/expand \
  -d '{"ids": ["obs_123", "obs_456"]}'
```

---

## 🧠 记忆进化

### 4 层记忆

| 层 | 说明 | 巩固 |
|----|------|------|
| **工作记忆** | 当前会话观察 | 会话结束 → 情景 |
| **情景记忆** | 特定会话事件 | 强度衰减 → 语义 |
| **语义记忆** | 一般事实、概念 | 关系图形成 |
| **程序记忆** | 如何做事、约定 | 最高强度 |

### 级联过时

```
记忆 A 被记忆 B 替代
  ↓
自动标记相关图节点为过时
  ↓
边、兄弟节点级联标记
  ↓
退休事实不再污染上下文
```

---

## 👥 团队记忆

### 命名空间

| 类型 | 范围 | 说明 |
|------|------|------|
| **共享记忆** | 团队 | 所有团队成员可见 |
| **私有记忆** | 个人 | 仅创建者可见 |

### P2P 网格同步

| 范围 | 说明 |
|------|------|
| **memories** | 记忆同步 |
| **actions** | 行动同步 |
| **semantic** | 语义记忆 |
| **procedural** | 程序记忆 |
| **relations** | 关系 |
| **graph** | 知识图谱 |

**7 范围** 跨代理实例同步。

---

## 📊 治理

### 操作

| 操作 | 说明 |
|------|------|
| **编辑** | 编辑特定记忆 |
| **删除** | 删除特定记忆 |
| **批量删除** | 批量删除记忆 |
| **审计追踪** | 所有记忆操作审计 |

### Git 快照

```bash
# 版本化记忆状态
git commit -m "Memory snapshot"

# 回滚
git revert <commit>

# Diff
git diff <commit1> <commit2> -- memory/
```

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **GitHub 仓库** | https://github.com/rohitg00/agentmemory |
| **基准报告** | benchmark/QUALITY.md, SCALE.md, REAL-EMBEDDINGS.md |
| **iii-engine** | https://iii.dev |

---

## 📊 翻译信息

| 项目 | 信息 |
|------|------|
| **翻译时间** | 2026-04-06 |
| **项目作者** | Rohit G00 |
| **项目平台** | GitHub |
| **翻译状态** | ✅ 完整翻译 + 核心能力详解 |

---

*翻译完成时间：2026-04-06 | 版本：v1.0*
