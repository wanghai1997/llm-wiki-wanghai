---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, foundations, welfare, CV]
confidence: medium
decay_category: slow
status: foundation
---

# 补偿变差（CV）

> Compensating Variation

补偿变差（Compensating Variation, CV）是衡量价格变化对消费者福利影响的**精确货币指标**。它回答的问题是：**在新的价格下，需要补偿（或可以取走）消费者多少钱，才能使其效用恢复到价格变化前的水平？**

## 定义

设价格从 $p^0$ 变为 $p^1$，消费者效用从 $V(p^0, I)$ 变为 $V(p^1, I)$。

**CV** = 在新的价格 $p^1$ 下，使消费者回到原效用水平 $V(p^0, I)$ 所需的收入变化：

$$V(p^1, I + CV) = V(p^0, I)$$

或用支出函数表示：

$$CV = e(p^1, V(p^0, I)) - e(p^0, V(p^0, I)) = e(p^1, U^0) - I$$

其中 $e(p, U)$ 是[[支出函数]]（达到效用水平 $U$ 所需的最小支出），$U^0 = V(p^0, I)$ 是原效用水平。

## 与 Hicksian 需求的关系

CV 可以表示为 Hicksian（补偿）需求曲线下的面积：

$$CV = \int_{p^1}^{p^0} h(p, U^0) \, dp$$

其中 $h(p, U^0)$ 是在原效用水平 $U^0$ 下的 Hicksian 需求（见 [[补偿需求曲线]]）。

### 几何解释

- 若价格**上升**（$p^1 > p^0$）：CV > 0，表示需要**补偿**消费者才能使其回到原效用水平。
- 若价格**下降**（$p^1 < p^0$）：CV < 0，表示可以**从消费者取走** $|CV|$ 而使其仍保持原效用水平。

## CV vs 消费者剩余（CS）

| 维度 | 消费者剩余（CS） | 补偿变差（CV） |
|---|---|---|
| 基于的需求 | Marshallian（无补偿） | Hicksian（补偿） |
| 效用假设 | 仅在[[准线性偏好]]下精确 | **对任何偏好都精确** |
| 计算难度 | 易（观察 Marshallian 需求） | 难（需 Hicksian 需求或支出函数） |
| 收入效应 | 忽略 | 正确处理 |
| 适用场景 | 粗略估计 | 精确福利分析 |

### 关系公式

在价格变化很小时，$CS \approx CV$（一阶近似）。但价格变化大时，差异可能显著——尤其在收入效应强的商品（如住房、食品）上。

## 应用：政策评估

CV 是政策评估的标准工具：

- **价格管制**：rent control 使房租下降 → CV 衡量租客的福利增益。
- **税收政策**：消费税使价格上升 → CV 衡量消费者福利损失。
- **公共品定价**：公园收费/免费 → CV 衡量访问者的福利变化。

### 与 EV 的比较

见 [[等价变差EV]]：CV 以**新价格**为基准计算补偿；EV 以**原价格**为基准计算补偿。两者通常不相等（除非准线性偏好）。

## 反面论点与数据空白

- CV 的**测量困难**：需要估计 Hicksian 需求或支出函数，但现实中只能观察到 Marshallian 需求。需要借助[[Slutsky方程]]进行转换。
- **等价标尺问题**（Equivalent Scale）：CV 使用货币作为福利标尺，但货币的边际效用因人而异（穷人 vs 富人）。人际比较时需谨慎。
- 教材 Ch 10 仅提及 CV/EV 概念，但未深入计算。MWG 等高级教材提供完整形式化。本 Wiki 在 Batch 4 补足，因 Ch 19 税收福利分析是引入 CV/EV 的自然时机。

## 相关页

- [[等价变差EV]] — CV 的对偶概念
- [[消费者剩余]] — 近似福利指标
- [[支出函数]] — CV 的支出函数定义
- [[补偿需求曲线]] — CV 的几何表示
- [[Hicksian需求]] — CV 计算的基础
- [[Slutsky方程]] — Marshallian 与 Hicksian 需求的转换工具
- [[无谓损失DWL]] — CV 可用于精确计算 DWL
