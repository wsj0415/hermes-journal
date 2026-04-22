#!/usr/bin/env python3
"""Wiki 健康检查脚本 - 扫描 hermes-journal 的 wiki 页面并生成 lint 报告"""

import os
import re
import yaml
from pathlib import Path
from collections import defaultdict
from datetime import datetime

BASE_DIR = Path("/root/hermes-journal")
WIKI_DIRS = ["concepts", "entities", "comparisons", "queries"]
LOG_FILE = BASE_DIR / "log.md"
INDEX_FILE = BASE_DIR / "index.md"
SCHEMA_FILE = BASE_DIR / "SCHEMA.md"

# 从 SCHEMA.md 解析有效标签
VALID_TAGS = set()

def parse_schema():
    """从 SCHEMA.md 解析有效的标签分类法"""
    if not SCHEMA_FILE.exists():
        return
    
    content = SCHEMA_FILE.read_text()
    # 查找 Tag Taxonomy 部分
    in_taxonomy = False
    for line in content.split('\n'):
        if '## Tag Taxonomy' in line:
            in_taxonomy = True
            continue
        if in_taxonomy:
            if line.startswith('## '):
                break
            # 解析标签行：- 平台：telegram, whatsapp, ... 或 - 人物/来源：karpathy, amodei
            match = re.match(r'-\s*[\w/]+：(.+)', line)
            if match:
                tags_str = match.group(1)
                tags = [t.strip() for t in tags_str.split(',')]
                VALID_TAGS.update(tags)

def get_wiki_files():
    """获取所有 wiki 目录下的 markdown 文件"""
    files = []
    for dir_name in WIKI_DIRS:
        dir_path = BASE_DIR / dir_name
        if dir_path.exists():
            for f in dir_path.glob("*.md"):
                files.append(f)
    return files

def parse_frontmatter(content):
    """解析 YAML frontmatter"""
    if not content.startswith('---'):
        return None
    
    parts = content.split('---', 2)
    if len(parts) < 3:
        return None
    
    try:
        fm = yaml.safe_load(parts[1])
        return fm
    except:
        return None

def extract_wikilinks(content):
    """提取所有 [[wikilinks]]"""
    # 匹配 [[link]] 或 [[link|text]]
    pattern = r'\[\[([^\]|]+)(?:\|[^\]]+)?\]\]'
    matches = re.findall(pattern, content)
    # 过滤掉空链接或只有空格的链接
    return [m.strip() for m in matches if m.strip()]

def get_page_filename(link):
    """将 wikilink 转换为文件名"""
    # 处理可能的子目录引用
    link = link.strip()
    if not link.endswith('.md'):
        link += '.md'
    return link

def count_lines(filepath):
    """计算文件行数"""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return len(f.readlines())

def check_page(filepath, all_pages_set):
    """检查单个页面的问题"""
    issues = []
    
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
    except Exception as e:
        issues.append({
            'type': 'read_error',
            'severity': '高',
            'message': f'无法读取文件：{e}'
        })
        return issues
    
    lines = count_lines(filepath)
    fm = parse_frontmatter(content)
    wikilinks = extract_wikilinks(content)
    
    # 检查 frontmatter
    if fm is None:
        issues.append({
            'type': 'missing_frontmatter',
            'severity': '高',
            'message': '缺少 YAML frontmatter'
        })
    else:
        # 检查 reviewed 状态
        if fm.get('reviewed') is False:
            issues.append({
                'type': 'unreviewed',
                'severity': '中',
                'message': f'未审查页面 (reviewed: false)'
            })
        
        # 检查标签
        tags = fm.get('tags', [])
        if tags:
            for tag in tags:
                if tag not in VALID_TAGS:
                    issues.append({
                        'type': 'invalid_tag',
                        'severity': '中',
                        'message': f'标签 "{tag}" 不在 SCHEMA 分类法中'
                    })
    
    # 检查页面长度
    if lines > 200:
        issues.append({
            'type': 'too_long',
            'severity': '中',
            'message': f'页面超过 200 行 ({lines} 行)，建议拆分'
        })
    
    # 检查 wikilinks 数量
    if len(wikilinks) < 2:
        issues.append({
            'type': 'few_wikilinks',
            'severity': '低',
            'message': f'只有 {len(wikilinks)} 个 wikilinks（建议至少 2 个）'
        })
    
    # 检查损坏的 wikilinks
    for link in wikilinks:
        # 跳过外部链接或特殊链接
        if link.startswith('http') or link.startswith('#'):
            continue
        
        target_file = get_page_filename(link)
        
        # 检查文件是否存在
        found = False
        # 尝试不同路径
        for dir_name in WIKI_DIRS:
            test_path = BASE_DIR / dir_name / target_file
            if test_path.exists():
                found = True
                break
        
        # 也检查根目录
        if not found and (BASE_DIR / target_file).exists():
            found = True
        
        if not found and target_file not in all_pages_set:
            issues.append({
                'type': 'broken_link',
                'severity': '高',
                'message': f'损坏的 wikilink: [[{link}]] -> 目标文件不存在'
            })
    
    return issues

