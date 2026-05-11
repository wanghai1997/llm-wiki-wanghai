---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [概念, microeconomics, foundations, batch3, 一般均衡]
confidence: medium
decay_category: slow
status: foundation
---

# 一般均衡-Walras版

> Léon Walras 1874-77 *Éléments d'économie politique pure* 提出。所有市场**同时**出清的价格向量 $p^*$。每个主体在 $p^*$ 下最优,所有商品的总需求 = 总供给。Arrow-Debreu 1954 给出现代严格存在性证明。

## 形式定义(纯交换经济)

设经济有 $N$ 个消费者,$L$ 种商品。消费者 $i$ 有禀赋 $\omega^i \in \mathbb{R}^L_+$ 与偏好 $U^i$。

**Walras 均衡**:价格向量 $p^* = (p_1^*, \ldots, p_L^*)$ 与配置 $\{x^{i*}\}_{i=1}^N$ 满足:
1. **个体最优**:$x^{i*} = \arg\max U^i(x)$ s.t. $p^* \cdot x \le p^* \cdot \omega^i$。
2. **市场出清**:$\sum_{i=1}^N x^{i*}_l = \sum_{i=1}^N \omega^i_l, \forall l = 1, \ldots, L$。

加上一个归一化条件(因价格向量可任意缩放):$p_L^* = 1$ 或 $\sum p_l^* = 1$。

## 核心特征

### 价格接受

每个消费者把 $p$ 视为给定,选择自己的 $x$ 使效用最大化。这要求经济足够大(详见 [[核收敛定理]] 的辩护)或假设 fragments 足够多。

### 同时出清

不只是某个市场,**所有**市场同时供需相等。这与部分均衡分析(只考虑单个市场)的关键区别。

### 货币的暧昧性

Walras 模型本身无货币——只有相对价格。归一化某商品 $L$ 为"计价物品"(numéraire),其他商品价格用它表示。Patinkin 1956 *Money, Interest, and Prices* 把货币内化于一般均衡,但 Nechyba 不展开。

## 存在性

### Walras 1874-77 提出问题

Walras 通过手工解联立方程组(代数方法)说明均衡可能存在,但未严格证明。

### Wald 1935 / McKenzie 1954 / Arrow-Debreu 1954

- **Wald 1935** 给出 2 阶段证明的早期版本。
- **McKenzie 1954** 与 **Arrow-Debreu 1954** 几乎同时给出现代证明,使用不动点定理(Brouwer / Kakutani)。
- **关键条件**:每个消费者偏好凸 + 连续 + 单调 + 局部非饱和;商品互补 / 替代关系满足某些"严格性"条件。

详见 [[Arrow-Debreu存在性定理]] [Batch 5]。

## 唯一性与稳定性

存在性 ≠ 唯一性 ≠ 稳定性。

- **唯一性**:并非保证。某些经济有多个 Walras 均衡(Kehoe 1985 的反例)。
- **稳定性**:tâtonnement(试错调价)是否收敛于 Walras 均衡?Scarf 1960 *International Economic Review* 的反例显示**未必**。
- **Sonnenschein-Mantel-Debreu 1972-74**:总超额需求函数可任意,因此一般均衡的唯一性 / 稳定性"几乎不能保证"。

> **教材立场**:Nechyba 16A 给出存在性(隐含),但**不强调** SMD 反例 + 稳定性问题。学生易得到"Walras 均衡是稳健概念"的过度信心。

## tâtonnement

Walras 提出的拟动态机制:
- 在某假设价格 $p^t$ 下,各市场出现超额需求 $z(p^t) = X^D(p^t) - X^S(p^t)$。
- $p^{t+1}_l = p^t_l + \alpha \cdot z_l(p^t)$:超额需求 → 价格上升;超额供给 → 价格下降。
- $t \to \infty$ 是否 $p^t \to p^*$?

> **不严格收敛**:Scarf 1960 反例表明 tâtonnement 可能在 Walras 均衡周围"绕"而不收敛。教材在 Ch 16 略有提及但不展开。

## 与 Edgeworth 盒的关系

两人两商品经济的 Walras 均衡可在 Edgeworth 盒中可视化:
- 给定 $\omega$,通过 $\omega$ 画斜率 $-p_1/p_2$ 的预算线。
- $A$ 沿预算线选 $U^A$ 最大化点;$B$ 同理。
- $p^*$ 满足两人最优点重合 = 同一点(市场出清)。
- 该点在 [[契约曲线]] 上(第一福利定理),且 ∈ [[互惠交易集MB]](无人变差)。

## 引入生产侧

加入 $J$ 家厂商,各有生产可能集 $Y^j \subseteq \mathbb{R}^L$。

**完整 Walras 均衡**:$(p^*, \{x^{i*}\}, \{y^{j*}\})$ 满足:
- 消费者最优:$x^{i*} \in \arg\max U^i$ s.t. $p^* \cdot x \le p^* \cdot \omega^i + \sum_j \theta^{ij} \pi^j(p^*)$,其中 $\theta^{ij}$ = $i$ 在 $j$ 中的份额, $\pi^j(p^*) = \max p^* \cdot y, y \in Y^j$。
- 厂商最优:$y^{j*} \in \arg\max p^* \cdot y, y \in Y^j$。
- 市场出清:$\sum_i x^i = \sum_i \omega^i + \sum_j y^j$。

详见 [[Robinson Crusoe经济]](1人 + 1厂商极简版)。

## 反面论点与数据空白

- **SMD 反例的严重性**:Sonnenschein-Mantel-Debreu (1972-74) 证明高维经济的总超额需求函数可任意,使一般均衡的唯一性 + 稳定性 + 比较静态都"几乎不能保证"。教材完全跳过。
- **稳定性问题**:Scarf 1960 / Hildenbrand-Kirman 1988 *Equilibrium Analysis* 强调 tâtonnement 不严格收敛于 Walras 均衡。Smale 1976 / Saari 1985 给出更严重的稳定性失败。
- **价格调整机制的现实暧昧**:Walras tâtonnement 假设有"拍卖师"调价。现实中价格如何形成,谁负责调整,完全未在模型中。Behavioral / search-theoretic 文献(Diamond 1971 / Mortensen-Pissarides 1994)给出微观基础但教材不连接。
- **数据空白**:CGE 实证模型(Whalley 1988 / Caliendo-Parro 2015)给出政策评估的具体数值,但模型校准依赖大量假设(弹性、市场结构、税基等),实证结果稳健性争议大。教材不引述。
- **金融危机的失效**:2008 危机展示一般均衡模型对系统性风险 / 金融脆弱性 / 信贷崩溃的处理不足。Geanakoplos 2010 *NBER Macroeconomics Annual* "The Leverage Cycle" 提出修补;教材不引述。
- **行为经济学**:Tversky-Kahneman 1979 等使"理性预期 + 完全信息" Walras 均衡的行为基础不稳。教材完全经典理性。

## 相关页

- 关键人物:[[Léon Walras]] / [[Vilfredo Pareto]] / [[Francis Edgeworth]]
- 几何:[[Edgeworth盒]] / [[契约曲线]]
- 关键性质:[[Walras定律]] / [[第一福利定理]] / [[第二福利定理]]
- 极限:[[核收敛定理]]
- 简化:[[Robinson Crusoe经济]]
- 主题:[[一般均衡]]
