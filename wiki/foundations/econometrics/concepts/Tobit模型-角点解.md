---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, limited-dependent-variable, Tobit, corner-solution, foundations, Wooldridge]
confidence: medium
decay_category: slow
status: foundation
---

# Tobit 模型——角点解

## 一句话定义

> **Tobit 模型** = 当因变量在零处"堆积"（大量零值，正值连续分布）时的**角点解模型**——同时建模"是否为正"和"正值有多大"两个决策。

## 角点解 vs 截取——Wooldridge 的关键区分

| | 角点解 (Tobit) | 截取 (Censored Regression) |
|---|---|---|
| 零的来源 | 是**选择的结果**（最优解在角点=0） | 是**数据收集问题**（真实值被隐藏） |
| 例子 | 个人捐赠金额（多数人不捐赠=最优捐赠为0） | 工资低于某阈值不被记录 |
| 方法 | Tobit（结构模型） | 截取回归（MLE/Tobit型估计） |
| 参数解释 | 潜变量 $y^*$ 的边际效应 | 截取前真实 $y$ 的边际效应 |

→ Wooldridge 教材是少数在教学层面清楚区分两者的教材。

## Tobit 模型

$$y^* = \beta_0 + x\boldsymbol{\beta} + u, \quad u|x \sim N(0, \sigma^2)$$
$$y = \max(0, y^*)$$

- $y^*$ = 潜变量（如"捐赠意愿"——可为负）
- 实际观测 $y$ = 如果 $y^* > 0$ → $y^*$；否则 → $0$

## Tobit 的偏效应

在 Tobit 模型中，$x$ 的效应有两个通道：
1. **"是否为正"的边际效应**：$P(y>0|x)$ 的变化
2. **"正值有多大"的边际效应**：$E(y|y>0, x)$ 的变化
3. **无条件期望的边际效应**（最常报告）：$\frac{\partial E(y|x)}{\partial x_j}$

**三个效应不同！** 仅报告 $\beta_j$ 不够。

## Tobit vs 两阶段模型

Tobit 的限制：同一个随机项 $u$ 驱动"是否为正"和"正值多大"——两者必须符号相同且相对效应被参数化约束。

更灵活的方法：**两部分模型** (Two-Part Model)
1. Logit/Probit 对 $P(y>0|x)$
2. OLS 对 $\ln y$（仅用 $y>0$ 的观测值）

两部分模型允许"是否参与"和"参与多少"由不同的过程驱动。

## 反面论点与数据空白

- **Tobit 的分布假设很强（正态 + 同方差）**——如果违反 → Tobit MLE 不一致。Poisson QMLE（对非负结果）或两部分模型（灵活性）是更稳健的替代。
- **"角点解 = 0"可能需要与经济理论对话**：为什么零是最优选择（而非小额参与）？

## 相关页

- [[截取与截断回归]] / [[样本选择修正-Heckman两步法]] / [[Poisson回归与指数均值模型]]
- [[Introductory-Econometrics-Wooldridge-8e]]
