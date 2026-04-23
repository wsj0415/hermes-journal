---
title: Imran - Hermes Power User
created: 2026-04-23
updated: 2026-04-23
type: entity
tags: [person, hermes-power-user, token-optimization, automation]
sources: [raw/articles/startup-ideas-pod-hermes-imran-2026-04.md]
reviewed: false
confidence: high
confidence_reason: 来自 The Startup Ideas Podcast 深度专访，117K 浏览，细节丰富
---

## 编译知识

**Imran (@imranye)** 是 Hermes Agent 的深度用户，在一家基金工作。他的使用模式展示了 Hermes 在真实工作场景中的价值：**不是工具本身，而是它帮你从盘子里清掉什么**。

### 核心配置

| 项目 | 配置 |
|------|------|
| **运行模式** | Bare metal + 每日更新 |
| **Agent 数量** | 4 个（他认为 1-2 个足够：1 个人 +1 工作） |
| **部署设备** | Mac + Solana Seeker Android 手机（命名 "Cookie Monster"） |
| **网络** | Tailscale 组网，手机电脑同虚拟网络 |
| **访问方式** | Telegram / WhatsApp + SSH |

### 关键成果

- **Token 花费降低 90%**：$130/5 天 → $10/5 天
- **创始人交流增加 20-30%**：agent 处理后台工作，释放时间
- **7 天持续使用** 达到大部分效果
- **20 天** 后 agent 自己搭建了 Obsidian dashboard

### 为什么从 OpenClaw 迁移到 Hermes

1. OpenClaw 没有内置记忆 — 反复告诉同样的事情
2. 网关不稳定 — 有一天每小时重启一次
3. Token 花费无透明度 — 不知道什么在烧钱

先试了 Nebula，适合 AI 同事但不适合个性化学习工作流。

---

## 时间线

- **2026-04-20**: The Startup Ideas Podcast 发布深度专访，Imran 分享完整使用模式 [[startup-ideas-pod-hermes-imran-2026-04]]

---

## 相关工作

- [[hermes-token-optimization]] — Token 优化策略（OpenRouter + 代码化重复任务）
- [[hermes-android-deployment]] — Android 部署模式（Termux + Termux API）
- [[hermes-best-practices]] — Hermes 最佳实践汇总
