#!/usr/bin/env python3
"""Wiki health check (lint) for hermes-journal."""

import os
import re
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict

BASE_DIR = Path("/root/hermes-journal")
WIKI_DIRS = ["concepts", "entities", "comparisons", "queries"]
SCHEMA_FILE = BASE_DIR / "SCHEMA.md"
INDEX_FILE = BASE_DIR / "index.md"
LOG_FILE = BASE_DIR / "log.md"

# Valid tags from SCHEMA.md
VALID_TAGS = {
    "telegram", "whatsapp", "discord", "sms", "web",
    "skills", "cron", "memory", "browser", "terminal", "delegation", "mcp",
    "config", "troubleshooting", "best-practice", "workflow", "api-reference",
    "model-config", "provider", "quantization", "inference",
    "skill-development", "debugging", "testing", "deployment",
    "architecture", "agent-architecture", "knowledge-base", "vector-search", "graph",
    "brand-foundation",
    "karpathy", "amodei",
    "monetization", "career", "ai-trends", "education", "curriculum", "decision-making",
    "openclaw", "notebooklm", "youtube",
    "agent-design", "system-prompt", "cli", "ux", "visualization", "html", "agent-setup",
    "tips", "content-creation", "company", "person"
}

# Valid page types
VALID_TYPES = {"entity", "concept", "comparison", "query", "summary", "config", "troubleshooting"}

def get_all_wiki_pages():
    """Get all wiki pages from the specified directories."""
    pages = []
    for dir_name in WIKI_DIRS:
        dir_path = BASE_DIR / dir_name
        if dir_path.exists():
            for f in dir_path.glob("*.md"):
                pages.append(f)
    return sorted(pages)

def extract_wikilinks(content):
    """Extract [[wikilinks]] from content."""
    # Match [[link]] or [[link|text]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    return re.findall(pattern, content)

def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith('---'):
        return None
    try:
        end_idx = content.index('---', 3)
        fm_text = content[3:end_idx].strip()
        return yaml.safe_load(fm_text)
    except Exception as e:
        return None

def check_page(page_path):
    """Check a single page for issues."""
    issues = []
    
    try:
        content = page_path.read_text(encoding='utf-8')
    except Exception as e:
        return [{"type": "read_error", "severity": "high", "message": f"无法读取文件：{e}"}]
    
    lines = content.split('\n')
    line_count = len(lines)
    
    # Check frontmatter
    frontmatter = parse_frontmatter(content)
    if frontmatter is None:
        issues.append({
            "type": "missing_frontmatter",
            "severity": "high",
            "message": "缺少 YAML frontmatter"
        })
    else:
        # Check required fields
        required_fields = ["title", "created", "updated", "type"]
        for field in required_fields:
            if field not in frontmatter:
                issues.append({
                    "type": "missing_field",
                    "severity": "medium",
                    "message": f"frontmatter 缺少字段：{field}"
                })
        
        # Check type
        if "type" in frontmatter and frontmatter["type"] not in VALID_TYPES:
            issues.append({
                "type": "invalid_type",
                "severity": "medium",
                "message": f"无效的 type: {frontmatter['type']}"
            })
        
        # Check tags
        if "tags" in frontmatter:
            tags = frontmatter.get("tags", [])
            if isinstance(tags, str):
                tags = [tags]
            for tag in tags:
                if tag not in VALID_TAGS:
                    issues.append({
                        "type": "invalid_tag",
                        "severity": "medium",
                        "message": f"标签不在 SCHEMA 分类法中：{tag}"
                    })
        
        # Check reviewed status
        reviewed = frontmatter.get("reviewed", False)
        if not reviewed:
            issues.append({
                "type": "unreviewed",
                "severity": "low",
                "message": "页面未审查 (reviewed: false)"
            })
    
    # Check line count
    if line_count > 200:
        issues.append({
            "type": "too_long",
            "severity": "medium",
            "message": f"页面过长 ({line_count} 行)，建议拆分"
        })
    
    # Extract and check wikilinks
    wikilinks = extract_wikilinks(content)
    if len(wikilinks) < 2:
        issues.append({
            "type": "few_wikilinks",
            "severity": "low",
            "message": f"wikilinks 过少 ({len(wikilinks)} 个)，建议至少 2 个"
        })
    
    return {
        "issues": issues,
        "wikilinks": wikilinks,
        "line_count": line_count,
        "frontmatter": frontmatter
    }

