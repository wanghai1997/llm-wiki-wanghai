---
created: 2026-05-03
updated: 2026-05-04
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 13", "健全现代货币政策框架.md"]
tags: [concept, macroeconomics, batch5, open-economy, core-model]
confidence: medium
decay_category: slow
status: completed
---

# Mundell-Fleming模型

The **Mundell-Fleming model** extends the [[IS-LM模型]] to an open economy with **perfect capital mobility** and a **small open economy** assumption (where the domestic interest rate equals the world interest rate). Co-developed by [[Marcus Fleming]] (1962) and [[Robert Mundell]] (1963), it is the canonical framework for analyzing short-run macroeconomic policy in an open economy.

## Model Assumptions

1. **Small open economy**: The economy is too small to affect the world interest rate ($r^*$)
2. **Perfect capital mobility**: Capital flows instantaneously to equalize returns; $r = r^*$
3. **Fixed price level**: Short-run analysis with sticky prices
4. **Static exchange rate expectations**

## The Model Structure

### IS* Curve (Goods Market Equilibrium)

$$Y = C(Y - T) + I(r^*) + G + NX(e)$$

Where:
- $NX(e)$ = net exports, decreasing in the exchange rate $e$ (defined as domestic currency per unit of foreign currency; a rise in $e$ is a depreciation)
- $I(r^*)$ = investment, determined by the exogenous world interest rate
- The IS* curve is **downward-sloping** in $(e, Y)$ space: a depreciation ($e \uparrow$) improves net exports, increasing output

### LM* Curve (Money Market Equilibrium)

$$\frac{M}{P} = L(r^*, Y)$$

Since $r = r^*$, the LM* curve is **vertical** in $(e, Y)$ space: money market equilibrium determines a unique level of output, regardless of the exchange rate.

```
Exchange Rate (e)
    │
    │     LM* (vertical)
    │        │
    │        │     IS*
    │        │    /
    │        │   /
    │        │  /
    │        │ /
    └────────│/───────→ Output (Y)
             Y*
```

**Equilibrium**: The intersection of IS* and LM* determines the equilibrium exchange rate $e^*$ and output $Y^*$.

## Key Results

The Mundell-Fleming model yields sharply different policy effectiveness results depending on the exchange rate regime:

### Under Floating Exchange Rates
- **Monetary policy is highly effective**
- **Fiscal policy is ineffective**

### Under Fixed Exchange Rates
- **Fiscal policy is highly effective**
- **Monetary policy is ineffective**

These results are the foundation of the [[不可能三角]] (impossible trinity).

## Relationship to IS-LM

The Mundell-Fleming model can be seen as IS-LM with two modifications:
1. The interest rate is fixed at $r^*$ (due to perfect capital mobility)
2. Net exports depend on the exchange rate, which becomes an endogenous variable

The exchange rate adjusts to ensure that both goods and money market equilibrium are maintained simultaneously.

## Limitations and Extensions

### Limitations
- **Small economy assumption**: Does not apply to the US, China, or Eurozone
- **Perfect capital mobility**: In reality, capital flows face frictions and risk premia
- **Static expectations**: Ignores exchange rate dynamics and overshooting (Dornbusch 1976)
- **No risk premia**: Ignores country risk and liquidity differentials

### Extensions
- **Dornbusch overshooting model**: Adds rational expectations and price stickiness; exchange rate overshoots its long-run equilibrium in response to monetary shocks
- **Portfolio balance model**: Allows for imperfect substitutability between domestic and foreign assets
- **New open economy macroeconomics**: DSGE models with microfoundations (Obstfeld-Rogoff 1995)

## 反面论点与数据空白

### [CONTRADICTION-1] "小型开放经济"假设与大型经济体现实

Mundell-Fleming假设小型开放经济(利率=世界利率),但:
- **美国**:联邦基金利率由美联储独立设定,受全球影响但不等于世界利率
- **中国**:资本账户管制使国内利率大幅偏离世界利率
- **欧元区**:作为整体是大型经济体,但成员国 individually 是小型的

教材在Ch 13-1说"most macroeconomists believe ... this model describes well the economy",却未讨论大型经济体的利率内生决定。

### [CONTRADICTION-2] 完美资本流动假设的现实偏离

现实中资本流动远非"完美":
- **资本管制**:中国、印度等新兴市场维持显著资本账户管制
- **风险溢价**:新兴市场面临主权风险溢价,即使资本自由流动,利率也不等于r*
- **金融摩擦**:2008危机显示跨境资本流动会突然停止(sudden stop),与"完美流动"假设矛盾
- **汇率风险**:即使无资本管制,汇率波动风险使资产非完全替代

### [CONTRADICTION-3] 忽略全球价值链和中间品贸易

传统NX(e)假设贸易品为最终品,但现实中:
- 全球价值链(GVC)使中间品贸易占总贸易的约60%
- 汇率贬值对出口的影响被进口中间品成本上升部分抵消
- 汇率传递(exchange rate pass-through)不完全

这些现代特征使Mundell-Fleming的净出口机制过于简化。

### 数据空白

1. **汇率制度的真实分类**:IMF将汇率制度分为硬钉住、软钉住、浮动等,但各国实际行为("害怕浮动")与法定分类差异巨大
2. **资本流动顺周期性**:资本流动在经济繁荣时流入、衰退时流出,放大波动——与Mundell-Fleming的平稳调整假设矛盾
3. **数字货币与汇率**:CBDC可能改变跨境资本流动模式,挑战现有框架

### [regional-bias] 中国"管理浮动 + 资本部分流动"的非典型适用

按 [[孙国峰]] 《健全现代货币政策框架》(2021),中国汇率制度是"以市场供求为基础、参考一篮子货币进行调节、有管理的浮动汇率制度"——既非纯粹浮动也非固定。**2019-08-05 人民币对美元汇率"破 7"事件**:

- 美国 2018-2019 加征关税升级 + 人民币贬值压力 → 央行允许 7.0 整数关口被突破。
- 教材标准 Mundell-Fleming 预测:浮动汇率下汇率自由调整;但 PBoC 通过逆周期调节因子 + 跨境资本流动审慎管理"管理"浮动幅度。
- 实际操作:汇率有时浮动有时干预,资本流动有时开放有时收紧 → **介于教材两个极端的中间态**。

中国情境对 Mundell-Fleming 的挑战:

1. 不可能三角的实际选择是"独立货币政策 + 部分资本流动管理 + 管理浮动"三者妥协。详见 [[不可能三角]] 中国变体。
2. PBoC 可同时使用利率工具(国内目标)+ 汇率工具(对外目标),违反 Mundell-Fleming 的二选一暗示。
3. [[人民币汇率市场化]] 改革表明中国正在向更接近纯浮动的方向演进,但保留干预选项。

详见 [[人民币汇率市场化]] / [[中国货币政策框架]]。

## See Also

- [[IS-LM模型]] — Mundell-Fleming的基础
- [[浮动汇率下的政策效应]] — 浮动汇率制度分析
- [[固定汇率下的政策效应]] — 固定汇率制度分析
- [[不可能三角]] — 政策三难困境
- [[小型开放经济模型]] — 古典长期版本(Batch 3)
- [[购买力平价]] — 长期汇率决定理论
- [[Robert Mundell]] — 模型共同提出者
- [[Marcus Fleming]] — 模型共同提出者
- [[人民币汇率市场化]] — 中国汇率制度改革(China case)
- [[中国货币政策框架]] — 中国版本
