---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, limited-dependent-variable, logit, probit, binary-response, foundations, Wooldridge]
confidence: medium
decay_category: slow
status: foundation
---

# 二值响应模型——Logit 与 Probit

## 一句话定义

> **Logit 和 Probit** = 当因变量是二值（0/1）时，用非线性函数将线性指数映射到 $[0,1]$ 的概率空间——修正了线性概率模型 (LPM) 的预测超出区间和异方差问题。

## 为什么 LPM 不够好

线性概率模型：$P(y=1|x) = \beta_0 + \beta_1 x$

- 预测概率可能 < 0 或 > 1
- 异方差必然存在：$\text{Var}(y|x) = P(1-P)$ 随 $x$ 变化
- 偏效应为常数（$\beta_1$），但真实世界中的概率效应通常是非线性的

## Probit 模型

$$P(y=1|x) = \Phi(\beta_0 + \beta_1 x)$$

- $\Phi(\cdot)$ = 标准正态 CDF
- 潜变量框架：$y^* = \beta_0 + \beta_1 x + u$，$u \sim N(0,1)$，$y = 1 \text{ if } y^* > 0$
- 偏效应 **不是** $\beta_1$ ——需要计算 $\frac{\partial P(y=1|x)}{\partial x} = \beta_1 \cdot \phi(\beta_0 + \beta_1 x)$

## Logit 模型

$$P(y=1|x) = \frac{\exp(\beta_0 + \beta_1 x)}{1 + \exp(\beta_0 + \beta_1 x)} = \Lambda(\beta_0 + \beta_1 x)$$

- $\Lambda(\cdot)$ = 逻辑分布 CDF（比正态分布尾部更厚）
- 偏效应 = $\beta_1 \cdot \Lambda(1-\Lambda)$（S 形函数）
- 优势比 (Odds Ratio)：$\exp(\beta_1)$ = $x$ 每增加一单位，优势比乘以此值

## Logit vs Probit——实践中如何选择

| | Probit | Logit |
|---|---|---|
| CDF 假设 | 标准正态 | 逻辑分布（$\sigma \approx 1.81$） |
| 偏效应 | 类似（缩放约 1.6 倍差异） | 类似 |
| 传统应用领域 | 经济学更常用 | 生物统计/流行病学更常用 |
| **实践中两者的偏效应估计几乎一致** | | |

→ **选择哪一个通常不重要**——报告 Logit 或 Probit 结果均可，关键是报告**平均偏效应 (APE)** 而非原始系数。

## 估计方法——最大似然 (MLE)

Logit/Probit 是非线性模型 → 不能使用 OLS → 使用**最大似然估计 (MLE)**：
- MLE 选择使观测数据"最可能"出现的参数值
- 在大样本下 MLE 是一致的、渐近正态的、渐近有效的

## 解释——APE（平均偏效应）

$$\text{APE}_j = \frac{1}{n} \sum_{i=1}^n \frac{\partial \hat{P}(y_i=1|x_i)}{\partial x_{ij}}$$

- 在每个人的 $x$ 处计算偏效应后取平均——比"在均值处"计算更有意义
- `margins` 命令（Stata）/ `marginaleffects`（R/Python）自动计算

## 反面论点与数据空白

- **Logit/Probit 是"参数模型"——分布假设错误时不一致**：如果真实 CDF 不是正态也不是逻辑分布，MLE 可能不一致。半参数方法（如 Manski 的最大得分估计）不需要分布假设。
- **"Logit = 固定效应 Logit"才能消除不可观测异质性**：在面板数据中，Probit 不能直接做 FE（异质性参数估计问题），但 Logit 可以用条件 MLE 做 FE。

## 相关页

- [[分数响应模型]] / [[Poisson回归与指数均值模型]] / [[Tobit模型-角点解]]
- [[Introductory-Econometrics-Wooldridge-8e]]
