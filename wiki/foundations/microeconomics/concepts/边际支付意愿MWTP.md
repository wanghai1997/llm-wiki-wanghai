---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, welfare, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# 边际支付意愿MWTP

## 一句话定义

> **MWTP（marginal willingness to pay）** = 消费者愿意为**多消费一单位** $x_1$ 付出的最大金额（以 $x_2$ 为计价单位）。在两商品图上即 [[边际替代率MRS]]——MWTP $= MRS$。

## 与需求曲线的关系

固定数量 $x_1$，遍历不同人 / 不同状态下的 MWTP，得**反需求曲线** $p_1 = MWTP(x_1)$。这是 Ch 10 把"需求曲线下方面积"理解为"全部支付意愿之和"的关键转换。

**直觉**：需求曲线 = 反需求曲线翻转。第 $x_1$ 单位上的高度 = 那个单位的边际支付意愿。

## 在 [[补偿需求曲线|Hicks]] vs [[Marshallian需求曲线|Marshall]] 上的差异

| 曲线 | MWTP 解读 |
|---|---|
| Hicksian | "保持效用不变下"愿付的最大值——**对偶**福利度量准确 |
| Marshallian | "在当前财富下"实际愿付——含 IE 偏差 |

二者在 [[准线性偏好]] 下重合。否则 Marshall 给出的"消费者剩余" = 沿 Marshall 曲线积分,与真实福利变化（CV/EV）有偏差。

## 公式

$$MWTP_1(x_1) = MRS_{12}(x_1, x_2) = \frac{\partial u/\partial x_1}{\partial u/\partial x_2}$$

在效用最大化处，MWTP $= p_1/p_2$ → 用 $x_2$ 为计价单位时 MWTP $= p_1$。

## 在 [[Microeconomics-Nechyba-2e|Nechyba 教材]] 中的位置

教材 Ch 10 把 MWTP 作为**消费者剩余的概念基底**——剩余 = "全部 MWTP 之和" 减去"实际支付总额"。这是 Ch 10A 不依赖微积分的"图形派"展开。

## 反面论点与数据空白

- **[BIAS] MWTP 可被市场环境影响**：实证 WTP 估计（contingent valuation, hedonic）系统性高估或低估真实 MWTP（Hausman 1993）。
- **数据空白**：教材未涉及 WTP 估计方法的争议。

## 相关页

- [[边际替代率MRS]] / [[消费者剩余]] / [[补偿需求曲线]]
- [[Marshallian需求曲线]] / [[Marshallian需求与Hicksian需求关系]]
- [[Microeconomics-Nechyba-2e]]
