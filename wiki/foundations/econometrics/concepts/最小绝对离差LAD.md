---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, LAD, robust-estimation, median-regression, foundations, Wooldridge, 技术]
confidence: medium
decay_category: medium
status: foundation
---

# 最小绝对离差 LAD

## 一句话定义

> **最小绝对离差 (LAD)** = 不最小化残差平方和（OLS），而是最小化残差的**绝对值之和**——估计的是**条件中位数**而非条件均值——对离群值**高度稳健**。

## LAD vs OLS

| | OLS | LAD |
|---|---|---|
| 最小化 | $\sum (y_i - \mathbf{x}_i'\boldsymbol{\beta})^2$ | $\sum |y_i - \mathbf{x}_i'\boldsymbol{\beta}|$ |
| 估计的是 | $E(y | x)$（条件均值） | $\text{Median}(y | x)$（条件中位数） |
| 对离群值的敏感度 | 高（平方放大极端残差） | 低（线性惩罚） |
| 效率（正态误差下） | 最优 | ~64% 效率 |
| 效率（厚尾误差下） | 差 | 可能比 OLS 更好 |
| 解析解 | 有（闭式公式） | 无（需线性规划） |

## LAD 的应用场景

- 因变量有长尾分布（收入、财富、公司规模）
- 怀疑数据中存在测量错误的极值
- 中位数比均值更有政策意义（如"中位家庭的教育回报"）
- 稳健性检验：LAD 和 OLS 结果差异大 → 结果受离群值驱动

## LAD 的局限性

- **无解析解**：需要数值优化（单纯形法或线性规划）
- **小样本推断复杂**：OLS 的 t/F 检验公式不适用于 LAD——需要 bootstrap 或渐近近似
- **假设更强**：需要误差中位数 = 0（比 $E(u|x)=0$ 弱），但一致性要求误差分布在中位数处连续

## 分位数回归

LAD 是**分位数回归**的特殊情形（中位数回归, $\tau = 0.5$）。分位数回归可以在任意分位数处估计 $x$ 对 $y$ 的效应——如：
- $\tau = 0.1$：$x$ 对低尾的效应
- $\tau = 0.9$：$x$ 对高尾的效应

→ 揭示效应的**分布影响**——教育可能对低收入者有更大的回报。

## 反面论点与数据空白

- **LAD 估计的因果解释**：与 OLS 一样，LAD 只在大假设（$u$ 的中位数 = 0）下识别因果效应——对离群值的稳健性不能替代好的识别策略。
- **LAD 在有截取/截断数据中的应用有限**：当 $y$ 不是完全可观测时（如 Ch 17 的受限因变量），LAD 不能简单应用。

## 相关页

- [[OLS估计量的统计性质]] / [[函数形式选择]]
- [[Introductory-Econometrics-Wooldridge-8e]]
