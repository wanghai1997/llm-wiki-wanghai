---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, instrumental-variables, LATE, causal-inference, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# 局部平均处理效应 LATE

## 一句话定义

> **LATE** = 工具变量识别的因果效应——不是全人口的平均处理效应（ATE），而是**恰好被工具变量推动改变处理状态的"依从者"（compliers）** 的平均因果效应。

## 为什么 IV 不识别 ATE

当处理的因果效应异质时（不同的人有不同的 $Y_{1i} - Y_{0i}$），IV 估计量 $\lambda$ 不等于 ATE，而是 LATE——compliers 的 ATE。

## 四种人群

在二值工具变量 $Z_i$ 和二值处理 $D_i$ 的情境下，人群被分为：

| 类型 | $D_i(1)$（$Z_i=1$ 时） | $D_i(0)$（$Z_i=0$ 时） | 定义 |
|------|----------------------|----------------------|------|
| **Compliers**（依从者） | 1 | 0 | 被工具推动改变处理 |
| **Always-takers**（总是接受者） | 1 | 1 | 不管工具，总是接受处理 |
| **Never-takers**（永不接受者） | 0 | 0 | 不管工具，永不接受处理 |
| **Defiers**（逆反者） | 0 | 1 | 工具推动时反而反向（通常假设不存在） |

> IV 估计量仅识别的 **Compliers 的因果效应** = LATE。

## LATE 定理

Angrist-Imbens-Rubin (1996) 证明：在 IV 的三个条件下，Wald Estimator 收敛于 LATE：

$$\lambda = \frac{E[Y_i|Z_i=1] - E[Y_i|Z_i=0]}{E[D_i|Z_i=1] - E[D_i|Z_i=0]} \xrightarrow{p} E[Y_{1i} - Y_{0i} | D_i(1) > D_i(0)]$$

> （右边：compliers 的平均因果效应）

## 在 Mastering 'Metrics 中的位置

Ch 3.1 [[KIPP特许学校彩票|KIPP 彩票案例]] 中：
- Compliers = 彩票赢家才上 KIPP、输家不上的学生（~74%）
- Always-takers = 不管赢不赢都设法上 KIPP 的学生（~3.5%）
- Never-takers = 即使赢了也不上 KIPP 的学生（~22.5%，选择去其他学校）
- LATE = .48σ（在 compliers 中 KIPP 的数学成绩效应）

## LATE 的精确性 vs 一般性的权衡

- **精确性**：LATE 是精确定义的——我们知道它适用于谁（compliers）
- **一般性受限**：LATE 不能直接推广到 always-takers 和 never-takers——"对不选 KIPP 的学生，KIPP 是否有益？"——IV 不能回答
- **不同工具的 LATE 不同**：KIPP 彩票的 LATE 和 Angrist-Krueger QOB 的 LATE 回答的是不同人群的效应——不可混为一谈

## 反面论点与数据空白

- **LATE 的政策相关性**：如果政策制定者关心的恰好是 compliers 的效应（如"抽签赢家如果真去上的话效果如何"）——LATE 完美适用。如果关心的是"如果强制所有人去上会如何"——LATE 不回答。
- **结构方法的批评**：Heckman-Urzua-Vytlacil (2006) 框架将 LATE 推广到连续工具变量和边际处理效应（MTE），可以外推到更广泛的政策参数——但需要更強的结构假设。
- **"Defiers" 假设**：标准 IV 框架假设无 defiers（单调性）——如果存在 defiers，IV 估计可能识别"有 defiers 时的奇怪加权组合"。

## 相关页

- [[工具变量IV]] / [[两阶段最小二乘法2SLS]]
- [[KIPP特许学校彩票]]
- [[Joshua-Angrist]]
- [[Mastering-Metrics]]
