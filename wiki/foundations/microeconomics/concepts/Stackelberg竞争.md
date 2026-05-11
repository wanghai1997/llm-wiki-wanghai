---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, foundations, batch5, oligopoly]
confidence: medium
decay_category: slow
status: foundation
---

# Stackelberg竞争

## 定义

Stackelberg竞争是寡头厂商的**序贯**竞争模型（Stackelberg 1934）：领导者先选择产量，追随者观察到领导者产量后做出最优反应。

## 双寡头模型

### 设定

- 领导者（厂商1）先选择产量 $q_1$
- 追随者（厂商2）观察到 $q_1$ 后，选择 $q_2$
- 追随者的反应函数（同Cournot）：$q_2 = R_2(q_1) = \frac{a - c - bq_1}{2b}$

### 领导者问题

领导者预期追随者的反应，将反应函数代入自身利润函数：

$$\pi_1 = [a - b(q_1 + R_2(q_1))]q_1 - cq_1$$

$$= [a - b(q_1 + \frac{a-c-bq_1}{2b})]q_1 - cq_1$$

$$= [\frac{a+c}{2} - \frac{bq_1}{2}]q_1 - cq_1$$

一阶条件：
$$\frac{a+c}{2} - bq_1 - c = 0$$

$$q_1^* = \frac{a-c}{2b}$$

### Stackelberg均衡

$$q_1^* = \frac{a-c}{2b}, \quad q_2^* = \frac{a-c}{4b}$$

总产量：$Q^* = \frac{3(a-c)}{4b}$

均衡价格：$P^* = \frac{a+3c}{4}$

## 与Cournot均衡比较

| 维度 | Stackelberg | Cournot |
|---|---|---|
| 领导者产量 | $\frac{a-c}{2b}$（更大）| $\frac{a-c}{3b}$ |
| 追随者产量 | $\frac{a-c}{4b}$（更小）| $\frac{a-c}{3b}$ |
| 总产量 | $\frac{3(a-c)}{4b}$（更大）| $\frac{2(a-c)}{3b}$ |
| 均衡价格 | $\frac{a+3c}{4}$（更低）| $\frac{a+2c}{3}$ |
| 领导者利润 | $\frac{(a-c)^2}{8b}$（更高）| $\frac{(a-c)^2}{9b}$ |
| 追随者利润 | $\frac{(a-c)^2}{16b}$（更低）| $\frac{(a-c)^2}{9b}$ |

**先动优势**：领导者产量更大、利润更高；追随者产量更小、利润更低。

## 承诺价值

先动优势的来源是**承诺的可信性**：

- 领导者一旦行动，产量成为沉没成本，不可撤销
- 追随者必须接受领导者的产量作为既定事实
- 若领导者可灵活调整产量（无承诺），则退化为Cournot均衡

### 沉没成本作为承诺装置

- 投资不可逆的产能（$k$）→ 领导者承诺生产至少 $k$ → 追随者预期高产量 → 减少自身产量
- Spence 1977；Dixit 1980 的进入威慑模型即基于此逻辑

## 反面论点与数据空白

- **领导者内生性问题**：Stackelberg模型假设领导者-追随者角色是外生的。现实中，角色通常由成本优势、产能规模、历史路径等因素内生决定。Hamilton-Slutsky 1990的内生序贯博弈模型证明，角色分配取决于厂商对"同时行动"vs"序贯行动"的偏好。
- **多领导者情形**：若存在多个潜在领导者，先动优势可能被竞争侵蚀。
- **动态承诺问题**：长期中，领导者可能重新谈判或调整产量，承诺可能失效。
- **数据空白**：Stackelberg模型的实证集中于航空业（主导航空公司设定航线容量，追随者调整）、半导体业（Intel的先发投资）。正式的结构估计困难。

## 相关页

- 原始来源：[[Heinrich von Stackelberg]]
- 对照模型：[[Cournot竞争]]、[[Bertrand竞争]]
- 承诺机制：[[进入威慑]]、[[序贯博弈]]
- 基础概念：[[子博弈精炼均衡]]、[[纳什均衡]]
- 主题页：[[不完全竞争与博弈论]]
