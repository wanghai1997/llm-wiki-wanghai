---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, regression, methodology, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Bad Controls 问题

## 一句话定义

> **Bad Controls** = 在回归模型中加入**被处理变量本身影响**的变量作为控制——反而**制造**选择偏差，而不是消除它。

## 核心原则：时机决定一切

- **好控制变量**：在处理**之前**测度的变量——不会被处理改变
- **坏控制变量**：在处理**之后**测度的变量——可能部分或完全是处理的**结果**

> "Variables measured before the treatment was determined are generally good controls. Variables measured later may have been determined in part by the treatment, in which case they aren't controls at all, they are outcomes."

## 教育回报案例中的坏控制

Mastering 'Metrics Ch 6.1 用了一个清晰的反例：

**"教师的收入高于护士助理，但教师也是多受教育的结果"**

如果我们在教育回报的回归中**控制职业**：
- 职业是教育的结果（部分或完全）
- 控制职业 → 剔除了"教育 → 更好职业 → 更高收入"这条因果通路
- → 教育系数**低估**真实回报（可能只测量了同一职业内的教育溢价）

## Table 6.1：坏控制的数学机制

$$\text{Short: } Y_i = \alpha_s + \rho_s S_i + \eta_{si}$$
$$\text{Long: } Y_i = \alpha_l + \rho_l S_i + \gamma A_i + \eta_{li}$$

如果 $A_i$（能力）是**好的忽略变量**（与教育和收入都相关）→ 短回归 $\rho_s$ 有 OVB。

但如果我们在短回归中加入 $O_i$（职业）——而 $O_i$ 是 $S_i$ 的**结果**：
- $O_i$ 吸收了教育对收入的**部分因果效应**
- 条件对比变成了"同一职业内"的教育效应——偏失了教育对职业流动性的贡献
- 如果教育仅通过"从护士助理到教授"来增加收入 → 控制职业后教育的系数趋近于零——**即使教育的因果效应很大**

→ **这比 OVB 更危险，因为它使因果效应消失**。

## 坏控制的典型例子

| 坏控制变量 | 处理 | 结果 | 为什么坏 |
|-----------|------|------|---------|
| 职业 | 教育 | 收入 | 教育 → 职业 → 收入 |
| 现任职位 | MBA 学位 | 收入 | MBA → 职位提升 |
| 当前体重 | 运动干预 | 心血管健康 | 运动 → 体重 → 健康 (这是中介，应该分离而非控制) |
| 中间考试成绩 | 补习 | 最终成绩 | 补习 → 中期考试 → 最终成绩 |

## 坏控制 vs 遗漏变量偏差

| | OVB（遗漏变量） | Bad Control（坏控制） |
|---|---|---|
| **不控制** | 有偏 | 无偏 |
| **控制** | 消除偏差 | **制造偏差** |
| **机制** | 遗漏了 ↑ 教育与 ↑ 收入的共因 | 阻断了教育 → 收入的因果通路 |

## 反面论点与数据空白

- **"时机"的模糊性**：某些变量既有前定性成分也有处理后成分——如大学专业选择既受大学前的能力影响又受大学教育本身影响。
- **中介分析 vs 坏控制**：在某些研究设计中，"控制中介变量"正是研究目标——如直接效应和间接效应的分解——需要结构方程或 DAG 方法辅助。
- **机器学习的坏控制风险**：变量选择算法（LASSO、随机森林）可能自动选择"预测力高"的变量——其中很多是坏控制——需要研究者的事前知识来约束变量集。

## 相关页

- [[教育回报率-因果估计]] / [[遗漏变量偏差公式]] / [[选择偏差]]
- [[Mincer方程]]
- [[Mastering-Metrics]]
