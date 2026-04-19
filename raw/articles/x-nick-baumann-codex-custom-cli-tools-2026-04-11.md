# 给 Codex 最好的工具是定制 CLI — Nick Baumann 的 Agent 工具哲学

**来源**: https://x.com/nickbaumann_/status/2042705384306336083  
**作者**: Nick Baumann  
**抓取时间**: 2026-04-11 03:14 UTC  
**类型**: X 推文线程  
**标签**: codex, cli, agent-tools, custom-tools, mcp, slack, typefully, developer-tools, ai-workflow, json-output

---

## 📊 一句话总结

Nick Baumann 分享为 Codex 创建定制 CLI 工具的经验 — 相比 MCP/Connector，定制 CLI 提供精确命令、稳定 JSON 输出、可预测错误、帮助屏幕，让 Codex 能搜索/缩小/重试/管道输出/写入大结果/检查--help/从上次结果组合下一命令，三个实际案例：codex-threads（搜索历史会话）、slack-cli（搜索 Slack 线程）、typefully-cli（内容创作调度）。

---

## 🏷️ 话题标签

#Codex #CLI #Agent 工具 #定制工具 #MCP #Slack #Typefully #开发者工具 #AI 工作流 #JSON 输出

---

## 🎨 封面图提示词（nano-banana-pro 技能库）

### 选项 1：终端命令行风格 ⭐ 推荐

**来源**: nano-banana-pro / App / Web Design  
**参考 ID**: 172 (Terminal/CLI Screenshot)  
**示例图**: https://cms-assets.youmind.com/media/1772519704183_45o67p_HCbTg4yXEAALxM2.jpg

```prompt
Terminal screenshot style for "Codex Custom CLI Tools".

Style: Dark terminal theme, syntax highlighted command output, clean CLI aesthetic.

Three CLI examples shown:

1. codex-threads --json
$ codex-threads --json messages search "build a CLI" --limit 20
$ codex-threads --json threads resolve "tweet idea"
$ codex-threads --json threads read <session-id>

2. slack-cli --json
$ slack-cli search "app server auth" --all-pages --max-pages 3 --json
$ slack-cli resolve-permalink "..."
$ slack-cli read-thread L143 123522523239.633199 --json
$ slack-cli context R152 25723525099.626199 --before 5 --after 5 --json

3. typefully-cli --json
$ typefully-cli --json drafts list --social-set <id> --limit 20
$ typefully-cli --json drafts read --social-set <id> <draft-id>
$ typefully-cli --json drafts create --social-set <id> --body-file draft.json
$ typefully-cli --json media upload --social-set <id> ./image.png
$ typefully-cli --json queue schedule-read --social-set <id>

Sidebar annotations:
- ✅ "Precise Commands"
- 📦 "Stable JSON Output"
- ⚠️ "Predictable Errors"
- ❓ "--help Screen"

Bottom status bar:
"Codex excels at tool composition" | "Wrap CLI in Skill"

Window title: "Custom CLI Tools for Codex — Nick Baumann"

Aspect ratio: 9:16 portrait
```

**为什么选这个风格**: 这是关于 CLI 工具的内容，终端截图风格直接展示实际命令用法，比抽象 infographic 更直观对开发者。

---

### 选项 2：Connector vs CLI 对比图

**来源**: nano-banana-pro / Infographic / Edu Visual  
**参考 ID**: 11165 (Technical Infographic Cutaway)  
**示例图**: https://cms-assets.youmind.com/media/1772433492844_q6zr64_HCTasgQaYAADK5w.jpg

