---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, causal-inference, doubly-robust, IPW-RA, foundations, Wooldridge]
confidence: medium
decay_category: slow
status: foundation
---

# 回归调整与 IPW 的结合

## 一句话定义

> **IPW-RA (IPW + Regression Adjustment)** = 同时使用倾向得分加权和回归调整的**双稳健 (Doubly Robust)** 估计量——只要**倾向得分模型**或**结果回归模型**中有**一个**被正确指定，估计就是一致的。

## 为什么"双保险"

- **仅回归调整**：如果回归模型函数形式错了 → 不一致
- **仅 IPW**：如果倾向得分模型错了 → 不一致
- **双稳健**：两个模型中只要有一个正确 → 一致

→ **显著降低了"模型选择错误"的风险**。

## 双稳健估计量

$$\widehat{\text{ATE}}_{DR} = \frac{1}{n}\sum_{i=1}^n \left[ \frac{D_i(y_i - \hat{m}_1(x_i))}{\hat{p}(x_i)} + \hat{m}_1(x_i) - \frac{(1-D_i)(y_i - \hat{m}_0(x_i))}{1-\hat{p}(x_i)} - \hat{m}_0(x_i) \right]$$

其中 $\hat{m}_d(x)$ = 在 $D=d$ 组中 $y$ 对 $x$ 的回归预测。

直观理解：IPW 处理"选择偏差"部分，回归调整处理"结果模型"部分——两者的"交叉项"提供了双稳健性。

## 实践中的实现

- Stata: `teffects ipwra`
- R: `DRDID` / `drgee` / `tmle` 包
- 通常与增强的倾向得分模型（包含交互项和非线性项）配合使用

## 双稳健的局限性

- **"其中一个正确"在实践中无法验证**——如果两个模型都错（但错的方向相同），DR 估计仍可能偏
- **在有限样本下**双稳健的优势可能被估计的额外噪声抵消
- **极端权重问题**仍存在——修剪或稳定权重可以部分缓解

## 相关页

- [[逆概率加权IPW]] / [[倾向得分方法]] / [[政策评估的回归调整]]
- [[Introductory-Econometrics-Wooldridge-8e]]
