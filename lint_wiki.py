#!/usr/bin/env python3
"""
Wiki Health Check (Lint) for Hermes Journal
Scans wiki pages and checks for various issues.
"""

import os
import re
import yaml
from datetime import datetime
from pathlib import Path
from collections import defaultdict

JOURNAL_ROOT = Path("/root/hermes-journal")
WIKI_DIRS = ["concepts", "entities", "comparisons", "queries", "references", "brand-foundation"]
SCHEMA_FILE = JOURNAL_ROOT / "SCHEMA.md"
INDEX_FILE = JOURNAL_ROOT / "index.md"
LOG_FILE = JOURNAL_ROOT / "log.md"

# Valid tags from SCHEMA.md
VALID_TAGS = {
    # 平台
    "telegram", "whatsapp", "discord", "sms", "web",
    # 功能
    "skills", "cron", "memory", "browser", "terminal", "delegation", "mcp",
    # 任务类型
    "config", "troubleshooting", "best-practice", "workflow", "api-reference",
    # 模型
    "model-config", "provider", "quantization", "inference",
    # 开发
    "skill-development", "debugging", "testing", "deployment",
    # 架构
    "architecture", "agent-architecture", "knowledge-base", "vector-search", "graph",
    # 内容
    "brand-foundation",
    # 人物/来源
    "karpathy", "amodei",
    # 主题
    "monetization", "career", "ai-trends", "education", "curriculum", "decision-making",
    # 工具/框架
    "openclaw", "notebooklm", "youtube",
    # 设计
    "agent-design", "system-prompt", "cli", "ux", "visualization", "html", "agent-setup",
    # 元数据
    "tips", "content-creation", "company", "person"
}

# Valid page types
VALID_TYPES = {"entity", "concept", "comparison", "query", "summary", "config", "troubleshooting"}

