---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, time-series, OLS, strict-exogeneity, foundations, Wooldridge]
confidence: medium
decay_category: slow
status: foundation
---

# 时间序列 OLS 的有限样本性质

## 一句话定义

> 时间序列中的 OLS 在**严格外生性**（TS.3）下保持无偏性——但严格外生性是比横截面 MLR.4 更强的假设，因为它排除了**任何时间上**的反馈效应。

## 时间序列 Gauss-Markov 假设

| 假设 | 内容 | 与横截面的区别 |
|------|------|--------------|
| **TS.1** | 模型关于参数是线性的 | 同 MLR.1 |
| **TS.2** | 无完全共线性 | 同 MLR.3 |
| **TS.3** | **严格外生性**：$E(u_t | \mathbf{x}_1, ..., \mathbf{x}_T) = 0$（对**所有**时期） | 比 $E(u_t | \mathbf{x}_t) = 0$ **强得多** |
| **TS.4** | 同方差：$\text{Var}(u_t | \mathbf{X}) = \sigma^2$ | 同 MLR.5 |
| **TS.5** | 无序列相关：$\text{Cov}(u_t, u_s | \mathbf{X}) = 0$（$t \neq s$） | **时间序列特有** |
| **TS.6** | 正态性 | 同 MLR.6 |

TS.1-3 → 无偏性
TS.1-5 → Gauss-Markov（OLS 是 BLUE）
TS.1-6 → 精确的 $t$/$F$ 分布

## 严格外生性 vs 同期外生性

- **同期外生性** $E(u_t | \mathbf{x}_t) = 0$：只要求**本期**的 $x$ 与**本期**的 $u$ 不相关
- **严格外生性** $E(u_t | \mathbf{x}_1, ..., \mathbf{x}_T) = 0$：要求**所有时期**的 $x$ 与**本期**的 $u$ 不相关

### 严格外生性排除的情况

- **反馈效应**：$y_t$ 影响 $x_{t+1}$（如今天的 GDP 影响明天的利率政策）
- **遗漏滞后变量**：$x_{t-1}$ 影响 $y_t$ 但未被包含在模型中

→ **严格外生性在宏观经济和金融时间序列中几乎永远不成立**——这是为什么大样本渐近理论（Ch 11）比有限样本理论更重要。

## 反面论点与数据空白

- **严格外生性的脆弱性**：很少有经济学时间序列满足严格外生性——政策变量、价格、利率几乎都受过去结果的影响 → 实际中依靠大样本近似和解释的谨慎性。
- **"序列相关不影响无偏性"但影响推断**——序列相关的存在使标准误被严重低估，$t$ 统计量过度拒绝。

## 相关页

- [[OLS估计量的统计性质]] — 横截面 OLS 的对应假设
- [[平稳性与弱相依]] / [[序列相关]]
- [[Introductory-Econometrics-Wooldridge-8e]]
