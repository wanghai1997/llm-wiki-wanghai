---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [人物, 数学家, 经济学家, 物理学家, 计算机科学家, 微观经济学, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# John von Neumann(1903–1957)

## 简介

匈牙利裔美籍数学家。20 世纪最具广度的科学家之一,在数学、物理、计算机科学、经济学、博弈论等多个领域均有奠基性贡献。普林斯顿高等研究院终身成员(1933 起,与爱因斯坦共事)。1944 年与经济学家 [[Oskar Morgenstern]] 合著《博弈论与经济行为》(Theory of Games and Economic Behavior),奠定了现代博弈论与期望效用理论。

> Nechyba Ch 17B 脚注 5:"Von Neumann made foundational contributions to fields as varied as quantum mechanics, computer science, statistics, and mathematics and served as a key member of the Manhattan Project (that developed the first nuclear bomb)."

## 在 Nechyba 中的引用脉络

教材在 Ch 17B.1 "'Utility' and Expected Utility"(p. 597 起)显式致敬 von Neumann-Morgenstern,引入 vN-M 期望效用函数 $U(x_G, x_B) = \delta u(x_B) + (1-\delta) u(x_G)$ 作为风险下偏好的标准表示。Ch 17 附录 1 详细讨论独立性公理。本 Wiki 为 vN 与 [[Oskar Morgenstern]] 各建独立人物页(决策点 5 默认推荐:5 人独立)。

## 核心贡献(与本 Wiki 相关)

| 年份 | 贡献 | 本 Wiki 对应页 |
|---|---|---|
| 1928 | "Zur Theorie der Gesellschaftsspiele"——零和二人博弈的极小极大定理(minimax theorem) | 留待 Batch 5 Ch 24(博弈论) |
| 1937 | 一般均衡的"扩张经济模型"(expanding economy model)——投入产出 + 增长率 | 不在本 Wiki 微观范围,留待计算 GE / 经济增长 |
| 1944 | 与 Morgenstern 合著《Theory of Games and Economic Behavior》——博弈论 + 期望效用公理化 | [[vN-M期望效用]] / [[独立性公理]];Batch 5 Ch 24 |
| 1944 附录 | vN-M 期望效用定理:满足完备性 + 传递性 + 连续性 + **独立性公理**的偏好 → 存在 $u(\cdot)$ 使偏好可由 $E[u(x)]$ 表示 | [[vN-M期望效用]] |
| 1946+ | 计算机架构(冯·诺依曼架构)、自我复制自动机理论 | 不在本 Wiki 范围 |
| Manhattan Project | 内爆透镜设计、核武器数学模型 | 不在本 Wiki 范围 |

## vN-M 期望效用(口语版)

> "如果你的偏好满足四条公理(完备 / 传递 / 连续 / 独立),那么存在一个'效用函数' $u(x)$,使得你对赌博的偏好恰好等于该赌博的期望效用 $\sum_s \pi_s u(x_s)$。"
>
> 关键洞察:期望效用**线性叠加**于概率,即 $U(\delta x_B + (1-\delta) x_G) = \delta u(x_B) + (1-\delta) u(x_G)$;但 $u(\cdot)$ 关于 $x$ 可以**非线性**(凹 → 风险厌恶,凸 → 风险偏好,线性 → 风险中性)。

详见 [[vN-M期望效用]] / [[独立性公理]]。

## 与同代经济学家的关系

- **与 [[Oskar Morgenstern]]**:1944 *TGEB* 合著者。两人 1938 年在普林斯顿相遇,Morgenstern 提供经济学问题,vN 提供数学工具。书的数学部分主要由 vN 完成,经济学动机与文字主要由 Morgenstern 完成。
- **与 Kenneth Arrow / Gerard Debreu**:Arrow-Debreu 1954 一般均衡存在性证明用到 vN 的不动点定理(Kakutani 1941,但 Kakutani 自承受 vN 启发)。状态相依商品(Arrow 1953)思想也与 vN-M 期望效用相通。
- **与 John Nash**:Nash 1950 博士论文(非合作博弈均衡)是在 vN 1944 *TGEB* 合作博弈框架基础上的"叛逆性"扩展。vN 起初对 Nash 均衡评价不高(认为太简单),但 Nash 均衡最终成为博弈论的标准解。
- **与 Maurice Allais**:Allais 1953 提出"Allais 悖论",直接挑战 vN-M 独立性公理。vN-M 框架由此进入"描述效力"的长期争论(参见 [[独立性公理]] [BIAS])。

## 反面论点与数据空白

- **独立性公理的描述失效**:Allais 1953 实验证明独立性公理在实验室中**系统性**被违反;Kahneman-Tversky 1979 *Prospect Theory* 给出系统性替代框架(参考点效应、损失厌恶、概率权重)。vN-M 在描述层面的效力在行为经济学的实证下持续退缩,但其规范地位(作为"理性"标准)仍存争议。
- **Ellsberg 悖论与模糊厌恶**:Ellsberg 1961 实验证明人对**已知概率**与**未知概率**的反应不同(模糊厌恶,ambiguity aversion),vN-M 框架不区分这两种不确定性。Schmeidler 1989 / Gilboa-Schmeidler 1989 提出非可加概率与最大最小期望效用作为修正。
- **基数效用的复辟**:vN-M 定理的副产品是把"效用"重新基数化(虽然 Pareto 1906 / Hicks 1934 序数革命刚把它驱逐出去)——但 vN-M 的基数性是"在风险下"的基数性,不是绝对的人际可比性。这一微妙区分常被混淆。
- **政治-道德争议**:vN 在 Manhattan Project 中的角色 + 其晚年对苏联预防性核打击的支持立场,使其形象在科学史中存在张力。学术界一般把 vN 的科学贡献与其政治立场分开评价。

## 相关页

- [[vN-M期望效用]] / [[独立性公理]] / [[期望效用函数]] / [[风险厌恶]]
- 合著者:[[Oskar Morgenstern]]
- 同代人物:[[Vilfredo Pareto]] / [[Léon Walras]]
- 教材:[[Microeconomics-Nechyba-2e]]
- 主题:[[风险与状态偏好]]
