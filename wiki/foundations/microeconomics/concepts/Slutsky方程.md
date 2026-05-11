---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, duality, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Slutsky方程

## 公式

$$\boxed{\frac{\partial x_i(p, m)}{\partial p_j} = \frac{\partial x_i^h(p, U)}{\partial p_j} \bigg|_{U = V(p, m)} - x_j(p, m) \cdot \frac{\partial x_i(p, m)}{\partial m}}$$

- 左侧：[[Marshallian需求曲线]] 的价格偏导（**总效应**）；
- 右第一项：[[补偿需求曲线|Hicksian]] 的价格偏导（**纯替代效应**）；
- 右第二项：**收入效应** ——$x_j$ 单位的购买力变化乘以 $i$ 商品对收入的响应。

## 历史

- **1915**：[[Eugen Slutsky]] 在 *Sulla teoria del bilancio del consumatore* 提出（意大利文，被埋没近 20 年）；
- **1934**：[[John Hicks|Hicks]] 与 Allen 重新发现并整合进新古典综合；
- **此后**：成为 [[消费者对偶性]] 的核心代数工具。

## 关键性质

| 性质 | 说明 |
|---|---|
| **对称性**（Slutsky symmetry） | $\partial x^h_i/\partial p_j = \partial x^h_j/\partial p_i$ ——交叉补偿效应对称 |
| **半负定性** | $[\partial x^h/\partial p]$ 矩阵半负定 → 自身价格效应 $\le 0$ |
| **0 阶齐次** | 价格全比例上涨 + 名义收入同比例上涨 → 需求不变 |

## 推导（教材 Ch 10B）

由 [[消费者对偶性]] 的恒等式 $x_i(p, m) = x^h_i(p, V(p, m))$，对 $p_j$ 求偏导：

$$\frac{\partial x_i}{\partial p_j} = \frac{\partial x^h_i}{\partial p_j} + \frac{\partial x^h_i}{\partial U} \cdot \frac{\partial V}{\partial p_j}$$

代入 [[Roy恒等式]] $\partial V/\partial p_j = -\lambda x_j$ 与 $\partial x^h/\partial U \cdot \lambda = \partial x/\partial m$ → 得 Slutsky 方程。

> 这个推导的核心是 [[包络定理]] + 对偶恒等式——纯代数。

## 应用

| 应用 | 章 |
|---|---|
| 区分 [[正常商品与劣等商品]] | Ch 7 |
| 推导 [[Giffen商品]] 的 SE-IE 反向条件 | Ch 7 |
| [[禀赋经济中的SE-IE]] 推广（加上禀赋项） | Ch 8 |
| 形式化 [[Marshallian需求与Hicksian需求关系]] | Ch 10 |
| 评估 [[无谓损失DWL]] 的需求曲线选择 | Ch 10 |

## 在 [[Microeconomics-Nechyba-2e|Nechyba 教材]] 中的位置

教材 Ch 7A 给出 SE-IE 的图形分解，Ch 10B 给出 Slutsky 方程的形式化推导。是连接整个 Ch 7-10 的中心代数。

## 反面论点与数据空白

- **[BIAS] Slutsky 对称性的实证检验**：当代消费需求文献（Browning, Deaton, Hausman）反复发现违反对称性——可能是模型设定误差或聚合偏差,教材在 Ch 1–10 不涉及。
- **数据空白**：Slutsky 方程的实证应用（如估计补偿弹性矩阵）的当代方法，教材未提及。

## 相关页

- [[消费者对偶性]] / [[替代效应]] / [[Marshallian需求与Hicksian需求关系]]
- [[Roy恒等式]] / [[Shephard引理]] / [[包络定理]]
- [[补偿预算]] / [[禀赋经济中的SE-IE]]
- [[Eugen Slutsky]] / [[John Hicks]] / [[Microeconomics-Nechyba-2e]]
