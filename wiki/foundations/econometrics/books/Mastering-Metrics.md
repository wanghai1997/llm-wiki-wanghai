---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [book, econometrics, causal-inference, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Mastering 'Metrics: The Path from Cause to Effect

## 基本信息

- **作者**：[[Joshua-Angrist|Joshua D. Angrist]]（MIT）、[[Jorn-Steffen-Pischke|Jörn-Steffen Pischke]]（LSE）
- **出版**：Princeton University Press, 2015
- **篇幅**：~270 页（6 章 + 引言 + 附录）
- **难度**：本科高年级 / 硕士一年级入门

## 核心理念

本书以**选择偏差（selection bias）**为贯穿全书的敌人，以**理想随机实验**为因果推断的金标准，围绕五种核心识别方法——作者称之为 **The Furious Five**——展开：

1. **Randomized Trials**（随机试验，Ch 1）
2. **Regression**（回归，Ch 2）
3. **Instrumental Variables**（工具变量，Ch 3）
4. **Regression Discontinuity Designs**（断点回归，Ch 4）
5. **Differences-in-Differences**（双重差分，Ch 5）

第六章将这些方法综合应用于"教育回报率"这一经典问题。

## 与传统教材的区别

| 维度 | 传统教材 (如 Wooldridge) | Mastering 'Metrics |
|------|--------------------------|---------------------|
| 组织逻辑 | 回归→假设检验→放宽假设→专题 | 因果问题→识别方法→实证案例 |
| 起点 | OLS 估计量的统计性质 | [[潜在结果框架]] + [[选择偏差]] |
| 技术深度 | 矩阵代数、渐近理论 | 直觉 + 图示 + 核心公式 |
| 案例驱动 | 习题数据 | 真实发表的顶尖实证研究 |
| 哲学 | "如何估计参数" | "如何识别因果" |

## 各章概述

| 章 | 标题 | 核心方法 | 旗舰案例 |
|----|------|---------|---------|
| 1 | Randomized Trials | 随机分配 / 平衡性检验 / 推断 | RAND HIE, Oregon OHP |
| 2 | Regression | 回归=自动匹配 / OVB 公式 | Dale-Krueger 私立大学溢价 |
| 3 | Instrumental Variables | IV / 2SLS / LATE | KIPP 特许学校, 家庭暴力实验 |
| 4 | Regression Discontinuity | 精确 RD / 模糊 RD | MLDA 饮酒年龄, 波士顿拉丁学校 |
| 5 | Differences-in-Differences | DD / 平行趋势 | 大萧条银行危机, MLDA DD |
| 6 | The Wages of Schooling | 五法综合应用 | 教育回报率（双胞胎 IV, QOB IV） |

## 在 Wiki 中的位置

本书是 `foundations/econometrics/` 的第一本教材——定位为**因果思维层**。后续 [[Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge)|Wooldridge (2020)]] 将作为**技术工具层**补充摄入。

## 相关页

- [[计量经济学foundations总览]]
- [[Joshua-Angrist]] / [[Jorn-Steffen-Pischke]]
- [[潜在结果框架]] / [[选择偏差]]
- [[随机对照试验RCT]] / [[工具变量IV]] / [[断点回归RD]] / [[双重差分DiD]]
- [[Macroeconomics-Mankiw-9e]] / [[Microeconomics-Nechyba-2e]] — 微观/宏观双柱
