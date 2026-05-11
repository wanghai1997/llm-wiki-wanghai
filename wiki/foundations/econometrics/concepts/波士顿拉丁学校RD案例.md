---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, regression-discontinuity, case-study, education, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# 波士顿拉丁学校 RD 案例

## 一句话定义

> **Boston Latin School RD** = Abdulkadiroglu, [[Joshua-Angrist|Angrist]] & Pathak (2014, *Econometrica*) 利用波士顿精英公立考试学校的**入学考试分数截断**，研究"精英学校是否提高学生成绩"。

## 研究设计

- **Running Variable**：入学考试加权分数（ISEE + GPA）
- **Cutoff**：每年的录取分数线
- **处理**：被 Boston Latin School (BLS) 录取——**模糊 RD**（过线学生更可能入学但非 100%）
- **结果**：7-8 年级 MCAS 数学和英语标准化考试成绩

## 为什么是模糊 RD

并非所有过线的学生都选择入学 BLS（有些去私立学校、有些去其他公立学校），也并非所有未过线的学生都不入学——因此过线 ≠ 确定性的处理接受。处理概率在断点处**跳跃但不到 1**。

→ 用"是否过线"作为**工具变量**来识别 BLS 入学的因果效应——本质上是一个**IV 策略**，但 instrument 来自 RD 的断点。

## 核心发现

| 发现 | 方向 |
|------|------|
| BLS 入学 → MCAS 数学成绩 | → **无显著效应** |
| BLS 入学 → MCAS 英语成绩 | → **无显著效应** |
| BLS 入学 → 同伴质量 | ↑（显著——同学的平均成绩更高） |
| BLS 入学 → 班级排名 | ↓（——学生在更有竞争力的群体中排名下降） |

**结论**：精英学校**确实提高了同伴质量**（你的同学更优秀），但**没有提高学生的标准化考试成绩**——这对"精英教育"的假设提出了挑战。

## 方法论贡献

- **模糊 RD 的教科书级应用**：first stage = 过线对入学概率的效应；reduced form = 过线对成绩的效应；IV ratio = causal effect
- **同伴效应的内生性**：传统教育生产函数中"好同学 → 好成绩"的假设可能是选择偏差——当同学质量通过 RD 被外生改变时，成绩不随之提升
- **安慰剂检验**：检查其他变量在断点处是否连续（基线成绩、人口特征等）

## 反面论点与数据空白

- **仅对 BLS 有效**：结论对不同类型的精英学校（如纽约 Stuyvesant、北京四中、法国 Grandes Écoles）未必适用——BLS 是波士顿特定制度下的产物。
- **短期效应 vs 长期效应**：仅追踪到 7-8 年级——精英学校的长远效应（大学录取、收入、社交网络）可能需要更长时间才能显现。
- **精英学校的其他收益**：标准考试成绩不是唯一的结果——非认知技能、公民参与、校友网络等可能更重要但更难测度。
- **弱工具变量问题**：如果过线概率的跳跃很小（接近断点处样本少），IV 估计可能不稳定。

## 相关页

- [[断点回归RD]] / [[工具变量IV]]
- [[Dale-Krueger大学溢价研究]] — 同样挑战"精英教育溢价"假设
- [[Joshua-Angrist]]
- [[Mastering-Metrics]]