class WikiLint:
    def __init__(self):
        self.issues = defaultdict(list)
        self.all_pages = {}  # slug -> file_path
        self.all_wikilinks = defaultdict(set)  # page -> set of linked pages
        self.incoming_links = defaultdict(set)  # page -> set of pages linking to it
        
    def slugify(self, filename):
        """Convert filename to slug (without .md)"""
        return filename.replace(".md", "")
    
    def get_all_wiki_pages(self):
        """Scan all wiki directories and collect pages"""
        for dir_name in WIKI_DIRS:
            dir_path = JOURNAL_ROOT / dir_name
            if dir_path.exists():
                for f in dir_path.glob("*.md"):
                    slug = self.slugify(f.name)
                    self.all_pages[slug] = f
        
        # Also include index.md and other root files
        for f in JOURNAL_ROOT.glob("*.md"):
            if f.name not in ["log.md", "SCHEMA.md"]:
                slug = self.slugify(f.name)
                self.all_pages[slug] = f
    
    def parse_frontmatter(self, file_path):
        """Parse YAML frontmatter from a markdown file"""
        try:
            content = file_path.read_text(encoding='utf-8')
            if not content.startswith("---"):
                return None, content
            
            # Find the end of frontmatter
            match = re.match(r'^---\n(.*?)\n---\n(.*)', content, re.DOTALL)
            if not match:
                return None, content
            
            fm_text = match.group(1)
            body = match.group(2)
            
            try:
                fm = yaml.safe_load(fm_text)
                return fm, body
            except yaml.YAMLError:
                return None, content
        except Exception as e:
            return None, ""
    
    def extract_wikilinks(self, content):
        """Extract all [[wikilinks]] from content"""
        # Match [[link]] or [[link|text]]
        pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
        links = re.findall(pattern, content)
        return links
    
    def analyze_all_pages(self):
        """Analyze all pages for issues"""
        for slug, file_path in self.all_pages.items():
            # Skip log.md
            if file_path.name == "log.md":
                continue
                
            content = file_path.read_text(encoding='utf-8', errors='ignore')
            lines = content.split('\n')
            fm, body = self.parse_frontmatter(file_path)
            
            # Check 1: Missing frontmatter
            if fm is None and file_path.name != "index.md":
                self.issues["missing_frontmatter"].append({
                    "file": str(file_path),
                    "severity": "高",
                    "suggestion": "添加 YAML frontmatter（title, created, updated, type, tags）"
                })
            else:
                # Check 2: Tags not in SCHEMA
                if fm and "tags" in fm:
                    for tag in fm.get("tags", []):
                        if tag not in VALID_TAGS:
                            self.issues["invalid_tag"].append({
                                "file": str(file_path),
                                "tag": tag,
                                "severity": "中",
                                "suggestion": f"标签 '{tag}' 不在 SCHEMA 分类法中，需要添加到 SCHEMA.md 或移除"
                            })
                
                # Check 3: Unreviewed pages
                if fm and fm.get("reviewed") == False:
                    self.issues["unreviewed"].append({
                        "file": str(file_path),
                        "severity": "低",
                        "suggestion": "审查页面后将 reviewed 改为 true，并填写 reviewed_at"
                    })
                
                # Check 4: Invalid type
                if fm and "type" in fm and fm["type"] not in VALID_TYPES:
                    self.issues["invalid_type"].append({
                        "file": str(file_path),
                        "type": fm["type"],
                        "severity": "中",
                        "suggestion": f"类型 '{fm['type']}' 无效，应为: {', '.join(VALID_TYPES)}"
                    })
            
            # Check 5: Page over 200 lines
            if len(lines) > 200:
                self.issues["too_long"].append({
                    "file": str(file_path),
                    "lines": len(lines),
                    "severity": "中",
                    "suggestion": f"页面有 {len(lines)} 行，建议拆分为多个子主题页面"
                })
            
            # Check 6: Too few wikilinks
            wikilinks = self.extract_wikilinks(content)
            # Filter out external links or special links
            internal_links = [l for l in wikilinks if not l.startswith("http")]
            
            if len(internal_links) < 2 and file_path.name not in ["index.md", "SCHEMA.md"]:
                self.issues["few_wikilinks"].append({
                    "file": str(file_path),
                    "count": len(internal_links),
                    "links": internal_links,
                    "severity": "中",
                    "suggestion": f"页面只有 {len(internal_links)} 个 wikilinks，建议至少添加 2 个内部链接"
                })
            
            # Track outgoing links for broken link detection
            self.all_wikilinks[slug] = set(internal_links)
            
            # Track incoming links
            for link in internal_links:
                self.incoming_links[link].add(slug)
    
    def check_orphaned_pages(self):
        """Find pages with no incoming links (except index.md)"""
        for slug, file_path in self.all_pages.items():
            if file_path.name in ["index.md", "SCHEMA.md", "log.md"]:
                continue
            
            # Check if any page links to this one
            incoming = self.incoming_links.get(slug, set())
            
            # Also check if it's listed in index.md
            index_content = INDEX_FILE.read_text(encoding='utf-8') if INDEX_FILE.exists() else ""
            in_index = slug in index_content
            
            if len(incoming) == 0 and not in_index:
                self.issues["orphaned"].append({
                    "file": str(file_path),
                    "slug": slug,
                    "severity": "高",
                    "suggestion": "页面无入链且未在 index.md 中列出，需要添加链接或加入索引"
                })
    
    def check_broken_links(self):
        """Find wikilinks pointing to non-existent pages"""
        for slug, links in self.all_wikilinks.items():
            for link in links:
                # Skip special links
                if link.startswith("#") or link.startswith("http"):
                    continue
                
                # Check if target page exists
                if link not in self.all_pages:
                    file_path = self.all_pages.get(slug)
                    self.issues["broken_link"].append({
                        "file": str(file_path),
                        "broken_link": link,
                        "severity": "高",
                        "suggestion": f"链接 [[{link}]] 指向不存在的页面，需要创建该页面或移除链接"
                    })
    
    def auto_fix_index(self):
        """Auto-fix: Update index.md with missing pages"""
        if not INDEX_FILE.exists():
            return False
        
        index_content = INDEX_FILE.read_text(encoding='utf-8')
        missing_pages = []
        
        for slug, file_path in self.all_pages.items():
            if file_path.name in ["index.md", "SCHEMA.md", "log.md"]:
                continue
            if file_path.parent.name not in WIKI_DIRS:
                continue
            if slug not in index_content:
                missing_pages.append((slug, file_path))
        
        if not missing_pages:
            return False
        
        # Try to add missing pages to index.md
        # Find the appropriate section based on directory
        additions = defaultdict(list)
        for slug, file_path in missing_pages:
            dir_name = file_path.parent.name
            additions[dir_name].append(slug)
        
        print(f"Auto-fix: Found {len(missing_pages)} pages missing from index.md")
        print(f"  Pages to add: {additions}")
        
        # For now, just report - manual fix needed for proper index structure
        return True
    
    def generate_report(self):
        """Generate the lint report"""
        report = []
        report.append("# Wiki Health Check Report")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append("")
        
        total_issues = sum(len(v) for v in self.issues.values())
        report.append(f"## Summary")
        report.append(f"Total pages scanned: {len(self.all_pages)}")
        report.append(f"Total issues found: {total_issues}")
        report.append("")
        
        # Sort issues by severity
        severity_order = {"高": 0, "中": 1, "低": 2}
        
        issue_categories = [
            ("orphaned", "孤立页面（无入链）"),
            ("broken_link", "损坏的 wikilinks"),
            ("missing_frontmatter", "缺少 frontmatter"),
            ("too_long", "超过 200 行的页面"),
            ("few_wikilinks", "少于 2 个 wikilinks"),
            ("invalid_tag", "标签不在 SCHEMA 分类法中"),
            ("unreviewed", "未审查页面"),
            ("invalid_type", "无效的页面类型"),
        ]
        
        for issue_key, issue_name in issue_categories:
            issues = self.issues.get(issue_key, [])
            if issues:
                report.append(f"## {issue_name} ({len(issues)} 个)")
                report.append("")
                for issue in sorted(issues, key=lambda x: severity_order.get(x.get("severity", "低"), 3)):
                    report.append(f"### [{issue['severity']}] {issue['file']}")
                    if "tag" in issue:
                        report.append(f"- 问题标签: {issue['tag']}")
                    if "type" in issue:
                        report.append(f"- 无效类型: {issue['type']}")
                    if "lines" in issue:
                        report.append(f"- 行数: {issue['lines']}")
                    if "count" in issue:
                        report.append(f"- 链接数: {issue['count']}")
                        if issue.get("links"):
                            report.append(f"- 当前链接: {', '.join(issue['links'])}")
                    if "broken_link" in issue:
                        report.append(f"- 损坏链接: [[{issue['broken_link']}]]")
                    if "slug" in issue:
                        report.append(f"- Slug: {issue['slug']}")
                    report.append(f"- 建议: {issue['suggestion']}")
                    report.append("")
        
        if total_issues == 0:
            report.append("✅ 未发现任何问题！")
        
        return "\n".join(report)
    
    def append_to_log(self, report):
        """Append the report to log.md"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"\n\n---\n\n## Wiki Health Check - {timestamp}\n\n"
        log_entry += report.replace("# Wiki Health Check Report", "")
        
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_entry)
    
    def run(self):
        """Run the full lint check"""
        print("Starting wiki health check...")
        
        # Step 1: Collect all pages
        print("Scanning wiki pages...")
        self.get_all_wiki_pages()
        print(f"Found {len(self.all_pages)} pages")
        
        # Step 2: Analyze pages
        print("Analyzing pages...")
        self.analyze_all_pages()
        
        # Step 3: Check orphaned pages
        print("Checking for orphaned pages...")
        self.check_orphaned_pages()
        
        # Step 4: Check broken links
        print("Checking for broken links...")
        self.check_broken_links()
        
        # Step 5: Auto-fix if possible
        print("Attempting auto-fixes...")
        self.auto_fix_index()
        
        # Step 6: Generate report
        print("Generating report...")
        report = self.generate_report()
        
        # Step 7: Append to log
        print("Appending to log.md...")
        self.append_to_log(report)
        
        print("\n" + "="*60)
        print(report)
        print("="*60)
        print(f"\nReport appended to {LOG_FILE}")
        
        return report

if __name__ == "__main__":
    linter = WikiLint()
    linter.run()
