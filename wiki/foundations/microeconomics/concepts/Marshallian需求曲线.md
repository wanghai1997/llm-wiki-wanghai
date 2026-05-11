---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, demand, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Marshallian需求曲线

## 一句话定义

> [[效用最大化问题|UMP]] 的解函数 $x_i^*(p, m)$ ——把"价格 $p$ 与收入 $m$"映射到"效用最大化时的消费量"。固定 $p_2$ 与 $m$，画 $(p_1, x_1^*)$ 即得 $x_1$ 的 **Marshallian 需求曲线**。

## 别称与定位

| 别称 | 来源 |
|---|---|
| Marshallian demand | [[Alfred Marshall]]（1895 *Principles*） |
| Uncompensated demand | 因不补偿购买力变化 |
| Walrasian demand | 一般均衡文献的同义词 |

> "Marshallian"是教材 Ch 9-10 的标准用法；"Hicksian"是其对偶版（[[补偿需求曲线]]）。

## 性质

| 性质 | 说明 |
|---|---|
| 0 阶齐次 | $x(\lambda p, \lambda m) = x(p, m)$ ——名义价格全比例上涨 + 收入同比例上涨 = 无变化 |
| 满足 Walras 律 | $\sum p_i x_i^*(p, m) = m$（预算紧约束） |
| 收入弹性 | $\partial x/\partial m \cdot m/x$ ——区分 [[正常商品与劣等商品]] |
| 价格效应 | 由 [[Slutsky方程]] 分解为 [[替代效应|SE]] + [[正常商品与劣等商品|IE]] |

## 与 [[补偿需求曲线|Hicksian]] 的关系

$$x_i(p, m) = x_i^h(p, V(p, m))$$

即：用间接效用 $V(p, m)$ 替代效用参数 $\bar U$,Marshall 与 Hicks **重合于同一点 $(p, m)$**。两者**斜率**通过 [[Slutsky方程]] 关联——见 [[Marshallian需求与Hicksian需求关系]]。

**只**在准线性下两条曲线**整段**重合（详见 [[准线性偏好]] / [[消费者剩余]]）。

## 反例—— [[Giffen商品]]

强劣等 + 大占比商品的 Marshall 需求曲线**上倾**——SE-IE 分解中"反向 IE 大于 SE"导致总效应反向。

## 在 [[Microeconomics-Nechyba-2e|Nechyba 教材]] 中的位置

教材 Ch 9 系统推导 Marshallian 需求——从 UMP 闭式解（Cobb-Douglas / CES）出发,沿 $p_1$ 取值画出需求曲线。Ch 10 把它作为消费者剩余 / 福利测度的**默认曲线**,但反复警告其度量偏差（与 Hicks 的差距）。

## 反面论点与数据空白

- **[BIAS] 教材偏置 CD 闭式示例**：CD 的 Marshall 需求是 $x_1^* = \alpha m / p_1$ ——形状极简,易让读者低估真实需求曲线的复杂度。
- **数据空白**：教材未涉及 Marshall 需求的实证估计（AIDS、QUAIDS、translog demand systems）。

## 相关页

- [[效用最大化问题]] / [[间接效用函数]] / [[Marshallian需求与Hicksian需求关系]]
- [[Slutsky方程]] / [[Roy恒等式]]
- [[Giffen商品]] / [[正常商品与劣等商品]] / [[需求曲线斜率与商品类型]]
- [[消费者剩余]]
- [[Alfred Marshall]] / [[Microeconomics-Nechyba-2e]]
