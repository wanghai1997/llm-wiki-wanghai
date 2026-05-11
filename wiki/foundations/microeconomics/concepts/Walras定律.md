---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [概念, microeconomics, foundations, batch3, 一般均衡]
confidence: medium
decay_category: slow
status: foundation
---

# Walras定律

> 在所有消费者满足预算约束的前提下:**所有市场超额需求的价值之和 ≡ 0**。这意味着如果 $L-1$ 个市场出清,第 $L$ 个市场自动出清。Walras 1874-77 自身证明的重要恒等式。

## 形式陈述

设 $L$ 种商品,价格向量 $p$,经济总超额需求函数 $z(p) = X^D(p) - X^S(p) \in \mathbb{R}^L$。

**Walras 定律**:
$$
p \cdot z(p) \equiv 0, \quad \forall p
$$

这是**恒等式**,对任意价格(不仅是均衡价格)成立。

## 推导

每个消费者 $i$ 满足预算约束:
$$
p \cdot x^i = p \cdot \omega^i + \sum_j \theta^{ij} \pi^j(p)
$$

(无生产经济中第二项为 0)。在所有消费者上加总:
$$
p \cdot \sum_i x^i = p \cdot \sum_i \omega^i + p \cdot \sum_j y^j
$$

用 $z(p) = \sum_i (x^i - \omega^i) - \sum_j y^j$:
$$
p \cdot z(p) = p \cdot \sum_i x^i - p \cdot \sum_i \omega^i - p \cdot \sum_j y^j = 0
$$

→ 恒等式成立。

## 关键含义

### 含义 1:$L-1$ 个市场决定第 $L$ 个

若 $z_1(p) = z_2(p) = \ldots = z_{L-1}(p) = 0$,且 $p_L > 0$,则由 $p \cdot z(p) = 0$ 推出 $z_L(p) = 0$。

→ **检验** Walras 均衡只需检验 $L-1$ 个市场;第 $L$ 个自动出清。这简化了存在性证明 + 数值算法。

### 含义 2:价格归一化的合理性

Walras 定律隐含价格"零次齐次"——只有相对价格有意义。所以可任意选某商品 $L$ 为 numéraire,$p_L = 1$,其他价格相对于 $L$ 表达。

### 含义 3:不能有"内部腐败"

任何持续的总超额需求都意味着对应的总超额供给(等价值)——需求与供给的总价值必然平衡。

## 与 Say 定律的混淆

> **常见误解**:Walras 定律 ≠ Say 定律("供给创造其自身需求")。

- **Walras 定律**:**恒等式**,对任意价格成立,不依赖均衡。
- **Say 定律**:经济**实际上**不会有持续超额供给(Say 1803 *Treatise on Political Economy*)——是宏观经济学经验主张,不是恒等式。

Keynes 1936 *General Theory* 否定 Say 定律,提出有效需求不足可能(失业 / 衰退);Walras 定律仍成立(总价值平衡是会计恒等式),但具体某市场可在 $p^* \ne 0$ 处持续不出清(Keynesian disequilibrium)。

## 历史

Walras 在 *Éléments d'économie politique pure* 第 35 章正式提出该定律。后由 Lange 1942 *"Say's Law: A Restatement and Criticism"* 系统讨论 Walras 定律 vs Say 定律的区别。教材简略带过,但这是宏观与微观接缘的关键概念。

## 反面论点与数据空白

- **预算约束的现实违反**:Walras 定律假设所有消费者**严格**满足预算约束。现实中信贷市场不完美 + 流动性约束使消费者可能跨期不满足预算约束(过度消费 / 信用违约)。教材静态预算约束下不暴露这一问题。
- **货币的暧昧性**:Walras 模型中无"货币"——只有相对价格。Patinkin 1956 *Money, Interest, and Prices* 把货币内化,但产生新问题(货币是否中性)。教材不展开。
- **超额需求函数的可证伪性**:SMD 定理(Sonnenschein-Mantel-Debreu)证明 $z(p)$ 可任意(满足 Walras 定律 + 零次齐次)→ 一般均衡的实证含义远比表面"清晰"少。教材不展开。
- **Keynesian 失业**:在某些工资 / 价格刚性下,劳动市场可在 $p^* \ne$ 完全竞争均衡价处持续不出清(失业)。Walras 定律仍成立,但宏观经济学需要其他工具。教材完全微观静态。
- **数据空白**:总超额需求函数的实证估计需要 CGE 模型(Caliendo-Parro 2015 / Hertel-Tsigas 1997),依赖大量假设。教材不连接实证。

## 相关页

- 上游:[[Léon Walras]]
- 一般均衡:[[一般均衡-Walras版]]
- 福利定理:[[第一福利定理]] / [[第二福利定理]]
- 反面 / 宏观:Say 定律 vs Keynes [Macroeconomics]
- 主题:[[一般均衡]]
