---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, instrumental-variables, causal-inference, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# 工具变量 IV

## 一句话定义

> **工具变量** = 利用一个与处理变量**强相关**、但通过**唯一渠道**（处理）影响结果的**外生变异**，来识别因果效应——当处理非随机时，IV 恢复**依从者**的因果效应。

## IV 三条件

一个有效的工具变量 $Z_i$ 必须同时满足：

1. **第一阶段（相关性）**：$Z_i$ 对处理 $D_i$ 有因果效应——$\text{Cov}(Z_i, D_i) \neq 0$
2. **独立性**：$Z_i$ 是随机分配的或"如同随机分配"——与不可观测混淆因素无关
3. **排他性约束**：$Z_i$ 影响结果 $Y_i$ 的**唯一渠道**是通过 $D_i$——不存在其他因果通路

## IV 的链式反应

$$Z_i \xrightarrow{\text{第一阶段 } \phi} D_i \xrightarrow{\text{因果效应 } \lambda} Y_i$$

- **第一阶段** $\phi$：$Z_i$ 对 $D_i$ 的因果效应（如彩票中签→KIPP 入学概率增加 0.74）
- **简约式** $\rho$：$Z_i$ 对 $Y_i$ 的总效应（如彩票中签→数学成绩提高 0.36σ）
- **IV 估计量** = $\lambda = \frac{\rho}{\phi}$（LATE）

## IV 估计量公式（Wald Estimator）

$$\lambda = \frac{E[Y_i|Z_i=1] - E[Y_i|Z_i=0]}{E[D_i|Z_i=1] - E[D_i|Z_i=0]} = \frac{\text{简约式}}{\text{第一阶段}}$$

## IV 三种变体的统一视角

Mastering 'Metrics Ch 3 用三个案例展示了一个统一的 IV 框架：

| 案例 | 工具变量 $Z_i$ | 处理 $D_i$ | 不依从问题 |
|------|---------------|-----------|-----------|
| [[KIPP特许学校彩票]] | 彩票中签 | 上 KIPP | 赢家不去、输家进入 |
| [[MDVE家庭暴力实验]] | 警察随机指令 | 实际执法行动 | 警察不按指令执行 |
| [[家庭规模-子女质量trade-off]] | 双胞胎/同性子女 | 实际子女数 | 家庭可能不按双胞胎调整行为 |

三个案例的共同结构：$Z_i$ 是随机/准随机的，但 $D_i$ ≠ $Z_i$——因此需要用 IV 从 ITT（$\rho$）恢复 LATE（$\lambda$）。

## 反面论点与数据空白

- **排他性约束永远不可直接检验**：只能通过制度知识和间接论证来辩护——这是 IV 方法的阿喀琉斯之踵。
- **弱工具变量问题**：如果第一阶段很弱（$Z_i$ 和 $D_i$ 关联小），IV 估计有偏且标准误巨大——Staiger-Stock (1997) F > 10 的经验法则。
- **LATE 的局部性**：IV 只恢复 compliers 的因果效应——对 always-takers 和 never-takers 无信息。不同工具变量的 LATE 可能不同。
- **同质效应假设用于推断**：Cov($D_i, Z_i$) ≠ 0 时 IV 估计识别的是什么？——没有额外假设时，IV 估计趋近于 LATE 而非 ATE。

## 相关页

- [[两阶段最小二乘法2SLS]] / [[局部平均处理效应LATE]]
- [[第一阶段与简约式]] / [[排他性约束]]
- [[KIPP特许学校彩票]] / [[MDVE家庭暴力实验]] / [[家庭规模-子女质量trade-off]]
- [[Sewall-Wright]]
- [[Mastering-Metrics]]
