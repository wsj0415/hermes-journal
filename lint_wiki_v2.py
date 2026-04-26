#!/usr/bin/env python3
"""Wiki Health Check v2 — comprehensive lint for hermes-journal."""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict

BASE = Path("/root/hermes-journal")
WIKI_DIRS = ["concepts", "entities", "comparisons", "queries"]
SCHEMA_FILE = BASE / "SCHEMA.md"
INDEX_FILE = BASE / "index.md"
LOG_FILE = BASE / "log.md"

# ── Tag Taxonomy (from SCHEMA.md) ──
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

# ── Data structures ──
pages = {}          # filename -> {path, frontmatter, content, lines, wikilinks, ...}
all_wikilinks = set()
incoming_links = defaultdict(set)  # target -> set of sources

# ── Results ──
issues = {
    "high": [],
    "medium": [],
    "low": [],
}


def extract_frontmatter(content):
    """Extract YAML frontmatter from markdown content."""
    m = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if m:
        try:
            return yaml.safe_load(m.group(1)), m.group(0)
        except yaml.YAMLError:
            return None, m.group(0)
    return None, None


def extract_wikilinks(content):
    """Extract all [[wikilinks]] from content."""
    return re.findall(r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]', content)


def filename_to_wikilink(filename):
    """Convert filename to wikilink target."""
    return filename.replace(".md", "")


def wikilink_to_filename(wikilink):
    """Convert wikilink target to possible filenames."""
    return wikilink + ".md"


def scan_wiki_pages():
    """Scan all wiki pages in the designated directories."""
    for d in WIKI_DIRS:
        dirpath = BASE / d
        if not dirpath.exists():
            continue
        for f in sorted(dirpath.iterdir()):
            if f.suffix == ".md":
                content = f.read_text(encoding="utf-8")
                lines = content.split("\n")
                fm, fm_raw = extract_frontmatter(content)
                wikilinks = extract_wikilinks(content)

                pages[f.name] = {
                    "path": str(f.relative_to(BASE)),
                    "dir": d,
                    "filename": f.name,
                    "frontmatter": fm,
                    "content": content,
                    "lines": len(lines),
                    "wikilinks": wikilinks,
                    "wikilink_count": len(wikilinks),
                }


def build_link_graph():
    """Build incoming link graph."""
    for fname, page in pages.items():
        for wl in page["wikilinks"]:
            all_wikilinks.add(wl)
            # Resolve wikilink to filename
            target_fn = wikilink_to_filename(wl)
            if target_fn in pages:
                incoming_links[target_fn].add(fname)


def check_orphan_pages():
    """Pages with no incoming links."""
    for fname, page in pages.items():
        if fname == "index.md":
            continue
        if fname not in incoming_links or len(incoming_links[fname]) == 0:
            issues["high"].append({
                "type": "孤立页面（无入链）",
                "file": page["path"],
                "detail": f"没有任何页面链接到此页，建议添加到 index.md 或相关页面",
            })


def check_broken_wikilinks():
    """Wikilinks pointing to non-existent pages."""
    for fname, page in pages.items():
        for wl in page["wikilinks"]:
            target_fn = wikilink_to_filename(wl)
            if target_fn not in pages and target_fn != "index.md":
                # Also check if it's in brand-foundation or references
                extra_paths = [
                    BASE / "brand-foundation" / target_fn,
                    BASE / "references" / target_fn,
                ]
                found = any(p.exists() for p in extra_paths)
                if not found:
                    issues["high"].append({
                        "type": "损坏的 wikilink",
                        "file": page["path"],
                        "detail": f"链接 [[{wl}]] 指向不存在的页面",
                    })


def check_missing_frontmatter():
    """Pages missing YAML frontmatter."""
    for fname, page in pages.items():
        if page["frontmatter"] is None:
            issues["high"].append({
                "type": "缺少 frontmatter",
                "file": page["path"],
                "detail": "页面缺少 YAML frontmatter，需添加 title/created/updated/type/tags",
            })


def check_page_length():
    """Pages over 200 lines."""
    for fname, page in pages.items():
        if page["lines"] > 200:
            issues["medium"].append({
                "type": "页面过长（超过 200 行）",
                "file": page["path"],
                "detail": f"当前 {page['lines']} 行，建议拆分为子主题",
            })


