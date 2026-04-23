---
title: Hermes Android 部署模式
created: 2026-04-23
updated: 2026-04-23
type: concept
tags: [android, termux, mobile-deployment, always-on, config]
sources: [raw/articles/startup-ideas-pod-hermes-imran-2026-04.md]
reviewed: false
confidence: high
confidence_reason: 来自实际生产部署案例，Imran 在 Solana Seeker 手机上运行
---

## 编译知识

**Hermes Android 部署** 是将 Hermes Agent 部署到 Android 手机的方案，通过 Termux + Termux API 实现完整功能。核心价值：**便宜的 Android 手机 + SIM 卡 = 常开、低功耗的专用 agent 设备**。

### 为什么用 Android 部署

| 优势 | 说明 |
|------|------|
| **成本** | 便宜 Android 手机 vs 抢购 Mac Mini |
| **常开** | 低功耗，24/7 运行 |
| **SIM 卡** | 独立网络连接，不依赖 WiFi |
| **传感器访问** | 电池、Wi-Fi、音量、相机、亮度、振动 |
| **真实设备** | 社交媒体发布不被限流（vs 调度 API） |

### 必需组件

1. **Termux** — Android 内的终端模拟器
2. **Termux API** — F-Droid 下载，提供传感器访问

### 解锁能力

- **直接读 SMS** — 自动化 2FA 验证码处理
- **真实设备发社交媒体** — 不被平台限流
- **传感器自动化** — 基于电量、位置、时间触发任务
- **常开监控** — 低功耗运行 cron jobs

---

## 部署步骤

```bash
# 1. 安装 Termux (F-Droid 或 GitHub)
# 2. 安装 Termux API (F-Droid)
# 3. 在 Termux 中运行 Hermes 安装脚本
# 参考官方文档的一行安装命令

# 4. 授予必要权限
termux-setup-storage
pm grant com.termux com.termux.permission.*

# 5. 安装必要依赖
pkg install python nodejs git
```

---

## Imran 的配置

| 项目 | 配置 |
|------|------|
| **设备** | Solana Seeker Android 手机 |
| **命名** | "Cookie Monster"（他的 agent 都以 Muppets 命名） |
| **网络** | Tailscale 组网 |
| **访问** | SSH + Telegram |
| **用途** | 社交媒体发布、SMS 读取、2FA 自动化 |

---

## 使用场景

### 1. 社交媒体自动化
```bash
# 从真实设备发布，不被限流
hermes "post to X about the new feature"
```

### 2. SMS 监控
```bash
# 读取新短信
termux-sms-list -n 5

# 自动化 2FA 处理
hermes "check for 2FA codes and forward to Telegram"
```

### 3. 传感器触发
```bash
# 低电量时通知
termux-battery-status | hermes "alert if below 20%"

# 到达特定位置触发任务
termux-location | hermes "run home-arrival-workflow"
```

---

## 安全考虑

1. **Tailscale 组网** — 手机电脑同虚拟网络，SSH 不暴露公网
2. **Telegram/WhatsApp 访问控制** — 只允许可信账号
3. **定期更新** — Imran 每晚更新，9 天不更新落后 535 commits
4. **密钥管理** — 使用 Hermes 自审：`"Is this secure?"`

---

## 成本对比

| 方案 | 成本 | 优点 | 缺点 |
|------|------|------|------|
| Mac Mini | $600+ | 性能强 | 贵、难买、功耗高 |
| VPS | $5-20/月 | 便宜、常开 | 无传感器、IP 可能被限流 |
| Android 手机 | $100-300 一次性 | 常开、传感器、真实设备 | 性能有限 |

---

## 时间线

- **2026-04-20**: Imran 在 The Startup Ideas Podcast 分享 Android 部署经验 [[imran-hermes-power-user]]

---

## 相关工作

- [[imran-hermes-power-user]] — Imran 完整使用模式
- [[hermes-security-setup]] — Hermes 安全设置（待创建）
- [[termux-api-reference]] — Termux API 命令参考（待创建）
