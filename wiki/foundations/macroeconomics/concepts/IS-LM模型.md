---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 11-3"]
tags: [concept, macroeconomics, batch5, core-model, is-lm]
confidence: medium
decay_category: medium
status: completed
---

# IS-LM模型

The **IS-LM model** (Investment–Saving / Liquidity preference–Money supply) is the canonical framework for analyzing short-run equilibrium in a closed economy. Developed by [[John Hicks]] (1937) and popularized by [[Alvin Hansen]], it combines goods market equilibrium (the [[IS曲线]]) with money market equilibrium (the [[LM曲线]]) to determine the equilibrium interest rate ($r^*$) and output ($Y^*$).

## Model Structure

```
Interest Rate (r)
    │
    │         LM
    │        /
    │       /
    │      /  IS
    │     / /
    │    / /
    │   / /
    │  / /
    │ / /
    └●/──────────→ Output (Y)
     r* Y*
```

**IS curve** (downward-sloping): $Y = C(Y-T) + I(r) + G$
**LM curve** (upward-sloping): $M/P = L(r, Y)$

**Equilibrium**: The intersection determines the unique $(r^*, Y^*)$ pair where both markets clear simultaneously.

## Comparative Statics

### Expansionary Fiscal Policy ($\Delta G > 0$ or $\Delta T < 0$)
- IS shifts right
- **Short-run effect**: $Y \uparrow$, $r \uparrow$
- **Crowding out**: Higher $r$ reduces investment, partially offsetting the fiscal expansion
- The output increase is smaller than the [[凯恩斯交叉模型]] predicts

### Expansionary Monetary Policy ($\Delta M > 0$)
- LM shifts right/down
- **Short-run effect**: $r \downarrow$, $Y \uparrow$
- Lower interest rates stimulate investment
- No crowding out (in fact, "crowding in" as lower rates boost investment)

### Contractionary Policies
- Fiscal austerity: IS shifts left, $Y \downarrow$, $r \downarrow$
- Monetary tightening: LM shifts left/up, $r \uparrow$, $Y \downarrow$

## Policy Mixes

Policymakers can combine fiscal and monetary policy:

| Policy Mix | Effect on $Y$ | Effect on $r$ | Example |
|---|---|---|---|
| Exp. fiscal + Exp. monetary | Strong $Y \uparrow$ | Ambiguous | 2009 stimulus + QE |
| Exp. fiscal + Cont. monetary | Modest $Y \uparrow$ | Strong $r \uparrow$ | 1980s US deficits |
| Cont. fiscal + Exp. monetary | Modest $Y \uparrow$ | Strong $r \downarrow$ | 1990s Clinton boom |
| Cont. fiscal + Cont. monetary | Strong $Y \downarrow$ | Ambiguous | Volcker disinflation |

## From IS-LM to Aggregate Demand

In Ch 12, Mankiw derives the [[总需求曲线]] from IS-LM:
- For a given price level $P$, the real money supply $M/P$ determines the LM position
- The IS-LM intersection gives equilibrium $Y$
- As $P$ falls, $M/P$ rises, LM shifts right, and equilibrium $Y$ rises
- Tracing these $(P, Y)$ pairs yields the downward-sloping AD curve

## Limitations and Assumptions

The IS-LM model assumes:
1. **Fixed price level** in the short run
2. **Closed economy** (relaxed in Mundell-Fleming)
3. **Static expectations**
4. **No international trade or capital flows** (in basic form)
5. **Exogenous investment function** (no financial accelerator)

These assumptions are progressively relaxed in more advanced models.

## Historical Significance

IS-LM dominated macroeconomic teaching and policymaking from the 1940s through the 1960s. It was the analytical backbone of:
- New Deal demand management
- Post-war Keynesian fiscal policy
- The Kennedy-Johnson tax cut of 1964
- Early Federal Reserve operational frameworks

Its decline began in the 1970s with the rise of monetarism, rational expectations, and real business cycle theory.

## 反面论点与数据空白

### [CONTRADICTION-1] IS-LM作为"教学模型" vs "政策工具"的张力

IS-LM是本科教学的核心模型,但现代央行决策几乎不直接使用它:
- **美联储**:FRB/US模型、DSGE模型、大量实时数据
- **欧央行**:NAWM、双支柱框架
- **中国人民银行**:多目标、多工具的综合框架

IS-LM的二维简化无法捕捉:
- 金融中介和信贷摩擦(Bernanke-Gertler-Gilchrist 1999)
- 预期和前瞻指引
- 多期动态、滞后效应、状态依赖
- 收入分配效应

教材将IS-LM呈现为"宏观经济学的主模型",但实际是"教学入门模型",这一差距未向学生明确说明。

### [CONTRADICTION-2] Lucas批判

[[Robert Lucas Jr]] (1976)指出:IS-LM中的参数(MPC,货币需求弹性等)是从历史数据估计的,但如果政策制度系统性改变,这些参数本身会变化。因此用IS-LM进行政策评估是可靠的——如果政策只是临时波动;但不可靠——如果政策规则永久改变。

这使得基于IS-LM的"乘数"和"政策效应"估计在政策创新时期(如2008后的QE)失去可信度。

### [CONTRADICTION-3] 挤出效应的实证微弱性

IS-LM预测财政政策会推高利率并挤出投资,但:
- **2008-2020**:美国巨额财政赤字伴随极低利率——没有挤出
- **日本**:政府债务/GDP超过260%,利率仍接近零——没有挤出
- **安全资产短缺**:Caballero等指出全球对安全资产的需求使发达国家可以大量发债而不推高利率

这些现象暗示IS-LM在流动性充裕、安全资产需求旺盛的环境中可能系统性失效。

### 数据空白

1. **非线性IS-LM**:在零下限、高债务、金融压力时期,关系可能非线性
2. **金融部门的角色**:银行信贷渠道在IS-LM中完全缺失
3. **全球IS-LM**:资本流动使一国IS-LM受全球利率和需求影响
4. **数字货币**:CBDC可能改变LM机制

## See Also

- [[IS曲线]] — 产品市场均衡
- [[LM曲线]] — 货币市场均衡
- [[总需求曲线]] — 从IS-LM推导
- [[凯恩斯交叉模型]] — IS-LM的基础
- [[Mundell-Fleming模型]] — 开放经济扩展
- [[流动性陷阱]] — IS-LM的极端情形
- [[John Hicks]] — 模型的提出者
- [[Alvin Hansen]] — 模型的普及者