```prompt
Technical comparison diagram for "MCP/Connector vs Custom CLI for Codex".

Layout: Side-by-side comparison with verdict.

Color Palette:
- Connector: Blue (#3B82F6)
- CLI: Green (#10B981)
- Background: Dark gradient

Left — MCP/Connector:
图标：连接器
优点：
- "Great for access"
- "Direct API integration"

缺点：
- "Output too big"
- "Too noisy"
- "Awkward raw format"
- "Drags whole thing into thread"

Right — Custom CLI:
图标：终端命令
优点：
- "Precise commands with flags"
- "Stable JSON output"
- "Predictable errors"
- "--help screen"
- "Search/narrow/retry"
- "Pipe output"
- "Write large results to file"
- "Inspect --help"
- "Compose from last result"

Bottom — Verdict:
"Not replacements for connectors"
"Sit next to connectors"
"When Codex needs to work through big source"
"Without dragging whole thing into thread"

Badge:
"3 Real Examples"
"codex-threads | slack-cli | typefully-cli"

Style: Clean technical comparison, dark mode with neon accents
Aspect ratio: 9:16 portrait
```

---

### 选项 3：三工具网格展示

**来源**: nano-banana-pro / Social Media Post  
**参考 ID**: 6847 (Premium liquid glass Bento grid)  
**示例图**: https://cms-assets.youmind.com/media/1768962051381_l9uih4_537980579-6f29d32a-c786-40c4-bd5a-79c640737496.png

```prompt
Create a premium liquid glass Bento grid with 4 modules for "3 Custom CLIs for Codex".

Color Palette:
- Primary: Green (#10B981)
- Accent: Blue (#3B82F6)
- Cards: Apple liquid glass (85-90% transparent)
- Background: Ethereal abstract glow, dark gradient

Module Content (4 Cards):

M1 — Hero:
"给 Codex 最好的工具"
"定制 CLI"
Icon: Terminal + robot

M2 — codex-threads:
搜索历史会话
"--json messages search"
"--json threads resolve"
"转技能的好起点"

M3 — slack-cli:
搜索 Slack 线程
"--all-pages --max-pages"
"--before 5 --after 5"
"引用关键消息"

M4 — typefully-cli:
内容创作调度
"drafts list/read/create"
"media upload"
"queue schedule"
"Skill 规定安全边界"

Output: 1 image, 9:16 portrait, ultra-premium liquid glass infographic.
```

---

## 核心理念

### 为什么定制 CLI 胜过原始 Connector

**问题**: MCP/Connector 虽然提供访问，但原始输出：
- 太大
- 太嘈杂
- 太笨拙
- 把整个东西拖入线程

**解决**: 定制 CLI 提供：
- 带标志的精确命令
- 稳定 JSON 输出
- 可预测错误
- `--help` 屏幕

**Codex 擅长**:
- 搜索
- 缩小范围
- 重试
- 管道输出
- 写入大结果到文件
- 检查 `--help`
- 从上次结果组合下一命令
- **几乎没有仪式**

---

## 三个实际 CLI 案例

### 1. codex-threads — 搜索 Codex 历史会话

**用途**: 保持本地可搜索索引 `~/.codex/sessions`，给 Codex 命令搜索/解析/阅读旧线程。

**命令示例**:
```bash
# 搜索消息
codex-threads --json messages search "build a CLI" --limit 20

# 解析线程
codex-threads --json threads resolve "tweet idea"

# 阅读会话
codex-threads --json threads read <session-id>

# 阅读事件
codex-threads --json events read <session-id> --limit 50
```

**为什么有用**:
- 原始会话归档太嘈杂（工具输出/部分尝试/仅当时有用的上下文）
- 直接让 Codex 读线程可行，但经常做会变慢和嘈杂
- **特别是想将线程转为技能时** — 好技能始于"找到成功的线程，保留模式"

---

### 2. slack-cli — 搜索 Slack 线程

**用途**: 当答案埋在手动画找不到的线程中时 — 为什么做出 app-server auth 决策、其他人是否看到相同本地开发失败、评审者在发布频道已同意什么。

**命令示例**:
```bash
# 广泛搜索
slack-cli search "app server auth" --all-pages --max-pages 3 --json

# 解析精确链接
slack-cli resolve-permalink "..."

# 阅读线程
slack-cli read-thread L143 123522523239.633199 --json

# 拉取附近上下文
slack-cli context R152 25723525099.626199 --before 5 --after 5 --json
```

