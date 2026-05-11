---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [概念, microeconomics, foundations, batch3, 一般均衡]
confidence: medium
decay_category: slow
status: foundation
---

# 核Core

> 一般均衡的合作博弈论概念。**任意联盟都无法阻断**的可达配置集合。两人经济中,核 = 互惠交易集 ∩ 契约曲线;多人经济中核更小。Edgeworth 1881 提出 recontracting 思想;Shubik 1959 / Debreu-Scarf 1963 给出现代核收敛定理。

## 形式定义

设 $N$ 人经济,禀赋 $\{\omega^i\}_{i=1}^N$,可达配置 $\{x^i\}_{i=1}^N$ 满足 $\sum x^i = \sum \omega^i$。

**联盟阻断**:存在子集 $S \subseteq N$ 与替代配置 $\{y^i\}_{i \in S}$,使
1. $\sum_{i \in S} y^i = \sum_{i \in S} \omega^i$(联盟内部资源约束)
2. 每个 $i \in S$ 满足 $U^i(y^i) \ge U^i(x^i)$,且至少一人严格 > 。

**核**:不能被任何联盟阻断的可达配置之集合 = $C$。

## 与 MB / 契约曲线的关系

两人经济($N=2$):
- 阻断联盟有三种:$\{A\}$、$\{B\}$、$\{A, B\}$。
- $\{A\}$ 单人阻断 $x$ ⇔ $U^A(\omega^A) > U^A(x^A)$ → 排除 MB 外的配置。
- $\{B\}$ 单人阻断 $x$ ⇔ $U^B(\omega^B) > U^B(x^B)$ → 同上。
- $\{A, B\}$ 全联盟阻断 $x$ ⇔ 存在 Pareto 改进 → 排除契约曲线外的配置。

→ **两人经济中**:$C = MB \cap CC$ = 互惠交易集 ∩ 契约曲线。

## 多人经济中核更小

$N \ge 3$ 时,中间联盟(如 $\{A, B\}$)可能阻断某些 $MB \cap CC$ 内的配置 → 核进一步收缩。

> **直觉**:$N$ 越大,可能的阻断联盟越多,核越小。极限下($N \to \infty$,经济**复制**),核收敛于 Walras 均衡集合。详见 [[核收敛定理]]。

## Walras 均衡 ⊆ 核

任意 Walras 均衡 $(p^*, x^*)$ 都属于核——即不存在联盟能给所有成员带来与 Walras 均衡相比的严格改进。

> **几何直觉**:Walras 均衡 = 价格作用下的稳态。任何脱离 Walras 均衡的"再谈判"必然使某人变差(否则不是均衡)。

形式证明:Edgeworth 1881 / Debreu-Scarf 1963 给出。

## 核收敛定理

**Edgeworth 1881 conjecture**:经济复制(每个消费者类型有 $r$ 个相同副本)时,核 → Walras 均衡集合。

**Debreu-Scarf 1963 *International Economic Review*** 严格证明这一收敛——大经济中核与 Walras 均衡几乎重合。

详见 [[核收敛定理]]。

## 与博弈论的连接

核是合作博弈论的核心概念,与非合作博弈论(Nash 均衡)对偶:
- **非合作均衡**(Walras / Nash):每人在给定他人策略 / 价格下最优。
- **合作均衡**(核):没有联盟能形成更优的协议。

Walras 均衡 ⊆ 核 + 核收敛于 Walras 均衡(大经济极限) → 两个均衡概念在大经济中等价。这是 *price-taking* 假设的合作博弈论辩护。

## 应用

- **房屋分配市场**:Shapley-Scarf 1974 *"On Cores and Indivisibility"* 证明 Top Trading Cycle 算法收敛于核中唯一点。
- **匹配市场**:Gale-Shapley 1962 *American Mathematical Monthly* "College Admissions and the Stability of Marriage" 证明稳定匹配 ∈ 核。
- **公司控制权交易**:Shapley-Shubik 1969 *"On Market Games"* 模型公司股东与债权人议价的核。

## 反面论点与数据空白

- **大数定律假设**:核收敛定理假设经济**复制**(每类消费者无穷多副本)——现实经济中既有大型企业(规模决定影响),也有小型主体(数量决定影响),不严格符合"复制"。
- **完全信息假设**:核的定义假设各联盟知道所有禀赋 / 偏好;现实中信息不对称使联盟形成困难。
- **联盟形成的成本**:Olson 1965 *Logic of Collective Action* 强调联盟形成有交易成本——即使存在改进性联盟,可能因协调成本无法形成。
- **公平失踪**:核中的某些点可能极不平等(类似契约曲线的批评)——核是"自愿"概念,不解决初始禀赋不公平。
- **数据空白**:实验经济学(Plott-Smith 1978 / Roth 1995 综述)展示真实议价收敛于核某子集,但具体收敛点 + 速度依赖制度细节。
- **动态稳定性**:核是静态概念,不考虑联盟形成 + 重组的动态。Shubik 1985 *Game Theory in the Social Sciences* 提出动态扩展,但教材不展开。

## 相关页

- 上游:[[Edgeworth盒]] / [[Francis Edgeworth]] / [[互惠交易集MB]] / [[契约曲线]]
- 阻断:[[阻断联盟]]
- 大经济极限:[[核收敛定理]]
- 福利定理:[[第一福利定理]] / [[第二福利定理]]
- 主题:[[一般均衡]]
