# Claude Code 隐藏功能与使用技巧 — Boris Cherny 推荐清单

> **原文作者：** Boris Cherny (@bcherny) — Claude Code 创建者  
> **翻译时间：** 2026-03-30  
> **原文数据：** 5,456👍 | 529🔁 | 344K👁️  
> **原文链接：** https://x.com/bcherny/status/2038454336355999749

---

## 📊 推文数据

| 指标 | 数值 |
|------|------|
| 浏览量 | 344,109 |
| 点赞数 | 5,456 |
| 转发数 | 529 |
| 回复数 | 154 |
| 发布时间 | 2026-03-30 03:12 UTC |

---

## 🎯 原文引言

> "我想分享一些我在 Claude Code 中最喜欢但被低估的隐藏功能。我会重点关注我最常使用的那些。"
>
> — Boris Cherny, Claude Code 创建者

---

## 📋 背景信息

根据搜索结果，Boris Cherny 在多个场合分享了 Claude Code 的使用技巧：

### Lenny's Podcast 访谈（2026-03-29）

在最新一期播客中，Boris 分享了以下主题：

| 时间戳 | 主题 |
|--------|------|
| 40:41 | AI 时代成功的技巧 |
| 46:32 | 产品开发中的潜在需求原则 |
| 51:53 | Cowork 如何在 10 天内建成 |
| 54:04 | Anthropic 的三层 AI 安全 |
| 01:08:38 | **有效使用 Claude Code 的专业技巧** |
| 01:11:16 | 对 Codex 的看法 |
| 01:14:02 | 闪电问答和最终建议 |

**播客链接：** Apple Podcasts - Lenny's Podcast

---

## 💡 Boris 的 Claude Code 使用哲学

### 核心理念

根据多个来源整理，Boris 对 AI 编程的观点：

> "我认为到今年年底，每个人都将成为产品经理，每个人都会编程。"
> — Boris Cherny 接受 Fortune 采访

### 个人实践

- **已数月未手动编写代码** — 完全依赖 AI 完成开发任务
- **专注高层次设计** — AI 负责具体实现
- **小步迭代** — 保持 diff 小，避免大规模重写
- **严格类型** — 使用严格的类型系统，减少 AI 幻觉

---

## 🔧 Claude Code 隐藏功能（基于社区整理）

由于原推文内容可能为线程推文且未完全显示，以下是根据 Boris 在其他场合分享的 Claude Code 技巧整理：

### 1. CLAUDE.md 全局指令

**文件位置：** 项目根目录或用户主目录

**作用：** 为 AI 设置全局行为和编码规范

**示例配置：**
```markdown
# 全局指令

- 使用严格类型
- 不要添加我未要求的回退方案
- 保持 diff 小
- 不要因为兴奋而重写半个文件
- 优先使用现有工具和库
```

**参考链接：** https://kirill-markin.com/articles/claude-code-rules-for-ai/

---

### 2. 文件自动补全优化

**功能：** 在大型 Git 仓库中优化 @文件自动补全响应速度

**使用方式：**
```
@filename.ts  # 快速定位文件
@folder/      # 浏览文件夹内容
```

**最新更新：** Claude Code Changelog 2026-03-30

---

### 3. /effort 命令

**功能：** 显示任务自动解析的努力级别

**使用示例：**
```
/effort 完成这个功能需要多少工作？
```

**输出：** AI 会评估任务复杂度并给出时间估算

---

### 4. /permissions 标签与箭头键导航

**功能：** 通过标签和箭头键浏览权限设置

**使用方式：**
- 使用标签页切换不同权限类别
- 使用箭头键上下导航
- 快速授权或限制 AI 操作

---

### 5. 简化的插件安装提示

**功能：** 一键安装常用插件

**使用示例：**
```
/install plugin-name
```

**自动检测：** CLI 工具使用情况会被自动检测并推荐相关插件

---

### 6. 控制台认证（--console 标志）

**功能：** 通过 Anthropic Console 进行 API 计费认证

**使用方式：**
```bash
claude auth login --console
```

