---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [人物, 经济学家, 微观经济学, 一般均衡, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Léon Walras(1834–1910)

## 简介

法国经济学家。被广泛尊为**一般均衡理论之父**;1874 年《纯粹经济学要素》(Éléments d'économie politique pure)首次给出"M 个市场同时出清"的方程组形式化,确立了一般均衡分析的基本范式。与 [[Alfred Marshall]] 的部分均衡传统并立,共同构成现代价格理论的两大源头。

> **教材笔误注**:Nechyba Ch 16B 脚注 8 写作"Leon Walras (1934-1910)",显然为打字错误,正确生卒为 **1834-1910**。本 Wiki 修正记录在此。

## 在 Nechyba 中的引用脉络

教材在 Ch 16B.1.5 "Walras's Law"显式致敬 Walras,作为一般均衡理论的奠基人。脚注同时记载一个有趣的史实:Walras 当年坚持"价格在横轴 / 数量在纵轴"的画法(数学上更正确),但经济学界沿用 Marshall 的反向画法至今。

## 核心贡献

| 年份 | 贡献 | 本 Wiki 对应页 |
|---|---|---|
| 1874-1877 | 《纯粹经济学要素》(分两卷出版)——一般均衡方程组、tâtonnement(摸索)价格调整过程 | [[一般均衡-Walras版]] |
| 1874 | Walras 定律:总需求恒等于总供给(预算约束在均衡的总量版本)→ M-1 个市场出清蕴含第 M 个出清 | [[Walras定律]] |
| 1874 | 数量与货币的二分法:实物市场均衡价格只能确定到一个相对价格(同次 0 度需求函数) | [[Walras定律]] §"价格归一化" |
| 1875+ | 边际效用价值论(独立于 Jevons / Menger 的边际革命三发现之一) | [[偏好五公理]] §"边际革命脉络" |

## Walras 定律(口语版)

> "在一个有 M 个市场的经济中,只要有 M-1 个市场出清,第 M 个市场必然自动出清。"
>
> 形式化:$\sum_m p_m \cdot \text{ED}_m = 0$ 恒成立(总超额需求 = 0),来源于每个个体预算约束 $\sum_m p_m x_m = \sum_m p_m e_m$ 的总量加总。

详细推导见 [[Walras定律]]。

## tâtonnement 与均衡稳定性

Walras 提出"摸索"价格调整过程:超额需求为正的市场价格上升,为负则下降,直到所有市场出清。这一过程隐含两个未严格证明的命题——
1. **存在性**:这样的均衡价格存在吗?(Arrow-Debreu 1954 严格证明)
2. **稳定性**:tâtonnement 是否收敛?(Scarf 1960 给出反例,Sonnenschein-Mantel-Debreu 1972-74 证明任意连续超额需求函数都可在某经济中实现 → 一般稳定性不成立)

Nechyba 在 Ch 16B 脚注 7 简要承认这些技术问题,但不展开。

## 与同代经济学家的关系

- **与 [[Alfred Marshall]]**:同代但路径分歧——Marshall 走部分均衡 + 直观图形;Walras 走一般均衡 + 数学方程组。两人通信稀少,Schumpeter 评价"Walras 是史上最伟大的经济学家",而 Marshall 在英语世界更具影响力。
- **与 Vilfredo Pareto**:Walras 在洛桑大学的继任者就是 [[Vilfredo Pareto]];Pareto 把 Walras 的均衡概念发展为"Pareto 效率",并在福利经济学方向推进。两人合称"洛桑学派"。
- **与 [[Francis Edgeworth]]**:Edgeworth 1881 *Mathematical Psychics* 与 Walras 1874 *Éléments* 几乎同期,但 Edgeworth 走"契约曲线 + 议价"路径,Walras 走"价格 + 出清"路径。两条路径在 Ch 16 通过核收敛定理重新会合。

## 反面论点与数据空白

- **存在性条件严苛**:Arrow-Debreu 1954 证明的存在性需要凸偏好 + 凸生产集 + 完全市场——任意一项被违反,均衡可能不存在(参见 [[第一福利定理]] / [[第二福利定理]] 反面论点)。
- **tâtonnement 不稳定**:Scarf 1960 / Sonnenschein-Mantel-Debreu(SMD)结果表明 Walras 摸索过程在三人以上经济**一般不收敛**;Walras 的"价格自动调整 → 均衡"叙事在数学上不成立。
- **与现实金融市场的差距**:Walras 假设所有市场同时存在并出清。现实中金融市场缺失(不完全市场,Hart 1975)、信息不对称(Akerlof 1970)、流动性约束(Kiyotaki-Moore 1997)使 Walras 框架在描述层面持续被修正。
- **货币缺位**:Walras 框架是实物经济,价格归一化后只剩相对价格;货币的中介职能、价值储藏职能在 Walras 体系中无对应。Patinkin 1956 *Money, Interest and Prices* 试图修补,争议至今。

## 相关页

- [[Walras定律]] / [[一般均衡-Walras版]] / [[第一福利定理]]
- 同代人物:[[Alfred Marshall]] / [[Vilfredo Pareto]] / [[Francis Edgeworth]]
- 教材:[[Microeconomics-Nechyba-2e]]
- 主题:[[一般均衡]]