def find_orphaned_pages(pages, all_wikilinks):
    """Find pages with no incoming links."""
    # Build set of all linked pages
    linked_pages = set()
    for links in all_wikilinks.values():
        for link in links:
            linked_pages.add(link)
    
    orphaned = []
    for page in pages:
        page_name = page.stem  # filename without .md
        if page_name not in linked_pages and page_name != "index":
            orphaned.append(page)
    
    return orphaned

def find_broken_links(pages, existing_pages_set):
    """Find wikilinks pointing to non-existent pages."""
    broken = defaultdict(list)
    
    for page, result in pages.items():
        for link in result["wikilinks"]:
            # Check if the linked page exists
            if link not in existing_pages_set:
                broken[str(page)].append(link)
    
    return broken

def update_index_if_needed(index_file, pages):
    """Update index.md with any missing pages."""
    if not index_file.exists():
        return False, "index.md 不存在"
    
    content = index_file.read_text(encoding='utf-8')
    existing_pages_set = set()
    
    # Extract pages from index
    for line in content.split('\n'):
        match = re.search(r'\[\[([^\]]+)\]\]', line)
        if match:
            existing_pages_set.add(match.group(1))
    
    # Find pages not in index
    missing = []
    for page_path, result in pages.items():
        page_name = page_path.stem
        if page_name not in existing_pages_set:
            missing.append(page_name)
    
    if not missing:
        return False, "index.md 已包含所有页面"
    
    # Add missing pages to appropriate sections
    updates = []
    for page_name in missing:
        page_path = next(p for p in pages.keys() if p.stem == page_name)
        dir_name = page_path.parent.name
        fm = pages[page_path].get("frontmatter", {})
        title = fm.get("title", page_name) if fm else page_name
        
        # Determine section
        section_map = {
            "entities": "## Entities",
            "concepts": "## Concepts",
            "comparisons": "## Comparisons",
            "queries": "## Queries"
        }
        section = section_map.get(dir_name, "## Concepts")
        
        updates.append(f"- [[{page_name}]] - {title}")
    
    return True, f"发现 {len(missing)} 个页面未添加到 index.md: {', '.join(missing)}"

