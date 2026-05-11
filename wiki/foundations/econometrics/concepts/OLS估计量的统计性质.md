---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, OLS, estimation, foundations, Wooldridge, 技术]
confidence: medium
decay_category: medium
status: foundation
---

# OLS 估计量的统计性质

## 一句话定义

> **OLS 估计量**在 Gauss-Markov 假设下的统计性质——**无偏性**（MLR.1-4）、**最优线性无偏**（MLR.1-5）、**一致性**（大样本）——构成了计量推断的基础。

> **前置阅读**：[[回归作为自动匹配]]（MM）提供了回归的因果直觉；本页补充**技术基础**。

## OLS 估计量

$$\hat{\boldsymbol{\beta}} = (\mathbf{X}'\mathbf{X})^{-1}\mathbf{X}'\mathbf{y}$$

在随机抽样和 MLR.1-4 下，$\hat{\beta}_j$ 是 $\beta_j$ 的**无偏**估计量：$E(\hat{\beta}_j) = \beta_j$。

## 五层 Gauss-Markov 假设体系

Wooldridge 教材的核心教学创新：**逐层引入假设，每个假设只为获得特定结论**——而非一次性列出所有假设。

| 假设 | 内容 | 获得什么 |
|------|------|---------|
| **MLR.1** | 模型关于参数是线性的：$y = \beta_0 + \beta_1 x_1 + ... + \beta_k x_k + u$ | 参数有定义 |
| **MLR.2** | 随机抽样 | 独立性 |
| **MLR.3** | 无完全共线性（$x_j$ 不是其他 $x$ 的完美线性组合） | $\hat{\beta}$ 可计算 |
| **MLR.4** | 零条件均值：$E(u | x_1,...,x_k) = 0$ | **无偏性** |
| **MLR.5** | 同方差：$\text{Var}(u | x_1,...,x_k) = \sigma^2$ | **BLUE** + 标准方差公式有效 |

- MLR.1-4 → **无偏性**
- MLR.1-5 → **Gauss-Markov 定理**（OLS 是 BLUE）
- + 正态性 MLR.6 → **精确的 t/F 分布**（小样本推断）

## OLS 方差

在 MLR.1-5 下：

$$\text{Var}(\hat{\beta}_j) = \frac{\sigma^2}{\text{SST}_j (1 - R_j^2)}$$

其中 $\sigma^2 = \text{Var}(u)$，$\text{SST}_j = \sum (x_{ij} - \bar{x}_j)^2$，$R_j^2$ 是 $x_j$ 对其他 $x$ 回归的 $R^2$。

**三个降低 $\text{Var}(\hat{\beta}_j)$ 的途径**：
1. 增大样本量 $n$ → $\text{SST}_j$ ↑
2. 减小误差方差 $\sigma^2$ → 加更多解释变量
3. 减小共线性 → $R_j^2$ ↓

## 与 MM 因果解释的整合

- MM 的 [[回归作为自动匹配|回归 = 匹配]] 解释的是**点估计值**的直觉
- Wooldridge 的 Gauss-Markov 理论解释的是**估计量的统计可靠性**
- 两者合一 → 既知道"估计值是什么意思"，又知道"这个估计值有多可信"

## 反面论点与数据空白

- **MLR.4（零条件均值）是永远不可检验的假设**——所有 OLS 的因果声称都依赖于此，这是 OLS 的阿喀琉斯之踵。
- **MLR.5（同方差）在现实中几乎永远被违反**——但异方差稳健标准误（Ch 8）多数时候可以补救推断。
- **无偏性在大样本下不如一致性重要**——许多计量方法（IV、非线性模型）放弃无偏性但保有一致性。

## 相关页

- [[Gauss-Markov定理]] / [[OLS渐近理论]] / [[OLS推断-t检验与F检验]]
- [[回归作为自动匹配]]（MM）— 前置因果直觉
- [[Introductory-Econometrics-Wooldridge-8e]]
