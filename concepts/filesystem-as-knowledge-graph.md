---
title: Filesystem as Knowledge Graph
created: 2026-04-15
updated: 2026-04-15
type: concept
tags: [architecture, graph, knowledge-base]
sources: [raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md]
reviewed: false
confidence: high
confidence_reason: SMF 核心架构创新
---

## 编译知识

**核心洞察**：POSIX symlink 是零成本的关系指针，文件系统本身就是知识图谱。

### Symlink 作为图谱边

```bash
# 创建类型化关系
ln -s /memory/actors/bob/ /memory/actors/alice/related/collaborated_with/bob
ln -s /memory/decisions/meeting-123/ /memory/actors/alice/related/decided_at/meeting-123

# 遍历图谱（无需图数据库）
ls -la /memory/actors/alice/related/
readlink /memory/actors/alice/related/collaborated_with/bob
```

**优势**：
- 原子操作（无部分状态，无写入冲突）
- 悬空 symlink 是特性而非 bug（readlink 返回目标路径，无论目标是否存在）
- 内核级操作，百万级条目无性能问题
- 任何人类或代理都可用标准工具检查

### 与知识库方案对比

| 系统 | 关系存储位置 | 查询方式 |
|------|-------------|----------|
| Karpathy Wiki | 无显式关系 | LLM 阅读索引文件 |
| GBrain | PostgreSQL | SQL + 向量搜索 |
| Obsidian | Markdown 文本引用 | 无法程序化查询 |
| **SMF** | **POSIX symlink** | **ls, readlink** |

### 可扩展性

**2026-04-07 Amazon S3 Files 更新**：
- S3 原生支持 POSIX 文件系统语义
- 通过 NFS v4.2 挂载
- POSIX 权限保存为 S3 对象元数据

**结果**：SMF 图谱可运行在 S3 上
- 几乎无限存储
- $0.023/GB-月
- 11 个 9 的持久性
- 最多 25,000 计算资源并发访问

### 访问控制

Unix 文件权限原生应用到每个实体目录和 symlink：

```bash
# 设置敏感度级别
chmod 750 /memory/actors/alice/          # 团队可读
chmod 700 /memory/vcos/confidential-123/ # 仅所有者
setfacl -m u:bob:rx /memory/topics/strategy/  # ACL
```

**4 个敏感度级别**：
- public
- internal
- confidential
- restricted

### 图谱遍历模式

```bash
# 理解决策上下文
ls /memory/decisions/switch-to-postgres/related/
# → 立即看到：相关演员、理由、讨论会议、履行的承诺

# 多跳遍历
find /memory/actors/alice/related/ -type l -exec readlink {} \;

# 查找所有合作者
ls -1 /memory/actors/*/related/collaborated_with/
```

### 为什么这是创新

据 SMF 作者所知，这是**首次将 POSIX symlink 用于基于 POSIX 的代理记忆**：
- Karpathy Wiki：条目间无文件系统级关系
- GBrain：关系在 PostgreSQL 中，不在文件系统
- Obsidian：wikilinks 是文本引用，不是文件系统指针

---

## 时间线

- 2026-04-15: 初始创建，来源 [[raw/articles/ashwin-gopinath-smf-skeleton-of-remembering-2026-04-14.md]]
- 2026-04-15: 关联 [[smf-semantic-memory-framework]], [[knowledge-base-vs-memory]]
