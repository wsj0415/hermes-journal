#!/usr/bin/env python3
"""Wiki Health Check v3 — comprehensive lint for hermes-journal."""

import os
import re
import sys
from collections import defaultdict
from datetime import datetime

BASE = "/root/hermes-journal"
WIKI_DIRS = ["concepts", "entities", "comparisons", "queries"]

# Valid tags from SCHEMA
VALID_TAGS = {
    # 平台
    "telegram", "whatsapp", "discord", "sms", "web", "android",
    # 功能
    "skills", "cron", "memory", "browser", "terminal", "delegation", "mcp", "automation",
    # 任务类型
    "config", "troubleshooting", "best-practice", "workflow", "api-reference",
    # 模型
    "model-config", "provider", "quantization", "inference", "rag", "optimization",
    # 开发
    "skill-development", "debugging", "testing", "deployment",
    # 架构
    "architecture", "agent-architecture", "knowledge-base", "vector-search", "graph",
    # 内容
    "brand-foundation",
    # 人物/来源
    "karpathy", "amodei", "hermes-power-user",
    # 主题
    "monetization", "career", "ai-trends", "education", "curriculum", "decision-making", "meta",
    # 工具/框架
    "openclaw", "notebooklm", "youtube", "openrouter", "termux",
    # 设计
    "agent-design", "system-prompt", "cli", "ux", "visualization", "html", "agent-setup",
    # 元数据
    "tips", "content-creation", "company", "person",
    # 部署
    "mobile-deployment", "always-on",
    # 成本
    "token-optimization", "cost-reduction",
}

def find_wiki_pages():
    """Find all wiki pages in the designated directories."""
    pages = []
    for d in WIKI_DIRS:
        dirpath = os.path.join(BASE, d)
        if not os.path.isdir(dirpath):
            continue
        for f in sorted(os.listdir(dirpath)):
            if f.endswith(".md"):
                pages.append(os.path.join(d, f))
    return pages

def parse_frontmatter(content):
    """Parse YAML frontmatter. Returns dict or None."""
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not m:
        return None
    raw = m.group(1)
    result = {}
    for line in raw.split('\n'):
        if ':' in line:
            key, _, val = line.partition(':')
            key = key.strip()
            val = val.strip()
            # Parse list
            if val.startswith('[') and val.endswith(']'):
                items = [i.strip().strip('"').strip("'") for i in val[1:-1].split(',') if i.strip()]
                result[key] = items
            elif val == '' or val is None:
                result[key] = None
            else:
                result[key] = val
    return result

def extract_wikilinks(content):
    """Extract all [[wikilinks]] from content."""
    return re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)

def get_all_wikilinks_in_journal(pages_content):
    """Build a map of all wikilinks across the journal."""
    all_links = defaultdict(list)  # target -> list of source pages
    for page, content in pages_content.items():
        fm = parse_frontmatter(content)
        links = extract_wikilinks(content)
        for link in links:
            all_links[link].append(page)
    return all_links

def resolve_wikilink_target(link, all_pages):
    """Resolve a wikilink to an actual page path."""
    # Direct match
    for p in all_pages:
        basename = os.path.basename(p).replace('.md', '')
        if link.lower() == basename.lower():
            return p
    # Try with directory prefix
    for d in WIKI_DIRS:
        candidate = os.path.join(d, link + ".md")
        if candidate in all_pages:
            return candidate
    # Try matching just the basename
    for p in all_pages:
        if link.replace(' ', '-').lower() == os.path.basename(p).replace('.md', '').lower():
            return p
    return None

def check_orphan_pages(pages, incoming_links):
    """Find pages with no incoming links."""
    orphans = []
    for page in pages:
        basename = os.path.basename(page).replace('.md', '')
        if basename not in incoming_links or len(incoming_links[basename]) == 0:
            orphans.append(page)
    return orphans

def check_broken_links(pages_content, all_pages):
    """Find wikilinks pointing to non-existent pages."""
    broken = defaultdict(list)  # page -> list of broken links
    for page, content in pages_content.items():
        links = extract_wikilinks(content)
        for link in links:
            resolved = resolve_wikilink_target(link, all_pages)
            if resolved is None:
                broken[page].append(link)
    return broken

def check_missing_frontmatter(pages_content):
    """Find pages without frontmatter."""
    missing = []
    for page, content in pages_content.items():
        if parse_frontmatter(content) is None:
            missing.append(page)
    return missing

def check_long_pages(pages_content):
    """Find pages over 200 lines."""
    long_pages = []
    for page, content in pages_content.items():
        lines = content.split('\n')
        if len(lines) > 200:
            long_pages.append((page, len(lines)))
    return long_pages

def check_low_link_count(pages_content):
    """Find pages with fewer than 2 wikilinks."""
    low = []
    for page, content in pages_content.items():
        links = extract_wikilinks(content)
        if len(links) < 2:
            low.append((page, len(links)))
    return low

def check_invalid_tags(pages_content):
    """Find pages with tags not in SCHEMA taxonomy."""
    invalid = []
    for page, content in pages_content.items():
        fm = parse_frontmatter(content)
        if fm is None:
            continue
        tags = fm.get('tags', [])
        if tags is None:
            continue
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(',')]
        for tag in tags:
            if tag not in VALID_TAGS:
                invalid.append((page, tag))
    return invalid