def check_min_wikilinks():
    """Pages with fewer than 2 wikilinks."""
    for fname, page in pages.items():
        if page["wikilink_count"] < 2:
            issues["medium"].append({
                "type": "wikilinks 不足（少于 2 个）",
                "file": page["path"],
                "detail": f"当前 {page['wikilink_count']} 个出站链接，建议至少 2 个",
            })


def check_invalid_tags():
    """Tags not in SCHEMA taxonomy."""
    for fname, page in pages.items():
        fm = page["frontmatter"]
        if fm is None:
            continue
        tags = fm.get("tags", [])
        if not tags:
            continue
        if isinstance(tags, str):
            tags = [t.strip() for t in tags.split(",")]
        for tag in tags:
            if tag not in VALID_TAGS:
                issues["medium"].append({
                    "type": "标签不在 SCHEMA 分类法中",
                    "file": page["path"],
                    "detail": f"标签 '{tag}' 不在 SCHEMA.md 分类法中",
                })


def check_unreviewed():
    """Pages with reviewed: false or missing reviewed field."""
    for fname, page in pages.items():
        fm = page["frontmatter"]
        if fm is None:
            continue
        reviewed = fm.get("reviewed")
        if reviewed is None or reviewed is False or reviewed == "false":
            issues["low"].append({
                "type": "未审查页面",
                "file": page["path"],
                "detail": f"reviewed={reviewed}，建议人工审查后标记为 true",
            })


def check_index_consistency():
    """Check if all pages are listed in index.md."""
    index_content = INDEX_FILE.read_text(encoding="utf-8")
    for fname, page in pages.items():
        link_target = fname.replace(".md", "")
        if f"[[{link_target}]]" not in index_content:
            issues["medium"].append({
                "type": "未收录于 index.md",
                "file": page["path"],
                "detail": f"页面未在 index.md 中列出，建议添加",
            })


def check_confidence_field():
    """Pages missing confidence field."""
    for fname, page in pages.items():
        fm = page["frontmatter"]
        if fm is None:
            continue
        if "confidence" not in fm:
            issues["low"].append({
                "type": "缺少 confidence 字段",
                "file": page["path"],
                "detail": "frontmatter 缺少 confidence 字段",
            })


def check_confidence_reason():
    """Pages with confidence but missing confidence_reason."""
    for fname, page in pages.items():
        fm = page["frontmatter"]
        if fm is None:
            continue
        if "confidence" in fm and "confidence_reason" not in fm:
            issues["low"].append({
                "type": "缺少 confidence_reason 字段",
                "file": page["path"],
                "detail": f"confidence={fm['confidence']} 但缺少 confidence_reason",
            })


def auto_fix_index():
    """Auto-add missing pages to index.md."""
    index_content = INDEX_FILE.read_text(encoding="utf-8")
    added = []

    for fname, page in pages.items():
        link_target = fname.replace(".md", "")
        if f"[[{link_target}]]" in index_content:
            continue

        # Determine section based on directory
        dir_section_map = {
            "concepts": "Concepts",
            "entities": "Entities",
            "comparisons": "Comparisons",
            "queries": "Queries",
        }
        section = dir_section_map.get(page["dir"], "Concepts")

        # Get title from frontmatter or filename
        fm = page["frontmatter"]
        if fm and "title" in fm:
            title = fm["title"]
        else:
            title = link_target.replace("-", " ").title()

        # Build entry
        entry = f"- [[{link_target}]] - {title}"

        # Find the section header and insert after it
        section_pattern = rf"(## {re.escape(section)}\s*\n)"
        match = re.search(section_pattern, index_content)
        if match:
            insert_pos = match.end()
            # Check if there are existing entries in this section
            remaining = index_content[insert_pos:]
            next_section = re.search(r'\n## ', remaining)
            if next_section:
                insert_pos += next_section.start()
            else:
                # Find next ## section or end
                next_sections = re.findall(r'\n## ', remaining)
                if next_sections:
                    insert_pos += remaining.index('\n## ')
            index_content = index_content[:insert_pos] + entry + "\n" + index_content[insert_pos:]
            added.append(fname)
        else:
            # Section doesn't exist, add at end
            index_content += f"\n## {section}\n\n{entry}\n"
            added.append(fname)

    if added:
        INDEX_FILE.write_text(index_content, encoding="utf-8")
        print(f"  ✅ 自动修复: 将 {len(added)} 个页面添加到 index.md")
        for a in added:
            print(f"     - {a}")
    return added


