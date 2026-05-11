---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, welfare, taxation, foundations]
confidence: medium
decay_category: medium
status: foundation
---

# DWL几何增长

## 一句话命题

> 在线性需求 / 供给假设下，从量税 $t$ 造成的 [[无谓损失DWL]] **正比于税率的平方**：
>
> $$DWL \propto t^2$$
>
> 含义：**税率翻倍，DWL 翻四倍** ——扭曲损失对税率高度敏感。

## 几何论证

税率 $t$ 引起：
- 税基（数量）线性下降 $\Delta Q \propto t$；
- 税收 $T = t \cdot (Q^* - \Delta Q) \approx t \cdot Q^*$（$\Delta Q$ 很小时）→ **线性**；
- DWL = "三角形"面积 = $(1/2) \cdot t \cdot \Delta Q \propto t \cdot t = t^2$ → **二次**。

## 政策含义

| 比较 | 直觉 |
|---|---|
| **加倍单一税 $t$** vs **拆成两个 $t/2$ 税** | 单一: $DWL \propto t^2$；拆分两个: $2 \cdot (t/2)^2 = t^2/2$ → **更优** |
| **均匀低税** vs **少数高税** | 均匀低税总 DWL 更小 → Ramsey 最优税理论的核心直觉 |
| **税基窄化 + 税率高** | DWL 急速膨胀 → 现代税制偏好"宽税基 + 低税率" |

> 这一二次增长性质是**后续最优税理论的核心动机**——见 Ch 22（Batch 5 摄入）。

## 与 [[Laffer曲线]] 的关系

Laffer 曲线刻画的是 $T(t)$ 关系（先升后降），DWL 几何增长刻画的是 $DWL(t)$ 关系（**始终单调上升**）。两者并存：
- 即使 $t < t^*$（增税仍增收），$DWL$ 仍**几何增长**；
- 减税不一定减税收（可能在 Laffer 后段），但**总能**减 DWL。

## 教材的数值示例

教材 Ch 10 Table 10.1 / 10.2 用 CES 偏好 $\sigma = 1$、$\sigma = 0.5$、$\sigma = 2$ 三档校准，给出不同税率下的 DWL/T 比率。
- $\sigma$ 越大 → 同税率下 DWL 越大（消费者越能躲）；
- $t$ 越大 → DWL/T 越快上升（"每多收 1 元税，社会损失越多"）。

> **数据空白**：教材引述"住房 $\sigma \approx 1$" 等参数但**未给一手实证文献**——Table 10.1/10.2 数值标定缺独立校验。

## 在 [[Microeconomics-Nechyba-2e|Nechyba 教材]] 中的位置

教材 Ch 10A 用图形论证 DWL 的二次增长，Ch 10B 用积分给出严格表达式。Ch 22 将其与最优税理论结合（Batch 5 摄入）。

## 反面论点与数据空白

- **[BIAS] 二次假设依赖线性需求/供给**：现实中弹性随价格变化、配给/折点存在，DWL 增长可能不是干净的 $t^2$。
- **[BIAS] 仅"扭曲税都有 DWL"**：忽略 Pigou 矫正性税可降低 DWL（外部性场景）——见 [[总额税与扭曲税]]。
- **数据空白**：DWL 在不同税收类型间的相对量级（销售 vs 所得 vs 资本）的实证排序，教材未提供。

## 相关页

- [[无谓损失DWL]] / [[总额税与扭曲税]] / [[Laffer曲线]]
- [[消费者剩余]] / [[补偿需求曲线]] / [[替代弹性]]
- [[Microeconomics-Nechyba-2e]]
