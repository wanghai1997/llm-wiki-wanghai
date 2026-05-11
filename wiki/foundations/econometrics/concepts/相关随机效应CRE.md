---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, panel-data, CRE, correlated-random-effects, Mundlak, foundations, Wooldridge]
confidence: medium
decay_category: slow
status: foundation
---

# 相关随机效应 CRE

## 一句话定义

> **CRE（Correlated Random Effects）** = RE 模型的推广——通过加入**解释变量的个体均值** $\bar{x}_i$ 来显式建模 $a_i$ 与 $x_{it}$ 的相关性——融合了 RE 的效率和 FE 的稳健性。

## 为什么 CRE 是"两全其美"

传统二分法：
- FE：允许 $\text{Cov}(x_{it}, a_i) \neq 0$——但不能识别时间不变变量
- RE：可以识别时间不变变量——但假设 $\text{Cov}(x_{it}, a_i) = 0$

**CRE 桥接了这两者**。

## Mundlak 装置

$$y_{it} = \beta_0 + \beta_1 x_{it} + \gamma \bar{x}_i + a_i^* + u_{it}$$

其中 $\bar{x}_i = \frac{1}{T}\sum_t x_{it}$（个体在时间上的均值）。

关键：加入 $\bar{x}_i$ 后，$\text{Cov}(x_{it}, a_i^*) = 0$（个体异质性中与 $x$ 相关的部分被 $\bar{x}_i$ "吸收"）。

→ **现在可以安全地添加时间不变变量**（如性别、种族），并获得它们的效应估计。

## CRE 估计

1. 将 $y_{it}$ 对 $x_{it}$、$\bar{x}_i$、时间虚拟变量（以及任何时间不变变量）进行 RE 估计
2. $\hat{\beta}_1$（$x_{it}$ 的系数）= FE 估计量（两者在代数上相同）
3. 时间不变变量的系数 = 在控制 $a_i$ 与 $x$ 的相关性后，这些变量的效应

## CRE vs FE vs RE

| | FE | RE | CRE |
|---|---|---|---|
| 允许 $\text{Cov}(x_{it}, a_i) \neq 0$ | ✅ | ❌ | ✅ |
| 可识别时间不变变量 | ❌ | ✅ | ✅ |
| 效率 | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ |
| 复杂度 | ⭐ | ⭐ | ⭐⭐ |

## 不平衡面板的 CRE

CRE 可以自然处理不平衡面板（某些个体某些时期缺失）——不像 FE 的 within transformation 需要每个个体至少有若干期。

## 反面论点与数据空白

- **$\bar{x}_i$ 的线性模型假设**：CRE 假设 $a_i$ 与 $\bar{x}_i$ 的关系是线性的——如果真实关系是非线性的，CRE 仍会有偏。
- **在 $T$ 很小时 $\bar{x}_i$ 的噪声很大**——CRE 的性能可能不如直接使用 FE。

## 相关页

- [[固定效应估计]] / [[随机效应估计]] / [[Hausman检验]]
- [[Introductory-Econometrics-Wooldridge-8e]]
