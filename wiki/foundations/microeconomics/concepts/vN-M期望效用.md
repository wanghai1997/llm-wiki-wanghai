---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [概念, microeconomics, foundations, batch3, 风险与状态偏好]
confidence: medium
decay_category: slow
status: foundation
---

# vN-M期望效用

> von Neumann-Morgenstern 1944 *Theory of Games and Economic Behavior* 严格公理化证明:满足完备性、传递性、连续性、独立性公理的偏好,必有期望效用表示 $U = \mathbb{E}[u]$。这是现代不确定性经济学 + 博弈论的基础。详见 [[John von Neumann]] / [[Oskar Morgenstern]] 人物页。

## 公理体系

设 $\mathcal{L}$ 为所有彩票(概率分布)的集合。偏好关系 $\succsim$ 在 $\mathcal{L}$ 上定义。

### 公理 1:完备性(Completeness)

对任意两个彩票 $L_1, L_2$:$L_1 \succsim L_2$ 或 $L_2 \succsim L_1$ 或两者(无差异)。

### 公理 2:传递性(Transitivity)

$L_1 \succsim L_2 \land L_2 \succsim L_3 \Rightarrow L_1 \succsim L_3$。

### 公理 3:连续性(Continuity)

若 $L_1 \succ L_2 \succ L_3$,则 $\exists \alpha \in (0, 1)$ 使 $L_2 \sim \alpha L_1 + (1-\alpha) L_3$。

### 公理 4:独立性(Independence)

$L_1 \succsim L_2 \iff \alpha L_1 + (1-\alpha) L_3 \succsim \alpha L_2 + (1-\alpha) L_3, \forall \alpha \in (0, 1), L_3$。

> 独立性是最具争议的公理。Allais 悖论(1953)、Ellsberg 悖论(1961)都攻击这一公理。详见 [[独立性公理]]。

## vN-M 表示定理

**定理**:若 $\succsim$ 满足完备性、传递性、连续性、独立性,则存在效用函数 $u$ 使得:

$$
L_1 \succsim L_2 \iff \sum_i p_i u(x_i) \ge \sum_i q_i u(y_i)
$$

其中 $L_1 = (p_1, x_1; \ldots; p_n, x_n)$,$L_2 = (q_1, y_1; \ldots; q_m, y_m)$。

$u$ 定义至正仿射变换(即 $v = a \cdot u + b$,$a > 0$ 表示相同偏好)。

## 证明思路(简述)

1. **最佳 / 最差彩票**:找到 $L^{best} \succsim L \succsim L^{worst}$ 对所有 $L$。
2. **混合比例唯一性**:对任意 $L$,存在唯一 $\alpha_L$ 使 $L \sim \alpha_L L^{best} + (1-\alpha_L) L^{worst}$。
3. **效用定义**:令 $u(L) = \alpha_L$。
4. **期望形式验证**:独立性公理保证 $u$ 在混合下满足线性 → $u$ = 期望效用。

## 历史意义

vN-M 1944 *TGEB* 把经济学从"效用可测量?"的哲学争论中解放出来:
- **不用可测量效用**:效用只是偏好排序的代表,不具有客观物理量意义。
- **可测试偏好**:通过观察主体的彩票选择行为,反推 $u$。
- **基数但有限制**:$u$ 是基数(可比较差异),但只允许正仿射变换 → 排除了 "双倍效用" 或 "效用排名" 等非线性比较。

## 应用

- **博弈论**:所有博弈的纳什均衡 / 子博弈完美均衡计算依赖 vN-M 期望效用(players 在混合策略上最大化期望效用)。
- **金融**:资产定价、投资组合优化、CAPM 都依赖期望效用。
- **保险**:精算公平保险 = 使期望效用最大化的保险策略(详见 [[精算公平保险]])。
- **公共政策**:成本-收益分析中的社会贴现率选择依赖社会时间偏好效用。

## 反面论点与数据空白

- **Allais 悖论**:Allais 1953 *"Le Comportement de l'Homme Rationnel devant le Risque"* 构造确定性效应:主体在确定性结果上过度偏好,违反独立性公理。
- **Ellsberg 悖论**:Ellsberg 1961 *"Risk, Ambiguity, and the Savage Axioms"* 构造模糊规避(ambiguity aversion):主体对已知概率 vs 未知概率的彩票有不同偏好,违反期望效用。
- **Prospect theory**:Kahneman-Tversky 1979 *"Prospect Theory: An Analysis of Decision under Risk"* 提出 $\alpha \neq 1$(价值函数非线性)+ $\lambda \approx 2.25$(损失厌恶)+ $\pi(\rho) \neq \rho$(概率权重)。Tversky-Kahneman 1992 改进版 CPT(cumulative prospect theory)更优地拟合实验数据。
- **反例的频率**:Harrison-Rutström 2009 *"Risk Aversion in the Laboratory"* 综述显示,虽然 vN-M 被反复"证伪",但在许多实验中仍是最简洁的描述框架。
- **数据空白**:Holt-Laury 2002 *American Economic Review* 实测 CRRA;Harrison-Rutström 2009 综述 180+ 实验;Fehr-Schmidt 1999 *Quarterly Journal of Economics* 社会偏好模型(不等规避)扩展 vN-M。教材仅保留 vN-M 基础框架。
- **神经经济学**:Glimcher 2010 *Foundations of Neuroeconomic Analysis* 尝试在神经层面寻找期望效用的生物学基础,但结论仍模棱两可。

## 相关页

- 上游:[[John von Neumann]] / [[Oskar Morgenstern]]
- 公理:[[独立性公理]]
- 数学:[[期望效用函数]]
- 风险:[[风险厌恶]] / [[确定性等价]] / [[风险溢价]]
- 反面:Allais 悖论 / Ellsberg 悖论 / Kahneman-Tversky 1979 [Batch 5]
- 主题:[[风险与状态偏好]]
