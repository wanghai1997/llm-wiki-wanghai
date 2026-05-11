---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, regression, statistical-phenomenon, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Galton 回归均值

## 一句话定义

> **回归均值** = 在双变量正态分布中，给定 $X$ 时 $Y$ 的条件期望倾向于**向均值"回归"**——这是一个**统计现象**，不是因果关系。

## 来源

[[Francis-Galton|Francis Galton]] 在 1886 年论文"Regression towards Mediocrity in Hereditary Stature"中发现：
- 高个子父亲的儿子平均身高高于总体均值，但**低于**父亲身高（向均值回归）
- 矮个子父亲的儿子平均身高低于总体均值，但**高于**父亲身高（同样向均值回归）

## 为什么发生

假设父代身高 $X$ 和子代身高 $Y$ 服从双变量正态分布，且边际分布稳定：
- 如果 $X$ 极高，$X$ 位于分布的极端尾部
- 由于 $X$ 和 $Y$ 并非完全相关（$\rho < 1$），$E[Y|X=\text{极高}] < X$
- 这是 **"选择极端值 → 重测 → 发现不那么极端"** 的统计必然性

## 与计量经济学的区分

Mastering 'Metrics Ch 2 强调这是最关键的概念区分之一：

| | Galton 的回归 | 计量经济学的回归 |
|------|-----------|----------------|
| 性质 | 统计描述 | （在 CIA 下）因果推断 |
| 问什么 | "给定 X，Y 的条件期望是多少？" | "改变 X，Y 会变化多少？" |
| 反事实 | 无 | 有——改变 P_i 的假设性对比 |

"Regression"这个词本身来自 Galton——它最初描述的是一个非因果的统计规律。现代计量经济学赋予回归**因果含义**——但这需要额外的识别假设。

## 实际中的回归均值陷阱

- **"获奖者诅咒"**：特别好的首次表现→第二次回归均值→误判为"退步"
- **"向均值回归 = 有效"的自欺**：给学生最低分的提供补习→成绩提升→误以为是补习有效（可能是回归均值）
- **RCT 仍可能受回归均值影响**：如果处理组在基线被"极端地"选择（随机化失败）——基线不显著≠没有回归均值问题

## 相关页

- [[回归的多重含义]] / [[Francis-Galton]]
- [[因果推断]] / [[选择偏差]]
- [[Mastering-Metrics]]
