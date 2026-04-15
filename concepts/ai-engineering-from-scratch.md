---
title: AI Engineering From Scratch 完整课程
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [education, curriculum, best-practice]
sources: [raw/articles/ai-engineering-from-scratch-full-guide.md]
reviewed: false
confidence: high
confidence_reason: 基于单一权威来源完整翻译，内容结构忠实原文
---

## 编译知识

AI Engineering From Scratch 是一个从零开始的 AI 工程完整课程，包含 260+ lessons、20 phases、预计 290 小时。核心理念：**你不是"学习 AI"，你是"用 AI 学习 AI"**。课程产出不是"我学到了东西"，而是可安装的工具、提示词、技能、Agent 作品集。

**关键数据**：84% 的学生已经在使用 AI 工具，只有 18% 觉得自己准备好专业地使用它们。这门课程填补了这个差距。

---

## 时间线

- 2026-04-15: 从 kilroy-cdn 迁移，来源 Rohit G00 (@rohitg00)

---

## 核心理念

### 学习哲学

```
你不是"学习 AI"。
你是"用 AI 学习 AI"。
然后你构建真实的东西。
然后你发布他人可以使用的工具。
```

### 与传统课程对比

| 维度 | 传统课程 | 本课程 |
|------|----------|--------|
| **范围** | 单一领域（NLP 或视觉或 Agent） | 全部：数学、ML、DL、NLP、视觉、语音、Transformer、LLM、Agent、集群 |
| **语言** | 仅 Python | Python, TypeScript, Rust, Julia |
| **输出** | "我学到了东西" | 可安装的工具、提示词、技能、Agent 作品集 |
| **深度** | 表面级或理论密集 | 先从零构建，再使用框架 |
| **格式** | 观看视频 | 可运行代码 + 文档 + Web 应用 + AI 测验 |
| **学习方式** | 被动消费 | AI 原生：使用 Claude Code 技能边学边测 |

**这不是你观看的课程。这是你与 AI 编码代理一起使用的课程。**

---

## 核心工具

### 内置 AI 技能

| 技能 | 功能 |
|------|------|
| **/find-your-level** | 10 问题测验，根据你的知识映射到起始阶段，构建个性化路径和时长估算 |
| **/check-understanding <phase>** | 每阶段测验（8 问题），带反馈和具体复习课程建议 |

### 课程产出

每节课结束不是"恭喜你，学会了 X"，而是产出**可复用的工具**：

| 产出类型 | 说明 |
|----------|------|
| **Prompts** | 粘贴到任何 AI 助手获得专家级帮助 |
| **Skills** | 安装到 Claude Code、Cursor 或任何编码代理 |
| **Agents** | 部署为自主工作者 |
| **MCP Servers** | 插入任何 MCP 兼容的 AI 应用 |

---

## 完整课程目录

### Phase 0: 设置与工具（12 课）

为接下来的一切准备环境。

| # | 课程 | 类型 | 语言 |
|---|------|------|------|
| 01 | [开发环境](phases/00-setup-and-tooling/01-dev-environment) | 构建 | Python, Node, Rust |
| 02 | [Git 与协作](phases/00-setup-and-tooling/02-git-and-collaboration) | 学习 | -- |
| 03 | [GPU 设置与云](phases/00-setup-and-tooling/03-gpu-setup-and-cloud) | 构建 | Python |
| 04 | [API 与密钥](phases/00-setup-and-tooling/04-apis-and-keys) | 构建 | Python, TS |
| 05 | [Jupyter Notebooks](phases/00-setup-and-tooling/05-jupyter-notebooks) | 构建 | Python |
| 06 | [Python 环境](phases/00-setup-and-tooling/06-python-environments) | 构建 | Python |
| 07 | [AI 的 Docker](phases/00-setup-and-tooling/07-docker-for-ai) | 构建 | Python |
| 08 | [编辑器设置](phases/00-setup-and-tooling/08-editor-setup) | 构建 | -- |
| 09 | [数据管理](phases/00-setup-and-tooling/09-data-management) | 构建 | Python |
| 10 | [终端与 Shell](phases/00-setup-and-tooling/10-terminal-and-shell) | 学习 | -- |
| 11 | [AI 的 Linux](phases/00-setup-and-tooling/11-linux-for-ai) | 学习 | -- |
| 12 | [调试与性能分析](phases/00-setup-and-tooling/12-debugging-and-profiling) | 构建 | Python |

---

### Phase 1-20: 核心内容

| Phase | 主题 | 课程数 | 预计时长 |
|-------|------|--------|----------|
| 1-2 | 数学基础 | 24 | 30h |
| 3-5 | 机器学习 | 36 | 45h |
| 6-8 | 深度学习 | 42 | 50h |
| 9-11 | NLP | 30 | 35h |
| 12-13 | 计算机视觉 | 24 | 30h |
| 14-15 | Transformer | 18 | 25h |
| 16-18 | LLM | 30 | 40h |
| 19 | AI Agent | 18 | 25h |
| 20 | 集群与部署 | 16 | 20h |

---

## 学习路径建议

### 初学者（0 经验）

```
Phase 0 → Phase 1-2 → Phase 3-5 → Phase 6-8 → 选择专业方向
预计时间：6-8 个月
```

### 有编程经验

```
使用 /find-your-level 测验
跳过已掌握的内容
预计时间：3-4 个月
```

### AI 从业者

```
直接跳转到专业阶段
使用 /check-understanding 验证知识
预计时间：1-2 个月
```

---

## 核心特色

### 1. 从零构建

每个核心概念都要求你**先从零构建**，然后再使用成熟框架：

```
学习神经网络？
→ 先用 NumPy 从零构建
→ 然后再用 PyTorch/TensorFlow

学习 Transformer？
→ 先手写注意力机制
→ 然后再用 Hugging Face
```

### 2. 多语言能力

| 语言 | 用途 |
|------|------|
| **Python** | ML/DL/LLM 主要语言 |
| **TypeScript** | Web 应用、前端集成 |
| **Rust** | 高性能推理、系统编程 |
| **Julia** | 科学计算、数值分析 |

### 3. 作品集导向

每阶段结束不是考试，而是**构建可发布的项目**：

| Phase | 项目示例 |
|-------|----------|
| 5 | 从零构建的 ML 库 |
| 8 | 图像分类 Web 应用 |
| 11 | 聊天机器人产品 |
| 15 | 自定义 Transformer 实现 |
| 18 | 部署的 LLM 应用 |
| 20 | 完整的 AI 系统 |

---

## 使用方式

### 与 AI 代理一起学习

```
1. 打开课程目录
2. 选择当前课程
3. 用 AI 代理（Claude Code/Cursor）一起构建
4. 运行 /check-understanding 测验
5. 完成后构建产出物
6. 发布到作品集
```

### 技能安装

```bash
# 安装课程技能到 Claude Code
claude skills install ai-engineering-from-scratch

# 使用技能
/find-your-level
/check-understanding phase-5
```

---

## 关键洞察

1. **用 AI 学习 AI** — 不是被动消费，而是主动构建
2. **从零开始** — 先理解底层，再用高级框架
3. **作品集导向** — 每节课都有可展示的产出
4. **多语言** — 适应不同场景的工具选择
5. **AI 原生** — 课程设计假设你有 AI 编码代理

---

## 相关链接

- [[12-agentic-harness-patterns]] - 12 个 Agentic Harness 模式
- [[claude-md-three-blocks-learning-system]] - Claude MD 三模块学习系统
- [GitHub 仓库](https://github.com/rohitg00/ai-engineering-from-scratch)
- [官方网站](https://aiengineeringfromscratch.com)
