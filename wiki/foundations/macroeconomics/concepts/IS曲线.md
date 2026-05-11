---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 11-2"]
tags: [concept, macroeconomics, batch5, is-lm]
confidence: medium
decay_category: medium
status: completed
---

# IS曲线

The **IS curve** (Investment–Saving) shows all combinations of the interest rate ($r$) and output ($Y$) at which the **goods market** is in equilibrium. It is downward-sloping: higher interest rates reduce investment, which reduces aggregate demand and equilibrium output.

## Derivation

The goods market equilibrium condition is:

$$Y = C(Y - T) + I(r) + G$$

Key behavioral assumptions:
- Consumption increases with disposable income: $C'(Y-T) > 0$ (MPC)
- Investment decreases with the interest rate: $I'(r) < 0$

### Why IS Slopes Downward

A higher interest rate ($r \uparrow$) reduces investment ($I \downarrow$), which reduces planned expenditure. For equilibrium to be restored, output must fall ($Y \downarrow$) to match the lower demand.

Formally, differentiating the equilibrium condition:

$$\frac{dY}{dr} = \frac{I'(r)}{1 - MPC} < 0$$

The slope depends on:
- **Sensitivity of investment to interest rates**: $|I'(r)|$ larger → flatter IS
- **The multiplier**: $1/(1-MPC)$ larger → flatter IS

## Shifts in the IS Curve

Any change in autonomous spending shifts the IS curve:

| Shock | Direction | Effect |
|---|---|---|
| $\Delta G > 0$ (expansionary fiscal) | IS shifts right | Higher $Y$ at any $r$ |
| $\Delta T < 0$ (tax cut) | IS shifts right | Higher $Y$ at any $r$ |
| $\Delta I > 0$ (investment boom) | IS shifts right | Higher $Y$ at any $r$ |
| $\Delta G < 0$ (austerity) | IS shifts left | Lower $Y$ at any $r$ |

The horizontal shift equals $\Delta G \times \frac{1}{1-MPC}$ (the Keynesian cross multiplier), but the **effective** output change in the full IS-LM model is smaller due to crowding out.

## IS in the Open Economy

In an open economy, the IS condition becomes:

$$Y = C(Y - T) + I(r) + G + NX(e)$$

Net exports depend on the real exchange rate ($e$), which in turn depends on the interest rate differential. This modification becomes central in the [[Mundell-Fleming模型]].

## The IS Curve and Aggregate Demand

The IS curve is one half of the [[IS-LM模型]]. Together with the LM curve, it determines the equilibrium interest rate and output for a given price level. In Ch 12, Mankiw shows how varying the price level traces out the [[总需求曲线]].

## 反面论点与数据空白

### [CONTRADICTION-1] 投资对利率的敏感度:实证微弱

IS曲线的负斜率依赖于 $I'(r) < 0$,但实证证据:
- **Summers (1981)**:投资对利率的弹性很小,很多时候统计上不显著
- **Fazzari-Hubbard-Petersen (1988)**:融资约束(现金流)比利率更重要,尤其对中小企业
- **2008后**:即使利率降至零下限,投资复苏缓慢——"推绳子"问题

如果投资对利率不敏感,IS曲线接近垂直,货币政策几乎无效——这与教材"IS-LM是核心政策框架"的叙事形成张力。

### [CONTRADICTION-2] 利率渠道的局限性

传统IS-LM假设货币政策通过 $r \rightarrow I$ 渠道传导,但现实中:
- **住房投资**:对长期利率和抵押贷款利率更敏感,而非短期政策利率
- **存货投资**:对销售预期更敏感
- **企业投资**:受动物精神、预期利润、产能利用率驱动
- **消费者耐用品**:受信贷可得性和消费者信心驱动

教材将投资简化为 $I(r)$,掩盖了复杂的传导机制。

### 数据空白

1. **IS曲线的实证估计**:需要识别政策冲击(如Romer-Romer货币政策冲击)来估计结构方程,但识别策略存在争议
2. **非线性IS**:在极低利率或极高债务水平时,IS关系可能非线性
3. **全球IS**:开放经济中,国内IS受全球利率和需求影响,而非仅国内因素

## See Also

- [[LM曲线]] — 货币市场均衡的另一半
- [[IS-LM模型]] — 完整框架
- [[凯恩斯交叉模型]] — IS的基础
- [[政府购买乘数]] — 财政政策乘数
- [[财政政策效应]] — 政策如何移动IS
- [[总需求曲线]] — 从IS-LM推导
