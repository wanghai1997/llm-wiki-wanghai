---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, limited-dependent-variable, Poisson, count-data, exponential-mean, foundations, Wooldridge]
confidence: medium
decay_category: slow
status: foundation
---

# Poisson 回归与指数均值模型

## 一句话定义

> **Poisson 回归** = 当因变量是非负整数（计数数据）或非负有上界变量时使用的**指数均值模型**——Poisson QMLE 在只正确指定条件均值时保持一致。

## 为什么是"指数均值模型"而非单纯的"Poisson 回归"

Wooldridge 强调：Poisson 回归的现代观点是——**只要条件均值的函数形式正确**（$E(y|x) = \exp(x\boldsymbol{\beta})$），MLE 就是一致的——即使 $y$ 的分布不是 Poisson。

→ 这是"拟最大似然"的力量：稳健性来自均值函数的正确性，而非分布假设的正确性。

## 适用场景

- **计数数据**：专利数、就诊次数、事故数
- **非负有上界变量**：教育年限、就业月数——Poisson QMLE 比 Tobit 更稳健（不需要完整分布假设）
- **任何非负结果**：支出、持续期——只要期望函数是指数形式

## 模型形式

$$E(y|x) = \exp(\beta_0 + \beta_1 x_1 + ... + \beta_k x_k)$$

- **半弹性解释**：$\%\Delta E(y|x) \approx 100\beta_1 \Delta x_1$（对连续变量）
- **偏效应**：$\frac{\partial E(y|x)}{\partial x_j} = \beta_j \cdot \exp(x\boldsymbol{\beta})$

## Poisson vs 负二项回归

传统上负二项回归（Negative Binomial）被用于处理"过度离散"（方差 > 均值）。但 Wooldridge 指出：

- **Poisson QMLE 在过度离散下仍然一致**（只要均值函数正确）——方差-均值关系不影响一致性
- 负二项回归在均值函数正确+方差函数正确的严格条件下才一致——如果方差函数错了，不如 Poisson QMLE 稳健
- → **实践中，Poisson QMLE + 稳健标准误通常是首选**

## 零膨胀问题

如果 $y=0$ 的比例异常高（如大多数人从未申请专利）：
- Poisson QMLE 仍然一致（零很多不违反均值假设）
- 如果零的生成机制不同（某些人"不可能"申请 vs "可能但不申请"）→ 零膨胀 Poisson (ZIP) 或 two-part model

## 反面论点与数据空白

- **指数均值假设的经济合理性需要检视**：$E(y|x)$ 随 $x$ 指数增长 → 在大 $x$ 处效应巨大——在数据范围外不宜外推。
- **QMLE 标准误在有限样本下可能表现不佳**：需要配合稳健标准误。

## 相关页

- [[二值响应模型-Logit与Probit]] / [[Tobit模型-角点解]]
- [[Introductory-Econometrics-Wooldridge-8e]]
