# Claude Code 安全设置 — 没人告诉你的配置

**来源**: https://x.com/noisyb0y1/status/2041947492065943810  
**抓取时间**: 2026-04-09 17:21 UTC  
**类型**: X Article 长文  
**标签**: claude-code, ai-security, credential-protection, developer-security, mcp-security, sandbox, permissions, trailofbits, devcontainer

---

## 核心洞察

**一句话总结**: Claude Code 默认无限制访问你的机器（SSH 密钥、AWS 凭证、.env 文件），55% 的 AI 项目开发者意外泄露敏感数据，单次损失$8,000-$50,000，平均 197 天才发现。本文提供 3 级安全配置方案，15 分钟防止 90% 攻击向量。

---

## ⚠️ 危险区域（默认无限制访问）

```
~/.ssh/            → 你的服务器密钥
~/.aws/            → 你的云凭证
~/.npmrc           → 你的 npm token
.env files         → 每个项目的 API 密钥
curl, wget, nc     → 可以发送数据到任何地方
~/.bashrc          → 每次打开终端都运行
```

**攻击不需要复杂**: 克隆仓库里的 CLAUDE.md 文件，依赖库里的注释，Claude 读取指令执行 — 凭据已经泄露。

---

## 📊 真实数据

| 指标 | 数值 |
|------|------|
| 开发者泄露敏感数据 | 55% |
| AI 项目凭据泄露率 | 比常规项目高 40% |
| 单次损失 | $8,000-$50,000 |
| 平均发现时间 | 197 天 |
| MCP 攻击向量 | Check Point 发现恶意配置劫持 |
| 关键漏洞 | Claude Code 2.0.65 前未修复 |

---

## 🛡️ 3 级安全配置

### LEVEL 1 — 15 分钟（覆盖 90%）

**步骤 1: 启用沙盒**
```bash
# 在 Claude Code 会话内运行
/sandbox
# 选择：Auto-allow mode
```

**步骤 2: 完整配置**

创建或编辑 `~/.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm run *)",
      "Bash(npm test *)",
      "Bash(npx prettier *)",
      "Bash(npx eslint *)",
      "Bash(git status)",
      "Bash(git diff *)",
      "Bash(git log *)",
      "Bash(git commit *)",
      "Bash(ls *)",
      "Bash(cat *)",
      "Bash(grep *)"
    ],
    "deny": [
      "Read(~/.ssh/**)",
      "Read(~/.gnupg/**)",
      "Read(~/.aws/**)",
      "Read(~/.azure/**)",
      "Read(~/.kube/**)",
      "Read(~/.npmrc)",
      "Read(~/.git-credentials)",
      "Read(~/.config/gh/**)",
      "Edit(~/.bashrc)",
      "Edit(~/.zshrc)",
      "Bash(curl *)",
      "Bash(wget *)",
      "Bash(nc *)",
      "Bash(ssh *)",
      "Bash(git push *)",
      "Read(*.env)",
      "Read(.env.*)"
    ]
  },
  "enableAllProjectMcpServers": false,
  "sandbox": {
    "filesystem": {
      "denyRead": ["./.env", "./.env.*"]
    }
  }
}
```

**步骤 3: 更新**
```bash
claude update
```

**Linux 需先安装**:
```bash
sudo apt-get install bubblewrap socat
```

---

### LEVEL 2 — 30 分钟（Trail of Bits 完整工作流）

**安装他们的市场**:
```bash
claude plugin marketplace add trailofbits/skills
```

**在 Claude Code 会话内**:
```bash
/trailofbits:config
```

**额外获得**:
- **Workflow hooks** — 强制编码前规划、结构化调试、发布前验证
- **Security skills** — 分析清单、漏洞模式、高级审计师决策逻辑
- **CLAUDE.md 模板** — 无投机功能、无过早抽象、每个依赖需理由

**技能链**: brainstorm → plan → execute → verify

---

### LEVEL 3 — 1 小时（完全隔离）

**安装 Devcontainer**:
```bash
npm install -g @devcontainers/cli

git clone https://github.com/trailofbits/claude-code-devcontainer \
  ~/.claude-devcontainer

~/.claude-devcontainer/install.sh self-install
```

**单个不可信仓库**:
```bash
git clone <suspicious-repo>
cd suspicious-repo
devc .         # 安装模板 + 启动容器
devc shell     # 在容器内打开 shell
claude         # 零主机访问工作
```

**bypassPermissions** 在容器内启用 — Claude 工作快因为容器就是沙盒。

---

## 📋 配置说明

### allow 块
- 安全的只读操作
- 自动确认
- 每次 git status 不弹窗

### deny 块
- **Read(~/.ssh, ~/.aws...)** — 凭据保护，Claude 无法触碰
- **Bash(curl, wget, nc, ssh)** — 无数据外泄，即使被黑也无法连接
- **Read(*.env)** — 阻止最常见的泄露向量

### enableAllProjectMcpServers: false
- 阻止克隆不可信仓库时加载恶意 MCP 配置

### sandbox → denyRead
- 双层 .env 保护
- 阻止 Claude 启动的程序读取

---

## 📈 投入产出比

| 级别 | 时间 | 防护 | 替换 |
|------|------|------|------|
| Level 1 | 15 分钟 | 90% 攻击向量 | 虚假安全感 |
| Level 2 | 30 分钟 | 完整工作流 | 数小时文档阅读 |
| Level 3 | 1 小时 | 零主机访问 | 在个人机器跑客户代码的焦虑 |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "55% 开发者泄露敏感数据" | 问题普遍性 |
| "$8,000-$50,000 单次损失" | 经济影响 |
| "197 天平均发现时间" | 检测滞后 |
| "Claude Code 强大因为能做一切，这正是你不想要的" | 核心矛盾 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **沙盒优先** — OS 级别隔离
2. **最小权限** — 只允许必要操作
3. **默认拒绝** — deny 块优先于 allow
4. **定期更新** — 修补已知漏洞

### 可实施
- 检查现有 Claude Code 配置
- 添加.deny 规则保护敏感文件
- 评估是否需要 Devcontainer 隔离
- 记录安全决策到 wiki/

---

*原始来源：https://x.com/noisyb0y1/status/2041947492065943810*
