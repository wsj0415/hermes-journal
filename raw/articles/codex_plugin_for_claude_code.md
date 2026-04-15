# Claude Code 的 Codex 插件 — OpenAI 官方集成

> **原文作者：** Vaibhav (VB) Srivastav (@reach_vb)  
> **翻译时间：** 2026-03-31  
> **原文数据：** 996👍 | 131🔁 | 932K👁️ | 1,462🔖  
> **推文链接：** https://x.com/reach_vb/status/2038670509768839458  
> **项目链接：** https://github.com/openai/codex-plugin-cc

---

## 📊 推文数据

| 指标 | 数值 |
|------|------|
| 浏览量 | 932,571 |
| 点赞数 | 996 |
| 转发数 | 131 |
| 书签数 | 1,462 |
| 回复数 | 未显示 |
| 发布时间 | 2026-03-30 17:31 UTC |

---

## 🎯 核心功能

**Codex Plugin for Claude Code** — 如果你已经使用 Claude Code，这个 Codex 插件提供了一种简单的方式将 Codex 纳入同一工作流。

### 三大用途

| 用途 | 说明 | 适用场景 |
|------|------|----------|
| **1. 标准 Codex 审查** | 正常的代码审查 | 日常代码检查 |
| **2. 对抗性审查** | 更具怀疑精神的挑战式审查 | 高风险任务、关键变更 |
| **3. 任务交接** | 将工作交给 Codex 进行第二轮 | 需要不同代理视角时 |

---

## 🛠️ 安装设置

### 系统要求

| 要求 | 说明 |
|------|------|
| **ChatGPT 订阅** | 包括免费版，或 OpenAI API Key |
| **Node.js** | 18.18 或更高版本 |
| **Claude Code** | 已安装并配置 |
| **Codex CLI** | 可选（插件会处理） |

### 项目地址

**GitHub:** https://github.com/openai/codex-plugin-cc

---

### 安装步骤

#### 情况 1：Codex 尚未安装

```bash
# 克隆插件仓库
git clone https://github.com/openai/codex-plugin-cc.git
cd codex-plugin-cc

# 运行安装脚本
npm install

# 设置插件
/codex:setup
```

#### 情况 2：Codex 已安装但未认证

```bash
# 运行认证
/codex:auth

# 按照提示完成 ChatGPT 或 API Key 认证
```

---

## 📋 核心命令

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| **/codex:review** | 标准只读 Codex 审查 | 日常代码审查 |
| **/codex:adversarial-review** | 可配置的挑战式审查 | 高风险任务、关键变更 |
| **/codex:rescue** | 直接将任务交给 Codex | 线程停滞或需要 Codex 接手 |
| **/codex:status** | 检查后台任务状态 | 长时间运行任务 |
| **/codex:result** | 获取后台任务结果 | 长时间运行任务 |
| **/codex:cancel** | 取消后台任务 | 需要终止任务时 |

---

## 🚀 使用示例

### 简单首次运行

```bash
# 1. 安装插件后
/codex:setup

# 2. 运行标准审查
/codex:review

# 3. 查看结果
# Codex 会直接在 Claude Code 对话中输出审查结果
```

---

## 💡 使用建议

### 推荐模式

**一个简单的默认模式：**

1. **对所有内容运行 `/codex:review`** — 作为标准第二遍审查
2. **对高风险内容运行 `/codex:adversarial-review`** — 深入挑战实现
3. **当线程停滞时使用 `/codex:rescue`** — 让 Codex 接手

---

### 对抗性审查的特别用途

**特别适用于以下场景：**

| 场景 | 原因 |
|------|------|
| **迁移工作** | 隐藏假设比明显语法错误更危险 |
| **认证变更** | 安全关键，需要深度审查 |
| **基础设施脚本** | 错误可能导致系统故障 |
| **重构** | 可能引入隐蔽的回归问题 |
| **核心业务逻辑** | 错误影响范围大 |

---

## ⚙️ 工作原理

```
Claude Code → Codex Plugin → Codex CLI → Codex App Server
     ↓              ↓             ↓              ↓
   用户界面      插件层       本地调用      Codex 服务
```

### 关键特点

