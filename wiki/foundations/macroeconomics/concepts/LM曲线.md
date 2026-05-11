---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 11-3"]
tags: [concept, macroeconomics, batch5, is-lm]
confidence: medium
decay_category: medium
status: completed
---

# LM曲线

The **LM curve** (Liquidity preference–Money supply) shows all combinations of the interest rate ($r$) and output ($Y$) at which the **money market** is in equilibrium. It is upward-sloping: higher income raises money demand, requiring a higher interest rate to maintain equilibrium with a fixed money supply.

## Derivation

The money market equilibrium condition is:

$$\frac{M}{P} = L(r, Y)$$

Where:
- $M/P$ = real money supply (exogenous, controlled by the central bank)
- $L(r, Y)$ = real money demand (liquidity preference)

Money demand properties:
- **Negative in $r$**: Higher interest rates increase the opportunity cost of holding money, reducing money demand
- **Positive in $Y$**: Higher income increases transactions needs, raising money demand

### Why LM Slopes Upward

An increase in output ($Y \uparrow$) raises money demand ($L \uparrow$). With a fixed real money supply ($M/P$), the interest rate must rise ($r \uparrow$) to reduce money demand back to equilibrium.

Formally:

$$\frac{dr}{dY} = -\frac{L_Y}{L_r} > 0$$

The slope depends on:
- **Income sensitivity of money demand** ($L_Y$): Higher → steeper LM
- **Interest sensitivity of money demand** ($|L_r|$): Higher → flatter LM

## Extreme Cases

### The Liquidity Trap (Horizontal LM)

When interest rates approach zero, money demand becomes perfectly elastic:
- People are indifferent between holding money and bonds at $r \approx 0$
- The central bank cannot lower rates further
- Monetary policy becomes ineffective
- **Fiscal policy is fully effective** (no crowding out)

See [[流动性陷阱]] for full discussion.

### The Classical Case (Vertical LM)

When money demand is completely insensitive to interest rates ($L_r = 0$):
- LM is vertical
- Money demand depends only on transactions ($Y$)
- **Fiscal policy is completely crowded out**: any IS shift is offset by interest rate changes that return $Y$ to the original level
- Monetary policy is highly effective

This corresponds to the classical quantity theory of money.

## Shifts in the LM Curve

| Shock | Direction | Effect |
|---|---|---|
| $\Delta M > 0$ (monetary expansion) | LM shifts right/down | Lower $r$ at any $Y$ |
| $\Delta M < 0$ (monetary contraction) | LM shifts left/up | Higher $r$ at any $Y$ |
| $\Delta P > 0$ (price level rise) | LM shifts left/up | Higher $r$ at any $Y$ (since $M/P$ falls) |
| $\Delta P < 0$ (deflation) | LM shifts right/down | Lower $r$ at any $Y$ |

## LM in the Open Economy

In the [[Mundell-Fleming模型]] (small open economy with perfect capital mobility):
- The domestic interest rate is fixed at the world rate: $r = r^*$
- The LM curve becomes horizontal at $r = r^*$
- Money supply adjustments must accommodate the fixed exchange rate (under fixed rates) or are endogenous to exchange rate changes (under floating rates)

## 反面论点与数据空白

### [CONTRADICTION-1] 货币需求函数的现代失效

LM曲线依赖于稳定的货币需求函数 $L(r,Y)$,但:
- **金融创新**:信用卡、电子支付、货币市场基金降低了交易性货币需求
- **量化宽松**:央行扩大基础货币但并未导致通胀——货币乘数崩溃
- **央行操作框架转变**:现代央行以利率为目标,而非货币供应量——LM的"货币供给外生"假设已不符合现实

事实上,现代央行(美联储、欧央行)根本不控制货币供应量,而是设定政策利率。LM曲线的货币供给机制是过时的描述。

### [CONTRADICTION-2] 利率作为政策工具 vs LM的货币供给假设

LM曲线假设央行控制 $M$,市场决定 $r$。但1980s后:
- **利率目标制**:央行设定短期利率,货币供应量内生调整
- **Taylor rule**: $r = r^* + \pi + 0.5(\pi - \pi^*) + 0.5(Y - \bar{Y})$——直接以利率为工具
- **流动性管理**:央行通过公开市场操作维持目标利率,货币供应量被动适应

将现代货币政策映射到LM框架需要"反向逻辑":央行选择 $r$, $M$ 内生调整以维持货币市场均衡。

### 数据空白

1. **货币需求的估计不稳定**:Goldfeld (1976) 发现传统货币需求函数在1970s出现"失踪货币"(missing money)——预测值系统性低于实际值
2. **影子银行与货币创造**:传统M1/M2忽略影子银行的货币创造功能
3. **数字货币**:CBDC可能根本改变货币需求和LM机制

## See Also

- [[IS曲线]] — 产品市场均衡
- [[IS-LM模型]] — 完整框架
- [[流动性陷阱]] — LM水平的极端情形
- [[货币政策效应]] — 政策如何移动LM
- [[总需求曲线]] — 从IS-LM推导
- [[货币数量论]] — 古典货币理论
