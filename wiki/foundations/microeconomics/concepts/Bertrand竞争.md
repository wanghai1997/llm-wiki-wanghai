---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, foundations, batch5, oligopoly]
confidence: medium
decay_category: slow
status: foundation
---

# Bertrand竞争

## 定义

Bertrand竞争是指寡头厂商以**价格**为策略变量、同时设定价格的竞争模型（Bertrand 1883）。与[[Cournot竞争]]（数量竞争）形成核心对照。

## 同质产品Bertrand模型

### 设定

- 两个厂商生产**同质产品**，边际成本相同 $MC_1 = MC_2 = c$
- 厂商同时设定价格 $P_1, P_2$
- 消费者只购买价格最低的厂商的产品（若价格相同，则平分市场）
- 需求函数：$Q = D(P)$（向下倾斜）

### 均衡

**Bertrand悖论**：唯一纳什均衡是 $P_1 = P_2 = MC = c$，利润为零。

推导：
- 若 $P_1 > P_2 > c$：厂商1可获得整个市场，有动机将价格降至略低于 $P_2$
- 若 $P_1 = P_2 > c$：任一厂商有动机将价格降至略低于对手，夺取全部市场
- 若 $P_1 = P_2 = c$：任何提价都失去全部市场，降价则亏损

**结论**：仅有两个厂商的Bertrand竞争即可达到完全竞争的结果。

## 差异化产品Bertrand模型

当产品存在差异化时，Bertrand悖论消解：

- 需求函数：$Q_i = D_i(P_i, P_j)$，满足 $\frac{\partial Q_i}{\partial P_i} < 0$，$\frac{\partial Q_i}{\partial P_j} > 0$
- 均衡：$P_1^* > c$，$P_2^* > c$，利润为正

均衡条件：$MR_i = P_i + Q_i \frac{\partial P_i}{\partial Q_i} = MC_i$

产品差异化程度越高，均衡价格越接近垄断价格。

## 与Cournot竞争比较

| 维度 | Bertrand（价格竞争） | Cournot（数量竞争） |
|---|---|---|
| 策略变量 | 价格 | 产量 |
| 同质产品均衡 | $P = MC$（完全竞争） | $P > MC$（介于垄断与竞争之间）|
| 差异化产品均衡 | $P > MC$，利润为正 | $P > MC$，利润为正 |
| 福利（同质产品）| 最高 | 中等 |
| 福利（差异化）| 取决于产品替代程度 | 取决于产品替代程度 |

## 产能约束与Kreps-Scheinkman模型

Kreps-Scheinkman 1983证明：若厂商先投资产能（Cournot阶段），再定价（Bertrand阶段），则均衡等价于Cournot结果。

- 产能约束打破了Bertrand悖论的极端结论
- 解释了为什么现实中价格竞争未必导致完全竞争

## 反面论点与数据空白

- **[BIAS] 价格匹配的悖论**：现实中厂商常承诺"价格匹配"（match any lower price）。表面上 intensify 竞争，实则可能soften竞争——消费者无动力搜寻低价，厂商可维持高价（Edgeworth 1925；Holt-Scheffman 1987）。
- **产能约束的现实重要性**：多数制造业存在产能约束，使得Bertrand模型需要修正。但服务业（如软件、数字内容）的产能接近无限，Bertrand竞争更适用。
- **动态价格竞争**：一次性Bertrand模型忽略了动态因素（如菜单成本、价格调整频率、消费者搜寻行为）。
- **数据空白**：Bertrand模型的实证检验集中于航空（Borenstein-Rose 1994）、零售（ supermarkets）等行业。结构式IO方法（Berry 1994；Nevo 2001）被广泛用于估计产品差异化程度，但识别策略争议持续。

## 相关页

- 原始来源：[[Joseph Bertrand]]
- 对照模型：[[Cournot竞争]]、[[Stackelberg竞争]]
- 基础概念：[[博弈论]]、[[纳什均衡]]
- 悖论消解：[[产品差异化]]、[[进入壁垒]]
- 主题页：[[不完全竞争与博弈论]]
