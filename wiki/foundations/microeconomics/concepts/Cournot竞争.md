---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, foundations, batch5, oligopoly]
confidence: medium
decay_category: slow
status: foundation
---

# Cournot竞争

## 定义

Cournot竞争是指寡头厂商以**产量**为策略变量、同时选择产量的竞争模型（Cournot 1838）。是最早的寡头理论，也是[[纳什均衡]]在特定博弈结构中的先驱。

## 双寡头模型

### 设定

- 两个厂商生产同质产品，边际成本相同 $MC_1 = MC_2 = c$
- 厂商同时选择产量 $q_1, q_2$
- 市场价格由总产量决定：$P = a - b(q_1 + q_2)$
- 厂商1的利润：$\pi_1 = [a - b(q_1 + q_2)]q_1 - cq_1$

### 反应函数

厂商1的最优反应：
$$\frac{\partial \pi_1}{\partial q_1} = a - c - 2bq_1 - bq_2 = 0$$

$$q_1 = R_1(q_2) = \frac{a - c - bq_2}{2b}$$

同理：$q_2 = R_2(q_1) = \frac{a - c - bq_1}{2b}$

### Cournot-Nash均衡

联立反应函数：
$$q_1^* = q_2^* = \frac{a - c}{3b}$$

总产量：$Q^* = \frac{2(a-c)}{3b}$

均衡价格：$P^* = a - bQ^* = \frac{a + 2c}{3}$

## 与完全竞争和垄断的比较

| 市场结构 | 产量 | 价格 | 利润 |
|---|---|---|---|
| 完全竞争 | $Q_c = \frac{a-c}{b}$ | $P_c = c$ | 0 |
| Cournot双寡头 | $Q^* = \frac{2(a-c)}{3b}$ | $P^* = \frac{a+2c}{3}$ | $\pi^* = \frac{(a-c)^2}{9b}$ |
| 垄断 | $Q_m = \frac{a-c}{2b}$ | $P_m = \frac{a+c}{2}$ | $\pi_m = \frac{(a-c)^2}{4b}$ |

- Cournot均衡介于完全竞争和垄断之间
- 随着厂商数量增加，Cournot均衡趋近完全竞争

## n厂商Cournot模型

n个相同厂商时：
- 每个厂商产量：$q^* = \frac{a-c}{(n+1)b}$
- 总产量：$Q^* = \frac{n(a-c)}{(n+1)b}$
- 均衡价格：$P^* = \frac{a + nc}{n+1}$

当 $n \to \infty$：$P^* \to c$，趋近完全竞争。

## 反面论点与数据空白

- **[BIAS] 产量作为策略变量**：现实中多数行业的竞争以价格为主（零售、航空），Cournot的产量假设可能不符合现实。但Kreps-Scheinkman 1983证明，若厂商先投资产能（数量决策），再定价，则均衡等价于Cournot——为产量竞争提供了微观基础。
- **静态假设**：Cournot模型是一次性博弈。现实中厂商可能通过产能调整、信号传递等进行动态竞争。
- **同质产品假设**：放松同质产品假设后，Cournot模型需要与产品差异化模型结合。
- **数据空白**：Cournot模型的实证检验集中于资源行业（石油、矿产）和重工业（钢铁、化工），这些行业的产量决策确实先于价格。但多数消费品的竞争更接近Bertrand模型。

## 相关页

- 原始来源：[[Antoine Augustin Cournot]]
- 对照模型：[[Bertrand竞争]]、[[Stackelberg竞争]]
- 基础概念：[[博弈论]]、[[纳什均衡]]
- 主题页：[[不完全竞争与博弈论]]