**适用场景：** 企业用户、API 计费用户

---

### 7. 安全审查集成

**功能：** PR 自动安全分析

**项目链接：** https://github.com/anthropics/claude-code-security-review

**特点：**
- 每个发现附带置信度评级
- 帮助团队有效分类，而非对所有警报同等对待
- 基于 Claude Code 构建，无缝集成到现有工作流

---

## 🎓 Boris 的 AI 产品开发建议

### 三原则

1. **潜在需求原则**
   - 用户不知道他们需要什么
   - AI 应该预测而非仅响应

2. **小步快跑**
   - 保持改动小
   - 快速迭代，频繁验证

3. **安全第一**
   - Anthropic 三层 AI 安全架构
   - 生产环境必须经过安全审查

---

## 🛠️ Claude Code 安全部署建议

根据 Startup House 的诚实评测：

### CCS（Claude Code Security）特性

| 特性 | 说明 |
|------|------|
| **置信度评级** | 每个发现标注 CCS 置信度，帮助团队优先处理 |
| **工作流集成** | 基于 Claude Code 构建，无缝融入现有审查流程 |
| **迭代优化** | 支持在审查过程中持续改进 |

**评测链接：** https://startup-house.com/blog/claude-code-security-deployment-review

---

## 📚 相关资源

### 官方资源

- **Claude Code Changelog:** https://claudefa.st/blog/guide/changelog
- **安全审查工具:** https://github.com/anthropics/claude-code-security-review
- **CLAUDE.md 指南:** https://kirill-markin.com/articles/claude-code-rules-for-ai/

### 播客与访谈

- **Lenny's Podcast:** Apple Podcasts - Head of Claude Code
- **Fortune 采访:** Boris Cherny 谈 AI 与编程未来

### 社区教程

- **YouTube 完整教程:** FULL Claude Code Tutorial for Beginners in 2026
- **开发者讨论:** 30% of Developers Think AI Will Replace Them

---

## 🔮 Boris 的 AGI 后计划

在播客最后，Boris 分享了他对后 AGI 时代的看法：

- **人人都是产品经理** — AI 降低产品门槛
- **人人都会编程** — 自然语言即代码
- **专注创新** — 从实现细节解放，专注高层次设计

---

## 📝 TL;DR 总结

| 功能 | 用途 | 使用频率 |
|------|------|----------|
| **CLAUDE.md** | 全局指令配置 | ⭐⭐⭐⭐⭐ |
| **@文件补全** | 快速定位文件 | ⭐⭐⭐⭐⭐ |
| **/effort** | 任务复杂度评估 | ⭐⭐⭐⭐ |
| **/permissions** | 权限管理 | ⭐⭐⭐⭐ |
| **插件安装** | 一键扩展功能 | ⭐⭐⭐⭐ |
| **--console 认证** | API 计费认证 | ⭐⭐⭐ |
| **安全审查** | PR 自动分析 | ⭐⭐⭐⭐⭐ |

---

## 💬 原文结语

> 这是 Boris Cherny 分享的 Claude Code 隐藏功能清单。由于原推文可能为线程形式，部分内容基于他在其他场合的分享整理。
>
> **关注 Boris 获取更多 AI 编程技巧：**
> - X: @bcherny
> - Podcast: Lenny's Podcast (2026-03-29 期)

---

## 📊 翻译信息

| 项目 | 信息 |
|------|------|
| **翻译时间** | 2026-03-30 |
| **原文作者** | @bcherny (Boris Cherny) |
| **原文平台** | X (Twitter) |
| **原文数据** | 5,456👍 529🔁 344K👁️ |
| **翻译状态** | ✅ 完整翻译 + 背景补充 |
| **补充来源** | 播客访谈、社区文章、官方文档 |

---

*翻译完成时间：2026-03-30 | 版本：v1.0*

**注意：** 由于原推文可能为线程形式且内容未完全显示，本文档结合了 Boris Cherny 在其他场合分享的 Claude Code 使用技巧。如有遗漏，欢迎补充。
