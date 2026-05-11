---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 18-1"]
tags: [concept, macroeconomics, batch7, money-demand, transactions, microfoundations]
confidence: medium
decay_category: medium
status: completed
---

# Baumol-Tobin模型

The **Baumol-Tobin model** (Baumol 1952, Tobin 1956) is the "inventory-theoretic" model of money demand. It formalizes the transaction motive: households face a tradeoff between the convenience of holding cash and the interest foregone by not holding bonds.

## The Setup

A household receives income $Y$ at the beginning of the period and spends it evenly. It can hold:
- **Money**: convenient for transactions but earns no interest
- **Bonds**: earn interest rate $i$ but converting to money costs $b$ per transaction

## The Optimization Problem

The household makes $N$ trips to convert bonds to money. Average money holdings:

$$M = \frac{Y}{2N}$$

Total cost:
- **Transaction costs**: $b \cdot N$
- **Foregone interest**: $i \cdot M = i \cdot \frac{Y}{2N}$

Minimize total cost with respect to $N$:

$$\min_N \; bN + \frac{iY}{2N}$$

## The Square Root Formula

First-order condition:

$$b = \frac{iY}{2N^2} \implies N^* = \sqrt{\frac{iY}{2b}}$$

Optimal average money holdings:

$$M^* = \frac{Y}{2N^*} = \sqrt{\frac{bY}{2i}}$$

## Key Properties

| Elasticity | Value | Interpretation |
|---|---|---|
| Income elasticity | 0.5 | Money demand rises with $\sqrt{Y}$, not proportionally |
| Interest elasticity | -0.5 | Money demand falls with $1/\sqrt{i}$ |
| Transaction cost elasticity | 0.5 | Higher conversion costs raise money holdings |

Aggregate money demand:

$$\left(\frac{M}{P}\right)^d = L(i, Y) = \sqrt{\frac{bY}{2i}}$$

## Limitations and Extensions

### Digital Payments Revolution
- Debit cards, credit cards, and mobile payments dramatically reduce $b$
- If $b \to 0$, the model predicts $M^* \to 0$
- But people still hold cash for privacy, habits, and the informal economy

### Aggregation Problems
- The square root formula applies to individuals
- Aggregate demand depends on the distribution of $Y$ and $b$ across households
- Firms' money demand may follow different logic

### Uncertainty (Miller-Orr 1966)
- When cash flows are stochastic, the optimal policy is a "band" strategy
- Hold money until balance hits an upper threshold, then convert to bonds
- When balance hits a lower threshold, convert bonds to money

## 反面论点与数据空白

- **数字时代失效**: 电子支付使交易成本 $b$ 趋近于零，但现实中仍有大量货币持有（现金、活期存款）。需要引入"支付习惯"、"隐私需求"、"地下经济"等非经济因素解释。
- **信用卡的省略**: 信用卡允许购买时无需持有货币——Baumol-Tobin的"现金 vs 债券"二分已不适用于现代消费。
- **企业现金持有的解释力弱**: 企业持有大量现金(苹果、微软等科技巨头的"现金山")主要出于税务筹划、并购期权、汇率对冲——与Baumol-Tobin的交易动机无关。
- **央行数字货币(CBDC)**: 如果CBDC提供利息同时保持支付便利性，b和i的区分将模糊——模型框架可能需要根本性重构。

## See Also

- [[货币需求理论]] — 货币需求的完整理论谱系
- [[James Tobin]] — 模型共同提出者
- [[货币需求投资组合理论]] — 资产组合视角的补充
- [[货币需求的经验证据]] — 实证估计
- [[实际货币余额与货币需求]] — 基础概念
