#!/bin/bash
# Hermes Journal 自动同步脚本
# 用法：./sync-journal.sh [commit_message]

set -e

WIKI_DIR="/root/hermes-journal"
cd "$WIKI_DIR"

# 检查是否有更改
if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "📝 检测到更改..."
    
    # 添加所有更改
    git add -A
    
    # 提交
    MESSAGE="${1:-Auto-sync: $(date +%Y-%m-%d\ %H:%M)}"
    git commit -m "$MESSAGE"
    
    # 推送
    echo "🚀 推送到 GitHub..."
    git push origin main
    
    echo "✅ 同步完成"
else
    echo "✓ 没有需要同步的更改"
fi
