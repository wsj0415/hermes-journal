# 发布 Claude Managed Agents — 预构建的可配置代理系统

**来源**: https://x.com/rlancemartin/status/2041927992986009773  
**抓取时间**: 2026-04-10 05:13 UTC  
**类型**: X Article 长文  
**标签**: claude-managed-agents, ai-agent, anthropic, agent-infrastructure, long-horizon-tasks, event-triggered, scheduled-tasks, fire-and-forget, multi-agent-orchestration, sdk

---

## 📊 一句话总结

Claude Managed Agents 是 Anthropic 推出的预构建、可配置代理系统，运行在托管基础设施上，用户只需定义代理模板（工具/技能/文件/仓库），系统提供代理 harness 和基础设施，设计用于支持长周期任务并随 Claude 智能增长而演进。

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：架构解耦图 ⭐ 推荐

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Create a clean technical architecture infographic for "Claude Managed Agents — Decoupled System Design".

Title: "Claude Managed Agents"
Subtitle: "预构建代理系统 + 托管基础设施"

Layout: Vertical 3-layer decoupled architecture.

Color Palette:
- Brain: Purple (#8B5CF6)
- Hands: Blue (#3B82F6)
- Session: Green (#10B981)
- Background: Dark gradient (#0F172A to #1E293B)
- Text: White

Top Section - 3 Core Concepts:

[Agent] 🟣
图标：配置文档
内容：
- 版本化配置
- 模型/系统提示词
- 工具/技能/MCP 服务器
- 创建一次，按 ID 引用

[Environment] 🔵
图标：沙盒容器
内容：
- 沙盒配置模板
- 运行时类型
- 网络策略
- 包配置

[Session] 🟢
图标：运行日志
内容：
- 状态化运行
- 新鲜沙盒
- 挂载资源（文件/仓库）
- 安全凭证存储

Middle Section - Decoupled Design:

[Brain] 大脑
图标：Claude 大脑 + harness
"模型 + 代理逻辑"
"独立演进"

[Hands] 手
图标：工具 + 沙盒
"执行动作"
"可替换"

[Session] 会话
图标：日志流
"事件记录"
"独立存储"

关键：三者解耦，可独立失败/替换

Bottom Section - Usage Patterns:

[Event-triggered] 事件触发
"系统标记 bug → 代理写 patch → 开 PR"
"无人工介入"

[Scheduled] 定时任务
"每日简报（X/GitHub 活动）"
"团队工作状态"

[Fire-and-forget] 发射不管
"Slack/Teams 分配任务"
"返回交付物（表格/幻灯片/应用）"

[Long-horizon] 长周期任务
"数天/周/月运行"
"人类最大挑战"

Badge:
"6 种语言 SDK"
"CLI + SDK 配合"
"随 Claude 智能演进"

Style: Modern technical architecture diagram, dark mode with neon accents
Aspect ratio: 9:16 portrait
```

---

### 选项 2：使用模式对比

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 6 modules for "Claude Managed Agents Usage Patterns".

Color Palette:
- Primary: Purple (#8B5CF6)
- Accent: Blue (#3B82F6)
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (6 Cards):

M1 — Hero:
"Claude Managed Agents"
"预构建 + 托管基础设施"
Icon: Robot + cloud

M2 — Agent 概念:
"版本化配置"
"模型/提示词/工具/技能"
"创建一次，按 ID 引用"

M3 — Environment:
"沙盒模板"
"运行时/网络/包配置"
"安全隔离"

M4 — Session:
"状态化运行"
"新鲜沙盒 + 挂载资源"
"安全凭证存储"

M5 — 使用模式:
事件触发 | 定时任务
发射不管 | 长周期

M6 — 关键优势:
"随 Claude 智能演进"
"无需维护 harness"
"6 种语言 SDK"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 为什么需要 Claude Managed Agents

### 当前挑战

**Claude API** 是模型的直接网关：接收消息，返回内容块。基于 messages API 构建的代理使用 harness 来路由 Claude 的工具调用到处理器并管理上下文。这带来几个挑战：

| 挑战 | 说明 |
|------|------|
| **Harness 需要跟上 Claude** | 代理 harness 编码了关于 Claude 不能做什么的假设，这些假设随 Claude 能力提升而过时，可能限制 Claude 性能 |
| **Claude 运行时间更长** | Claude 的自主运行时间已超过 10 个人类小时（METR 基准），对基础设施提出压力：需要安全、弹性支持长周期任务、支持扩展（如多代理团队） |

### 解决思路

**Claude Managed Agents 是下一步演进**：一个具有 harness 和托管基础设施的系统，设计用于在预期 Claude 工作的时间范围内支持安全、可靠的执行。

**关键洞察**: 构建能与 Claude 智能同步扩展的代理是**基础设施挑战**，而不仅仅是 harness 设计问题。

---

## 三个核心概念

### 1. Agent（代理）

**定义**: 版本化配置，存放代理的身份

**包含**:
- 模型
- 系统提示词
- 工具
- 技能
- MCP 服务器
- 文件/仓库

**使用方式**: 创建一次，按 ID 引用

---

### 2. Environment（环境）

**定义**: 模板，描述如何配置代理工具运行的沙盒

**包含**:
- 运行时类型
- 网络策略
- 包配置

**用途**: 定义代理执行代码的隔离环境

---

### 3. Session（会话）

**定义**: 使用预创建的代理配置和环境的**状态化运行**

**流程**:
1. 从环境模板配置新鲜沙盒
2. 挂载每次运行的资源（文件、GitHub 仓库）
3. 将认证信息存储在安全 vault（MCP 凭证）

**关系**: 一个 Agent 可以有多个 Sessions

---

### 三者关系

```
Agent = 配置（身份定义）
Environment = 沙盒模板（执行环境）
Session = 状态化运行（实际执行）
```

---

## 解耦的系统设计

### 设计理念

**不设计特定的 agent harness** — 预期 harness 会不断演进。

**解耦三个组件**:

| 组件 | 职责 | 特点 |
|------|------|------|
| **Brain（大脑）** | Claude + harness | 模型 + 代理逻辑，独立演进 |
| **Hands（手）** | 沙盒 + 工具 | 执行动作，可替换 |
| **Session（会话）** | 事件日志 | 独立存储 |

**优势**:
- 每个组件成为接口，对其他组件假设最少
- 每个组件可独立失败或替换
- 系统获得可靠性、安全性、灵活性

---

## 使用模式

### 1. 事件触发 (Event-triggered)

**流程**: 服务触发 Managed Agent 执行任务

**示例**:
```
系统标记 bug → Managed Agent 写 patch → 开 PR
```

**特点**: 标记到行动之间**无人工介入**

---

### 2. 定时任务 (Scheduled)

**流程**: Managed Agent 按计划执行任务

**示例**:
- 每日简报（X 或 GitHub 活动）
- 团队工作状态汇报

**作者自用**: X 活动每日简报

---

### 3. 发射不管 (Fire-and-forget)

**流程**: 人类触发 Managed Agent 执行任务

**示例**:
```
通过 Slack/Teams 分配任务 → 返回交付物
（电子表格/幻灯片/应用）
```

**特点**: 人类只负责触发，等待结果

---

### 4. 长周期任务 (Long-horizon tasks)

**作者观点**: Managed Agents 特别有用的领域

**探索**:
-  fork auto-research 仓库
- 探索应用于工程博客内容

**预期**: 未来 Claude 将在数天、周、月上运行，解决人类最大挑战

---

## 如何开始

### 快速入门

**方式 1: 使用开源技能（推荐）**

```bash
# 更新 Claude Code 到最新版
$ claude update

# 运行 Managed Agents onboarding 技能
$ claude /claude-api managed-agents-onboarding
```

**方式 2: SDK 或 CLI**

- 查看官方文档获取 SDK 快速入门
- 使用 CLI 原型化代理

---

### 使用方式

| 工具 | 用途 | 支持语言 |
|------|------|----------|
| **SDK** | 代码级：在应用中导入，运行时驱动会话 | Python, TypeScript, Java, Go, Ruby, PHP（6 种） |
| **CLI** | 终端级：每个 API 资源（agents/environments/sessions/vaults/skills/files）都作为子命令暴露 | 所有资源 |

**常见模式**:
- CLI 用于设置
- SDK 用于运行时
- 代理模板是持久的：创建后存储（如 YAML，包含模型/系统提示词/工具/MCP 服务器/技能），在部署流水线中用 CLI 应用

---

## 关键数据

| 指标 | 数值 |
|------|------|
| SDK 支持语言 | 6 种（Python/TS/Java/Go/Ruby/PHP） |
| Claude 自主运行时间 | 超过 10 个人类小时（METR 基准） |
| 核心概念 | 3 个（Agent/Environment/Session） |
| 使用模式 | 4 种（事件触发/定时/发射不管/长周期） |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "构建能与 Claude 智能同步扩展的代理是基础设施挑战" | 核心理念 |
| "Harness 需要不断更新以跟上 Claude" | 当前痛点 |
| "解耦大脑/手/会话，各自独立演进" | 设计原则 |
| "未来 Claude 将在数天/周/月上运行" | 长期愿景 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **解耦设计** — 大脑/手/会话独立演进
2. **版本化配置** — Agent 作为可复用模板
3. **安全沙盒** — Environment 隔离执行
4. **状态化会话** — Session 记录完整事件流
5. **多使用模式** — 事件/定时/手动/长周期

### 可实施
- 评估是否需要托管基础设施
- 设计内容创作的 Agent 模板
- 建立沙盒执行环境
- 记录每次会话完整日志
- 支持定时简报和事件触发

---

## 相关资源

| 资源 | 说明 |
|------|------|
| 使用模式和客户案例 | 官方文档 |
| Claude Managed Agents 设计 | 工程博客 |
| Onboarding/CLI/SDK 概述 | 快速入门指南 |
| Skills | 开源技能，用于上手新功能 |

---

*原始来源：https://x.com/rlancemartin/status/2041927992986009773*
