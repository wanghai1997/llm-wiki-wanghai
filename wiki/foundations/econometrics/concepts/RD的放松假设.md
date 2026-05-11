---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, regression-discontinuity, fuzzy-RD, unconfoundedness, foundations, Wooldridge]
confidence: medium
decay_category: slow
status: foundation
---

# RD 的放松假设

## 一句话定义

> 模糊 RD (Fuzzy RD) 的标准识别依赖于**断点处的无混淆性（局部 IV）**——Wooldridge Ch 19 讨论了如何在放松这个假设时仍能识别因果效应，这是 RD 方法论的前沿。

> **前置阅读**：[[断点回归RD]]（MM Ch 4）提供 RD 的完整直觉和基础概念。

## Sharp RD 的再表述

Sharp RD 在断点处：处理概率从 0 跳到 1 → 在断点处不需要排除性约束以外的工具：
$$\tau_{SRD} = \frac{\lim_{x \downarrow c} E(y|x) - \lim_{x \uparrow c} E(y|x)}{1 - 0}$$

## Fuzzy RD 的标准处理

当处理概率在断点处跳跃但不到 1：

$$\tau_{FRD} = \frac{\lim_{x \downarrow c} E(y|x) - \lim_{x \uparrow c} E(y|x)}{\lim_{x \downarrow c} E(D|x) - \lim_{x \uparrow c} E(D|x)}$$

这是**断点处的 Wald 估计量**——用"过线"作为处理 $"D"$ 的工具变量。

## 放松无混淆性——FRD 的进一步推广

标准 FRD 假设：给定 running variable $x$，在断点附近 $D$ 的分配是随机的（局部无混淆）。

Ch 19 讨论：如果这个假设不成立（即过线与否之外，还有其他因素影响处理接受），我们可以：
1. 用**控制变量/工具变量**来辅助识别
2. 使用控制函数来处理 FRD 中的残留内生性
3. 结合 IPW 和 FRD 来双重稳健估计

## 补充分析

RD 实证中的标准补充：
- **安慰剂断点**：在无实际处理的假断点处运行 RD → 应该没有效应
- **改变带宽**：在多个带宽下估计以检验结论的敏感性
- **Donut RD**：排除恰好落在断点上的观测（如果怀疑操纵）
- **协变量连续性**：检验基线协变量在断点处是否连续

## 反面论点与数据空白

- **FRD 的工具强度测试**：过线对处理的概率跳跃有多大？——如果跳跃很小（如在 Boston Latin 案例中），工具极弱 → IV 估计不可靠。

## 相关页

- [[断点回归RD]]（MM）/ [[MLDA饮酒年龄RD案例]]（MM）/ [[波士顿拉丁学校RD案例]]（MM）
- [[控制函数方法]] / [[倾向得分方法]]
- [[Introductory-Econometrics-Wooldridge-8e]]
