---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 8-1"]
tags: [concept, macroeconomics, batch4, growth]
confidence: medium
decay_category: slow
status: completed
---

# Solow增长模型

The **Solow growth model** (Solow 1956; Swan 1956) is the foundational framework of neoclassical growth theory. It explains how capital accumulation, population growth, and technological progress interact to determine long-run standards of living.

## Model Setup

### Production Function

The economy produces a single good using capital and labor:

$$Y = F(K, L)$$

Assumptions:
- **Constant returns to scale (CRS)**: $F(\lambda K, \lambda L) = \lambda F(K, L)$
- **Diminishing marginal product of capital**: $\partial^2 F / \partial K^2 < 0$
- **Inada conditions**: $F_K \to \infty$ as $K \to 0$; $F_K \to 0$ as $K \to \infty$

By defining per-worker quantities $y = Y/L$ and $k = K/L$, CRS implies:

$$y = f(k) = F(k, 1)$$

where $f'(k) > 0$ and $f''(k) < 0$.

### Capital Accumulation

Output is divided between consumption and investment. A constant fraction $s$ is saved and invested:

$$\Delta k = sf(k) - \delta k$$

where:
- $s$ = saving rate (exogenous)
- $\delta$ = depreciation rate
- $sf(k)$ = actual investment per worker
- $\delta k$ = break-even investment (to keep $k$ constant given depreciation)

## Steady State

The **steady state** $k^*$ occurs when investment equals depreciation:

$$sf(k^*) = \delta k^*$$

At $k^*$:
- Per-capita capital is constant: $\Delta k = 0$
- Per-capita output is constant: $y^* = f(k^*)$
- Total output grows at rate $n$ (population growth)

### Dynamics
- If $k < k^*$: $sf(k) > \delta k$, so $k$ rises toward $k^*$
- If $k > k^*$: $sf(k) < \delta k$, so $k$ falls toward $k^*$

The steady state is **globally stable**: the economy converges to $k^*$ from any initial $k_0 > 0$.

## Comparative Statics

### Higher Saving Rate
An increase in $s$ shifts the investment curve up, raising $k^*$ and $y^*$. However:
- The economy experiences **temporary growth** during transition to the new steady state
- In the **new steady state**, per-capita growth returns to zero
- Thus, saving has a **level effect** but **no long-run growth effect**

### Population Growth
When population grows at rate $n$ (see [[人口增长与索洛模型]]), break-even investment becomes $(\delta + n)k$:

$$\Delta k = sf(k) - (\delta + n)k$$

Higher $n$ raises break-even investment, lowering $k^*$ and $y^*$.

### Technological Progress
When labor-augmenting technology grows at rate $g$ (see [[技术进步与索洛模型]]), the effective per-worker capital stock evolves as:

$$\Delta \tilde{k} = sf(\tilde{k}) - (\delta + n + g)\tilde{k}$$

where $\tilde{k} = K/(L \cdot E)$ and $E$ grows at rate $g$. Now the steady state features **positive per-capita growth at rate $g$**.

## The Golden Rule

The steady state that **maximizes consumption per capita** is called the **Golden Rule** level of capital (see [[黄金律资本水平]]):

$$MPK = \delta + n + g$$

or equivalently, $MPK - \delta = n + g$.

## Key Predictions and Their Empirical Fate

| Prediction | Empirical Status |
|---|---|
| Absolute convergence (poor countries grow faster unconditionally) | **Rejected**: no unconditional convergence across all countries |
| Conditional convergence (countries converge to their own steady states) | **Supported**: convergence holds after controlling for $s$, $n$, human capital |
| Factor shares are stable | **Supported**: roughly 1/3 capital, 2/3 labor |
| Saving rate affects level but not long-run growth rate | **Supported**: rich countries don't grow faster than poor ones in steady state |

The [[Mankiw-Romer-Weil模型]] (1992) resolved the absolute convergence puzzle by adding human capital as a third factor.

## 反面论点与数据空白

### [CONTRADICTION-1] Level Effect vs Transitional Growth
The textbook (Ch 8-1, p.221) states that "higher saving rate is said to have a **level effect**" and "only the level of income per person—not its growth rate—is influenced by the saving rate in the steady state." Yet Ch 9-3 (p.252) says increasing savings would make the economy "grow more rapidly and eventually reach a steady state with higher consumption." This creates a **wording trap**: "grow more rapidly" refers to **transitional dynamics**, not steady-state growth. The textbook never explicitly marks this distinction in Chinese pedagogical terms. Students frequently conflate the two.

### [CONTRADICTION-2] Three Incompatible Population-Growth Theories
Ch 8-3 presents Solow, Malthus, and Kremer in the same section without explaining their mutually exclusive predictions or historical boundaries. Solow says higher $n$ lowers $y^*$; Malthus says population keeps income at subsistence; Kremer says larger population accelerates technology. All three are presented as "perspectives" without the crucial caveat: **Malthus describes pre-industrial agrarian economies; Solow describes industrial market economies with exogenous technology; Kremer describes the very long run or innovation-cluster dynamics.** The textbook's silence on boundaries is a significant conceptual gap.

### [BIAS-1] Neoclassical Growth as "Victory Narrative"
Ch 9-2 (p.246) frames growth theory history as Solow's triumph over Marx: "Marx predicted that the return to capital would decline over time... Economic history has not supported Marx's prediction." This presentation erases the post-Keynesian growth tradition (Kaldor 1957 distribution theory, Pasinetti structural dynamics) and structuralist development economics (Prebisch-Singer hypothesis). The textbook implicitly presents neoclassical growth as the only viable framework—a methodological choice reflecting its mainstream New Keynesian orientation.

### 数据空白
- The basic Solow model omits **human capital**, which the [[Mankiw-Romer-Weil模型]] shows is empirically essential
- The model assumes **exogenous technology**, which [[Paul Romer]] and subsequent endogenous growth theory internalized
- **Ramsey-Cass-Koopmans optimal growth**: The Solow model takes $s$ as exogenous; the Ramsey model derives optimal savings from household utility maximization. Mankiw's textbook omits this foundational framework entirely
- **Overlapping Generations (Diamond 1965)**: The standard tool for analyzing dynamic inefficiency (overaccumulation of capital) is absent from the textbook

## See Also

- [[Robert Solow]] / [[Trevor Swan]] — Model originators
- [[资本积累与稳态]] — Investment-depreciation mechanism and transition dynamics
- [[储蓄率与经济增长]] — Level effect vs growth effect distinction
- [[黄金律资本水平]] — Consumption-maximizing steady state
- [[人口增长与索洛模型]] — Population growth in the Solow framework
- [[技术进步与索洛模型]] — Labor-augmenting technical change
- [[Mankiw-Romer-Weil模型]] — Augmented Solow with human capital
- [[内生增长理论]] — Models that endogenize technological progress
- [[平衡增长路径]] — Kaldor stylized facts and the model's reconciliation thereof
