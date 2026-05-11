---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, welfare, taxation, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# 无谓损失DWL

## 一句话定义

> **DWL（deadweight loss）** = 价格扭曲（税 / 补贴 / 配给 / 垄断）所导致的**总剩余损失中无人获益的部分**——既不进入政府税收，也不归生产者或消费者。

## 公式（小三角形几何）

在线性需求与供给下，从量税 $t$（per unit）造成的 DWL：

$$DWL = \frac{1}{2} t^2 \cdot \frac{\varepsilon_d \cdot \varepsilon_s}{\varepsilon_d + \varepsilon_s} \cdot \frac{Q^*}{P^*}$$

其中 $\varepsilon_d$ / $\varepsilon_s$ 是需求 / 供给的价格弹性。**关键**：DWL **正比于税率的平方** —— 详见 [[DWL几何增长]]。

## 来源——[[消费者剩余]] 的"消失"部分

税前消费者剩余 $CS_0$ → 税后 $CS_1$ + 税收 $T$ + DWL，其中：
- $CS_0 - CS_1$ = 总损失（含税 + DWL）；
- $T$ = $t \cdot Q^{taxed}$ = 政府收入（重新分配）；
- DWL = $CS_0 - CS_1 - T$ = **真正消失**的福利。

## 关键参数

| 影响因素 | 作用 |
|---|---|
| 税率 $t$ | $DWL \propto t^2$ ——见 [[DWL几何增长]] |
| 替代弹性 $\sigma$ | $\sigma$ 越大 → 消费者越能"躲" → DWL 越大 |
| 需求 / 供给弹性 | 越弹性 → DWL 越大 |
| 商品在预算中的份额 | 大份额商品的扭曲影响更大 |

## 用 [[补偿需求曲线|Hicks]] 还是 [[Marshallian需求曲线|Marshall]] 度量？

教材 Ch 10 强调：**Hicks 曲线下的 DWL 是真实福利损失**；**Marshall 下的 DWL 是带 IE 偏差的近似**。仅在 [[准线性偏好]] 下两者相等。

## 在 [[Microeconomics-Nechyba-2e|Nechyba 教材]] 中的位置

教材 Ch 10 把 DWL 作为**所有扭曲性政策评估的统一度量**。Ch 22 进一步把 DWL 与最优税理论结合（Ramsey、Mirrlees——Batch 4 / 5 摄入），Ch 21 引入 Pigou 矫正性税概念以改写"DWL 一定为正"的结论（在外部性场景下 DWL 可为负）。

## DWL 与弹性的关系（Batch 4 补充）

DWL 的大小取决于供需弹性：

$$DWL \approx \frac{1}{2} \cdot t^2 \cdot X^{LR} \cdot \frac{\eta^D \eta^S}{\eta^S + \eta^D}$$

- **弹性越大** → 消费者和厂商越能"躲避"税收（转买替代品、转产）→ DWL 越大。
- **弹性越小** → 税收对行为的扭曲越小 → DWL 越小。
- **极端**：完全无弹性供给（如土地）→ $DWL = 0$（见 [[土地税]]）。

这一关系是 [[弹性与剩余分配]] 的效率侧镜像：弹性小的一方承担更多税负（分配），同时总效率损失更小。

## 教材偏置警告

⚠️ Ch 10A.3.4 节 "几乎所有现实税都低效" 强调 DWL 的不可避免性,但**不**讨论 Pigou 矫正性税（要到 Ch 21 才出现）——这与 Ch 1 [[经济学六大教训|教训 6]] "政府干预未必更好"形成连锁的"小政府"叙事。详见 [[Microeconomics-Nechyba-2e]]。

> **Batch 4 修正**：Ch 21 [[Pigou税与DWL]] 系统证明 Pigou 税**消除** DWL（与扭曲税相反）。教材 Ch 10 的"几乎所有税都低效"叙事在 Ch 21 得到修正——但读者可能在读到 Ch 21 之前已形成根深蒂固的印象。

## 反面论点与数据空白

- **[BIAS] 教材偏向"扭曲税都有 DWL"叙事**：但 Pigou 税矫正外部性时 DWL 可为负——教材在 Ch 10 不平衡讨论。
- **[BIAS] DWL 仅度量效率，不度量公平**：高 DWL 政策可能仍是"再分配公平最优"的（见 Diamond-Mirrlees）。教材未平衡。
- **数据空白**：教材的 DWL 数值（Table 10.1/10.2）依赖 $\sigma$ 校准，缺一手文献。

## 相关页

- [[消费者剩余]] / [[补偿需求曲线]] / [[Marshallian需求曲线]]
- [[DWL几何增长]] / [[总额税与扭曲税]]
- [[Laffer曲线]] / [[IRA与跨期税收]]
- [[Microeconomics-Nechyba-2e]]
