---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 12-2"]
tags: [concept, macroeconomics, batch5, derivation]
confidence: medium
decay_category: medium
status: completed
---

# IS-LM模型推导总需求曲线

The [[总需求曲线]] can be formally derived from the [[IS-LM模型]] by allowing the price level to vary. This derivation establishes the microfoundations of aggregate demand and shows why the AD curve slopes downward.

## The Derivation

### Step 1: Fix a Price Level

For a given price level $P_1$, the real money supply is $M/P_1$. This determines the position of the LM curve.

### Step 2: Find IS-LM Equilibrium

The intersection of IS and LM at $P_1$ gives the equilibrium output $Y_1$ and interest rate $r_1$.

### Step 3: Change the Price Level

Now suppose the price level falls to $P_2 < P_1$:
- The real money supply increases: $M/P_2 > M/P_1$
- The LM curve shifts **right/down**
- The new equilibrium has lower $r_2$ and higher $Y_2$

### Step 4: Trace the AD Curve

Plotting the $(P, Y)$ pairs from different price levels traces out the downward-sloping AD curve:

```
Price Level (P)          Interest Rate (r)          Output (Y)
    │                         │                        │
P₁ ─┼─                    r₁ ─┼─                    Y₁ ─┼─
    │  \                       │  \                      │  /
    │   \  LM(P₁)              │   \  IS                 │ /   AD
    │    \                     │    \                    │/
P₂ ─┼────\───              r₂ ─┼────\───             Y₂ ─┼────────
    │      \ LM(P₂)            │      \                  │
    └───────→ Y                └───────→ Y              └───────→ P
      Y₁  Y₂                     r₂  r₁                  P₂  P₁
```

## The Three Channels (Revisited)

The IS-LM derivation makes explicit the three channels through which the price level affects output:

### 1. The Interest-Rate Effect (Keynes Effect)
$$P \downarrow \Rightarrow \frac{M}{P} \uparrow \Rightarrow r \downarrow \Rightarrow I \uparrow \Rightarrow Y \uparrow$$

This is the primary mechanism in the IS-LM framework.

### 2. The Wealth Effect (Pigou Effect)
$$P \downarrow \Rightarrow \text{real wealth} \uparrow \Rightarrow C \uparrow \Rightarrow Y \uparrow$$

This shifts the IS curve rightward as the price level falls, reinforcing the interest-rate effect.

### 3. The Exchange-Rate Effect
$$P \downarrow \Rightarrow r \downarrow \Rightarrow \text{capital outflows} \Rightarrow e \downarrow \Rightarrow NX \uparrow \Rightarrow Y \uparrow$$

This channel becomes explicit in the [[Mundell-Fleming模型]].

## Mathematical Derivation

Totally differentiating the IS-LM system:

**IS**: $Y = C(Y-T) + I(r) + G$
**LM**: $\frac{M}{P} = L(r, Y)$

Taking differentials:

$$dY = C' dY + I' dr + dG$$
$$-\frac{M}{P^2} dP = L_r dr + L_Y dY$$

Solving for $\frac{dY}{dP}$ with $dG = 0$:

$$\frac{dY}{dP} = -\frac{M/P^2 \cdot I'/(1-C')}{L_r + L_Y \cdot I'/(1-C')} < 0$$

The AD curve slopes downward because:
- $I' < 0$ (investment decreases with interest rates)
- $L_r < 0$ (money demand decreases with interest rates)
- $1 - C' > 0$ (marginal propensity to save is positive)

## Shifts in the AD Curve

Any factor that shifts IS or LM (for a given price level) shifts the AD curve:

| Shock | IS/LM Shift | AD Shift |
|---|---|---|
| $\Delta G > 0$ | IS right | AD right |
| $\Delta T < 0$ | IS right | AD right |
| $\Delta M > 0$ | LM right | AD right |
| $\Delta C > 0$ (confidence) | IS right | AD right |
| $\Delta I > 0$ (animal spirits) | IS right | AD right |

## AD Curve Slope and Parameter Sensitivity

The slope of the AD curve depends on:

**Flatter AD** (more output response to price changes):
- Large interest sensitivity of money demand ($|L_r|$ large)
- Large interest sensitivity of investment ($|I'|$ large)
- Large multiplier ($1/(1-MPC)$ large)

**Steeper AD** (less output response):
- Small interest sensitivity of money demand
- Small interest sensitivity of investment
- Small multiplier

In the extreme:
- **Liquidity trap** ($L_r \to -\infty$): LM horizontal, AD vertical (prices do not affect output)
- **Classical case** ($L_r = 0$): LM vertical, AD has finite slope

## 反面论点与数据空白

### [CONTRADICTION-1] 推导依赖强假设

AD曲线的IS-LM推导依赖于:
- **固定名义货币供给M**:但现代央行以利率为目标,M内生
- **价格水平变化不影响IS**:但价格变化影响实际财富(Pigou效应)和实际汇率,这些应在IS中体现
- **静态预期**:预期价格变化会影响当前行为,但模型未纳入

如果央行以利率为目标(现实情况),价格下降不会自动增加M/P——央行会调整M以维持目标利率。此时AD曲线的推导需要重新考虑。

### [CONTRADICTION-2] 零利率下限时的AD曲线

在流动性陷阱中:
- LM水平,AD垂直
- 价格下降不能进一步降低利率
- 产出对价格变化完全不敏感

这意味着**通缩可能无法自我修复**——价格下降不会自动刺激需求。这是日本"失去的二十年"和2008后发达经济体的核心问题,但教材对AD垂直性的政策含义讨论不足。

### 数据空白

1. **AD曲线的实证估计**:由于无法直接观测AD,只能用SVAR等方法识别——结果高度依赖识别假设
2. **非线性AD**:在零利率附近,AD可能呈现"折线"形状——传统线性分析不适用
3. **全球AD**:在高度开放的经济体中,国内AD受全球价格和利率影响,而非仅国内因素

## See Also

- [[总需求曲线]] — 推导的目标
- [[IS-LM模型]] — 推导的工具
- [[IS曲线]] — 产品市场均衡
- [[LM曲线]] — 货币市场均衡
- [[AD-AS模型]] — AD曲线的应用场景
- [[Mundell-Fleming模型]] — 开放经济扩展
