---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 14-2"]
tags: [concept, macroeconomics, batch6, lucas-critique, rational-expectations, policy-evaluation]
confidence: medium
decay_category: fast
status: completed
---

# Lucas批判

The **Lucas critique**, articulated by [[Robert Lucas Jr]] in his 1976 paper "Econometric Policy Evaluation: A Critique," is one of the most consequential methodological arguments in modern macroeconomics. It states that traditional econometric models cannot be used to evaluate policy changes because their estimated parameters depend on the policy regime in place during the estimation period. When policy changes, the parameters change too.

## The Core Argument

### The Problem with Historical Estimation

Traditional Keynesian macroeconometric models (Klein-Goldberger, Wharton, Brookings) estimated behavioral equations from historical data and then used these equations to simulate the effects of policy changes.

Lucas showed this is logically invalid.

### Why Parameters Change

Economic agents optimize given their environment, including policy rules. If policy changes:
1. Agents' decision rules change
2. The estimated "structural" parameters are actually **reduced-form** combinations of deeper structural parameters and the policy rule
3. Therefore, the estimated relationships **break down** under the new policy

**Example: The Phillips Curve**
- In a regime of erratic monetary policy, agents form expectations slowly ([[适应性预期]])
- The estimated Phillips curve slope is steep (inflation responds strongly to unemployment gaps)
- If the central bank adopts inflation targeting and credible commitment, agents switch to [[理性预期]]
- The Phillips curve flattens or disappears entirely
- **Conclusion**: The original estimated slope is useless for evaluating the new policy

## Formal Statement

Consider an economic relationship estimated under policy rule $R_0$:

$$y_t = \alpha_0 + \beta_0 x_t + \varepsilon_t$$

where $\beta_0$ reflects how agents responded to $x_t$ under $R_0$. Under a new policy rule $R_1$, agents' behavior changes:

$$\beta_1 = f(R_1) \neq \beta_0$$

The estimated $\hat{\beta}_0$ from historical data tells us nothing about $\beta_1$.

## Implications

### For Policy Evaluation

- **Rejection of traditional macroeconometrics**: Historical estimated models cannot evaluate policy changes
- **Demand for microfoundations**: Models must be built from optimizing agents with deep structural parameters (preferences, technology) that are invariant to policy changes
- **Birth of DSGE**: Dynamic Stochastic General Equilibrium models explicitly incorporate optimizing agents and rational expectations

### For the Phillips Curve

The Lucas critique was particularly devastating for the Phillips curve:
- The "tradeoff" between inflation and unemployment was not a structural relationship
- It was an artifact of a particular monetary policy regime
- Under a credible low-inflation regime, the tradeoff could disappear entirely

### For Central Banking

Modern central banks now routinely worry about the Lucas critique:
- **Forward guidance**: Announcing future policy changes expectations today
- **Credibility building**: Changing the policy regime to alter private-sector behavior
- **Model uncertainty**: Recognizing that estimated relationships may not be stable

## 反面论点与数据空白

### [CONTRADICTION-1] Lucas批判的过度应用

Lucas批判被用来否定几乎所有经验宏观经济学,但:
- **一些参数确实稳定**:消费者偏好、生产技术变化缓慢,不受政策影响
- **并非所有关系都是"虚假的"**:Okun法则(产出-失业关系)在多种制度下保持稳定
- **局部均衡分析仍有用**:即使结构参数变化,方向性判断往往可靠

### [CONTRADICTION-2] 微基础模型并未更好预测

DSGE模型(微基础化的回应)在预测上并未明显优于传统模型:
- **2008危机**:DSGE模型普遍未能预测金融危机
- **参数识别问题**:DSGE中的"深层参数"同样难以识别
- **冲击的ad hoc性质**:为了拟合数据,DSGE模型引入大量未经解释的"冲击"

### [CONTRADICTION-3] 行为因素的缺失

Lucas批判假设代理人完全理性地回应政策变化。但行为经济学发现:
- **惯性**:即使政策改变,行为调整可能缓慢且不完全
- **认知限制**:代理人可能不理解政策规则的变化
- **制度摩擦**:合同、习惯、社会规范使行为对政策变化不敏感

这意味着**历史估计的某些关系可能比Lucas批判预测的更持久**。

### 数据空白

1. **Lucas批判的量化**:如何衡量一个特定关系受政策制度变化影响的程度?
2. **参数稳定性检验**:哪些宏观关系在历史上真正"断裂"了,哪些保持稳定?
3. **学习动态**:代理人需要多长时间才能完全适应新制度?
4. **发展中国家的Lucas批判**:制度不完善时,政策变化是否引发更大的参数不稳定?

## See Also

- [[理性预期]] — Lucas批判的理论基础
- [[Phillips曲线]] — Lucas批判的经典应用对象
- [[无代价反通胀]] — 理性预期框架下的政策推论
- [[适应性预期]] — Lucas批判所针对的预期形成机制
- [[新凯恩斯主义]] — 在Lucas批判压力下发展的现代宏观框架
- [[Robert Lucas Jr]] — 理论的提出者
