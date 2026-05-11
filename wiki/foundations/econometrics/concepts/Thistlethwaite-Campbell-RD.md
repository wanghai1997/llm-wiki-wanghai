---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, regression-discontinuity, history, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Thistlethwaite-Campbell RD（原始论文）

## 一句话定义

> **Thistlethwaite & Campbell (1960)** = 断点回归设计的**原始论文**——用 National Merit Scholarship 表彰证书的考试截断，研究"获奖是否增强学生攻读研究生的意愿"。

## 研究背景

美国 National Merit Scholarship 竞赛中，成绩超过某一分数线的学生获得"表彰证书"（Certificate of Merit），刚过线和刚未过线的学生差异仅在于是否获得这个荣誉。

## 研究设计

- **Running Variable**：PSAT 考试成绩
- **Cutoff**：表彰证书的分数线
- **处理**：获得表彰证书
- **结果**：(I) 计划读 3 年以上研究生；(J) 计划成为大学教师或科研人员

## 核心发现

在截断点处：
- 计划读研的比例**显著跳跃**（约 +10 个百分点）
- 计划成为大学教师/科研人员的比例**显著跳跃**

结论：表彰证书本身（而非获奖者的先天能力差异）增加了学术追求意愿。

## 方法论地位

这是历史上第一篇**正式命名并论证"回归-断点分析"**的论文。原文中的 RD 图示（Figure 3 in original）被 Mastering 'Metrics 作为 Figure 4.10 重现——两条 discontinuous 的曲线是 RD 方法的视觉原型。

Mastering 'Metrics 评价：这篇论文**超前于时代至少 30 年**——直到 1990 年代末，RD 才在经济学中获得广泛认可和应用（Hahn-Todd-Van der Klaauw 2001 的形式化论文是关键转折点）。

## 反面论点与数据空白

- **心理效应 vs 信号效应**：获奖可能只是改变了学生的自我认知（"我是优秀的"），而非释放了任何外部信号（大学招生官本就能看到实际分数）——RD 不能区分这两种机制。
- **带宽极宽**：原始论文使用所有数据点而非断点附近的小邻域——今天的 RD 方法论（局部线性 + 小带宽）会更精确但可能改变结论方向。

## 相关页

- [[断点回归RD]] / [[Donald-Campbell]]
- [[Mastering-Metrics]]
