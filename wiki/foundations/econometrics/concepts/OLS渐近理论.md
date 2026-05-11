---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, OLS, asymptotics, consistency, foundations, Wooldridge, 技术]
confidence: medium
decay_category: slow
status: foundation
---

# OLS 渐近理论

## 一句话定义

> **OLS 渐近理论** = 当样本量 $n \to \infty$ 时，OLS 估计量在**无需正态性**和**无需严格同方差**的条件下，仍是**一致的**和**渐近正态的**——这是大样本推断的基础。

## 为什么需要渐近理论

Gauss-Markov 定理和 t/F 检验依赖：
1. MLR.5（同方差）→ 方差公式有效
2. MLR.6（正态性）→ 精确的 t/F 分布

→ **现实中这两个假设几乎永远被违反**。渐近理论提供了更弱假设下的推断框架。

## 一致性 (Consistency)

在 MLR.1-4（无需同方差，无需正态性）下：

$$\text{plim } \hat{\beta}_j = \beta_j \quad \text{（$n \to \infty$）}$$

- **无偏 ≠ 一致**：一个估计量可以在小样本下无偏但不一致，也可以在小样本下有偏但一致
- OLS 在 MLR.1-4 下：既无偏又一致

### 不一致性 (Inconsistency)

当 MLR.4（零条件均值）被违反时：

$$\text{plim } \hat{\beta}_1 = \beta_1 + \frac{\text{Cov}(x_1, u)}{\text{Var}(x_1)}$$

→ 第二项是**渐近偏差**——即使 $n \to \infty$，OLS 也不趋近 $\beta_1$。这就是为什么遗漏变量偏差和联立性偏差在大样本下**不会消失**。

## 渐近正态性

在 MLR.1-5（不加正态性）下：

$$\frac{\hat{\beta}_j - \beta_j}{\text{se}(\hat{\beta}_j)} \xrightarrow{d} N(0, 1)$$

- 即使误差 $u$ 不是正态分布，$\hat{\beta}_j$ 的抽样分布在 $n$ 足够大时趋近正态——**CLT 在起作用**
- 这是为什么大样本下"t 检验 ≈ z 检验"——自由度足够大时 t 分布趋近正态

## 渐近有效性

在 MLR.1-5 下，OLS 在所有**一致的、渐近正态的**估计量中，具有最小的渐近方差——OLS 在大样本下也是"最优"的（在适当定义的类别中）。

## 从有限样本推断到大样本推断

| 假设集 | 推断类型 | 依赖于 |
|--------|---------|--------|
| MLR.1-6 | 精确的 t/F 分布 | 正态性 |
| MLR.1-5 | 渐近正态 | 同方差 + CLT |
| MLR.1-4 + 异方差稳健 SE | 渐近正态（异方差稳健） | CLT + 异方差校正 |

→ **实践中最常用的是第 3 行**：OLS + 异方差稳健标准误 + 大样本正态近似。

## 反面论点与数据空白

- **"n 多大才算大？"**没有统一答案——取决于误差分布的形状和回归变量的行为。高度偏态数据（如收入）比对称数据需要更大的 $n$。
- **聚类数据中的渐近理论**：如果有聚类（如学生→学校），需要聚类数（非观测值数）→∞ ——这在大面板（少量聚类）中是有问题的。

## 相关页

- [[OLS估计量的统计性质]] / [[OLS推断-t检验与F检验]]
- [[大数定律与中心极限定理-应用]]（MM）— CLT / LLN 的因果框架
- [[Introductory-Econometrics-Wooldridge-8e]]
