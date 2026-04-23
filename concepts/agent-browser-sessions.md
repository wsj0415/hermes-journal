---
title: Agent Browser Sessions 管理
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [browser, automation, config]
sources: [raw/articles/nottelabs-session-profiles-2026-02.md]
reviewed: false
confidence: medium
confidence_reason: 基于 agent-browser.dev 文档
---

# agent-browser Sessions 文档

**来源**: agent-browser.dev  
**链接**: https://agent-browser.dev/sessions  
**相关**: [[nottelabs-session-profiles-2026-02]]

---

## 核心功能

运行多个隔离的浏览器实例，每个 session 有自己的：
- 浏览器实例
- Cookies 和存储
- 导航历史
- 认证状态

---

## 使用模式

### 1. Session 管理

```bash
# 不同 sessions
agent-browser --session agent1 open site-a.com
agent-browser --session agent2 open site-b.com

# 环境变量
export AGENT_BROWSER_SESSION=agent1
agent-browser click "#btn"

# 列出 active sessions
agent-browser session list

# 显示当前 session
agent-browser session
```

### 2. Chrome Profile 复用（最简单）

复用已有的登录状态：

```bash
# 列出可用 Chrome profiles
agent-browser profiles

# 复用 Default profile 的登录状态
agent-browser --profile Default open https://gmail.com

# 用 named profile
agent-browser --profile "Work" open https://app.example.com

# 环境变量
export AGENT_BROWSER_PROFILE=Default
agent-browser open https://gmail.com
```

**细节：**
| 项目 | 说明 |
|------|------|
| 支持浏览器 | Chrome, Chrome Canary, Chromium, Brave |
| 复制内容 | Cookies, local storage, extensions state（cache dirs 排除） |
| 原 profile | 永不修改（read-only snapshot） |
| 清理 | 浏览器关闭时 temp copy 删除 |
| Windows 注意 | 使用前关闭 Chrome |

### 3. Persistent Profiles

自定义 profile 目录，跨浏览器重启持久化：

```bash
# 使用 persistent profile directory
agent-browser --profile ~/.myapp-profile open myapp.com

# 登录一次，然后复用认证 session
agent-browser --profile ~/.myapp-profile open myapp.com/dashboard

# 环境变量
export AGENT_BROWSER_PROFILE=~/.myapp-profile
agent-browser open myapp.com
```

**Profile 目录存储：**
- Cookies 和 localStorage
- IndexedDB 数据
- Service workers
- Browser cache
- Login sessions

### 4. 从浏览器导入认证状态

如果已经在 Chrome 中登录了某个网站，可以抓取 auth state 并复用。

**Step 1:** 启动 Chrome with remote debugging：

```bash
# macOS
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --remote-debugging-port=9222

# Linux
google-chrome --remote-debugging-port=9222
```

在这个 Chrome 窗口中登录目标网站。

> ⚠️ `--remote-debugging-port` 在 localhost 暴露完整浏览器控制。任何本地进程都能连接。只在可信机器上使用，用完关闭 Chrome。

**Step 2:** 连接并保存认证状态：

```bash
agent-browser --auto-connect state save ./my-auth.json
```

**Step 3:** 在未来 sessions 中使用保存的 auth：

```bash
# 启动时加载 auth
agent-browser --state ./my-auth.json open https://app.example.com/dashboard

# 或加载到现有 session
agent-browser state load ./my-auth.json
agent-browser open https://app.example.com/dashboard
```

**结合 `--session-name` 实现跨重启自动持久化：**

```bash
agent-browser --session-name myapp state load ./my-auth.json
# 之后 state 自动保存
```

---

## 与 Hermes 集成

Hermes 有 browser 工具，但 session 持久化需要额外配置。可以：

1. 用 agent-browser 管理认证 session
2. Hermes 调用 agent-browser 作为子进程
3. 或直接用 agent-browser 的 profile 作为 Hermes browser 的基础

---

## 相关工作

- [[nottelabs-session-profiles-2026-02]] — Session Profiles 概念说明
- [[hermes-browser-automation]] — Hermes 浏览器自动化（待创建）
- [[hermes-android-deployment]] — Android 部署（Termux 中也可用 agent-browser）
