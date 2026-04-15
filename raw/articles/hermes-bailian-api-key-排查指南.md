# Hermes Agent 配置 Bailian API Key 故障排查指南

> 记录一次 Bailian Coding Platform API Key 配置问题的完整排查过程和解决方案
> 
> 日期：2026-04-15
> 环境：Hermes Agent + Bailian Coding Platform (通义千问)

---

## 问题描述

用户按照 Hermes Agent 文档配置了 Bailian Coding Plan 的 API Key，但无法与 Hermes 对话，返回认证失败错误。

### 错误日志

```
Error code: 401 - {
  'error': {
    'code': 'invalid_api_key', 
    'message': 'invalid access token or token expired', 
    'param': None, 
    'type': 'invalid_request_error'
  }, 
  'request_id': 'aa2b44d5-2524-9c48-9b21-24b8dc9c71ef'
}
```

---

## 排查过程

### 第一步：检查配置文件

查看 `.env` 文件确认 API Key 已配置：

```bash
cat ~/.hermes/.env

# 输出：
DASHSCOPE_API_KEY=sk-sp-43dee298b8254660ba5e2c01d4998d17
BAILIAN_API_KEY=sk-sp-43dee298b8254660ba5e2c01d4998d17
```

查看 `config.yaml` 确认 provider 配置：

```yaml
model:
  default: qwen3.5-plus
  provider: custom
  base_url: https://coding.dashscope.aliyuncs.com/v1
  api_mode: chat_completions
```

### 第二步：发现问题

**问题 1：`custom` provider 未配置 API Key 环境变量**

当使用 `provider: custom` 时，Hermes 不会自动从环境变量读取 API Key，需要在 `custom_providers` 中明确指定：

```yaml
custom_providers:
- name: bailian
  base_url: https://coding.dashscope.aliyuncs.com/v1
  api_key: ''          # ← 这里是空的！
  api_mode: chat_completions
```

**问题 2：API Key 格式验证**

虽然 `.env` 中配置了 `BAILIAN_API_KEY`，但 `custom_providers` 没有引用该环境变量。

### 第三步：验证 API Key 有效性

使用 curl 直接测试 API Key 是否有效：

```bash
curl -s -X POST https://coding.dashscope.aliyuncs.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-sp-43dee298b8254660ba5e2c01d4998d17" \
  -d '{"model": "qwen3.5-plus", "messages": [{"role": "user", "content": "hi"}]}'
```

**成功响应示例：**

```json
{
  "created": 1776241135,
  "model": "qwen3.5-plus",
  "id": "chatcmpl-8e576ff1-f3eb-961b-a111-068938989e3b",
  "choices": [{
    "finish_reason": "stop",
    "message": {
      "role": "assistant",
      "content": "Hello! How can I help you today?"
    }
  }]
}
```

如果返回 401 错误，说明 API Key 无效或已过期。

---

## 解决方案

### 方案一：使用内置 `alibaba` provider（推荐）

将主模型配置改为使用内置的 `alibaba` provider，它会自动读取 `DASHSCOPE_API_KEY` 环境变量：

```yaml
model:
  default: qwen3.5-plus
  provider: alibaba
  base_url: https://coding.dashscope.aliyuncs.com/v1
  api_mode: chat_completions
```

**优点：**
- 无需额外配置，自动读取环境变量
- 支持 `DASHSCOPE_BASE_URL` 覆盖
- 与 Hermes 其他功能兼容性更好

### 方案二：修复 `custom_providers` 配置

如果需要保留 `custom` provider，需要明确指定 `api_key_env`：

```yaml
model:
  default: qwen3.5-plus
  provider: custom
  base_url: https://coding.dashscope.aliyuncs.com/v1
  api_mode: chat_completions

custom_providers:
- name: bailian
  base_url: https://coding.dashscope.aliyuncs.com/v1
  api_key_env: BAILIAN_API_KEY    # ← 添加这行
  api_mode: chat_completions
  model: qwen3.5-plus
```

---

## 完整配置示例

