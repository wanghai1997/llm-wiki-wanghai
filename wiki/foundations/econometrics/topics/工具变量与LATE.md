---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [topic, econometrics, instrumental-variables, batch2, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# 工具变量与 LATE

> Ch 3 导览页：连接 [[工具变量IV]] 的三个案例和 IV 理论框架。

## 为什么需要 IV

当处理非随机时（几乎所有观察性研究），即使控制丰富的协变量，[[选择偏差]] 仍可能残留。IV 通过寻找**自然的或制度产生的随机变异**——"就好像部分的随机实验"——来恢复因果效应。

## IV 的逻辑链

```
工具变量 Z
    │
    ├─ 第一阶段 φ：Z → D（处理）
    │    必须强（F > 10）
    │
    ├─ 简约式 ρ：Z → Y（结果）
    │    = ITT（intent-to-treat）
    │
    └─ IV 估计：λ = ρ/φ
         = LATE（compliers 的因果效应）
```

## 三个案例的 IV 结构

| | KIPP 彩票 | MDVE 家暴 | 子女质量 trade-off |
|---|---|---|---|
| **Z** | 彩票中签 | 警察随机指令 | 双胞胎 / 同性子女 |
| **D** | KIPP 入学 | 实际逮捕 | 子女数 |
| **Y** | 数学成绩 | 再犯率 | 子女教育成就 |
| **φ** | 0.74 | ~0.70 | 不一 |
| **ρ** | +0.36σ | — | — |
| **λ (LATE)** | +0.48σ | 显著 | 接近零 |

## IV 的关键假设和威胁

| 假设 | 含义 | 威胁 |
|------|------|------|
| **第一阶段** | Z 必须影响 D | 弱工具 → 偏差 + 大 SE |
| **独立性** | Z 如同随机分配 | Z 与混淆相关 |
| **排他性** | Z 仅通过 D 影响 Y | Z 有独立于 D 的效应路径 |

## IV 的边界

- **LATE 仅适用于 compliers**——不能推广到全人口
- **不同工具识别不同的 LATE**——KIPP 彩票的 LATE ≠ QOB 的 LATE
- **不能检验排他性**——只能通过制度知识和间接论证辩护
- **弱工具危险**——即使大样本，弱 IV 的 2SLS 也可能有严重偏差

## 相关页

- [[工具变量IV]] / [[两阶段最小二乘法2SLS]] / [[局部平均处理效应LATE]]
- [[KIPP特许学校彩票]] / [[MDVE家庭暴力实验]] / [[家庭规模-子女质量trade-off]]
- [[第一阶段与简约式]] / [[排他性约束]]
- [[Sewall-Wright]]
- [[计量经济学foundations总览]] / [[Mastering-Metrics]]
