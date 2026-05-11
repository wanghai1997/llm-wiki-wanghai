---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 17-2"]
tags: [concept, macroeconomics, batch7, investment, tobin-q, financial-markets]
confidence: medium
decay_category: slow
status: completed
---

# Tobin q理论

**Tobin's q**, developed by [[James Tobin]] (1969), is the ratio of the market value of installed capital to its replacement cost. It provides a forward-looking, financial-market-based signal for firm investment decisions.

$$q = \frac{\text{Market value of installed capital}}{\text{Replacement cost of capital}}$$

## The Investment Decision Rule

| Condition | Interpretation | Investment Response |
|---|---|---|
| $q > 1$ | Market values capital above cost | Invest (buy new capital) |
| $q < 1$ | Market values capital below cost | Do not invest (buying existing firms is cheaper) |
| $q = 1$ | Equilibrium | Investment equals depreciation |

## Connection to the Neoclassical Model

Tobin's q can be derived from the neoclassical framework:
- **Numerator**: Present discounted value of future marginal products of capital
- **Denominator**: Cost of acquiring new capital

With no adjustment costs, $q = 1$ and $MPK = r + \delta$.

With convex adjustment costs (Hayashi 1982):

$$I/K = f(q - 1), \quad f(0) = 0, \quad f' > 0$$

q becomes a **sufficient statistic** for investment: firms do not need to know the entire future path of profitability, only the current market valuation.

## Empirical Performance

### Supporting Evidence
- Brainard-Tobin (1977): Early work found reasonable predictive power
- Forward-looking: q incorporates expectations about future profitability
- Aggregate q correlates with aggregate investment (NBER data)

### Critiques
- **Blanchard-Rhee-Summers (1993)**: q explains only 10-20% of investment variation; cash flow dominates
- **Stock market bubbles**: q may reflect speculative valuations rather than fundamental MPK
- **Measurement**: The "market value of installed capital" is hard to measure for non-public firms

## Forward-Looking Advantage

Unlike the neoclassical model, which requires firms to know future MPK schedules:
- q **aggregates expectations** in financial market prices
- It reflects the market's collective assessment of future profitability
- But this is a double-edged sword: if markets are inefficient, q is misleading

## 反面论点与数据空白

- **现金流的压倒性影响**: Fazzari-Hubbard-Petersen (1988) show that for financially constrained firms, cash flow predicts investment better than q. This suggests credit market imperfections, not market valuation, drive investment.
- **q的测量难题**: 对于未上市公司、无形资产(软件、专利)密集型企业，"已安装资本的市场价值"无法直接观察，q的可操作性受限。
- **股票市场的非理性**: 2000年互联网泡沫和2008年房地产泡沫期间，q远超1但事后证明是错误信号——如果 firms 据此投资，会造成资源错配。
- **跨国差异**: q理论假设发达的金融市场和有效的股价形成。新兴市场(低流动性、政府干预、信息披露差)中q的投资信号功能可能很弱。
- **数字时代的挑战**: 平台经济中企业的价值主要来自网络效应和数据资产，而非传统"已安装资本"——q的分母定义变得模糊。

## See Also

- [[James Tobin]] — q理论的提出者
- [[新古典投资模型]] — q的微基础
- [[融资约束]] — q忽视的信贷摩擦
- [[投资理论]] — 完整投资理论谱系
- [[行为金融学]] — 市场非理性对q的扭曲
