---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, instrumental-variables, education, QOB, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# 义务教育法 IV

## 一句话定义

> **义务教育法 IV** = 利用美国的**义务教育法**（compulsory schooling laws）和**童工法**（child labor laws）作为工具变量——这些法律外生地迫使青少年接受更多教育，从而识别教育回报。

## 两个旗舰研究

| 研究 | 工具变量 | 核心创新 |
|------|---------|---------|
| **Angrist & [[Alan-Krueger\|Krueger]] (1991, *QJE*)** | **出生季度**（QOB）× 义务教育法年限 | QOB + 义务教育法交互 → 外生的受教育变异 |
| **Acemoglu & [[Joshua-Angrist\|Angrist]] (2001, *NBER Macro Annual*)** | **州童工法差异**（14 岁时所在州的法律要求） | 不同州的不同法律 → 跨州外生变异 |

## QOB（Quarter of Birth）IV 的逻辑

美国义务教育法通常规定：学生必须在校直到满 **16/17 岁**。但不同出生季度的孩子：
- **Q1（1-3 月出生）**：在学年年初满法定年龄 → 可以最早合法辍学 → **最少**受教育年限
- **Q4（10-12 月出生）**：在学年末满法定年龄 → 必须等更久 → **最多**受教育年限

→ 出生季度与受教育年限**系统性相关**——这是自然产生的随机变异（出生季度是随机的）。

### QOB 的第一阶段

$$\text{Schooling}_i = \pi_0 + \pi_1 \text{QOB}_i + \mathbf{X}_i'\pi_2 + \nu_i$$

- 男性、1930-1939 年出生队列：Q4 出生的人比 Q1 出生的人平均多 ~0.1 年教育
- $\pi_1$ 虽小但统计显著——F 统计量需检查（这是弱 IV 的经典案例）

### QOB 的简约式

$$\ln \text{Wage}_i = \rho_0 + \rho_1 \text{QOB}_i + \mathbf{X}_i'\rho_2 + \varepsilon_i$$

- Q4 出生的人收入略高——但 $\rho_1$ 不大

### IV 估计

$$\lambda = \frac{\rho_1}{\pi_1} \approx 0.07-0.10$$

→ 教育回报 ~7-10%/年（与 OLS ~11% 接近，差异在统计误差范围内）

## 方法论贡献

- **QOB 是计量学最著名的工具之一**：因其"随机性"易于直观理解（无人能选择出生季度）——尽管弱工具变量问题随后引发大量争论
- **"出生季度 ≈ 随机分配教育"的逻辑**：简化了 IV 三个条件的辩护——独立性 √、第一阶段 √（虽弱）、排他性需辩护（QOB 是否通过健康/早产影响收入？）

## 反面论点与数据空白

- **弱工具变量问题**：QOB 的第一阶段非常弱（Partial $R^2$ ~0.0001）→ Bound-Jaeger-Baker (1995) 证明在这种情况下 2SLS 可能有严重偏差。Angrist-Krueger 使用多种 QOB 分组（30 个出生季度 × 出生年份交互）——当工具数接近样本量时，2SLS 倾向于 OLS。
- **QOB 的排他性是否成立？**：早产/冬季婴儿的健康差异可能直接影响收入——如果排他性约束不成立，QOB IV 有偏。
- **仅对"辍学边缘"的 LATE**：QOB IV 仅识别那些因为出生季度被迫多读书的学生的效应——对从不辍学或坚决辍学的人无信息。
- **时代局限性**：Angrist-Krueger 使用 1930-1939 年出生的 1980 年人口普查数据——当时高中辍学率远高于现在（更少的学生在"辍学边缘"）→ 当代的 QOB LATE 可能更弱。

## 相关页

- [[工具变量IV]] / [[局部平均处理效应LATE]] / [[第一阶段与简约式]]
- [[教育回报率-因果估计]] / [[Mincer方程]]
- [[Alan-Krueger]] / [[Joshua-Angrist]]
- [[Mastering-Metrics]]
