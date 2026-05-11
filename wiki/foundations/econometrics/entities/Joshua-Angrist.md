---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [person, economist, econometrics, causal-inference, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Joshua D. Angrist

## 基本信息

- **生卒**：1960–，美国劳动经济学家
- **所属**：MIT 经济系 Ford Professor
- **荣誉**：2021 年诺贝尔经济学奖（与 David Card、Guido Imbens 共享）——"对因果推断方法论的贡献"
- **代表作**：
  - *Mostly Harmless Econometrics*（2009，与 [[Jorn-Steffen-Pischke]] 合著）——研究生级因果推断教材
  - *Mastering 'Metrics*（2015，与 Pischke 合著）——本科生级因果推断入门

## 与本 Wiki 的接口

Angrist 是 `foundations/econometrics/` 的第一支柱人物。[[Mastering-Metrics]] 教材将其因果哲学具象化为 **The Furious Five**（五种核心方法），每一章以他本人参与或指导的顶尖实证研究为案例：

| 方法 | Angrist 相关研究 |
|------|-----------------|
| IV / LATE | Angrist-Imbens-Rubin (1996) LATE 定理 |
| IV / 教育回报 | Angrist-Krueger (1991) 季度出生 IV |
| IV / 特许学校 | Angrist et al. (2012) KIPP 彩票研究 |
| 双胞胎方法 | Angrist-Krueger (1994) 双胞胎教育回报 |
| 义务教育法 | Acemoglu-Angrist (2001) 义务就学法 IV |
| RD / 考试学校 | Abdulkadiroglu-Angrist-Pathak (2014) 波士顿/纽约考试学校 |

## 学术思想要点

- **LATE 框架**：Angrist-Imbens-Rubin (1996) 将 IV 估计量重新解释为**局部平均处理效应**（complier average causal effect），使 IV 的因果解释从"全人口平均效应"收缩为"依从者子群体效应"——精确但范围收窄。
- **因果设计的实验模板思维**：Angrist 反复强调"你理想中的实验是什么？"——即使实际研究非随机化，理想实验仍然是判断识别策略好坏的基准。
- **"计量经济学是原始数据科学"**：*Mastering 'Metrics* 引言中的定位——早于"数据科学"成为流行词。

## 关键引用

> "The notion of an ideal experiment disciplines our approach to econometric research."

## 利益相关与批评

- **LATE 的外部有效性**：LATE 仅对 compliers 有效，无法直接推广到 always-takers 和 never-takers。Heckman-Urzua-Vytlacil (2006) 等强调结构方法可获得更广泛的政策参数。
- **简约式 vs 结构式**：Angrist 是简约式（reduced-form）阵营的代表人物，与结构计量经济学（Heckman, Wolpin, Keane 等）存在方法论张力——本 Wiki 在 Wooldridge 摄入时会展开。

## 相关页

- [[Mastering-Metrics]]
- [[Jorn-Steffen-Pischke]]
- [[工具变量IV]] / [[局部平均处理效应LATE]] / [[潜在结果框架]]
- [[教育回报率-因果估计]]
