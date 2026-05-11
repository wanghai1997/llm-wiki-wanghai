---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, causal-inference, IPW, propensity-score, doubly-robust, foundations, Wooldridge]
confidence: medium
decay_category: slow
status: foundation
---

# 逆概率加权 IPW

## 一句话定义

> **逆概率加权 (IPW)** = 用倾向得分的倒数对观测值重新加权——给"被处理概率低但实际被处理"的个体更高权重，在无混淆假设下识别 ATE。

> **前置阅读**：[[随机对照试验RCT]]（MM）/ [[条件独立假设CIA]]（MM）。

## IPW 的直觉

RCT 中，每个个体被处理的概率已知为 $\pi$（如 0.5）→ 我们自然地在处理组和控制组之间比较。

在观察性数据中，处理概率因人而异（有些人的特征使他们更可能接受处理）→ IPW 通过重新加权"模拟"随机分配：
- 给定协变量 $x$，处理概率 = $p(x)$
- 处理组个体的权重 = $1/p(x)$（被处理的概率低但实际被处理 = 信息量大）
- 控制组个体的权重 = $1/(1-p(x))$（被处理的概率高但实际未被处理 = 信息量大）

## 倾向得分 (Propensity Score)

$$p(x_i) = P(D_i = 1 | x_i)$$

- 通常通过 Logit/Probit 估计
- **平衡性诊断**：加权后，处理组和控制组在 $x$ 上应该在统计上"平衡"——如果有变量不平衡 → 倾向得分模型可能错指定

## IPW 估计量

$$\widehat{\text{ATE}} = \frac{1}{n}\sum_{i=1}^n \left[ \frac{D_i y_i}{\hat{p}(x_i)} - \frac{(1-D_i)y_i}{1-\hat{p}(x_i)} \right]$$

- 处理组的观测被赋予 $1/\hat{p}(x_i)$ 的权重
- 控制组的观测被赋予 $1/(1-\hat{p}(x_i))$ 的权重

## IPW 的危险——权重极值

如果某些个体的 $\hat{p}(x_i) \approx 0$ 但 $D_i = 1$ → 权重 $1/0.01 = 100$ → 极少数个体主导整个估计。

### 处理极值权重

- **修剪 (Trimming)**：丢弃 $\hat{p}(x_i) < 0.05$ 或 $> 0.95$ 的观测（丢弃了"几乎一定被处理/不被处理"的人）
- **重叠假设 (Overlap)**：检查 $\hat{p}(x_i)$ 分布在处理组和控制组是否重叠——没有重叠 → IPW 无效

## 双稳健估计 (Doubly Robust)

结合 IPW 和回归调整：$\widehat{\text{ATE}}_{DR} =$ IPW 加权 + 回归调整的"双重保险"——只要**倾向得分模型**或**回归模型**中有一个正确，估计就是一致的。

## 反面论点与数据空白

- **IPW 的"双稳健"属性是有代价的**：在小样本中，DR 估计量可能不如"单保险"方法（如纯回归调整或纯 IPW）表现好。
- **倾向得分无法替代随机化**：IPW 只能消除**可观测的**选择偏差——不可观测的混淆是 RCT 和 IPW 之间的根本差距。

## 相关页

- [[倾向得分方法]] / [[控制函数方法]] / [[回归调整与IPW的结合]]
- [[随机对照试验RCT]]（MM）/ [[条件独立假设CIA]]（MM）
- [[Introductory-Econometrics-Wooldridge-8e]]
