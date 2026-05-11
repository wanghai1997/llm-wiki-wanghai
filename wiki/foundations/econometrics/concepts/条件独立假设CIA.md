---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, regression, identification, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# 条件独立假设 CIA

## 一句话定义

> **条件独立假设** = 在控制可观测的协变量之后，处理分配与潜在结果**独立**——即所有选择偏差仅来自可观测变量，不存在不可观测的混淆因素。

## 正式表述

$$Y_{0i}, Y_{1i} \perp\!\!\!\perp D_i \mid X_i$$

在控制 $X_i$（协变量）后，处理 $D_i$ 如同随机分配——选择偏差被 $X_i$ "吸收"。

## 其他名称

- **Selection on Observables**（基于可观测变量的选择）
- **Unconfoundedness**（无混淆假设）
- **Conditional Independence Assumption (CIA)**
- **Ignorability**（可忽略性）

## CIA 下的因果识别

CIA 成立时，回归/匹配可以识别平均处理效应。但 CIA **不可直接检验**（因为我们永远看不到 $Y_{0i}$ 对于处理组个体的值）。

## 如何（间接）辩护 CIA

1. **丰富的数据**：控制足够多的协变量 → 让 CIA 更可信
2. **机构知识**：理解处理分配的实际机制 → 判断是否遗漏重要变量
3. **系数稳定性**：逐步添加控制变量 → 系数是否稳定？Dale-Krueger 的"加了选择度组→系数崩溃→再加其他→系数稳定"是经典模式
4. **伪结果检验**：对不应该被处理的变量（如处理前的历史结果）运行回归 → 如果"处理效应"为零，增强 CIA 可信度

> 但这些都不能**证明** CIA 成立。

## 反面论点与数据空白

- **CIA 的核心困境**：最强的辩护是间接的——事实上不可检验。这是回归/匹配方法相对于 RCT 的根本弱点。
- **Altonji-Elder-Taber (2005) 比率**：一种量化"需要多少不可观测选择偏差才能推翻现有结果"的方法——但仍需假设不可观测选择与可观测选择"比例相同"。
- **CIA vs 其他识别策略**：IV、RD、DiD 各自替换 CIA 为其他（可能更可信的）假设——IV 用排他性约束，RD 用断点连续性，DiD 用平行趋势。
- **机器学习时代的 CIA**：高维控制变量（Double Lasso、因果森林）可能让 CIA 在实践上更可信——但也带来了过度拟合和"控制后门路径"的风险。

## 相关页

- [[回归作为自动匹配]] / [[遗漏变量偏差公式]] / [[选择偏差]]
- [[理想实验基准]]
- [[Mastering-Metrics]]
