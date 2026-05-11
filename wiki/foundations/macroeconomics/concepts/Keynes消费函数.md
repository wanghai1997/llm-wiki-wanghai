---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 16-1"]
tags: [concept, macroeconomics, batch7, consumption, keynes, microfoundations]
confidence: medium
decay_category: medium
status: completed
---

# Keynes消费函数

**Keynes's consumption function** is the foundational model of household spending behavior in macroeconomics. Introduced in *The General Theory of Employment, Interest and Money* (1936), it posits that consumption depends primarily on **current disposable income**, with the marginal propensity to consume (MPC) between 0 and 1.

## The Basic Equation

$$C = \bar{C} + c(Y - T), \quad 0 < c < 1$$

- $\bar{C}$: Autonomous consumption (basic living costs, independent of income)
- $c = MPC$: Marginal propensity to consume
- $Y - T$: Disposable income

**Key properties**:
- $0 < MPC < 1$: When income rises, consumption rises but by less
- $MPC < APC$: Average propensity to consume falls as income rises
- **Current income matters**: Not wealth, not expectations, not lifetime resources

## The Consumption Puzzle

[[Simon Kuznets]] (1946) discovered a contradiction:

| Horizon | MPC Estimate | Implication |
|---|---|---|
| **Short-run** (cross-section) | ~0.9 | Keynes was approximately right |
| **Long-run** (time series) | ~1.0 | Consumption tracks income one-for-one |

**The puzzle**: If MPC < 1 in the short run, how can MPC ≈ 1 in the long run? The Keynesian model cannot explain this.

## Resolution: Later Theories

The consumption puzzle motivated the development of more sophisticated models:

1. **Fisher (1930)**: Intertemporal optimization — consumers smooth consumption over time
2. **Modigliani (1954)**: Life-cycle hypothesis — consumption depends on lifetime resources
3. **Friedman (1957)**: Permanent income hypothesis — distinguishing temporary vs. permanent income shocks
4. **Hall (1978)**: Random walk — under rational expectations, only unanticipated shocks change consumption
5. **Laibson (1997)**: Behavioral — present bias and self-control problems

See [[消费理论]] for the full hierarchy.

## In Mankiw 9e

Keynes's consumption function serves as:
- **Ch 3**: The simplest building block of the classical model
- **Ch 16**: The historical starting point, immediately followed by its limitations
- **Teaching device**: Students understand why more sophisticated models were needed

## 反面论点与数据空白

- **过度简化**: $C(Y-T)$ 把储蓄决策当成静态选择，忽略跨期最优、流动性约束、预期、风险——使古典模型在解释 2008 后消费行为时严重失败。
- **MPC 异质性不可忽略**: 把 $c$ 当常数掩盖了财富分布对加总 MPC 的影响。Auclert 2019 *Monetary Policy and the Redistribution Channel* 显示：加总 MPC 跨周期波动主要由财富分配变化驱动。
- **跨期决策被忽略**: Friedman 永久收入 / Modigliani 生命周期 / Hall 随机游走都隐含**跨期最优化**，与 Keynes 静态决策框架不兼容。详见 [[微观基础]] 中关于 Lucas 批判的讨论。
- **行为偏差**: [[Robert Shiller]] / Akerlof Animal Spirits、Laibson 双曲贴现、Thaler 心理账户等显示真实消费行为偏离任何"理性"模型——但 Keynes 本人其实已经承认了"动物精神"。
- **regional-bias**: MPC 估计集中在美国；发展中国家因金融排斥、非正式部门规模庞大，MPC 异质性可能更极端。

## See Also

- [[消费理论]] — 消费理论的完整谱系
- [[Fisher跨期选择模型]] — 跨期优化框架
- [[生命周期假说]] — Modigliani 的终身框架
- [[永久收入假说]] — Friedman 的分解
- [[随机游走假说]] — Hall 的理性预期延伸
- [[行为消费理论]] — Laibson 的行为修正
- [[古典消费函数]] — Mankiw Ch 3 简化版本
- [[Milton Friedman]] — 永久收入假说提出者
- [[Simon Kuznets]] — 消费谜题发现者
- [[John Maynard Keynes]] — 消费函数创始人
