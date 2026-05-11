---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [概念, microeconomics, foundations, batch3, 一般均衡]
confidence: medium
decay_category: slow
status: foundation
---

# Edgeworth盒

> 两人两商品交换经济的几何表示。Francis Edgeworth 1881 *Mathematical Psychics* 提出。盒边长 = 两商品总禀赋,盒内每点 = 两人各自的消费组合(B 视角是 A 视角的反射)。

## 构造

设两人 $A, B$,两商品 $x_1, x_2$。总禀赋 $(\bar{x}_1, \bar{x}_2)$。

- **盒尺寸**:宽 = $\bar{x}_1$,高 = $\bar{x}_2$。
- **A 的原点**:左下角。A 的消费 $(x_1^A, x_2^A)$ = 盒内任意点的横纵坐标。
- **B 的原点**:右上角(180° 旋转)。B 的消费 $(x_1^B, x_2^B) = (\bar{x}_1 - x_1^A, \bar{x}_2 - x_2^A)$。

每个点 $E = (x_1^A, x_2^A)$ 同时表达 A 和 B 的消费组合(总和恰好等于禀赋,资源约束自动满足)。

## 初始禀赋点

设 A 初始有 $(\omega_1^A, \omega_2^A)$,B 初始有 $(\omega_1^B, \omega_2^B) = (\bar{x}_1 - \omega_1^A, \bar{x}_2 - \omega_2^A)$。
**禀赋点** $\omega = (\omega_1^A, \omega_2^A)$ 是 Edgeworth 盒内一个特定点。

## 偏好的几何表示

A 的无差异曲线:从 A 的原点(左下)向右上凸,$U^A$ 越高曲线越远离左下角。
B 的无差异曲线:从 B 的原点(右上)向左下凸,$U^B$ 越高曲线越远离右上角。

**两条无差异曲线相切**的点 = Pareto 高效点(详见 [[契约曲线]])。

## 互惠交易集

**互惠交易集 MB(mutually beneficial)**:从禀赋 $\omega$ 出发,所有同时使 $U^A \ge U^A(\omega)$ 和 $U^B \ge U^B(\omega)$ 的点构成的"透镜形"区域,以两条经过 $\omega$ 的无差异曲线为边界。

详见 [[互惠交易集MB]]。

## 价格线与预算约束

给定相对价格 $p_1/p_2$,从 $\omega$ 出发画斜率为 $-p_1/p_2$ 的直线 = 双方的预算线(同时是 A 和 B 的预算线,两人共享)。

每人沿预算线选最优:
- $A$ 选 $U^A$ 最大化点(切于预算线)→ 净需求 $x^A - \omega^A$。
- $B$ 选 $U^B$ 最大化点(切于预算线)→ 净需求 $x^B - \omega^B$。

**Walras 均衡**:$p^*$ 使 $A$ 净需求 + $B$ 净需求 = 0(市场出清)。详见 [[一般均衡-Walras版]]。

## Edgeworth 盒的核心用途

1. **可视化 Pareto 集**:契约曲线 = 盒内所有 Pareto 高效点。
2. **Walras 均衡可视化**:在 $\omega$ 与预算线交于契约曲线的某点上。
3. **第一福利定理几何证明**:Walras 均衡点 ∈ 契约曲线 → Pareto 高效。
4. **第二福利定理几何证明**:任意 Pareto 点都可作为某再分配后的 Walras 均衡。
5. **核(Core)的几何**:阻断联盟无法击败的配置集合,核 ⊆ 契约曲线 ∩ 互惠交易集。

## 历史

Edgeworth 1881 *Mathematical Psychics: An Essay on the Application of Mathematics to the Moral Sciences* 第二版引入"Edgeworth Box"。Pareto 1906 *Manuale di Economia Politica* 给出无差异曲线的现代名称。Bowley 1924 教科书使该图标准化。

> **历史小注**:Edgeworth 盒在英国传统中也称 "Edgeworth-Bowley Box";美国传统简称 Edgeworth Box。

## 局限

Edgeworth 盒只能表示**两人两商品**经济。三人或三商品需要 Edgeworth 立方体(数学复杂)或代数表达。一般均衡的多商品多消费者扩展由 Walras 1874-77 *Éléments d'économie politique pure* 给出代数 / 矩阵表达,但无简单几何对应。

## 反面论点与数据空白

- **2x2 限制**:现实经济有数百商品 + 数百万主体,Edgeworth 盒的"几何洞察"对此无法直接迁移。Sonnenschein-Mantel-Debreu (1972-74) [SMD theorem] 证明高维一般均衡的反应函数可任意——Edgeworth 盒的"清晰几何"是 2x2 偶然结果。
- **静态偏好假设**:盒内分析假设偏好外生固定,但现实中偏好受历史 / 文化 / 教育影响——Becker-Stigler 1977 vs Bowles-Gintis 2011 的偏好内生化文献,教材不展开。
- **生产侧缺失**:纯交换经济假设禀赋外生 → 忽略生产决策、技术选择、要素投入分配。Robinson Crusoe 经济(详见 [[Robinson Crusoe经济]])加入生产,但仍是 1 人 2 商品 的简化。
- **公平 vs 高效**:Edgeworth 盒的几何聚焦于 Pareto 集合,但 Pareto 集合中有许多极不平等的点(全部资源给 A,B 一无所有也是 Pareto 高效)。Sen 1970 *Collective Choice and Social Welfare* 强调这一无可比性。
- **经验数据空白**:Edgeworth 盒是教学工具,几乎无直接实证应用——一般均衡的实证主要靠 CGE 模型(Caliendo-Parro 2015 等),而非盒图。

## 相关页

- 上游:[[Francis Edgeworth]] / [[市场需求曲线]] / [[偏好类型]]
- 概念衍生:[[互惠交易集MB]] / [[契约曲线]] / [[核Core]]
- 一般均衡:[[一般均衡-Walras版]] / [[Walras定律]]
- 福利定理:[[第一福利定理]] / [[第二福利定理]]
- 主题:[[一般均衡]]
