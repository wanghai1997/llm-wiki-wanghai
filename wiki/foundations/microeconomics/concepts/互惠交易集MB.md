---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [概念, microeconomics, foundations, batch3, 一般均衡]
confidence: medium
decay_category: slow
status: foundation
---

# 互惠交易集MB

> Edgeworth 盒中**从禀赋 $\omega$ 出发,使两人都不变差**的所有可达配置构成的"透镜形"区域。两条经过 $\omega$ 的无差异曲线 $U^A(\omega)$ 与 $U^B(\omega)$ 围成。

## 形式定义

设禀赋 $\omega = (\omega^A, \omega^B)$,$U^A(\omega), U^B(\omega)$ 分别是两人在禀赋点的效用。

**互惠交易集**:
$$
MB(\omega) = \{ (x^A, x^B) \mid x^A + x^B = \bar{x}, \quad U^A(x^A) \ge U^A(\omega), \quad U^B(x^B) \ge U^B(\omega) \}
$$

几何上是 Edgeworth 盒中由两条无差异曲线 $U^A(\omega)$ 和 $U^B(\omega)$ 围成的"透镜形"。

## 几何描述

- $U^A(\omega)$ 从 A 视角看,是经过 $\omega$ 的无差异曲线,$\omega$ 上方右方都是 $U^A > U^A(\omega)$。
- $U^B(\omega)$ 从 B 视角看,是经过 $\omega$ 的无差异曲线,在盒内 $\omega$ 下方左方都是 $U^B > U^B(\omega)$(B 原点在右上)。
- 两条曲线在 $\omega$ 处通常**相交而非相切**(除非 $\omega$ 已是 Pareto 高效)。
- 两曲线之间的"透镜形"区域 = 互惠交易集。

## 重要性质

### 性质 1:MB 总是非空

只要 $\omega$ 不是 Pareto 高效点,MB 包含**$\omega$ 本身 + 透镜形内部**——存在交易使两人都获益。

### 性质 2:MB 与契约曲线相交

互惠交易集与 [[契约曲线]] 的交集 = 既是 Pareto 高效又使两人都获益的配置。

> **Edgeworth 推断**:任何"理性"交易最终在 MB ∩ 契约曲线内——因 MB 外两人有人变差(自愿交易不能产生),契约曲线外可被进一步交易改善。

### 性质 3:Walras 均衡 ∈ MB

Walras 均衡是某价格下两人各自最优 + 市场出清,作为自愿交易后果,必然在 MB 内 + 契约曲线上。

## 与核(Core)的连接

两人经济中,**核 = MB ∩ 契约曲线**(两人版的"无人愿意阻断"的配置)。在多人经济中,核要求**任意联盟**都无法阻断 → 核可能小于 MB ∩ 契约曲线。详见 [[核Core]]。

## 与第二福利定理的连接

第二福利定理的逆过程:任何 MB ∩ 契约曲线内的点,都可通过一次 lump-sum 重分配 + 自由交易达到。这把"分配"与"高效"分离——任意公平的分配目标,只要在契约曲线上,都可实现为某再分配后的 Walras 均衡。详见 [[第二福利定理]]。

## 几何图景演化

教材 16A.2 给出三步图:
1. **静态**:禀赋 $\omega$ → 画两条无差异曲线 → 透镜形 MB。
2. **动态**:从 $\omega$ 沿任意路径"交易"达到 MB 内任意点。
3. **核 / 福利**:MB ∩ 契约曲线 = 自愿交易的稳态集合,Walras 均衡是其中之一。

## 反面论点与数据空白

- **MB 假设理性 + 完美信息**:现实交易有搜寻 / 谈判 / 信息不对称成本,实际可达点不构成完美透镜。
- **静态忽略时间维度**:MB 是单期交易集合,未考虑跨期偏好、风险、未来禀赋。Ch 17 状态相依商品扩展是部分回应。
- **多人对偶**:两人 MB 几何清晰,多人 MB 是高维多面体,失去"透镜"直觉。
- **行为经济学**:Loss aversion(Kahneman-Tversky 1979)使两人对禀赋有"偏向", 现实"无差异曲线"在禀赋点有 kink → MB 形状被扭曲。
- **数据空白**:Edgeworth 盒的实验经济学测试(Smith 1962 *Journal of Political Economy* "An Experimental Study of Competitive Market Behavior")在双方 / 多方议价 / 拍卖框架下,MB 收敛于核 vs Walras 均衡的实证证据。教材不引述。

## 相关页

- 上游:[[Edgeworth盒]] / [[Francis Edgeworth]]
- 邻居:[[契约曲线]] / [[核Core]] / [[阻断联盟]]
- 福利:[[第一福利定理]] / [[第二福利定理]]
- 主题:[[一般均衡]]
