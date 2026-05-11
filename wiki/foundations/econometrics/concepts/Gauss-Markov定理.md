---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, Gauss-Markov, OLS, BLUE, foundations, Wooldridge, 技术]
confidence: medium
decay_category: slow
status: foundation
---

# Gauss-Markov 定理

## 一句话定义

> **Gauss-Markov 定理** = 在 MLR.1-5（线性、随机抽样、无完全共线性、零条件均值、同方差）下，OLS 估计量是**最优线性无偏估计量 (BLUE)**——在所有线性无偏估计量中方差最小。

## 定理表述

$$\text{Var}(\tilde{\beta}_j) \geq \text{Var}(\hat{\beta}_j^{\text{OLS}})$$

对任何其他线性无偏估计量 $\tilde{\beta}_j$ 成立。

## 五个假设的作用分解

| 假设 | 用于证明什么 |
|------|-------------|
| MLR.1（线性） | 参数模型有意义 |
| MLR.2（随机抽样） | $\hat{\beta}$ 的方差可推导 |
| MLR.3（无完全共线性） | $\hat{\beta}$ 可唯一计算 |
| MLR.4（零条件均值） | **无偏性** |
| MLR.5（同方差） | **BLUE** + 标准方差公式 |
| MLR.6（正态性，可选） | 精确的 t/F 分布 |

> Wooldridge 的教材强调：**Gauss-Markov 不需要正态性**——这是常见的教学错误。

## BLUE 的含义

| 字母 | 含义 | 说明 |
|------|------|------|
| **B**est | 方差最小（最优） | 给定线性 + 无偏的约束 |
| **L**inear | 是 $y_i$ 的线性组合 | $\hat{\beta} = \sum w_i y_i$ |
| **U**nbiased | 无偏 | $E(\hat{\beta}) = \beta$ |
| **E**stimator | 估计量 | 区别于估计值 |

## 定理的局限

- **"线性"限制**：可能存在**非线性**无偏估计量比 OLS 更好（虽然在实际中罕见）
- **同方差假设不可缺**：违反 MLR.5 → OLS 不再是 BLUE → [[加权最小二乘法WLS|WLS/GLS]] 更有效
- **"最优"只在给定假设下**：如果零条件均值不成立 → OLS 有偏 → 所有关于 BLUE 的讨论失去意义

## 反面论点与数据空白

- **Gauss-Markov 不保护你不受选择偏差侵害**：BLUE 保证的是**统计效率**而非**因果有效性**——有偏的 OLS 可以是 BLUE（例如遗漏变量导致的 OVB 下 OLS 仍是 BLUE，只是它估计的是错误的参数）。
- **同方差在现代计量中的角色下降**：异方差稳健标准误使 OLS 的推断在同方差违反时仍可用——因此 MLR.5 的重要性更多在效率而非有效性。

## 相关页

- [[OLS估计量的统计性质]] / [[OLS渐近理论]]
- [[加权最小二乘法WLS]] — 同方差违反时的替代
- [[Introductory-Econometrics-Wooldridge-8e]]
