---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [概念, microeconomics, foundations, batch2, 生产理论]
confidence: medium
decay_category: slow
status: foundation
---

# 边际技术替代率 MRTS

> 生产侧的 MRTS 与消费者侧的 [[边际替代率MRS]] 完全镜像；二者本质都是"等值线切线斜率"。

## 定义

**边际技术替代率**（Marginal Rate of Technical Substitution）= 沿 [[等产量线]] 减少 1 单位 $L$ 时**为维持产出**须增加的 $K$：

$$
MRTS_{LK} = -\frac{dK}{dL}\bigg|_{f(L,K) = \bar x} = \frac{MP_L}{MP_K}
$$

由全微分 $df = MP_L \, dL + MP_K \, dK = 0$ 解出。

## 几何

[[等产量线]] 上某点的**切线斜率绝对值**。沿凸向原点的等产量线，MRTS **递减**——继续替代 $L$ 替 $K$ 越来越"困难"（[[边际产品MP|MP 递减]] 的几何映射）。

## 经济学含义

> "若再多 1 单位 $L$ 能替代 $\frac{MP_L}{MP_K}$ 单位 $K$（保持产出不变），那么市场上换 1 单位 $L$ 须付 $w/r$ 单位 $K$ 的成本——若 $MRTS > w/r$，多用 $L$ 更便宜。"

成本最小化的内点 FOC：

$$
\boxed{MRTS_{LK} = \frac{w}{r}}
$$

——即"技术替代率 = 市场价格比"。这是 [[成本最小化问题|CMP]] 与 [[消费者对偶性|EMP]] 内点条件 $MRS = p_1/p_2$ 的完全镜像。

## 与 MRS 的镜像

| 消费者侧 [[边际替代率MRS]] | 生产侧 MRTS |
|---|---|
| $MRS = MU_1/MU_2 = p_1/p_2$ | $MRTS = MP_L/MP_K = w/r$ |
| 序数偏好的"主观换算率" | 客观技术的"工程换算率" |
| 沿无差异曲线递减（凸偏好）| 沿等产量线递减（[[边际产品MP|MP 递减]]）|

> 关键差异：MRS 在不同消费者间不可基数比较；MRTS 在所有厂商面对相同技术时**完全一致**（行业内技术普及）。

## 与替代弹性的关系

[[替代弹性]] σ（生产侧）= MRTS 沿等产量线变化的快慢的对数刻画：

$$
\sigma = \frac{d \ln(K/L)}{d \ln(MRTS)}
$$

- σ = 0：MRTS 在折角处突变（Leontief，完全互补）
- σ = ∞：MRTS 沿曲线不变（线性，完全替代）
- σ = 1：Cobb-Douglas

## 应用

1. **CMP 求解**：把 $MRTS = w/r$ 与 $f(L, K) = \bar x$ 联立，得 [[条件投入需求]]。
2. **PMP 求解**：在 [[利润最大化问题]] 中，$MRTS$ 在两步分解的 Step 1 决定投入比例；Step 2 决定输出规模。
3. **行业要素份额**：在 Cobb-Douglas $f = L^\alpha K^\beta$ 下，$MRTS = (\alpha/\beta)(K/L)$；要素相对工资 $w/r$ 即决定要素相对用量 $L/K$。

## 反面论点与数据空白

- **MRTS 的"客观性"假设**：现实中不同企业面对**异质技术**（管理质量、组织资本），同一行业内 MRTS 差异显著（Bloom-Van Reenen 2007 实证）。Nechyba 把技术当行业级标量。
- **不光滑生产**：Leontief 在折角处 MRTS 不存在；Activity Analysis 在多技术组合下 MRTS 跃变。
- **数据空白**：行业 MRTS 估计依赖 σ 估计，二者高度相关。Berndt 1991 *The Practice of Econometrics* 给出能源 / 资本替代弹性的范围（0.3-1.5），Nechyba 不引。

## 相关页

- 镜像：[[边际替代率MRS]]
- 上游：[[等产量线]]、[[边际产品MP]]
- 下游：[[替代弹性]]、[[成本最小化问题]]、[[条件投入需求]]、[[规模报酬]]
- 主题：[[厂商最优化选择]]
