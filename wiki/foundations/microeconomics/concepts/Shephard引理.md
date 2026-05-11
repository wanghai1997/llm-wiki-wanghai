---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, duality, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Shephard引理

## 公式

$$\boxed{x_i^h(p, U) = \frac{\partial E(p, U)}{\partial p_i}}$$

[[补偿需求曲线|Hicksian]] 需求 = [[支出函数]] $E$ 对该商品价格的偏导。

## 历史

由 [[Ronald Shephard]] 在 *Cost and Production Functions*（Princeton, 1953）系统化引入。原本同一引理在生产侧（条件投入需求 = 成本对工资的偏导）也适用——见 Batch 2 厂商章节。

## 直觉

由 [[包络定理]]：在最优束处，$E$ 关于 $p_i$ 的偏导**只通过 $x^h_i$ 这一直接通道**——其余通道（$x_j^h$ 受 $p_i$ 影响）的贡献为 0,因为它们处于最优,一阶变动相互抵消。

## 推导（教材 Ch 10B）

EMP 的拉格朗日：$\mathcal L = p \cdot x - \mu (u(x) - U)$

最优处 $E(p, U) = p \cdot x^h(p, U)$。对 $p_i$ 求偏导：

$$\frac{\partial E}{\partial p_i} = x_i^h + \sum_j p_j \frac{\partial x_j^h}{\partial p_i}$$

由 EMP 的 FOC（$p_j = \mu u_j$）+ 约束 $u(x^h) = U$ 求导（$\sum u_j \partial x^h_j/\partial p_i = 0$）→ 第二项 = 0 → $\partial E/\partial p_i = x_i^h$。

## 重要推论

1. **$E$ 关于 $p$ 单调不减**：因 $x^h \ge 0$，故 $\partial E/\partial p_i \ge 0$。
2. **$E$ 关于 $p$ 凹**：因 Hicksian 需求是单调下倾（自身价格 SE 非正）。
3. **对称性**：$\partial^2 E/\partial p_i \partial p_j = \partial x_i^h/\partial p_j = \partial x_j^h/\partial p_i$（[[Slutsky方程]] 对称性的直接来源）。

## 在 [[Microeconomics-Nechyba-2e|Nechyba 教材]] 中的位置

教材 Ch 10B 把 Shephard 引理与 [[Roy恒等式]] 并列引入,作为 [[消费者对偶性]] 的两件核心机器——前者从 $E$ 提取 Hicksian 需求,后者从 $V$ 提取 Marshallian 需求。两者**结构对偶**。

## 生产侧镜像：Shephard 引理（同名）

由于 Shephard 1953 原始版本就是**生产侧**（成本函数 → 条件投入需求），消费侧反而是"对偶引入"。Batch 2 [[成本函数]] 上：

$$
\boxed{L^c(w, r, \bar x) = \frac{\partial C(w, r, \bar x)}{\partial w}}, \quad K^c(w, r, \bar x) = \frac{\partial C(w, r, \bar x)}{\partial r}
$$

→ [[条件投入需求]] = [[成本函数]] 对要素价格的偏导。

### 两侧对照

| 消费侧 Shephard | 生产侧 Shephard |
|---|---|
| EMP（最小化支出）| CMP（最小化成本）|
| $\partial E/\partial p_i = x_i^h$ | $\partial C/\partial w = L^c$ |
| $E$ 关于 $p$ 凹 | $C$ 关于 $(w, r)$ 凹 |
| Slutsky 对称：$\partial x_i^h/\partial p_j = \partial x_j^h/\partial p_i$ | "厂商 Slutsky"对称：$\partial L^c/\partial r = \partial K^c/\partial w$ |
| 推论：$\partial x_i^h/\partial p_i \leq 0$（无 Giffen for compensated）| 推论：$\partial L^c/\partial w \leq 0$（条件需求单调下降）|

### 与生产侧 Hotelling 的关系

Shephard（生产侧）来自 CMP；[[Hotelling引理]] 来自 PMP。两者由 [[厂商对偶性]] 联结：

$$
L^*(p, w, r) = L^c(w, r, x^*(p, w, r))
$$

即"无条件 = 条件 + 最优产出代入"（详见 [[无条件投入需求]] 的 Slutsky-like 分解）。

## Roy 在生产侧的对应

消费侧 Roy 由"$p$ 仅在预算约束中出现"派生；生产侧 PMP 中 $p$ 在**目标函数**中出现，故对应的引理是 **Hotelling**（直接 $\partial \pi^*/\partial p = x^*$，无需除以拉格朗日乘子）。

| 消费侧 | 生产侧 |
|---|---|
| Roy（除法形式）：$x_i = -V_{p_i}/V_m$ | Hotelling（直接）：$x^* = \pi^*_p$ |
| 因 $p$ 在约束中 | 因 $p$ 在目标中 |
| 序数效用 → 需归一化 | 基数利润 → 直接读 |

详见 [[Hotelling引理]] §"为何不是 Roy 形式"。

## 反面论点与数据空白

- **[BIAS] 凹性假设**：Shephard 引理依赖 $E$ 关于 $p$ 的凹性,这要求偏好凸 + 内点解；非凸或角点处需修正——教材 Ch 10 不深入。
- **数据空白**：Shephard 引理的实证应用（用 $\partial E/\partial p$ 估计补偿弹性）在 Ch 1–10 不展开。

## 相关页

- [[消费者对偶性]] / [[支出函数]] / [[补偿需求曲线]] / [[支出最小化问题]]
- [[Roy恒等式]] / [[Slutsky方程]] / [[包络定理]]
- 生产侧镜像：[[Hotelling引理]] / [[厂商对偶性]] / [[成本函数]] / [[条件投入需求]]
- [[Ronald Shephard]] / [[Microeconomics-Nechyba-2e]]