def generate_report():
    """Generate the lint report."""
    total_pages = len(pages)
    total_issues = sum(len(v) for v in issues.values())

    report = []
    report.append("## Wiki 健康检查报告")
    report.append(f"")
    report.append(f"- **扫描时间**: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append(f"- **扫描范围**: {', '.join(WIKI_DIRS)}/")
    report.append(f"- **页面总数**: {total_pages}")
    report.append(f"- **问题总数**: {total_issues}")
    report.append(f"  - 🔴 高: {len(issues['high'])}")
    report.append(f"  - 🟡 中: {len(issues['medium'])}")
    report.append(f"  - 🟢 低: {len(issues['low'])}")
    report.append(f"")

    # Group issues by type
    by_type = defaultdict(list)
    for severity in ["high", "medium", "low"]:
        for issue in issues[severity]:
            by_type[issue["type"]].append((severity, issue))

    for issue_type, items in by_type.items():
        severity = items[0][0]
        emoji = {"high": "🔴", "medium": "🟡", "low": "🟢"}[severity]
        report.append(f"### {emoji} {issue_type} ({len(items)} 个)")
        report.append(f"")
        for sev, issue in items:
            report.append(f"- **{issue['file']}**: {issue['detail']}")
        report.append(f"")

    # Link health summary
    report.append("### 📊 链接健康概览")
    report.append(f"")
    report.append(f"- 总 wikilinks: {sum(p['wikilink_count'] for p in pages.values())}")
    report.append(f"- 有入链的页面: {len(incoming_links)} / {total_pages}")
    orphan_count = sum(1 for f in pages if f not in incoming_links or len(incoming_links[f]) == 0)
    report.append(f"- 孤立页面: {orphan_count}")
    report.append(f"")

    # Top linked pages
    if incoming_links:
        report.append("### 🔗 被引用最多的页面 (Top 10)")
        report.append(f"")
        sorted_links = sorted(incoming_links.items(), key=lambda x: len(x[1]), reverse=True)[:10]
        for target, sources in sorted_links:
            report.append(f"- **{target}**: {len(sources)} 个入链 ({', '.join(list(sources)[:5])})")
        report.append(f"")

    return "\n".join(report)


def append_to_log(report):
    """Append report to log.md."""
    timestamp = __import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    entry = f"\n\n---\n\n### Wiki 健康检查 — {timestamp}\n\n{report}\n"
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(entry)
    print(f"  ✅ 检查结果已追加到 log.md")


def main():
    print("=" * 60)
    print("Wiki Health Check v2")
    print("=" * 60)

    print("\n[1/8] 扫描 wiki 页面...")
    scan_wiki_pages()
    print(f"  发现 {len(pages)} 个页面")

    print("\n[2/8] 构建链接图...")
    build_link_graph()
    print(f"  发现 {len(all_wikilinks)} 个唯一 wikilink 目标")

    print("\n[3/8] 检查孤立页面...")
    check_orphan_pages()
    print(f"  发现 {len(issues['high'])} 个高优先级问题")

    print("\n[4/8] 检查损坏的 wikilinks...")
    check_broken_wikilinks()

    print("\n[5/8] 检查 frontmatter / 页面长度 / 标签 / 审查状态...")
    check_missing_frontmatter()
    check_page_length()
    check_min_wikilinks()
    check_invalid_tags()
    check_unreviewed()
    check_index_consistency()
    check_confidence_field()
    check_confidence_reason()

    print("\n[6/8] 自动修复 index.md...")
    auto_fix_index()

    print("\n[7/8] 生成报告...")
    report = generate_report()

    print("\n[8/8] 追加到 log.md...")
    append_to_log(report)

    print("\n" + "=" * 60)
    print("检查完成!")
    print("=" * 60)

    # Print summary
    print(f"\n📊 问题统计:")
    print(f"  🔴 高: {len(issues['high'])}")
    print(f"  🟡 中: {len(issues['medium'])}")
    print(f"  🟢 低: {len(issues['low'])}")

    # Print report to stdout
    print(f"\n{'=' * 60}")
    print(report)


if __name__ == "__main__":
    main()