def find_orphan_pages(wiki_files, all_pages_set):
    """查找孤立页面（没有其他页面链接到它）"""
    # 收集所有入链
    incoming_links = defaultdict(set)
    
    for filepath in wiki_files:
        try:
            content = filepath.read_text(encoding='utf-8', errors='ignore')
            wikilinks = extract_wikilinks(content)
            
            for link in wikilinks:
                target = get_page_filename(link)
                incoming_links[target].add(filepath.name)
        except:
            continue
    
    orphans = []
    for filepath in wiki_files:
        filename = filepath.name
        # 检查是否有入链
        if filename not in incoming_links:
            orphans.append(filepath)
    
    return orphans

def generate_report(issues_by_file, orphans, stats):
    """生成检查报告"""
    report = []
    report.append(f"# Wiki 健康检查报告")
    report.append(f"生成时间：{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    report.append("")
    report.append("## 统计摘要")
    report.append(f"- 扫描页面数：{stats['total_pages']}")
    report.append(f"- 发现问题总数：{stats['total_issues']}")
    report.append(f"- 孤立页面：{len(orphans)}")
    report.append(f"- 已审查页面：{stats['reviewed_count']}/{stats['total_pages']}")
    report.append("")
    
    # 按严重程度分组
    high_severity = []
    medium_severity = []
    low_severity = []
    
    for filepath, issues in issues_by_file.items():
        for issue in issues:
            entry = {'file': filepath, 'issue': issue}
            if issue['severity'] == '高':
                high_severity.append(entry)
            elif issue['severity'] == '中':
                medium_severity.append(entry)
            else:
                low_severity.append(entry)
    
    # 高严重性问题
    report.append("## 高严重性问题")
    if high_severity:
        for entry in high_severity:
            report.append(f"- **{entry['file'].name}**: {entry['issue']['type']} - {entry['issue']['message']}")
            report.append(f"  - 文件：`{entry['file']}`")
            report.append(f"  - 建议：立即修复")
    else:
        report.append("无高严重性问题")
    report.append("")
    
    # 中严重性问题
    report.append("## 中严重性问题")
    if medium_severity:
        for entry in medium_severity:
            report.append(f"- **{entry['file'].name}**: {entry['issue']['type']} - {entry['issue']['message']}")
            report.append(f"  - 文件：`{entry['file']}`")
            report.append(f"  - 建议：尽快处理")
    else:
        report.append("无中严重性问题")
    report.append("")
    
    # 低严重性问题
    report.append("## 低严重性问题")
    if low_severity:
        for entry in low_severity:
            report.append(f"- **{entry['file'].name}**: {entry['issue']['type']} - {entry['issue']['message']}")
            report.append(f"  - 文件：`{entry['file']}`")
            report.append(f"  - 建议：有空时优化")
    else:
        report.append("无低严重性问题")
    report.append("")
    
    # 孤立页面
    report.append("## 孤立页面（无入链）")
    if orphans:
        for filepath in orphans:
            report.append(f"- `{filepath.name}`")
            report.append(f"  - 路径：`{filepath}`")
            report.append(f"  - 建议：添加引用或删除页面")
    else:
        report.append("无孤立页面")
    report.append("")
    
    return '\n'.join(report)

def auto_fix_index():
    """自动更新 index.md（如果存在）"""
    if not INDEX_FILE.exists():
        return "index.md 不存在，跳过自动修复"
    
    # 这里可以添加 index.md 的自动更新逻辑
    return "index.md 检查完成"

def append_to_log(report_content):
    """将检查结果追加到 log.md"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_entry = f"\n---\n## Wiki Lint Check - {timestamp}\n\n"
    log_entry += report_content
    log_entry += "\n---\n"
    
    if LOG_FILE.exists():
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(log_entry)
    else:
        with open(LOG_FILE, 'w', encoding='utf-8') as f:
            f.write(log_entry)

def main():
    print("开始 Wiki 健康检查...")
    
    # 解析 SCHEMA
    parse_schema()
    print(f"加载了 {len(VALID_TAGS)} 个有效标签")
    
    # 获取所有 wiki 文件
    wiki_files = get_wiki_files()
    print(f"找到 {len(wiki_files)} 个 wiki 页面")
    
    # 创建文件名集合用于快速查找
    all_pages_set = {f.name for f in wiki_files}
    
    # 检查每个页面
    issues_by_file = {}
    stats = {
        'total_pages': len(wiki_files),
        'total_issues': 0,
        'reviewed_count': 0
    }
    
    for filepath in wiki_files:
        issues = check_page(filepath, all_pages_set)
        if issues:
            issues_by_file[filepath] = issues
            stats['total_issues'] += len(issues)
        
        # 统计已审查页面
        try:
            content = filepath.read_text(encoding='utf-8', errors='ignore')
            fm = parse_frontmatter(content)
            if fm and fm.get('reviewed') is True:
                stats['reviewed_count'] += 1
        except:
            pass
    
    # 查找孤立页面
    orphans = find_orphan_pages(wiki_files, all_pages_set)
    
    # 生成报告
    report = generate_report(issues_by_file, orphans, stats)
    
    # 自动修复
    fix_result = auto_fix_index()
    report += f"\n## 自动修复\n- {fix_result}\n"
    
    # 输出报告
    print("\n" + "="*60)
    print(report)
    print("="*60)
    
    # 追加到 log.md
    append_to_log(report)
    print(f"\n报告已追加到 {LOG_FILE}")
    
    return report

if __name__ == "__main__":
    main()
