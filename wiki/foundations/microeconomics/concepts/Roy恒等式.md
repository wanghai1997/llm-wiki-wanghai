---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, duality, foundations]
confidence: medium
decay_category: medium
status: foundation
---

# Roy恒等式

## 公式

$$\boxed{x_i(p, m) = -\frac{\partial V(p, m)/\partial p_i}{\partial V(p, m)/\partial m}}$$

[[Marshallian需求曲线]] = [[间接效用函数]] $V$ 对**价格的偏导**除以**收入的偏导**（再取负号）。

## 历史

由 [[René Roy]] 在 *La distribution du revenu entre les divers biens*（Econometrica, 1947）系统化。是对偶系统中"间接效用 → Marshallian 需求"的形式通道。

## 直觉（[[包络定理]] 解读）

UMP 的最优值函数 $V(p, m) = u(x^*(p, m))$。对 $p_i$ 求偏导（用包络定理）：

$$\frac{\partial V}{\partial p_i} = -\lambda \cdot x_i^*$$

其中 $\lambda = \partial V/\partial m$ 是收入边际效用。两式相除（取负号）→ Roy 恒等式。

直觉：**$p_i$ 微小上涨给消费者造成的福利损失** $= x_i^* \cdot \lambda$（损失 $x_i^*$ 单位购买力 × 每单位收入的边际效用）。

## 与 [[Shephard引理]] 的对偶位置

| 通道 | 公式 |
|---|---|
| **Shephard**（支出 → Hicksian） | $x_i^h = \partial E/\partial p_i$ |
| **Roy**（间接效用 → Marshallian） | $x_i = -V_{p_i}/V_m$ |

两者结构镜像，是 [[消费者对偶性]] 的核心机器对。

## 推导细节

UMP 一阶条件 + 包络定理：

$$\frac{\partial V}{\partial p_i} = \frac{\partial \mathcal L^*}{\partial p_i} = -\lambda x_i^*, \quad \frac{\partial V}{\partial m} = \frac{\partial \mathcal L^*}{\partial m} = \lambda$$

→ 比值消去 $\lambda$ → $x_i^* = -V_{p_i}/V_m$。

## 应用

- **从 $V$ 还原需求函数** ：若已估出间接效用（如 logit / nested logit 模型），可用 Roy 恒等式直接生成需求曲线，无需重解 UMP。
- **CV / EV 推导** ：[[补偿变差CV]] / [[等价变差EV]] 用 $V$ 在两价格下的反函数给出（推迟 Batch 4 / MWG）。

## 在 [[Microeconomics-Nechyba-2e|Nechyba 教材]] 中的位置

教材 Ch 10B 与 [[Shephard引理]] 并列引入——构成"价值函数 → 需求函数"的双通道。后续 Ch 16 / Ch 22 / 福利经济学章节反复用此简化。

## 反面论点与数据空白

- **[BIAS] 假设 $V$ 可微**：偏好不光滑（[[折点预算]] / [[非凸偏好与多解]]）时 $V$ 可能不可微——教材 Ch 10 不展开。
- **数据空白**：Roy 恒等式的实证应用（如离散选择模型的"间接效用 → 选择概率"）在 Ch 1–10 不涉及。

## 相关页

- [[消费者对偶性]] / [[间接效用函数]] / [[Marshallian需求曲线]] / [[效用最大化问题]]
- [[Shephard引理]] / [[Slutsky方程]] / [[包络定理]]
- [[René Roy]] / [[Microeconomics-Nechyba-2e]]
