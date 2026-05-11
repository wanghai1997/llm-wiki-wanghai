---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [概念, microeconomics, foundations, batch2, 生产理论, 对偶]
confidence: medium
decay_category: slow
status: foundation
---

# Hotelling 引理

> [[利润函数]] 对**任一价格**的偏导直接给出对应的最优数量——产品价格的偏导得 [[输出供给曲线|输出供给]]，要素价格的偏导得 [[无条件投入需求]] 的负值。是 [[包络定理]] 在 PMP 上的应用，也是 [[Roy恒等式]] 与 [[Shephard引理]] 的"双侧扩展"。

## 引理陈述

设 [[利润函数]] $\pi^*(p, w, r)$ 在内点处可微，则：

$$
\boxed{
\frac{\partial \pi^*}{\partial p} = x^*(p, w, r), \quad \frac{\partial \pi^*}{\partial w} = -L^*(p, w, r), \quad \frac{\partial \pi^*}{\partial r} = -K^*(p, w, r)
}
$$

读法："不需要重新求 PMP——只需对值函数偏导，符号自动给出最优数量。"

## 证明（包络定理）

PMP 的拉格朗日（无约束版）：

$$
\pi(L, K, x; p, w, r) = p f(L, K) - wL - rK \quad \text{（实质就是目标函数）}
$$

对参数 $w$ 求 $\pi^*$ 偏导：

$$
\frac{\partial \pi^*}{\partial w} = \frac{\partial \pi}{\partial w} \bigg|_{(L, K) = (L^*, K^*)} + \underbrace{\frac{\partial \pi}{\partial L} \cdot \frac{\partial L^*}{\partial w} + \frac{\partial \pi}{\partial K} \cdot \frac{\partial K^*}{\partial w}}_{= 0 \text{（FOC）}}
$$

第二项由 PMP 的 FOC（$\partial \pi / \partial L = 0$、$\partial \pi / \partial K = 0$）为零；第一项 $= -L^*(p, w, r)$。证毕。

## 两步证明法（通过 $C$ 中介）

由 [[两步利润最大化]]：$\pi^*(p, w, r) = p x^*(p, w, r) - C(w, r, x^*(p, w, r))$。

对 $w$ 偏导，应用包络定理：

$$
\frac{\partial \pi^*}{\partial w} = -\frac{\partial C}{\partial w} \bigg|_{x = x^*} = -L^c(w, r, x^*) = -L^*(p, w, r)
$$

第一等号用 [[Shephard引理]] 在 $x^*$ 处取值；第二等号用 [[厂商对偶性]] 恒等式 $L^* = L^c(w, r, x^*)$。

对 $p$ 偏导：

$$
\frac{\partial \pi^*}{\partial p} = x^* + \underbrace{(p - MC) \cdot \frac{\partial x^*}{\partial p}}_{= 0 \text{（PMP FOC: } p = MC \text{）}} = x^*
$$

## 三个引理的统一视角

| 引理 | 函数 | 偏导对象 | 给出 |
|---|---|---|---|
| [[Roy恒等式]] | 间接效用 $V(p, I)$ | $p_i, I$ | 马歇尔需求 $x^M_i$ |
| [[Shephard引理]] | 支出 $E(p, \bar u)$；成本 $C(w, r, \bar x)$ | $p_i$；$w$ | 补偿需求 $h_i$；条件需求 $L^c$ |
| **Hotelling 引理** | 利润 $\pi^*(p, w, r)$ | $p, w, r$ | $x^*, -L^*, -K^*$ |

> 三者皆是 [[包络定理]] 的应用，但应用的"包络面"不同：UMP（Roy）、EMP/CMP（Shephard）、PMP（Hotelling）。

## 与 Shephard 的差异

| 维度 | Shephard（CMP / EMP）| Hotelling（PMP）|
|---|---|---|
| 值函数 | $C(w, r, \bar x)$（凹于 $w, r$）| $\pi^*(p, w, r)$（凸于 $p, w, r$）|
| 数量约束 | 输出 / 效用**外生** | 数量**内生** |
| 一阶偏导符号 | $\partial C / \partial w = +L^c$ | $\partial \pi^* / \partial w = -L^*$（要素是惩罚项）|
| 二阶偏导单调性 | $\partial L^c / \partial w \leq 0$（凹）| $\partial L^* / \partial w \leq 0$（凸 → $-\partial L^* \geq 0$，即 $\partial L^* \leq 0$）|

两者结合给出"Slutsky-like" 分解（详见 [[厂商对偶性]] §"关键恒等式"）。

## 应用

1. **生产者剩余 = $\Delta \pi^*$**：政策改变 $p$ 时，$\Delta \pi^* = \int x^* \, dp$（梯度 = $x^*$）；类似消费者侧 $\Delta CV / EV$ 用 [[补偿需求曲线]]。
2. **要素需求弹性预测**：$\eta_{Lw} = (\partial L^* / \partial w)(w / L^*)$ = 二阶导数 / 一阶导数比，$\pi^*$ 凸性保证 $\eta \leq 0$。
3. **跨价格效应对称**：$\partial L^* / \partial r = \partial K^* / \partial w$（$\pi^*$ 二阶混合偏导对称）——这是厂商侧的"Slutsky 对称性"，无需消费者侧的"补偿"修正。
4. **政策评估**：碳税 $\tau$ 加在能源要素 $E$，$\Delta \pi^* = -\int L_E^* \, d\tau$（厂商损失），可用于税负归宿分析。

## 反面论点与数据空白

- **可微性要求**：$\pi^*$ 在 kink 点（多 PMP 解，如离散投入）不可微，引理需用次梯度。
- **凸生产集前提**：$\pi^*$ 凸性依赖 $f$ 凹（或生产集凸）；IRS 下 $\pi^*$ 无界，引理失去意义（详见 [[规模报酬]] [BIAS]）。
- **价格外生**：垄断 / 寡头下 $p$ 内生于需求曲线，$\pi^*$ 不再是 $(p, \cdot)$ 的函数，引理形式变为 $\partial \pi^* / \partial \theta$（其中 $\theta$ 是产品差异化等参数）。
- **多产出**：单产出 $x \in \mathbb{R}$ 时 $\partial \pi^* / \partial p$ 是标量；多产出下 $\nabla_p \pi^* \in \mathbb{R}^m$ 给出向量供给。
- **数据空白**：实证识别 Hotelling 偏导需要可信的价格外生变化（自然实验、IV）；跨国跨行业实证发现要素需求弹性 $\eta \in [-0.3, -1.0]$（Hamermesh 1993），但 Nechyba 不引。

## 历史

[[Harold Hotelling]] 1932 年在《Journal of Political Economy》论文 "Edgeworth's Taxation Paradox and the Nature of Demand and Supply Functions" 中给出此引理。早于 [[Shephard引理]]（1953）和 [[Roy恒等式]]（1947）。本 Wiki 在 [[Harold Hotelling]] 页给出其完整工作背景。

## 相关页

- 关联引理：[[Roy恒等式]]、[[Shephard引理]]、[[包络定理]]
- 上游：[[利润函数]]、[[利润最大化问题]]
- 下游：[[输出供给曲线]]、[[无条件投入需求]]、[[厂商对偶性]]
- 提出者：[[Harold Hotelling]]
- 主题：[[厂商最优化选择]]
