---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, regression-discontinuity, causal-inference, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# 断点回归 RD

## 一句话定义

> **断点回归** = 利用制度或规则在某个精确的**截断点（cutoff）**处不连续地改变处理概率——在断点附近，处理分配"近似随机"，从而识别**局部因果效应**。

## 直觉

许多制度和规则包含刚性的截断：
- 21 岁生日 → 合法饮酒（精确到天）
- 考试分数 ≥ 分数线 → 录取
- 收入 ≤ 贫困线 → 获得补贴

在截断点**无限窄**的邻域内，刚好在截断点之上和之下的人在**所有其他方面几乎完全相同**——只有处理状态不同。断点附近于是成为一个"局部随机实验"。

## 精确 RD vs 模糊 RD

| 类型 | 截断点处的处理变化 | 识别 |
|------|-------------------|------|
| **Sharp RD**（精确） | 0 → 1（完全跳变） | 断点处的 ATE |
| **Fuzzy RD**（模糊） | 跳跃但非确定性 | 断点处的 [[局部平均处理效应LATE\|LATE]]（需 IV） |

[[MLDA饮酒年龄RD案例|MLDA 饮酒年龄]] 是精确 RD——21 岁生日那天，合法饮酒从 0 变为 1（确定性的）。

[[波士顿拉丁学校RD案例|波士顿拉丁学校]] 是模糊 RD——过分数线的学生更可能入学但非 100%（有学生放弃入学）。

## 关键假设

1. **断点不可操纵**：个体不能精确控制 running variable 在截断哪一侧
2. **连续性**：除处理外，所有结果和特征在截断处应**连续变化**（无跳跃）

这两个假设共同确保：断点附近的"处理-对照"比较识别因果效应。

## 在 Mastering 'Metrics 中的位置

Ch 4 介绍了两个旗舰案例：
- [[MLDA饮酒年龄RD案例|MLDA 饮酒年龄]]：21 岁生日前后死亡率比较
- [[波士顿拉丁学校RD案例|波士顿拉丁学校]]：考试分数线前后学业表现比较

## 反面论点与数据空白

- **断点操纵**：如果个体能精确控制 on which side of the cutoff they fall——如补考刚好过线——断点不再"随机"（McCrary 2008 密度检验是对此的标准诊断）。
- **带宽选择的任意性**：RD 的估计对"断点多远算近"高度敏感——不同带宽可能得出不同结论。
- **仅识别局部效应**：RD 只估计**断点处**的因果效应——对远离断点的个体无信息。MLDA 的效应仅对"刚好 21 岁"有效——不能推广到 25 岁或 35 岁。
- **外部有效性受限**：RD 估计的局部性意味着不同的 cutoff（不同制度/不同人群）的效应可能完全不同。
- **高次多项式的风险**：用高次多项式拟合断点两侧的趋势可能导致过度拟合和误导性结论（Gelman-Imbens 2019 建议用局部线性 + 小带宽）。

## 相关页

- [[MLDA饮酒年龄RD案例]] / [[波士顿拉丁学校RD案例]]
- [[Thistlethwaite-Campbell-RD]] / [[运行变量与带宽选择]]
- [[Donald-Campbell]]
- [[Mastering-Metrics]]
