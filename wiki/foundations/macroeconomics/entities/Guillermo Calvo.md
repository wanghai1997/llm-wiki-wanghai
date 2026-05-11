---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 14-1 (implicit)"]
tags: [entity, macroeconomics, batch6, new-keynesian, pricing]
confidence: medium
decay_category: medium
status: completed
---

# Guillermo Calvo

**Guillermo Antonio Calvo** (born 1941), Argentine economist at Columbia University, is the creator of **Calvo pricing** (1983)—the most widely used model of nominal price stickiness in modern macroeconomics. His work provided the key microfoundation that allowed New Keynesian economists to build dynamic stochastic general equilibrium (DSGE) models with rigorous foundations for sticky prices.

## Core Contribution: Calvo Pricing (1983)

In his 1983 paper *"Staggered Prices in a Utility-Maximizing Framework,"* Calvo solved a fundamental problem in New Keynesian economics: how to model price stickiness in a way that is both **microfounded** (derived from optimizing behavior) and **tractable** (mathematically manageable for dynamic models).

### The Mechanism

In the Calvo model:
- Each firm faces a constant probability $\theta$ of being able to reset its price in any given period
- This probability is **random** and **independent** across firms and time
- A fraction $(1-\theta)$ of firms keep their prices unchanged each period
- When a firm does get to reset, it chooses a price that maximizes the expected discounted value of profits, knowing that the price may remain fixed for a random duration

### Key Implications

1. **Forward-looking pricing**: Firms set prices based on expectations of future costs and demand, not just current conditions
2. **Aggregate price level inertia**: Even though individual prices jump when reset, the aggregate price level adjusts gradually because only a fraction of firms change prices each period
3. **New Keynesian Phillips curve**: The Calvo model delivers a structural Phillips curve:
   $$\pi_t = \beta E_t\pi_{t+1} + \kappa (y_t - \bar{y}_t)$$
   where inflation depends on expected future inflation and the output gap

### Why Calvo Won Over Taylor

Before Calvo, [[John Taylor]] (1980) proposed a model of fixed-duration ("staggered") contracts. But the Calvo model became standard because:
- **Tractability**: The random-duration assumption yields a much simpler aggregation
- **No calendar-time effects**: No need to track which cohort of firms is adjusting
- **Elegant math**: The model delivers a clean, recursive Phillips curve equation

## Other Contributions

### Capital Flows and Sudden Stops

Calvo has also made major contributions to international macroeconomics:
- **"Sudden stops"** (Calvo 1998): Abrupt reversals of capital inflows to emerging markets, causing severe crises
- **Fear of floating** (Calvo and Reinhart 2002): Many countries that claim to float actually intervene heavily
- **Original sin** (Calvo and others): Emerging markets' inability to borrow in their own currencies

### Debt Crises and Default

Calvo's work on sovereign debt has shaped understanding of:
- Self-fulfilling debt crises
- The role of international lenders of last resort
- Currency boards and monetary regimes in emerging markets

## Relationship to Mankiw's Framework

Mankiw 9e Ch 14-1 presents the three theories of aggregate supply (sticky wages, sticky prices, imperfect information) in an intuitive, non-technical manner. The sticky prices discussion—particularly the idea that firms adjust prices at different times and that only a fraction change in any period—is essentially a verbal description of the Calvo mechanism.

Mankiw himself contributed to this literature with his 1985 menu cost model, but the Calvo framework is what made sticky prices tractable for dynamic general equilibrium analysis.

## Critical Assessment

The Calvo model is elegant but has limitations:
- **Random adjustment probability**: In reality, firms choose when to adjust prices; it is not purely random
- **No selection effect**: The model assumes all adjusting firms are equally "out of line"; in reality, firms with the most misaligned prices are most likely to adjust
- **Constant hazard rate**: Empirical evidence suggests the probability of adjustment increases with the duration since last adjustment

More recent work (Golosov-Lucas 2007, Midrigan 2011) has developed "state-dependent" pricing models that address these limitations, but Calvo pricing remains the workhorse of policy-oriented DSGE models.

## See Also

- [[粘性价格理论]] — The concept Calvo formalized
- [[总供给的微观基础]] — Where Calvo pricing fits in the broader picture
- [[Phillips曲线]] — The NKPC derived from Calvo pricing
- [[John Taylor]] — Staggered contracts, an alternative pricing model
- [[Robert Lucas Jr]] — The rational expectations tradition within which Calvo worked