**让 Codex 能**:
- 广泛搜索
- 解析精确线程
- 拉取附近上下文
- 引用关键消息

**重要**: slack-cli 仍使用批准的 Codex apps gateway — 不是权限绕过，是相同访问模型，塑造成 agent 可组合的命令。

---

### 3. typefully-cli — 内容创作调度

**用途**: 用 Codex 写作和调度大量内容，Typefully 有好 API 但不需要 Codex 每次重新学习整个 API。

**命令示例**:
```bash
# 列出草稿
typefully-cli --json drafts list --social-set <id> --limit 20

# 阅读草稿
typefully-cli --json drafts read --social-set <id> <draft-id>

# 创建草稿
typefully-cli --json drafts create --social-set <id> --body-file draft.json

# 上传媒体
typefully-cli --json media upload --social-set <id> ./image.png

# 调度阅读
typefully-cli --json queue schedule-read --social-set <id>
```

**实现方式**: 让 Codex 阅读 API 文档并构建 typefully-cli 作为小 Rust 二进制，可从任何仓库运行。

---

## Skill 包装同样重要

**typefully-cli 的 Skill 告诉 Codex**:
- 使用 JSON
- 默认创建草稿
- shell 引用变烦时用 body 文件
- **除非明确要求，永不发布/调度/删除/覆盖任何内容**

**关键点**: 不想每次请求帮助写帖子时都输入"不要发布这个"。

---

## 核心洞察

### 何时需要定制 CLI

> "如果我持续给 Codex 相同的文档/导出/日志/API 怪异，我通常想停止解释它，给它一个命令。"

**流程**:
1. 识别重复模式（相同文档/导出/日志/API）
2. 让 Codex 构建 CLI
3. 用 Skill 包装 CLI
4. Codex 记住如何使用它

### Skill 的作用

Skill 告诉 Codex：
- 首先运行哪些命令
- 拉回多少输出
- 哪些行动需要批准

---

## 如何创建 CLI

Nick 提到他写了完整指南：

**Playbook**: "Create a CLI Codex can use"

**两部分**:
1. 用 Codex 创建 CLI
2. 用 Skill 包装 CLI，让未来 Codex 线程知道：
   - 首先运行哪些命令
   - 拉回多少输出
   - 哪些行动需要批准

---

## 关键数据

| 指标 | 数值 |
|------|------|
| 案例 CLI | 3 个 |
| codex-threads 命令 | 5 个 |
| slack-cli 命令 | 4 个 |
| typefully-cli 命令 | 5 个 |
| 输出格式 | JSON |

---

## 核心引用

| 引用 | 含义 |
|------|------|
| "Codex 擅长使用可表达为精确命令的工具" | 核心洞察 |
| "几乎没有仪式" | CLI 优势 |
| "不是 Connector 的替代品" | 定位清晰 |
| "Skill 和二进制同样重要" | 安全边界 |
| "停止解释，给它命令" | 核心哲学 |

---

## 对 KilroyContentBot 的启示

### 可借鉴点
1. **定制 CLI 思维** — 重复任务塑造成命令
2. **JSON 输出** — 稳定格式便于 Agent 处理
3. **Skill 包装** — 规定使用方式和安全边界
4. **历史会话搜索** — codex-threads 模式可参考
5. **--help 屏幕** — 自文档化便于 Agent 探索

### 可实施
- 为重复内容分析任务创建 CLI 工具
- 输出稳定 JSON 格式
- 用 Skill 包装规定使用规则
- 实现历史分析会话搜索
- 添加--help 自文档化

---

## 相关资源

| 资源 | 链接 |
|------|------|
| Nick Baumann Playbook | 文中提及（未提供链接） |
| Codex CLI 创建指南 | 待查找 |

---

*原始来源：https://x.com/nickbaumann_/status/2042705384306336083*