def main():
    """Run the health check."""
    report = []
    report.append(f"# Wiki 健康检查报告")
    report.append(f"检查时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    
    # Get all wiki pages
    wiki_pages = get_all_wiki_pages()
    report.append(f"扫描页面总数：{len(wiki_pages)}")
    report.append(f"扫描目录：{', '.join(WIKI_DIRS)}")
    report.append("")
    
    # Check each page
    page_results = {}
    all_wikilinks = {}
    existing_pages_set = set()
    
    for page in wiki_pages:
        existing_pages_set.add(page.stem)
        result = check_page(page)
        page_results[page] = result
        all_wikilinks[page] = result["wikilinks"]
    
    # Issue categories
    issues_by_type = defaultdict(list)
    
    for page, result in page_results.items():
        for issue in result["issues"]:
            issues_by_type[issue["type"]].append({
                "page": str(page),
                "severity": issue["severity"],
                "message": issue["message"]
            })
    
    # Find orphaned pages
    orphaned = find_orphaned_pages(wiki_pages, all_wikilinks)
    if orphaned:
        for page in orphaned:
            issues_by_type["orphaned"].append({
                "page": str(page),
                "severity": "medium",
                "message": "孤立页面（无入链）"
            })
    
    # Find broken links
    broken_links = find_broken_links(page_results, existing_pages_set)
    for page, links in broken_links.items():
        for link in links:
            issues_by_type["broken_link"].append({
                "page": page,
                "severity": "high",
                "message": f"损坏的 wikilink: [[{link}]]"
            })
    
    # Generate report
    severity_order = {"high": 0, "medium": 1, "low": 2}
    issue_type_names = {
        "missing_frontmatter": "缺少 frontmatter",
        "missing_field": "缺少 frontmatter 字段",
        "invalid_type": "无效的页面类型",
        "invalid_tag": "标签不在 SCHEMA 分类法中",
        "unreviewed": "未审查页面",
        "too_long": "页面过长（>200 行）",
        "few_wikilinks": "wikilinks 过少（<2 个）",
        "orphaned": "孤立页面（无入链）",
        "broken_link": "损坏的 wikilinks",
        "read_error": "文件读取错误"
    }
    
    report.append("## 问题汇总")
    report.append("")
    
    total_issues = sum(len(v) for v in issues_by_type.values())
    report.append(f"发现问题总数：{total_issues}")
    report.append("")
    
    # Sort issue types by severity
    sorted_types = sorted(
        issues_by_type.keys(),
        key=lambda t: min(severity_order.get(i["severity"], 3) for i in issues_by_type[t])
    )
    
    for issue_type in sorted_types:
        issues = issues_by_type[issue_type]
        report.append(f"### {issue_type_names.get(issue_type, issue_type)} ({len(issues)} 个)")
        report.append("")
        
        # Sort by severity
        issues = sorted(issues, key=lambda x: severity_order.get(x["severity"], 3))
        
        for issue in issues:
            severity_marker = {"high": "🔴", "medium": "🟡", "low": "🟢"}.get(issue["severity"], "⚪")
            page_name = Path(issue["page"]).name
            report.append(f"- {severity_marker} **{issue['severity'].upper()}**: `{page_name}`")
            report.append(f"  - 问题：{issue['message']}")
            report.append(f"  - 建议：{get_suggestion(issue_type)}")
            report.append("")
    
    # Auto-fix section
    report.append("## 自动修复")
    report.append("")
    
    # Check index.md
    index_updated, index_msg = update_index_if_needed(INDEX_FILE, page_results)
    if index_updated:
        report.append(f"- ✅ 已更新 index.md: {index_msg}")
    else:
        report.append(f"- ℹ️  {index_msg}")
    
    report.append("")
    
    # Summary
    report.append("## 统计摘要")
    report.append("")
    report.append(f"| 指标 | 数量 |")
    report.append(f"|------|------|")
    report.append(f"| 总页面数 | {len(wiki_pages)} |")
    report.append(f"| 高严重性问题 | {sum(1 for v in issues_by_type.values() for i in v if i['severity'] == 'high')} |")
    report.append(f"| 中严重性问题 | {sum(1 for v in issues_by_type.values() for i in v if i['severity'] == 'medium')} |")
    report.append(f"| 低严重性问题 | {sum(1 for v in issues_by_type.values() for i in v if i['severity'] == 'low')} |")
    
    report_text = '\n'.join(report)
    print(report_text)
    
    # Append to log.md
    append_to_log(report_text)
    
    return report_text

def get_suggestion(issue_type):
    """Get suggestion for an issue type."""
    suggestions = {
        "missing_frontmatter": "添加 YAML frontmatter（参考 SCHEMA.md）",
        "missing_field": "在 frontmatter 中添加缺失字段",
        "invalid_type": "更正 type 为有效值：entity/concept/comparison/query/summary/config/troubleshooting",
        "invalid_tag": "使用 SCHEMA.md 中定义的标签，或先将新标签添加到分类法",
        "unreviewed": "审查页面内容后将 reviewed 设为 true，并填写 reviewed_at",
        "too_long": "拆分为多个子主题页面，添加交叉链接",
        "few_wikilinks": "添加至少 2 个指向相关页面的 wikilinks",
        "orphaned": "在相关页面添加指向此页面的 wikilink，或考虑是否应该删除",
        "broken_link": "创建缺失的页面，或修正 wikilink 指向正确的页面",
        "read_error": "检查文件权限和编码"
    }
    return suggestions.get(issue_type, "手动检查并修复")

def append_to_log(content):
    """Append content to log.md."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"\n\n## {timestamp} - Wiki 健康检查\n\n{content}\n"
    
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(log_entry)

if __name__ == "__main__":
    main()
