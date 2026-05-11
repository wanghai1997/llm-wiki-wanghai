---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, demand, duality, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Marshallian需求与Hicksian需求关系

## 一句话定义

> 同一消费者的 Marshallian 需求 $x(p, m)$ 与 Hicksian 需求 $x^h(p, U)$ **在原始 $(p, m)$ 处重合**，但斜率不同。两者通过 [[Slutsky方程]] 形式化关联。

## 一致性条件

$$x_i^h(p, V(p, m)) = x_i(p, m), \qquad x_i(p, E(p, U)) = x_i^h(p, U)$$

在**原始**消费点二者相等；偏离原始点时分歧。

## 斜率分歧（[[Slutsky方程]]）

$$\underbrace{\frac{\partial x_i}{\partial p_i}}_{\text{Marshall 价格效应}} = \underbrace{\frac{\partial x_i^h}{\partial p_i}}_{\text{Hicks 价格效应（纯 SE）}} - \underbrace{x_i \cdot \frac{\partial x_i}{\partial m}}_{\text{IE}}$$

- Marshall 斜率 = Hicks 斜率 - IE 项；
- IE 项符号取决于商品是 [[正常商品与劣等商品|正常 / 劣等]];
- 通常 Marshall 比 Hicks **更陡峭**（正常商品 + 同方向 IE）。

## 整段重合 ⟺ 准线性

[[准线性偏好]] $u = v(x_1) + x_2$ 下：
- $\partial x_1/\partial m = 0$ → IE 项消失；
- → Marshall = Hicks **整段重合**。

> 教材 Ch 10 反复强调这一充分条件：**仅在准线性下** $\Delta CS$ 沿 Marshall 曲线积分 = 真实福利变化（CV/EV）。

## CD 不是准线性

⚠️ Cobb-Douglas $u = x_1^\alpha x_2^{1-\alpha}$ 是 $\sigma = 1$ 的特殊 CES、属 [[同位偏好|同位偏好]]，**但不是准线性** ——CD 下 $\partial x_1/\partial m = \alpha/p_1 \ne 0$，IE 项不消失。教材在 Ch 6-9 反复用 CD 求闭式解,在 Ch 10 切换到准线性时容易让读者误把"CD ≈ 准线性"——实际上 CD 与 Hicks 曲线**整段不重合**。详见 [[消费者剩余]] / [[Microeconomics-Nechyba-2e]] 的偏置警告。

## 几何

| | Marshall | Hicks |
|---|---|---|
| $p_1$ 上升 | 沿**新预算线**到新切点 → 含 IE | 沿**原 IC**到新斜率切点 → 仅 SE |
| 该商品需求降幅 | **更大**（正常商品 + IE 反向） | 较小 |

## 在 [[Microeconomics-Nechyba-2e|Nechyba 教材]] 中的位置

教材 Ch 10 把"M / H 关系"作为对偶系统的"双侧角色分配"——
- M 是**实际可观测**的需求函数；
- H 是**福利度量准确**的需求函数；
- 二者通过 [[Slutsky方程]] 连接。

## 反面论点与数据空白

- **[BIAS] 教材的 CD 偏置**：见 [[消费者剩余]] 与 [[Microeconomics-Nechyba-2e]]。
- **[BIAS] 单消费者图景**：现实需求曲线是聚合曲线,Marshall 与 Hicks 的关系在聚合层级更复杂（Sonnenschein-Mantel-Debreu）。
- **数据空白**：教材未涉及"如何从 Marshall 数据反推 Hicks 曲线"的实证方法。

## 相关页

- [[Marshallian需求曲线]] / [[补偿需求曲线]] / [[Slutsky方程]]
- [[准线性偏好]] / [[同位偏好]] / [[偏好类型]]
- [[消费者剩余]] / [[消费者对偶性]]
- [[Microeconomics-Nechyba-2e]]
