---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [人物, 经济学家, 数理经济学, 微观经济学, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Francis Ysidro Edgeworth(1845–1926)

## 简介

爱尔兰裔英国经济学家、统计学家。1881 *Mathematical Psychics* 是数理经济学开山之作之一,引入**无差异曲线**(后被 Pareto 推广)、**契约曲线**(contract curve)、以及今日所称的 **Edgeworth Box** 几何分析框架。1891 起任牛津大学经济学教授,*Economic Journal* 创刊主编(1891-1911,与 Keynes 父子均为该刊创办者)。Edgeworth 同时是数理统计先驱,Edgeworth 展开式(Edgeworth expansion,正态近似的高阶修正)以其命名。

## 在 Nechyba 中的引用脉络

教材未为 Edgeworth 单独设脚注,但 Ch 16 全章"Edgeworth Box"作为核心工具贯穿。Edgeworth 1881 的工作直接奠基了 Ch 16A "The Edgeworth Box"的几何讲法。本 Wiki 为 Edgeworth 建立独立人物页,因其概念(Edgeworth Box)在 Wiki 中的中心地位。

## 核心贡献(与本 Wiki 相关)

| 年份 | 贡献 | 本 Wiki 对应页 |
|---|---|---|
| 1881 | *Mathematical Psychics: An Essay on the Application of Mathematics to the Moral Sciences*——无差异曲线 / 契约曲线 / 议价博弈、不确定的契约范围(indeterminacy of contract) | [[Edgeworth盒]] / [[契约曲线]] / [[核Core]] |
| 1881 | 核(core)的雏形思想:N 人议价的"recontracting"过程,大经济中收敛到竞争均衡 | [[核收敛定理]](严格版由 Debreu-Scarf 1963 完成) |
| 1897 | "The Pure Theory of Monopoly"——双寡头价格的不确定性、Edgeworth 价格周期 | 留待 Batch 5 Ch 25(寡头) |
| 1908 | "On the Probable Errors of Frequency Constants"——Edgeworth 展开式 | 不在本 Wiki 微观范围 |

## Edgeworth Box(口语版)

> "把两个消费者的禀赋集合画进一个矩形,横边长度 = $x_1$ 总禀赋,纵边长度 = $x_2$ 总禀赋。任意一点同时表示两人的配置——一人从左下角看,另一人从右上角倒着看。"

详见 [[Edgeworth盒]]。Edgeworth 1881 的原始构造是双人议价的几何工具;教材 Ch 16 把它推广到 N 人 / M 商品(代价是失去几何可视化)。

## 不确定的契约范围与核

Edgeworth 1881 的关键洞察是:**两人议价的结果不是单点**,而是一个"契约范围"(contract curve)——议价能力强的一方多得,弱者少得,但所有议价结果都满足两个条件:
1. 互惠(双方至少不变差);
2. Pareto 高效(无可改进空间)。

这就是后来定义的 [[核Core]]。Edgeworth 进一步猜想(未严格证明):随着市场参与者数量增加,核的范围会**收缩**到一点——这一点就是 [[一般均衡-Walras版|Walras 竞争均衡]]。这个猜想由 Debreu-Scarf 1963 严格证明,即 [[核收敛定理]]。

## 与同代经济学家的关系

- **与 [[Alfred Marshall]]**:同期英国经济学界的两大支柱。Marshall 1890 *Principles* 走"代表性消费者 + 部分均衡"路径;Edgeworth 1881 走"个体异质 + 议价 / 契约"路径。两人都坚持基数效用观。
- **与 [[Vilfredo Pareto]]**:Pareto 1906 *Manuale* 继承 Edgeworth 的无差异曲线工具,但**剥离**了 Edgeworth 持有的基数效用观,转向序数效用论。Edgeworth 本人对此转向并不完全认同。
- **与 [[Léon Walras]]**:Walras 1874 *Éléments* 与 Edgeworth 1881 *Mathematical Psychics* 几乎同期,但路径不同——Walras 走"价格 + 出清"(价格机制内生于市场),Edgeworth 走"契约 + 议价"(交易内生于双方协商)。核收敛定理在大经济中调和了两条路径。
- **与 [[Harold Hotelling]]**:Hotelling 1932 论文标题"Edgeworth's Taxation Paradox"直接致敬 Edgeworth 1897 关于双寡头与税收的悖论。

## 反面论点与数据空白

- **议价能力的不可观测性**:Edgeworth 1881 框架下契约范围的具体落点取决于"议价能力",但议价能力本身在模型中不可观测、不可形式化(Nash 1950 议价解才给出公理化处理)。这一缺陷在 [[美团骑手管理平台]] 等现实平台议价场景特别明显。
- **大经济假设的现实距离**:核收敛定理需要"经济无限大"才严格成立。现实经济虽大,但有限;Aumann 1964 用连续统经济(测度论意义上的"无限多消费者")给出严格构造,但与现实经济的可观测距离仍大。
- **基数效用 vs 序数效用的方法论争**:Edgeworth 在 *Mathematical Psychics* 假设效用可基数测度并人际比较(他甚至设想"hedonimeter"——快乐计量仪)。这一立场被 Pareto 1906 和 Hicks 1934 推翻。当代经济学中,Edgeworth 的几何工具被保留,但其哲学基础被替换。
- **晚期 Edgeworth 价格悖论**:Edgeworth 1897 在双寡头模型中证明价格可能**不收敛**(Edgeworth 价格周期),挑战了 Bertrand 价格竞争的稳定性。这一发现在 Batch 5 Ch 25 寡头分析中重新出现。

## 相关页

- [[Edgeworth盒]] / [[契约曲线]] / [[核Core]] / [[核收敛定理]]
- 同代人物:[[Alfred Marshall]] / [[Vilfredo Pareto]] / [[Léon Walras]] / [[Harold Hotelling]]
- 教材:[[Microeconomics-Nechyba-2e]]
- 主题:[[一般均衡]]
