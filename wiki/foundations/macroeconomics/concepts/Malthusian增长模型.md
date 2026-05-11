---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 8-3"]
tags: [concept, macroeconomics, batch4, growth]
confidence: medium
decay_category: medium
status: completed
---

# Malthusian增长模型

The **Malthusian model**, based on [[Thomas Robert Malthus]]'s *An Essay on the Principle of Population* (1798), describes an economic regime in which population growth keeps per-capita income at or near subsistence level. It is the dominant framework for understanding pre-industrial economies.

## Core Mechanism

### Two Key Assumptions

1. **Food production** grows arithmetically (linearly): Each additional worker on fixed land yields diminishing marginal returns. Total output is bounded by land and natural resources.

2. **Population** grows geometrically (exponentially): When income exceeds subsistence, fertility rises and mortality falls, causing population to expand rapidly.

### The Malthusian Trap

The interaction creates a powerful negative feedback:
- A positive technology shock (better farming techniques, new crops) temporarily raises income above subsistence
- Higher income reduces mortality and increases fertility
- Population grows until income is driven back down to subsistence
- **Result**: Per-capita income is permanently pinned at subsistence; all technological gains are absorbed by population growth

### Formal Representation

Let $y$ = income per capita, $\bar{y}$ = subsistence level.

Population growth rate:
$$n(y) = \begin{cases} n_{max} & y > \bar{y} \text{ (population grows)} \\ 0 & y = \bar{y} \text{ (equilibrium)} \\ < 0 & y < \bar{y} \text{ (population declines)} \end{cases}$$

The economy has a **stable equilibrium at $y = \bar{y}$**. Any deviation triggers population adjustment that restores subsistence.

## Why the Industrial Revolution Broke the Trap

The Malthusian era ended in Western Europe around 1800 because:

1. **Technology outran population**: The rate of technological progress accelerated sufficiently that output growth exceeded population growth even at rising living standards
2. **The demographic transition**: As incomes rose, fertility eventually **fell** (the "quantity-quality tradeoff"—parents invested more in fewer children)
3. **Capital accumulation**: Land was no longer the binding constraint; reproducible capital became the primary input

This transition is the central puzzle of economic history: why did the Malthusian equilibrium persist for millennia, then collapse in a specific time and place?

## Historical Accuracy

Modern economic historians (e.g., Clark 2007, *A Farewell to Alms*) broadly confirm that:
- Pre-industrial England and other societies were in a Malthusian equilibrium
- Real wages showed no sustained trend for centuries
- Positive shocks (Black Death, New World crops) raised incomes temporarily but were eventually reversed by population growth

However, the simple Malthusian model has been refined:
- **Preventive checks**: In some societies (e.g., England with late marriage), fertility was restrained by social norms before income fell to bare subsistence
- **Disease environment**: High mortality (rather than low fertility) was often the binding constraint in tropical regions
- **Institutional factors**: Property rights and class structure affected how agricultural surplus was distributed

## Contrast with Solow

| Feature | Malthusian | Solow |
|---|---|---|
| Binding constraint | Fixed land | Reproducible capital |
| Population effect | Endogenous, restores subsistence | Exogenous, dilutes capital |
| Technology | Slowly growing, absorbed by population | Exogenous driver of per-capita growth |
| Steady-state income | Subsistence | Determined by $s$, $n$, technology |
| Applicability | Pre-1800 agrarian economies | Post-1800 industrial economies |

## In Mankiw's Textbook

Mankiw Ch 8-3 presents the Malthusian model primarily as a **contrast** to the Solow model: "Malthus's dark predictions have not come to pass" for modern economies. The textbook does not explore the model's historical validity for pre-industrial societies or the mechanisms of the Industrial Revolution transition.

This treatment understates the Malthusian model's importance: it accurately describes most of human history and is the default framework in economic history and unified growth theory.

## 反面论点与数据空白

### [CONTRADICTION] 适用边界未说明
教材将 Malthus 与 Solow 并置，却不明确说明 Malthus 描述的是前工业时代（pre-1800），而 Solow 描述的是工业时代（post-1800）。学生可能误以为 Malthus 的预测对现代经济体仍有效，或认为 Solow 可以解释所有历史时期的增长。

### [BIAS] "Malthus错了"的叙事
教材强调 "Malthus's dark predictions have not come to pass"，强化了新古典增长理论的胜利叙事。但：
- Malthus 对前工业时代的描述基本正确
- 在某些当代情境下（最穷的国家、环境资源约束），Malthusian 机制仍有相关性
- 气候变化可能重新引入资源约束，使 Malthusian 逻辑部分复活

### 数据空白
- **统一增长理论**：Galor (2000, 2011) 的 unified growth theory 将 Malthusian、post-Malthusian 和现代增长 regime 整合在一个框架中，解释从一种 regime 到另一种的 transition。教材完全未涉及
- **大分流**：Why did the Industrial Revolution happen in Britain/Europe rather than China or India? The "Great Divergence" literature (Pomeranz, *The Great Divergence* 2000) emphasizes colonialism, coal, and Atlantic trade—factors absent from both Malthus and Solow
- **当代 Malthusian 压力**：IPCC 情景下，气候变化可能重新引入资源约束，使全球南方面临 Malthusian 压力。教材的 "Malthus was wrong" 叙事掩盖了这一风险

## See Also

- [[Thomas Robert Malthus]] — Historical figure page
- [[人口增长与索洛模型]] — Comparison of Malthus, Solow, and Kremer
- [[Solow增长模型]] — Industrial-era growth framework
- [[Kremerian人口增长模型]] — Opposing view: population drives progress
- [[Michael Kremer]] — Proponent of scale effects in innovation
