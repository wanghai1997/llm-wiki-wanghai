---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, instrumental-variables, heteroskedasticity, panel-IV, GMM, foundations, Wooldridge]
confidence: medium
decay_category: slow
status: foundation
---

# IV 中的异方差与面板应用

## 一句话定义

> 当 IV 估计中存在异方差时，2SLS 的标准误不可靠，需要使用**异方差稳健标准误**；在面板数据中使用 IV 时，需要组合 **FE + IV**（或 **FD + IV**）并聚类标准误。

## 2SLS 与异方差

### 问题

- 2SLS 在异方差下仍然**一致**
- 但 2SLS 的默认标准误假设同方差——在有异方差时**标准误有偏**
- → 使用异方差稳健标准误（类似于 OLS 的异方差稳健 SE）

### 在更复杂的异方差/序列相关结构下

- **GMM (Generalized Method of Moments)**：利用"最优加权矩阵" → 比 2SLS 更有效的 IV 估计（在异方差下 GMM 是渐近有效的，2SLS 不是）
- 在实践中，GMM 与 2SLS 通常给出相似的点估计——但在异方差严重时 GMM 的标准误更可靠

## IV 在面板数据中的应用

### FE-IV

面板 FE 消除了不随时间变化的 $a_i$，然后对残留的时变内生变量使用 IV：

$$\ddot{y}_{it} = \beta_1 \ddot{x}_{it}^{endo} + \ddot{\mathbf{x}}_{it}^{exo}\boldsymbol{\gamma} + \ddot{u}_{it}$$

用 $\ddot{z}_{it}$ 作为 $\ddot{x}_{it}^{endo}$ 的工具。

### FD-IV

与 FE-IV 类似但使用一阶差分：

$$\Delta y_{it} = \beta_1 \Delta x_{it}^{endo} + \Delta \mathbf{x}_{it}^{exo}\boldsymbol{\gamma} + \Delta u_{it}$$

用 $\Delta z_{it}$ 作为 $\Delta x_{it}^{endo}$ 的工具。FD-IV 在误差有随机趋势（$\Delta u_{it}$ 无序列相关）时尤其合适。

### 面板 IV 中的标准误

- **必须聚类**在个体层面——面板数据的 IV 误差在个体内自动相关
- 聚类标准误对异方差和个体内的任意序列相关都稳健

## 实践注意事项

- 面板 IV 的工具通常是**随时间变化的**外生冲击（如政策变化、天气冲击）
- 第一阶段在面板中可能更弱（因为 FE/FD 消除了个体的跨期均值后剩余变异减少）

## 相关页

- [[工具变量IV]]（MM）/ [[弱工具变量问题]] / [[联立方程与面板数据]]
- [[固定效应估计]] / [[异方差]]
- [[Introductory-Econometrics-Wooldridge-8e]]
