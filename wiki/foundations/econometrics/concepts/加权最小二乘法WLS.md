---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, WLS, FGLS, heteroskedasticity, efficiency, foundations, Wooldridge, 技术]
confidence: medium
decay_category: medium
status: foundation
---

# 加权最小二乘法 WLS

## 一句话定义

> **加权最小二乘法 (WLS)** = 当异方差形式已知时，对每个观测值按照其误差方差的倒数加权——使变换后的模型满足同方差，从而 OLS 恢复 BLUE 性质。

## 为什么 OLS 不是 BLUE（在同方差违反下）

[[Gauss-Markov定理|Gauss-Markov]] 要求同方差 → 如果 $\text{Var}(u|x)$ 不是常数 → OLS 仍无偏、一致，但不再是**最优**（方差最小）的线性无偏估计量。

WLS 将异方差的模型变换为同方差模型，从而恢复 BLUE。

## WLS 的机制

假设 $\text{Var}(u|x) = \sigma^2 h(x)$，其中 $h(x)$ 已知：

1. 原始模型：$y_i = \beta_0 + \beta_1 x_{i1} + ... + \beta_k x_{ik} + u_i$
2. 除以 $\sqrt{h_i} = \sqrt{h(x_i)}$：
   $$\frac{y_i}{\sqrt{h_i}} = \beta_0 \frac{1}{\sqrt{h_i}} + \beta_1 \frac{x_{i1}}{\sqrt{h_i}} + ... + \frac{u_i}{\sqrt{h_i}}$$
3. 变换后误差的方差：$\text{Var}(u_i / \sqrt{h_i} | x_i) = \sigma^2$（同方差！）
4. 对变换后的方程跑 OLS → WLS 估计量

**直觉**：WLS 给误差方差**小**的观测值**更大**的权重（因为它们的信息更精确）。

## 可行 GLS (FGLS)

**问题**：$h(x)$ 在实际中几乎永远未知。

**FGLS 解决方案**：
1. 从 OLS 获得残差 $\hat{u}_i$
2. 用 $\ln \hat{u}_i^2$ 对解释变量回归 → 估计异方差函数 $\hat{h}_i$
3. 用 $\hat{h}_i$ 做 WLS

→ 在大样本下，FGLS 与"已知 $h(x)$ 的 WLS"具有相同的渐近性质。

## WLS vs 异方差稳健 OLS

| | 异方差稳健 OLS | WLS/FGLS |
|---|---|---|
| 一致性 | ✅ | ✅（如果 $h(x)$ 正确指定） |
| 有效性 | 次于 WLS | **最优**（如果 $h(x)$ 正确） |
| 稳健性 | 对任何形式的异方差都稳健 | 如果 $h(x)$ 错误 → 仍然一致但有效性损失 |
| 简单性 | ⭐⭐⭐ | ⭐ |

→ **实践中，异方差稳健 OLS 是默认选择；WLS/FGLS 在异方差形式明确时使用。**

## 反面论点与数据空白

- **FGLS 对异方差函数形式的错误指定敏感**：如果 $\hat{h}(x)$ 的形式错了，FGLS 仍然一致但不再比 OLS 更有效——投入的额外工作量可能没有回报。
- **有限样本下 FGLS 可能不如异方差稳健 OLS**：$\hat{h}$ 的估计误差在 $n$ 小时不可忽略。

## 相关页

- [[异方差]] / [[Gauss-Markov定理]] / [[OLS估计量的统计性质]]
- [[Introductory-Econometrics-Wooldridge-8e]]
