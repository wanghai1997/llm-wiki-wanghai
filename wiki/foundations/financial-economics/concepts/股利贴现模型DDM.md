---
created: 2026-05-05
updated: 2026-05-05
sources:
  - "徐高 (2017), 金融经济学二十五讲, 第4讲"
tags:
  - 金融经济学
  - 股票估值
  - DDM
confidence: medium
decay_category: medium
status: evergreen
---

# 股利贴现模型（DDM）

**股利贴现模型（Dividend Discount Model, DDM）** 是股票估值的最常用模型。核心思想：股票价值 = 未来所有预期分红的现值之和。

## 推导

$$S_0 = \frac{D_1}{1+r} + \frac{S_1}{1+r} = \sum_{t=1}^{\infty} \frac{D_t}{(1+r)^t}$$

通过不断将未来股价用更远期的分红替代，股价最终仅由未来分红决定——**未来股价不影响当前估值**（它只是更远期分红的反映）。

## 戈登增长模型（Gordon Growth Model）

假设分红以恒定增长率 g 永续增长：$D_t = D_0 (1+g)^t$

$$S_0 = \frac{D_1}{r - g} \quad (\text{要求 } r > g)$$

## 核心洞见

- 股价对贴现率 r 高度敏感——r 微调导致价格大幅变动
- g 不能超过 r——否则股价无穷大
- DDM 揭示了"为什么股价波动这么大"：不是分红预期变了，而是贴现率预期变了

## 连接

- [[净现值与内部收益率]]：DDM 就是 NPV 在股票上的应用
- [[到期收益率]]：债券 YTM vs 股票贴现率 r
- [[CAPM]]：r 如何被系统性地确定（后续讲次）
