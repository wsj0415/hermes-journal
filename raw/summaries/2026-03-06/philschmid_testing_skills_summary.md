# 📝 Practical Guide to Evaluating and Testing Agent Skills 总结

**日期**: 2026-03-06  
**来源**: https://www.philschmid.de/testing-skills  
**作者**: Philipp Schmid  
**主题**: Agent Skills 评估与测试实战指南

---

## 🎯 核心问题

**现状**:
- SkillsBench 统计：47,000+ 独特技能，分布在 6,300+ 仓库中
- ❌ 几乎没有人测试技能
- ❌ 大多数技能是 AI 生成的
- ❌ 仅靠手动"感觉检查"(vibe-check)几次就发布
- **类比**: 你不会发布没有测试的代码，为什么要发布没有评估的技能？

---

## 📚 什么是 Agent Skills?

**定义**: Agent Skills 是文件夹形式的指令、脚本和资源集合，用于增强 agent 能力，无需重新训练或微调模型。

**最小结构** (SKILL.md):
```yaml
---
name: gemini-interactions-api
description: 使用此技能编写调用 Gemini API 的代码
---
```

**组成部分**:
| 部分 | 作用 | 重要性 |
|------|------|--------|
| **Frontmatter** | name + description (YAML) | ⭐⭐⭐⭐⭐ 最关键，决定触发可靠性 |
| **Body** | Markdown 指令 (API/模式/注意事项) | ⭐⭐⭐⭐ |
| **Resources** | scripts/, examples/, references/ | ⭐⭐⭐ 可选 |

**技能分类**:
| 类型 | 特点 | 测试意义 |
|------|------|----------|
| **能力型技能** | 完成基础模型无法一致完成的任务 | 评估何时可被淘汰 (模型进步后) |
| **偏好型技能** | 记录特定工作流程 | 验证与真实工作流程的保真度 |

---

## ✅ 第一步：定义成功标准

**在写评估之前，先写下"成功"的可衡量定义**

### 三个评估维度

| 维度 | 检查项 | 重要性 |
|------|--------|--------|
| **结果 (Outcome)** | 代码编译、图片渲染、文档创建、API 返回有效响应 | 基线，输出不可用则一切无意义 |
| **风格与指令** | 遵循约定和技能指令 (正确的 SDK、模型 ID、命名规范、格式) | 确保一致性 |
| **效率** | 时间、tokens、精力消耗 (无必要重试、合理 token 数、无命令摇摆) | **最被低估的维度**，回归是真实成本 |

### Interactions API 技能的具体检查

```python
# 可正则检查的项
- ✅ 正确的 SDK 导入 (from google import genai)
- ✅ 当前模型 ID (不使用已弃用的 gemini-2.0-flash)
- ✅ 使用 interactions.create() 而非 generateContent
- ✅ 多轮对话使用 previous_interaction_id
```

---

## 🛠️ 评估框架实战指南

### 步骤 1: 创建提示词集合

**10-20 个提示词足够开始**，每个测试特定场景并声明成功标准：

```json
[
  {
    "id": "py_basic_generation",
    "prompt": "编写 Python 脚本发送文本提示到 Gemini 并打印响应",
    "language": "python",
    "should_trigger": true,
    "expected_checks": ["correct_sdk", "no_old_sdk", "current_model", "interactions_api"]
  },
  {
    "id": "py_deprecated_model",
    "prompt": "使用 Gemini 2.0 Flash 编写 Interactions API 脚本",
    "language": "python",
    "should_trigger": true,
    "expected_checks": ["correct_sdk", "interactions_api", "deprecated_model_rejected"]
  },
  {
    "id": "negative_unrelated",
    "prompt": "编写 Python 脚本读取 CSV 并用 matplotlib 绘制柱状图",
    "language": "python",
    "should_trigger": false,
    "expected_checks": []
  }
]
```

