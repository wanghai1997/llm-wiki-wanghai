# Wiki Frontmatter 规范（ARS 兼容扩展）

> 本规范定义 Wiki 页面的 YAML Frontmatter 标准，向后兼容现有格式，新增 ARS 协同所需字段。

## 基础字段（所有页面必需）

```yaml
---
created: YYYY-MM-DD        # 创建日期
updated: YYYY-MM-DD        # 最后更新日期
tags: [tag1, tag2]         # 标签列表
status: evergreen|draft|stub|foundation  # 页面成熟度
---
```

## 知识质量字段（所有知识页必需）

```yaml
---
confidence: high|medium|low   # 基于来源数量和质量的可靠性评估
decay_category: slow|medium|fast  # 知识衰减速度
---
```

### confidence（置信度）

保守取值（宁低勿高）。

| 值 | 条件 |
|----|------|
| `high` | ≥3 个来源且含学术/书籍来源；或 ≥2 个高质量学术来源。多源交叉验证。 |
| `medium` | ≥1 个学术来源（论文/教材/正式出版物）；或 ≥2 个中等质量来源。 |
| `low` | 单一非学术来源（公众号文章/网页/未经验证的单一文档）。 |

### decay_category（衰减类别）

保守取值（默认更快衰减）。

| 值 | 条件 | 示例 |
|----|------|------|
| `slow` | 界定性/公理性/基础理论——知识长期稳定 | 数学定理、定义、基本概念、均衡理论、利益相关者元框架 |
| `medium` | 应用理论/实证研究/制度分析——知识逐步演化 | 实证文献、补偿机制、制度框架、政策设计 |
| `fast` | 案例/当前政策/市场数据/技术——知识快速变化 | 地方案例、碳汇交易、VEP2.0、当前事件、AI政策 |

**判断优先级**：先看页面是"定义/理论框架"（→slow）还是"案例/应用/工具"（→fast），中等程度取 medium。案例名/地名（丽水、韶关等）仅从标签和文件名匹配，不从正文引用匹配——防止理论页因提及案例而被误判为 fast。

## 扩展字段（按页面类型）

### 教材/书籍页（type: book）

```yaml
---
created: 2026-05-05
updated: 2026-05-05
sources:
  - "Author (Year), Title, Publisher"
tags: [tag1, tag2]
status: evergreen
citekey: AuthorYearTitle     # ARS: 引用键
authors: [Family, Given]    # ARS: 作者列表
year: 2026                  # ARS: 出版年
---
```

### 概念/主题页（type: concept, topic_guide）

现有格式已满足 adapter 需求。`sources` 字段会由 adapter 自动提取作者信息。

### 源文件页（type: source, in raw/archive/）

```yaml
---
title: "文档标题"
source: "原始 URL 或文件路径"
author: "作者"
published: YYYY-MM-DD       # ARS: 出版日期
created: YYYY-MM-DD
tags: [clippings, ...]
---
```
> 源文件页不需要 `status` 字段（在 archive 中，非活跃知识页）。

## Adapter 自动推断规则

| ARS 字段 | 推断来源 |
|----------|---------|
| `citation_key` | 相对路径（去掉 .md），如 `foundations/financial-economics/concepts/CAPM` |
| `title` | frontmatter.title > 正文 H1 > 文件名 |
| `type` | 路径：/books/→book, /concepts/→concept, /entities/→entity 等 |
| `year` | frontmatter.published > frontmatter.created 中的年份 |
| `authors` | 从 sources 列表中正则提取英文姓名模式 |
| `tags` | frontmatter.tags |

## 校验规则

| 校验项 | 适用页面类型 |
|--------|------------|
| 必须有 title（H1 或 frontmatter） | 所有非 meta 页面 |
| 必须有 tags | 知识页（concept/entity/topic/book/policy/case） |
| 必须有 status | 知识页 |
| 必须有 sources | concept/topic/book 页 |
| 必须有 confidence | 知识页（concept/entity/topic/book/policy/case） |
| 必须有 decay_category | 知识页（concept/entity/topic/book/policy/case） |
