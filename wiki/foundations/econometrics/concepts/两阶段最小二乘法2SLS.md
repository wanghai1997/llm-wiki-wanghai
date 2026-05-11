---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, instrumental-variables, 2SLS, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# 两阶段最小二乘法 2SLS

## 一句话定义

> **2SLS** = IV 方法在多工具和多控制变量情境下的推广——第一阶段用 $Z_i$（和控制变量）预测 $\hat{D}_i$，第二阶段用 $\hat{D}_i$ 替代原 $D_i$ 进行回归。

## 两阶段过程

### 第一阶段

$$D_i = \pi_0 + \pi_1 Z_i + \mathbf{X}_i'\pi_2 + \nu_i$$

→ 获得 $\hat{D}_i$（处理变量的预测值——**仅由 $Z_i$ 和其他外生变量驱动的变异**）

### 第二阶段

$$Y_i = \alpha + \lambda \hat{D}_i + \mathbf{X}_i'\beta + \varepsilon_i$$

→ $\hat{\lambda}$ 是 IV/2SLS 的因果效应估计

## 为什么需要 2SLS

- **单工具 + 无控制变量** → 2SLS = Wald Estimator（$\rho / \phi$）
- **多工具** → 2SLS 自动生成最优的工具组合（工具变量的加权组合）
- **需要控制变量** → 2SLS 自然容纳协变量——控制变量必须在第一阶段**和**第二阶段中同时出现

## 在 Mastering 'Metrics 中的位置

Ch 3.3 "The Population Bomb"（[[家庭规模-子女质量trade-off]]）是 2SLS 的旗舰案例——同时使用**两个工具**（双胞胎出生 + 同性子女组合）来识别家庭规模对子女教育成就的因果效应。

## 反面论点与数据空白

- **2SLS 的有限样本偏差**：在小样本中，2SLS 倾向于接近 OLS（有偏）——即使工具有效。偏差随第一阶段 $F$ 统计量增大而减小。
- **"禁止回归" (Forbidden Regression)**：第二阶段必须使用 $\hat{D}_i$ 中的所有外生变异——如果将非线性预测（如 Probit）用于第一阶段而不调整第二阶段标准误，会导致不一致。
- **多工具时的过度拟合**：工具太多时，$\hat{D}_i$ 过度拟合样本 → 2SLS 趋向 OLS → 偏差增大 → LIML (Limited Information Maximum Likelihood) 是替代方案。

## 相关页

- [[工具变量IV]] / [[局部平均处理效应LATE]]
- [[第一阶段与简约式]] / [[家庭规模-子女质量trade-off]]
- [[Mastering-Metrics]]