**测试分布示例** (17 个测试):
- 核心能力：7 个
- 已弃用模型防护：4 个
- 扩展功能 (不在技能示例中)：3 个
- **负向控制**: 2 个 ⚠️ **不要跳过负向测试** (防止技能描述过宽)

### 步骤 2: 运行 agent 并捕获输出

```python
def run_gemini_cli(prompt):
    cmd = [
        "gemini",
        "-m", "gemini-3-flash-preview",
        "--output-format", "json",
        "-p", prompt,
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=3600)
    data = json.loads(result.stdout.strip())
    return CLIOutput(
        response_text=data.get("response", ""),
        stats=data.get("stats", {}),
        exit_code=result.returncode,
    )
```

### 步骤 3: 编写确定性检查

**每个检查都是小函数，使用正则返回布尔值**:

```python
# 检查是否使用正确的 SDK
def check_correct_sdk(code, language):
    if language == "python":
        return bool(re.search(r"from\s+google\s+import\s+genai", code))
    return bool(re.search(r"""['\"]@google/genai['\"]""", code))

# 检查是否使用当前模型
DEPRECATED_MODELS = ["gemini-2.0-flash", "gemini-1.5-pro", "gemini-1.5-flash"]

def check_current_model(code, language):
    return not any(model in code for model in DEPRECATED_MODELS)

# 注册检查
CHECK_REGISTRY = {
    "correct_sdk": check_correct_sdk,
    "current_model": check_current_model,
    "interactions_api": check_interactions_api,
    "no_old_sdk": check_no_old_sdk,
    # ... 共 11 个检查
}
```

---

## 📊 评估流程

```python
def run_eval(test_case):
    output = run_gemini_cli(test_case["prompt"])
    code = extract_code_blocks(output.response_text)
    
    results = {}
    for check_id in test_case["expected_checks"]:
        check_fn = CHECK_REGISTRY[check_id]
        results[check_id] = check_fn(code, test_case["language"])
    
    pass_rate = sum(results.values()) / len(results)
    return results, pass_rate
```

---

## 🎯 实战成果

**Gemini Interactions API 技能**:
- 初始通过率：**66.7%**
- 最终通过率：**100%**
- 测试覆盖：17 个测试 × 11 个检查 = 187 个验证点

---

## 💡 关键洞察

1. **手动迭代不是浪费时间** - 每次手动修复都应转化为自动化检查
2. **负向测试至关重要** - 防止技能描述过宽导致误触发
3. **效率是真实成本** - 两个正确输出可能 token 消耗差 3 倍
4. **评估揭示技能何时过时** - 能力型技能可能随模型进步而淘汰
5. **保真度决定价值** - 偏好型技能的价值取决于与真实工作流程的匹配度

---

## 🔗 相关资源

- [SkillsBench 研究](https://arxiv.org/html/2602.12670v1)
- [Agent Skills 框架](https://agentskills.io/home)
- [Gemini Interactions API Skill](https://github.com/google-gemini/gemini-skills/blob/main/skills/gemini-interactions-api/SKILL.md)
- [LangChain 评估经验](https://blog.langchain.com/evaluating-deep-agents-our-learnings/)
- [原文链接](https://www.philschmid.de/testing-skills)

---

## 📌 行动建议

### 立即开始
1. 为现有技能定义 3 个评估维度 (结果/风格/效率)
2. 创建 10-20 个测试提示词 (包含负向测试)
3. 编写 5-10 个自动化检查函数

### 持续改进
1. 每次手动修复后添加新的自动化检查
2. 定期评估技能通过率，目标 >90%
3. 监控效率指标 (token 消耗、执行时间)

### 团队协作
1. 建立技能测试标准
2. 共享检查函数库
3. 定期回顾技能质量数据

---

**生成工具**: KilroyContentBot  
**仓库**: https://github.com/wsj0415/kilroy-cdn  
**分类**: 技能开发/评估测试
