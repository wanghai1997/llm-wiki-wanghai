---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 16-2"]
tags: [concept, macroeconomics, batch7, consumption, intertemporal-choice, fisher]
confidence: medium
decay_category: medium
status: completed
---

# Fisher跨期选择模型

Irving Fisher's **intertemporal choice model** (1930) is the foundational framework for modern consumption theory. It models consumers as choosing consumption across time periods to maximize lifetime utility, subject to a lifetime budget constraint. All subsequent consumption theories (Modigliani's life-cycle, Friedman's permanent income, Hall's random walk) are extensions of this core framework.

## The Two-Period Model

### Setup

A consumer lives for two periods with:
- Income: $y_1$ (period 1), $y_2$ (period 2)
- Consumption: $c_1$ (period 1), $c_2$ (period 2)
- Interest rate: $r$ (for borrowing and lending)

### The Budget Constraint

**Period-by-period**:
$$c_1 + s = y_1$$
$$c_2 = y_2 + (1+r)s$$

Combining (eliminating $s$):
$$c_1 + \frac{c_2}{1+r} = y_1 + \frac{y_2}{1+r}$$

**The intertemporal budget constraint**: The present value of lifetime consumption equals the present value of lifetime income.

### Graphical Representation

```
c₂
│
│    ● (endowment point: y₁, y₂)
│   /│
│  / │  Budget line: slope = -(1+r)
│ /  │
├────┼────────
│    │\  Indifference curves
│    │ \
└────┴────────→ c₁
```

- **Endowment point**: $(y_1, y_2)$ — consumption if the consumer neither borrows nor lends
- **Budget line slope**: $-(1+r)$ — the rate at which the market allows trading $c_1$ for $c_2$
- **Optimal consumption**: Where the budget line is tangent to the highest attainable indifference curve

### The Optimality Condition

$$MRS = 1 + r$$

where $MRS = \frac{MU_1}{MU_2}$ is the marginal rate of substitution between period-1 and period-2 consumption.

**Interpretation**: At the optimum, the consumer's subjective tradeoff between current and future consumption equals the market tradeoff (the interest rate).

## Consumption Smoothing

### The Core Insight

Consumers prefer a **smooth consumption path** rather than matching consumption to income in each period.

**Example**: A consumer with $y_1 = 100$, $y_2 = 50$, $r = 0$:
- No smoothing: $c_1 = 100$, $c_2 = 50$
- With smoothing: $c_1 = c_2 = 75$ (save 25 in period 1, consume savings in period 2)

### The Role of the Interest Rate

An increase in $r$ rotates the budget line:
- **Substitution effect**: $c_1$ becomes more expensive relative to $c_2$ → consume less today, more tomorrow
- **Income effect**: Higher $r$ increases lifetime resources (if a net saver) → may consume more in both periods
- **Net effect on saving**: Ambiguous; depends on whether substitution or income effect dominates

### Borrowing Constraints

If consumers cannot borrow ($s \geq 0$):
- The budget constraint becomes $c_1 \leq y_1$
- Consumers who would like to consume more than $y_1$ are constrained
- **Key implication**: Current income directly affects consumption for constrained consumers, even if lifetime income is unchanged

## Extensions to Multi-Period and Uncertainty

### The T-Period Model

$$\sum_{t=1}^{T} \frac{c_t}{(1+r)^t} = \sum_{t=1}^{T} \frac{y_t}{(1+r)^t} + W_0$$

where $W_0$ is initial wealth.

### The Euler Equation

For a consumer with CRRA utility $U(c) = \frac{c^{1-\sigma}}{1-\sigma}$:

$$\frac{c_{t+1}}{c_t} = \left[\frac{1+r}{1+\rho}\right]^{1/\sigma}$$

where $\rho$ is the rate of time preference.

**Key implications**:
- If $r > \rho$: consumption grows over time ($c_{t+1} > c_t$)
- If $r < \rho$: consumption falls over time
- The elasticity of intertemporal substitution ($1/\sigma$) determines how responsive consumption growth is to $r - \rho$

### Uncertainty

With uncertain future income, the Euler equation becomes:

$$U'(c_t) = \frac{1+r}{1+\rho} E_t[U'(c_{t+1})]$$

This is the foundation for **precautionary saving**: if utility is convex in consumption ($U''' > 0$), uncertainty about future income increases current saving.

## 反面论点与数据空白

### [CONTRADICTION-1] 消费过度敏感(Excess Sensitivity)

Flavin (1981) found that consumption responds more to **predictable** changes in current income than the Fisher model predicts. If consumers are forward-looking and unconstrained, only **unanticipated** income changes should affect consumption.

**Possible explanations**:
- **Liquidity constraints**: Many households cannot borrow
- **Rule-of-thumb consumers**: Some fraction of households simply spend current income
- **Near-rationality**: Small costs of optimization lead to inertia

### [CONTRADICTION-2] 消费过度平滑(Excess Smoothness)

Campbell-Deaton (1989) found that consumption is **too smooth** relative to permanent income. If income follows a random walk, consumption should be as volatile as income. In reality, consumption is smoother.

**Possible explanations**:
- **Partial information**: Consumers cannot perfectly distinguish permanent from transitory shocks
- **Habit formation**: Past consumption affects current utility, creating inertia
- **Aggregation**: Individual consumption may be volatile, but aggregate is smooth due to averaging

### [CONTRADICTION-3] 利率弹性微弱

The model predicts strong response of consumption growth to $r - \rho$. But empirically:
- **Housing consumption** responds to mortgage rates
- **Nondurable consumption** shows very low interest elasticity
- **Overall saving rate**: Appears relatively insensitive to interest rate changes

### [CONTRADICTION-4] 代表性代理人假设

Fisher模型假设单一代表性代理人,但:
- **Kaplan-Moll-Violante (2018)**: 不同wealth群体的MPC差异巨大(穷人~0.5,富人~0.05)
- **HANK模型**: 异质性代理人新凯恩斯模型显示aggregate结果与representative agent截然不同
- **信贷市场分割**: 穷人面对借贷约束,富人不受约束

### 数据空白

1. **借贷约束的量化**: 多少家庭受约束?约束如何随周期变化?
2. **习惯形成参数**: 习惯强度在不同商品、不同国家如何变化?
3. **中国的跨期选择**: 高储蓄率、高房价、独生子女政策如何改变生命周期消费模式?
4. **数字金融的影响**: 移动支付、P2P借贷、消费信贷APP是否放松了借贷约束?

## See Also

- [[消费理论]] — 消费理论的完整谱系
- [[生命周期假说]] — Fisher模型的生命周期间扩展
- [[永久收入假说]] — Fisher模型的收入分解扩展
- [[随机游走假说]] — Fisher模型+理性预期
- [[行为消费理论]] — Fisher模型+行为偏差
- [[跨期预算约束]] — (微观侧) 消费侧基础概念
- [[禀赋经济中的SE-IE]] — (微观侧) 利率变化的SE-IE分解

