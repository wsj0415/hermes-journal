# Session Profiles: Persistent Authentication for Browser Agents

**来源**: Notte Labs (Medium)  
**作者**: nottelabs  
**发布日期**: 2026-02-25  
**链接**: https://medium.com/@nottelabs/session-profiles-persistent-authentication-for-browser-agents-d1ba1fdbf269

---

## 问题

Browser agents 每次运行都要重新认证，因为 session state 不持久化。这破坏了依赖登录 session 的工作流。

> Most agent browser demos break the moment a login session matters. You sign in once, the task ends, and the next run starts from scratch.

---

## 解决方案：Session Profiles

**Session Profiles** 保存浏览器状态（cookies、cache、local storage），让 agent 在 session 之间保持认证状态。

**核心逻辑：**
1. 手动登录一次（LinkedIn、Gmail 或任何需要认证的服务）
2. 停止 session
3. 所有状态持久化到存储
4. 下次用同一个 profile 启动 session → agent 已经登录
5. 无需重新认证，无需人工干预

---

## 为什么重要

**大部分有价值的 web 数据都在登录墙后面。**

Session Profiles 让 agent 可以：
- 抓取私有 dashboard
- 管理 SaaS 账号
- 监控内部工具
- 自动化需要认证的工作流

> Authenticate once. Automate everything after.

---

## 相关工作

- [[agent-browser-sessions]] — agent-browser 的 session 管理实现
- [[hermes-browser-automation]] — Hermes 浏览器自动化（待创建）
