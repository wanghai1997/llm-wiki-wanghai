---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 17-2, Ch 18-2"]
tags: [entity, macroeconomics, batch7, investment, money-demand, portfolio, nobel-1981]
confidence: medium
decay_category: medium
status: completed
---

# James Tobin

**James Tobin** (1918–2002) was an American economist at Yale University, awarded the **1981 Nobel Prize in Economic Sciences** "for his analysis of financial markets and their relations to expenditure decisions, employment, production and prices." He made foundational contributions to investment theory (Tobin's q), money demand (the Baumol-Tobin model), and portfolio selection.

## Tobin's q Theory of Investment (1969)

### The Core Idea

In *"A General Equilibrium Approach to Monetary Theory"* (Journal of Money, Credit and Banking, 1969), Tobin developed a theory linking financial markets to real investment decisions through the ratio:

$$q = \frac{\text{Market value of installed capital}}{\text{Replacement cost of capital}}$$

**The mechanism**:
- **$q > 1$**: The stock market values capital more highly than its replacement cost → firms should invest (buy new capital)
- **$q < 1$**: The stock market values capital below replacement cost → firms should not invest (buying existing firms is cheaper than building new)
- **$q = 1$**: Long-run equilibrium where investment equals depreciation

### Connection to the Neoclassical Model

Tobin's q can be derived from the neoclassical investment model:
- The numerator (market value) reflects the present discounted value of future marginal products of capital
- The denominator is the cost of acquiring new capital
- In equilibrium with no adjustment costs: $q = 1$ and $MPK = r + \delta$

With **convex adjustment costs** (Hayashi 1982), $q$ becomes a sufficient statistic for investment:
$$I/K = f(q - 1), \quad f(0) = 0, \quad f' > 0$$

### Empirical Performance

- **Brainard-Tobin (1977)**: Early empirical work found $q$ predicts investment reasonably well
- **Subsequent critique**: Stock market valuations may reflect bubbles or speculation, not fundamental MPK (Blanchard-Rhee-Summers 1993)
- **Forward-looking advantage**: $q$ incorporates expectations about future profitability, unlike backward-looking measures

## The Baumol-Tobin Model of Money Demand (1956)

### The Core Idea

Tobin (1956, independently Baumol 1952) developed the **"inventory-theoretic" model** of money demand. Households face a tradeoff:
- **Holding money**: Convenient for transactions but earns no interest
- **Holding bonds**: Earns interest but converting to money involves transaction costs

### The Square Root Formula

For an individual with income $Y$, transaction cost $b$ per conversion, and interest rate $i$:

$$M^* = \sqrt{\frac{bY}{2i}}$$

Key properties:
- Money demand increases with **income** ($M^* \propto \sqrt{Y}$) — income elasticity = 0.5
- Money demand decreases with **interest rate** ($M^* \propto 1/\sqrt{i}$) — interest elasticity = -0.5
- Money demand increases with **transaction costs** ($M^* \propto \sqrt{b}$)

**Aggregate money demand**:
$$\left(\frac{M}{P}\right)^d = L(i, Y) = \sqrt{\frac{bY}{2i}}$$

### Limitations

- **Debit cards / electronic payments**: Reduce $b$ dramatically, lowering optimal money holdings
- **Credit cards**: Allow purchasing without holding money
- **Aggregation**: The square root formula applies to individuals; aggregation to the economy is not straightforward

## Portfolio Selection and Money Demand (1958)

Tobin (1958) extended money demand theory using **mean-variance portfolio analysis**:
- Money is one asset in a portfolio that includes bonds, stocks, and other assets
- The demand for money depends on its **risk-return characteristics** relative to other assets
- Expected inflation increases the **opportunity cost** of holding money, reducing demand

This was an important step beyond the simple transactions motive toward an **asset demand** view of money.

## 反面论点与数据空白

- **q理论的经验弱点**: q与投资的相关性在统计上显著但经济意义有限——q的波动只能解释投资变动的10-20%(Blanchard-Rhee-Summers 1993)。现金流(反映融资约束)往往比q更有解释力。
- **Baumol-Tobin模型在数字时代失效**: 电子支付使$b$趋近于零,按模型最优货币持有量应趋近于零——但这与现实中仍有大量货币持有(现金、活期存款)矛盾。需要引入"支付习惯"、"隐私需求"、"地下经济"等非经济因素。
- **Tobin税的争议**: Tobin (1972)提议对外汇交易征税以减少投机。支持者认为可减少汇率波动;反对者认为会减少市场流动性、使税收负担转嫁给实体经济。教材未涉及此政策建议。
- **regional-bias**: Tobin的理论以美国金融市场为默认假设(流动性高、信息透明、交易成本可忽略),对发展中国家(金融抑制、高交易成本、现金经济)适用性有限。

## See Also

- [[Tobin q理论]] — 投资理论的核心概念页
- [[Baumol-Tobin模型]] — 货币需求的存货理论
- [[货币需求投资组合理论]] — Tobin's asset demand extension
- [[新古典投资模型]] — q理论的微基础
- [[融资约束]] — q理论忽视的信贷摩擦
- [[投资理论]] — 投资理论的完整谱系
