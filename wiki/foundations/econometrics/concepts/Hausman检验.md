---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, panel-data, Hausman-test, FE-vs-RE, foundations, Wooldridge]
confidence: medium
decay_category: slow
status: foundation
---

# Hausman 检验

## 一句话定义

> **Hausman 检验** = 比较 FE 和 RE 估计量的差异——如果两者**统计上显著不同** → 拒绝 RE 假设（$\text{Cov}(x_{it}, a_i) = 0$）→ 使用 FE；如果接近 → RE 可用（更有效）。

## 检验逻辑

- **RE**：假设 $\text{Cov}(x_{it}, a_i) = 0$ → 在 $H_0$ 下一致且有效
- **FE**：不对 $\text{Cov}(x_{it}, a_i)$ 做任何假设 → 无论 $H_0$ 是否成立都一致

$$H = (\hat{\boldsymbol{\beta}}_{FE} - \hat{\boldsymbol{\beta}}_{RE})' [\widehat{\text{Var}}(\hat{\boldsymbol{\beta}}_{FE}) - \widehat{\text{Var}}(\hat{\boldsymbol{\beta}}_{RE})]^{-1} (\hat{\boldsymbol{\beta}}_{FE} - \hat{\boldsymbol{\beta}}_{RE}) \sim \chi^2_k$$

如果 $H$ 大 → FE 和 RE 估计量有显著差异 → 拒绝 $H_0$ → **使用 FE**。

## 实际操作

1. 估计 RE 模型
2. 估计 FE 模型
3. 如果 Hausman 统计量大（$p < 0.05$）→ **使用 FE**
4. 如果 Hausman 统计量小 → **可以使用 RE**（但你仍然可以选择 FE 作为稳健性检验）

## Hausman 检验在实践中的注意事项

- **只对随时间变化的变量进行**：时间不变变量的 FE 估计不存在 → 无法比较
- **需要在同方差 + 无序列相关下才严格有效**：稳健 Hausman 检验（Wooldridge 的 "variable addition test"）更常用
- **"显著就用 FE，不显著就用 RE"是过度简化的**：即使 Hausman 不显著，RE 假设可能仍然违反——在政策评估中，FE 通常是更安全的选择

## 稳健 Hausman 检验（更推荐的版本）

Wooldridge 的方法：在 FE 回归中检验 $H_0: \gamma = 0$：

$$\ddot{y}_{it} = \beta_1 \ddot{x}_{it} + \gamma (\bar{x}_i) + \ddot{u}_{it}$$

如果 $\gamma \neq 0$ → RE 不成立 → 使用 FE。这个版本对异方差和序列相关稳健。

## 反面论点与数据空白

- **"显著 = FE，不显著 = RE"的二分法忽略了经济显著性**：即使统计上显著，FE 和 RE 的实际差异可能很小——报告两者使读者自行判断。
- **Hausman 检验在弱序列相关下可能低功效**：不拒绝 RE ≠ RE 正确。

## 相关页

- [[固定效应估计]] / [[随机效应估计]] / [[相关随机效应CRE]]
- [[Introductory-Econometrics-Wooldridge-8e]]