```yaml
# ~/.hermes/config.yaml

# 主模型配置（使用内置 alibaba provider）
model:
  default: qwen3.5-plus
  provider: alibaba
  base_url: https://coding.dashscope.aliyuncs.com/v1
  api_mode: chat_completions

# 备用 provider 配置（可选）
custom_providers:
- name: zai
  base_url: https://open.bigmodel.cn/api/coding/paas/v4
  api_key_env: GLM_API_KEY
  api_mode: chat_completions
- name: bailian
  base_url: https://coding.dashscope.aliyuncs.com/v1
  api_key_env: BAILIAN_API_KEY
  api_mode: chat_completions
  model: qwen3.5-plus
```

```bash
# ~/.hermes/.env

DASHSCOPE_API_KEY=sk-sp-xxxxxxxxxxxxxxxx
BAILIAN_API_KEY=sk-sp-xxxxxxxxxxxxxxxx  # 可以与 DASHSCOPE_API_KEY 相同
TAVILY_API_KEY=tvly-xxxxxxxxxxxxxxxx
TELEGRAM_BOT_TOKEN=xxxxxxxxxxxxxxxx
TELEGRAM_ALLOWED_USERS=your_telegram_id
GATEWAY_ALLOW_ALL_USERS=true
```

---

## Bailian Coding Platform 接口信息

| 接口类型 | 端点 URL | 用途 |
|---------|---------|------|
| OpenAI 兼容 | `https://coding.dashscope.aliyuncs.com/v1` | 推荐，兼容大多数工具 |
| Anthropic 兼容 | `https://coding.dashscope.aliyuncs.com/apps/anthropic` | 兼容 Claude API 格式 |

---

## 常见问题及解决方案

### 1. 401 Invalid API Key

**可能原因：**
- API Key 已过期
- API Key 权限不足（没有访问 Bailian Coding Platform 的权限）
- 配置文件中 `api_key` 字段为空
- 使用了错误的 `api_key_env` 变量名

**解决方案：**
1. 登录 [阿里云 DashScope 控制台](https://dashscope.console.aliyun.com/) 确认 API Key 状态
2. 检查 API Key 是否有访问 Bailian Coding Platform 的权限
3. 使用 curl 测试 API Key 是否有效

### 2. 429 Rate Limit Exceeded

**可能原因：**
- API Key 达到请求频率限制
- 账户余额不足

**解决方案：**
1. 配置多个 API Key 使用 credential pool
2. 升级账户套餐

### 3. Connection Refused

**可能原因：**
- 网络问题
- 防火墙阻止

**解决方案：**
1. 检查网络连接
2. 尝试使用不同的 base_url（如国际版 `dashscope-intl.aliyuncs.com`）

---

## 验证配置

重启 Hermes 网关后，查看日志确认配置生效：

```bash
# 重启网关
pkill -f "gateway run"
nohup python -m hermes_cli.main gateway run > /tmp/gateway.log 2>&1 &

# 查看日志
tail -30 ~/.hermes/logs/agent.log
```

**成功的日志输出示例：**

```
INFO agent.auxiliary_client: Vision auto-detect: using active provider alibaba (qwen3.5-plus)
INFO agent.auxiliary_client: Auxiliary auto-detect: using main provider alibaba (qwen3.5-plus)
INFO gateway.run: ✓ telegram connected
INFO gateway.run: Gateway running with 1 platform(s)
```

---

## 经验总结

1. **优先使用内置 provider**：Hermes 内置的 `alibaba` provider 配置更简单，兼容性更好
2. **custom provider 需要明确配置**：使用 `provider: custom` 时必须指定 `api_key_env` 或 `api_key`
3. **先验证 API Key 有效性**：在修改配置前，先用 curl 测试 API Key 是否有效
4. **查看日志定位问题**：`~/.hermes/logs/agent.log` 是最重要的调试信息来源
5. **API Key 格式区分**：
   - `sk-sp-xxx`：阿里云 DashScope 标准格式
   - 确保 API Key 有访问对应 endpoint 的权限

---

## 参考链接

- [Hermes Agent 官方文档 - AI Providers](https://coding.dashscope.aliyuncs.com/)
- [阿里云 DashScope 控制台](https://dashscope.console.aliyun.com/)
- [通义千问 API 文档](https://help.aliyun.com/zh/model-studio/)

---

**作者：** Hermes Agent 用户
**创建时间：** 2026-04-15
**更新时间：** 2026-04-15