def check_unreviewed(pages_content):
    """Find pages with reviewed: false or missing reviewed field."""
    unreviewed = []
    for page, content in pages_content.items():
        fm = parse_frontmatter(content)
        if fm is None:
            unreviewed.append((page, "no frontmatter"))
            continue
        reviewed = fm.get('reviewed')
        if reviewed is None:
            unreviewed.append((page, "reviewed field missing"))
        elif reviewed is False or reviewed == 'false' or reviewed == False:
            unreviewed.append((page, "reviewed: false"))
    return unreviewed

def check_missing_from_index(pages, index_content):
    """Find pages not listed in index.md."""
    missing_from_index = []
    for page in pages:
        basename = os.path.basename(page).replace('.md', '')
        # Check if the page is referenced in index.md
        if f'[[{basename}' not in index_content and f'{basename}' not in index_content:
            missing_from_index.append(page)
    return missing_from_index

def main():
    pages = find_wiki_pages()
    all_pages = set(pages)
    
    # Read all content
    pages_content = {}
    for page in pages:
        path = os.path.join(BASE, page)
        with open(path, 'r', encoding='utf-8') as f:
            pages_content[page] = f.read()
    
    # Read index
    index_path = os.path.join(BASE, "index.md")
    index_content = ""
    if os.path.exists(index_path):
        with open(index_path, 'r', encoding='utf-8') as f:
            index_content = f.read()
    
    # Build incoming links map
    all_links = get_all_wikilinks_in_journal(pages_content)
    
    # Run checks
    orphans = check_orphan_pages(pages, all_links)
    broken = check_broken_links(pages_content, all_pages)
    missing_fm = check_missing_frontmatter(pages_content)
    long_pages = check_long_pages(pages_content)
    low_links = check_low_link_count(pages_content)
    invalid_tags = check_invalid_tags(pages_content)
    unreviewed = check_unreviewed(pages_content)
    missing_index = check_missing_from_index(pages, index_content)
    
    # Print report
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    report = []
    report.append(f"## Wiki Health Check Report — {now}")
    report.append(f"Total wiki pages scanned: {len(pages)}")
    report.append("")
    
    # Severity helper
    def severity(level, label, items):
        if not items:
            return
        report.append(f"### [{level}] {label} ({len(items)} issue{'s' if len(items) != 1 else ''})")
        report.append("")
        for item in items:
            if isinstance(item, tuple):
                report.append(f"- **{item[0]}**: {item[1]}")
            else:
                report.append(f"- `{item}`")
        report.append("")
    
    # HIGH severity
    severity("高", "孤立页面（无入链）", orphans)
    severity("高", "损坏的 wikilinks", [(f"{page}: {', '.join(links)}") for page, links in broken.items()])
    severity("高", "缺少 frontmatter", missing_fm)
    
    # MEDIUM severity
    severity("中", "超过 200 行的页面", [(f"{page} ({lines} 行)", "建议拆分") for page, lines in long_pages])
    severity("中", "缺少索引条目", missing_index)
    
    # LOW severity
    severity("低", "少于 2 个 wikilinks 的页面", [(f"{page} ({count} 个链接)", "建议添加更多交叉引用") for page, count in low_links])
    severity("低", "标签不在 SCHEMA 分类法中", [(f"{page}: tag '{tag}'", "请添加到 SCHEMA.md 或移除") for page, tag in invalid_tags])
    severity("低", "未审查页面", [(f"{page}", reason) for page, reason in unreviewed])
    
    # Summary
    total_issues = len(orphans) + len(broken) + len(missing_fm) + len(long_pages) + len(low_links) + len(invalid_tags) + len(unreviewed)
    high_count = len(orphans) + len(broken) + len(missing_fm)
    med_count = len(long_pages) + len(missing_index)
    low_count = len(low_links) + len(invalid_tags) + len(unreviewed)
    
    report.append("---")
    report.append(f"**总计**: {total_issues} 个问题")
    report.append(f"- 🔴 高: {high_count}")
    report.append(f"- 🟡 中: {med_count}")
    report.append(f"- 🟢 低: {low_count}")
    report.append("")
    
    # Auto-fix: update index.md with missing pages
    if missing_index:
        report.append("### 🔧 自动修复：更新 index.md")
        report.append("")
        # Group by directory
        by_dir = defaultdict(list)
        for page in missing_index:
            d = page.split('/')[0]
            basename = os.path.basename(page).replace('.md', '')
            by_dir[d].append((page, basename))
        
        for d, items in by_dir.items():
            for page, basename in items:
                # Find the section in index.md
                section_header = f"## {d.capitalize()}"
                if section_header in index_content:
                    # Insert after the section header
                    lines = index_content.split('\n')
                    insert_idx = None
                    for i, line in enumerate(lines):
                        if line.startswith(section_header):
                            insert_idx = i + 1
                            break
                    if insert_idx:
                        # Find the next section or end
                        next_section = None
                        for i in range(insert_idx, len(lines)):
                            if lines[i].startswith('## '):
                                next_section = i
                                break
                        insert_pos = next_section if next_section else len(lines)
                        new_line = f"- [[{basename}]]"
                        # Check if already there (case insensitive)
                        already = False
                        for line in lines[insert_idx:insert_pos]:
                            if basename.lower() in line.lower():
                                already = True
                                break
                        if not already:
                            lines.insert(insert_pos, new_line)
                            index_content = '\n'.join(lines)
                            report.append(f"- Added `{basename}` to index under {d}/")
        
        # Write updated index
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_content)
        report.append("")
    
    report_text = '\n'.join(report)
    print(report_text)
    
    # Append to log.md
    log_path = os.path.join(BASE, "log.md")
    log_entry = f"\n\n---\n\n{report_text}"
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(log_entry)
    
    print(f"\n[✓] Report appended to log.md")

if __name__ == "__main__":
    main()
