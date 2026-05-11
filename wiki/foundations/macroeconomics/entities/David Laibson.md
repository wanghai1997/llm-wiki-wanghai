---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 16-5"]
tags: [entity, macroeconomics, batch7, behavioral-economics, consumption, hyperbolic-discounting]
confidence: medium
decay_category: medium
status: completed
---

# David Laibson

**David Laibson** (b. 1966) is an American economist at Harvard University and a leading figure in **behavioral economics**, particularly in applying psychological insights to macroeconomic questions of consumption, saving, and financial decision-making. He is best known for introducing **quasi-hyperbolic discounting** (the $\beta$-$\delta$ model) into economics, providing a formal framework for understanding time-inconsistent preferences and self-control problems.

## Quasi-Hyperbolic Discounting ($\beta$-$\delta$ Model)

### The Problem with Exponential Discounting

Standard economics assumes **exponential discounting**: utility at time $t$ is discounted by $\delta^t$ where $\delta < 1$.

$$U_t = u_t + \delta u_{t+1} + \delta^2 u_{t+2} + \cdots$$

This implies **time-consistent** preferences: the relative tradeoff between $t+1$ and $t+2$ is the same whether evaluated at $t$ or at $t+1$.

### The $\beta$-$\delta$ Model

Laibson (1997, "Golden Eggs and Hyperbolic Discounting") proposed:

$$U_t = u_t + \beta\delta u_{t+1} + \beta\delta^2 u_{t+2} + \beta\delta^3 u_{t+3} + \cdots$$

where:
- $\delta < 1$: standard long-run discount factor
- $\beta < 1$: **additional** short-run discount factor (present bias)

**The key implication**: From the perspective of today, the near future ($t+1$) is discounted by $\beta\delta$, while the distant future ($t+2, t+3, ...$) is discounted by $\beta\delta^2, \beta\delta^3$, etc. The **relative** discount between $t+1$ and $t+2$ is $\delta$.

But when tomorrow arrives, the perspective shifts: $t+1$ becomes "now," and the relative discount between $t+1$ and $t+2$ becomes $\beta\delta / \beta\delta^2 = 1/\delta$ — a fundamentally different tradeoff.

### Time Inconsistency

This creates a conflict between:
- **The "planner" self** (today): Wants to save for retirement
- **The "doer" self** (tomorrow): Wants to consume now

**Empirical estimates**: Laibson et al. (2007) estimate $\beta \approx 0.5$–$0.7$ for typical consumers — a substantial present bias.

## Applications to Consumption and Saving

### The Consumption-Saving Puzzle

Laibson's model explains several puzzles that standard models cannot:

1. **Low retirement savings**: Even when 401(k) plans are available, many workers under-save
2. **Credit card debt**: High-interest credit card borrowing coexists with low-interest savings
3. **MPC out of tax rebates**: Consumers spend 20-40% of tax rebates immediately — higher than PIH predicts
4. **Commitment devices**: People use illiquid savings (retirement accounts, home equity) to constrain future consumption

### The "Golden Eggs" Strategy

Laibson showed that consumers with present bias will:
- Prefer **illiquid assets** (retirement accounts, housing) that constrain future consumption
- Avoid **liquid assets** that tempt immediate spending
- This explains the prevalence of commitment devices in financial markets

## Behavioral Macroeconomics

Laibson's work extends beyond consumption to broader macro questions:

- **Asset pricing**: Present bias may contribute to equity premium puzzles and bubbles
- **Monetary policy**: Consumers with present bias may respond differently to interest rate changes
- **Public policy**: "Nudges" (default enrollment in savings plans, commitment savings products) may be more effective than price incentives

## 反面论点与数据空白

- **$\beta$-$\delta$模型的简化性**: 模型假设所有"未来"被同等对待(除当期外),但现实中人们对"下周"vs"明年"vs"十年后"的贴现可能呈连续递减。其他模型(如Loewenstein-Prelec 1992 generalized hyperbolic)可能更灵活。
- **$\beta$的异质性**: 实证估计的$\beta$差异巨大(0.3-0.9),取决于测量方法(实验、田野数据、结构性估计)。可能不存在单一的"$\beta$",而是情境依赖的。
- **神经科学证据**: 神经经济学发现大脑不同区域(边缘系统vs前额叶皮层)对即时和延迟回报的反应不同,支持present bias的生物学基础。但神经证据与$\beta$-$\delta$模型的精确对应关系尚不明确。
- **政策应用的伦理争议**: 如果消费者有present bias,政府/企业是否应该"纠正"其选择?自由主义家长主义(Thaler-Sunstein)认为应助推其向长期最优;批评者认为这是精英对普通选择的干预。平台算法利用present bias(如短视频的无限滚动)是反向应用。
- **regional-bias**: Laibson的研究以美国消费者和金融市场为背景。发展中国家(信贷市场不发达、非正规金融、家庭网络作为保险)中present bias的表现和后果可能截然不同。

## See Also

- [[行为消费理论]] — Laibson框架的概念页
- [[现时偏向偏好]] — (微观侧) Beta-delta模型的基础
- [[承诺装置]] — (微观侧) 应对时间不一致的工具
- [[永久收入假说]] — Laibson修正的标准模型
- [[随机游走假说]] — 理性预期下的消费路径
- [[时间不一致性]] — 政策层面的时间不一致
- [[Richard Thaler]] — 行为经济学/自由主义家长主义

