---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, preferences, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# 边际替代率MRS

## 一句话定义

> **MRS（marginal rate of substitution）** = 在保持效用不变的前提下，再多一单位 $x_1$ 时**愿意放弃多少** $x_2$。几何上是 [[无差异曲线]] 在该点的**斜率**（取负号或绝对值由教材约定）。

## 公式

$$MRS_{12} = - \frac{dx_2}{dx_1}\bigg|_{u=\bar u} = \frac{\partial u/\partial x_1}{\partial u/\partial x_2} = \frac{MU_1}{MU_2}$$

即**边际效用之比**——这是 Ch 4B 微积分版的关键结论。

## 与最优化条件的连接

[[内点最优条件]]：最优束处 [[预算约束|预算线]] 与 [[无差异曲线]] 相切——
$$MRS = \frac{p_1}{p_2}$$
即"再换一单位 $x_1$ 你愿意付的最多 $x_2$" = "市场要你付出的 $x_2$"。
若 $MRS > p_1/p_2$ → 你愿付得比市价多 → 应增 $x_1$；反之应减。

## 沿 IC 的递减性（[[偏好五公理|凸性]] 的几何投影）

凸偏好（公理 5）在 IC 上表现为：沿 IC 向右下移动，**$x_1$ 越多越不稀缺，越愿意用更少的 $x_2$ 换更多 $x_1$**——MRS 单调递减。

> 这是"边际替代率递减"（diminishing MRS）的标准说法,与"边际效用递减"**不**同——后者是基数效用概念，前者是序数效用下的几何性质。

## 与替代弹性的关系

[[替代弹性]] $\sigma = d \ln(x_2/x_1) / d \ln MRS$ ——衡量"MRS 变化 1% 时，最优束比例 $x_2/x_1$ 变化多少%"。
- $\sigma \to 0$ ：互补（IC 直角形）
- $\sigma = 1$ ：Cobb-Douglas（IC 双曲形）
- $\sigma \to \infty$ ：完全替代（IC 直线）

## 在 [[Microeconomics-Nechyba-2e|Nechyba 教材]] 中的位置

教材 Ch 4 把 MRS 作为**偏好性质的"图形指标"**，Ch 6 用它写出最优化的"切点条件"，Ch 7 用它讨论 SE 时"沿原 IC 滑动到新斜率所对应点"。MRS 几乎是全书 Ch 4–10 的核心几何工具。

## 反面论点与数据空白

- **[BIAS] MRS 假设光滑可微**：在折点偏好（如完全互补）处 MRS 不存在或取区间——教材在 Ch 5 简短提及，但 Ch 6–10 大量推导默认光滑。
- **数据空白**：教材未讨论 MRS 的实证识别（Hausman, Browning 等），在 Ch 1–10 完全是理论概念。

## 相关页

- [[偏好五公理]] / [[无差异曲线]] / [[偏好类型]] / [[替代弹性]]
- [[内点最优条件]] / [[效用最大化问题]] / [[替代效应]]
- [[Microeconomics-Nechyba-2e]]