- **通过本地 Codex CLI 和 Codex 应用服务器委托**
- **使用相同的本地认证、配置、环境和 MCP 设置**
- **轻量级 — 不是单独的运行时**
- **就是 Codex，只是从 Claude Code 内部调用**

---

## 🚪 可选审查门

### 启用审查门

```bash
# 配置审查门（可选）
/codex:gate enable
```

### 作用

- **阻止 Claude Code 在 Codex 审查完成前退出**
- **确保审查一定运行**

### ⚠️ 注意事项

- **谨慎使用**
- **可能创建长的 Claude/Codex 循环**
- **可能快速消耗使用限额**

---

## 📊 使用场景对比

| 场景 | 推荐命令 | 说明 |
|------|----------|------|
| **日常代码审查** | `/codex:review` | 快速检查代码质量 |
| **安全关键变更** | `/codex:adversarial-review` | 深度挑战实现 |
| **复杂重构** | `/codex:adversarial-review` | 发现隐藏问题 |
| **任务卡住** | `/codex:rescue` | 换角度解决 |
| **长时间任务** | `/codex:rescue` + `/codex:status` | 后台运行 |
| **认证/基础设施** | `/codex:adversarial-review` | 安全审查 |

---

## 🎯 核心价值主张

### 主要价值

**从不同代理获得真正的第二遍审查，无需离开 Claude Code。**

### 优势

| 优势 | 说明 |
|------|------|
| **无缝集成** | 在 Claude Code 内直接使用 Codex |
| **双代理视角** | Claude + Codex 双重审查 |
| **轻量级** | 不是单独运行时，使用现有配置 |
| **灵活选择** | 标准审查/对抗审查/任务交接 |
| **后台运行** | 长时间任务可后台执行 |

---

## 📋 最佳实践

### ✅ 推荐做法

1. **将 `/codex:review` 作为默认第二遍审查**
2. **对高风险任务使用对抗性审查**
3. **当 Claude Code 线程停滞时使用 rescue**
4. **对认证、基础设施、迁移使用对抗性审查**
5. **谨慎使用审查门，避免消耗限额**

### ❌ 避免做法

1. **不要对所有任务都用对抗性审查** — 消耗大
2. **不要滥用审查门** — 可能造成死循环
3. **不要忘记后台任务** — 定期检查状态
4. **不要忽略 Codex 建议** — 认真对待审查结果

---

## 🔗 相关资源

| 资源 | 链接 |
|------|------|
| **插件仓库** | https://github.com/openai/codex-plugin-cc |
| **Codex 官方** | https://openai.com/codex |
| **Claude Code** | https://code.claude.com |
| **安装指南** | 查看 README.md |

---

## 💬 原文总结

> 这个插件提供了一种简单的方式，保持你的 Claude Code 工作流，同时在 Codex 擅长的地方使用 Codex。
>
> 安装它，运行 `/codex:setup`，将 `/codex:review` 作为默认第二遍审查，当你需要超过例行审查时使用 `/codex:adversarial-review` 或 `/codex:rescue`。
>
> — Vaibhav (VB) Srivastav

---

## 📊 翻译信息

| 项目 | 信息 |
|------|------|
| **翻译时间** | 2026-03-31 |
| **原文作者** | Vaibhav (VB) Srivastav (@reach_vb) |
| **原文平台** | X (Twitter) |
| **原文数据** | 996👍 131🔁 932K👁️ 1,462🔖 |
| **翻译状态** | ✅ 完整翻译 + 使用指南 |

---

## 🎯 TL;DR 总结

| 概念 | 核心要点 |
|------|----------|
| **核心功能** | 在 Claude Code 内使用 Codex 进行第二遍审查 |
| **三大用途** | 标准审查/对抗审查/任务交接 |
| **核心命令** | `/codex:review` `/codex:adversarial-review` `/codex:rescue` |
| **适用场景** | 日常审查/高风险任务/线程停滞 |
| **工作原理** | 通过本地 Codex CLI 委托，轻量级集成 |
| **注意事项** | 谨慎使用审查门，避免消耗限额 |

---

*翻译完成时间：2026-03-31 | 版本：v1.0*
