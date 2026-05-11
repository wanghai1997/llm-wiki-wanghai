---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, foundations, batch5, political-economy]
confidence: medium
decay_category: slow
status: foundation
---

# Arrow不可能定理（Arrow's Impossibility Theorem）

## 定义

Arrow 1951 在其博士论文《社会选择与个人价值》中证明：

> 不存在同时满足以下五条公理的社会福利函数（将个体偏好聚合为社会偏好）：

## 五条公理

### 1. 无限制定义域（Unrestricted Domain, U）

社会福利函数对所有可能的个体偏好组合都有定义。

- **含义**：无论个体偏好多么"怪异"，社会都应能做出选择
- **争议**：现实中的投票制度通常限制定义域（如单峰偏好）

### 2. 帕累托效率（Pareto Efficiency, P）

若所有个体都偏好 A 胜于 B，则社会也偏好 A 胜于 B。

- **含义**：社会选择至少应尊重全体一致

### 3. 无关选择独立性（Independence of Irrelevant Alternatives, IIA）

社会对 A 和 B 的排序只取决于个体对 A 和 B 的排序，与其他选项无关。

- **含义**：引入新选项 C 不应改变 A 和 B 的相对排序
- **违反案例**：2000年美国大选——Nader的加入改变了Bush和Gore的竞争结果

### 4. 非独裁（Non-Dictatorship, ND）

不存在一个人的偏好总是等于社会偏好。

- **含义**：民主制度不应是"一人统治"

### 5. 完全性与传递性（Completeness and Transitivity）

社会偏好是完全且传递的：
- 完全性：对任意 A, B，社会能比较 A 和 B
- 传递性：若 A ≻ B 且 B ≻ C，则 A ≻ C

## 定理陈述

Arrow不可能定理：

> 同时满足 U、P、IIA、ND 和传递性的社会福利函数**不存在**。

## 含义

任何民主投票制度都必须在上述公理中至少放弃一条。

### 常见的规避方式

| 放弃公理 | 机制 | 例子 |
|---|---|---|
| **限制定义域（放弃U）** | 单峰偏好下的多数决 | Black 1948的中位选民定理 |
| **放弃传递性** | 允许循环偏好 | Condorcet悖论 |
| **放弃IIA** | 考虑所有选项的相对位置 | Borda计数法 |
| **放弃ND** | 接受独裁 | 实际不存在 |

## Condorcet悖论

Condorcet 1785 发现：即使个体偏好传递，社会偏好也可能不传递。

例子：
- 选民1：A ≻ B ≻ C
- 选民2：B ≻ C ≻ A
- 选民3：C ≻ A ≻ B

多数决：
- A vs B：A 胜（2:1）
- B vs C：B 胜（2:1）
- C vs A：C 胜（2:1）

社会偏好循环：A ≻ B ≻ C ≻ A

## 反面论点与数据空白

- **无限制定义域的争议**：Arrow定理的悲观结论很大程度上依赖于"无限制定义域"公理。现实中的民主制度通过限制议程来规避不可能性（如两党制限制了选择空间）。Sen 1970证明，即使放松非独裁为"最小自由"，也可能出现矛盾。
- **机制设计的突破**：Vickrey 1961 / Clarke 1971 / Groves 1973证明，在拟线性偏好下，VCG机制可实现效率且满足激励相容（尽管可能不满足预算平衡）。这显示Arrow定理的"不可能"在特定条件下可被局部突破。
- **民主制度的稳健性**：Arrow定理是规范性结论，但现实中的民主制度尽管不完美，仍能产生可接受的集体决策（Riker 1982）。
- **数据空白**：社会选择理论的实证研究主要集中在投票行为（选举数据）和实验经济学（实验室投票实验）。

## 相关页

- 原始来源：[[Kenneth Arrow]]
- 规避方式：[[社会选择理论]]
- 应用：[[公共品]]、[[寻租]]
- 主题页：[[公共品与政治经济]]
