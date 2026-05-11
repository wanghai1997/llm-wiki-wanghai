---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [book, econometrics, regression, time-series, panel-data, foundations]
confidence: medium
decay_category: medium
status: foundation
---

# Introductory Econometrics: A Modern Approach, 8e

## 基本信息

- **作者**：[[Jeffrey-Wooldridge|Jeffrey M. Wooldridge]] (Michigan State University)
- **出版**：Cengage Learning, 第 8 版 (2025)
- **篇幅**：~800 页（20 章 + 数学附录）
- **难度**：本科计量经济学标准教材
- **新内容（第 8 版）**：Ch 19 进阶因果推断方法（IPW、倾向得分、控制函数）

## 组织架构

全书按**数据类型**组织——这是 Wooldridge 区别于传统计量教材（按统计假设组织）的核心创新：

```
Part 1: 横截面回归分析 (Ch 1-9)
  Ch 1   计量经济学本质与数据类型
  Ch 2   简单回归模型
  Ch 3   多元回归：估计
  Ch 4   多元回归：推断
  Ch 5   OLS 渐近理论
  Ch 6   多元回归：进阶问题
  Ch 7   含定性信息的回归
  Ch 8   异方差
  Ch 9   模型设定与数据问题

Part 2: 时间序列回归分析 (Ch 10-12)
  Ch 10  基础时间序列回归
  Ch 11  OLS 在时间序列中的进阶
  Ch 12  序列相关与异方差

Part 3: 进阶专题 (Ch 13-20)
  Ch 13  混合横截面与简单面板
  Ch 14  进阶面板方法
  Ch 15  IV 估计与 2SLS
  Ch 16  联立方程模型
  Ch 17  受限因变量模型
  Ch 18  进阶时间序列专题
  Ch 19  进阶因果推断方法
  Ch 20  实证项目实践
```

## 与 Mastering 'Metrics 的互补

| 方法/主题 | MM 贡献 | Wooldridge 增量 |
|-----------|---------|----------------|
| 回归 | 匹配解释、OVB 公式 | Gauss-Markov、推断、渐近、诊断 |
| IV | 直觉、LATE、三案例 | 弱 IV、过度识别、内生性检验、面板 IV |
| RD | 直觉、两案例 | Sharp/Fuzzy 技术、放松假设 |
| DiD | 直觉、两案例 | 面板 FE/FD 形式化、事件研究 |
| **时间序列** | — | 全新：平稳性、序列相关、协整、预测 |
| **面板数据** | — | 全新：FE、RE、CRE、Hausman |
| **受限因变量** | — | 全新：Logit/Probit/Tobit/Poisson/Heckman |
| **联立方程** | — | 全新：结构识别、2SLS 估计 |
| **实证实践** | — | 全新：项目设计、写作规范 |

## 在 Wiki 中的位置

Wooldridge 是 `foundations/econometrics/` 的**第二本教材**——定位为**技术工具层**。所有概念页标注 `[技术]`，与 [[Mastering-Metrics|MM 因果直觉页]] 做双向链接。

## 相关页

- [[Jeffrey-Wooldridge]]
- [[Mastering-Metrics]]
- [[计量经济学foundations总览]]
- [[OLS估计量的统计性质]] / [[Gauss-Markov定理]] / [[异方差]]
