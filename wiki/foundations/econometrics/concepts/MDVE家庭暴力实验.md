---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, instrumental-variables, case-study, domestic-violence, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# MDVE 家庭暴力实验

## 一句话定义

> **MDVE (Minneapolis Domestic Violence Experiment)** = Sherman & Berk (1984) 的里程碑式现场实验——警察随机分配三种对家暴的反应，但实际执法时常偏离指令，**非依从性**使其成为 IV 方法的经典案例。

## 研究设计

- **随机分配**：警察到达家暴现场后，通过随机卡片获得三种指令之一：
  1. **逮捕**（arrest）
  2. **劝离**（separate/advise）
  3. **调解**（mediate）
- **实际执法**：警察有时不按指令行事（如原本指令"劝离"但警察认为情节严重 → 逮捕）
- **结果**：6 个月内的再犯率（重复家暴报警）

## 非依从问题

随机指令 ≠ 实际执行：

| 指令 | 实际逮捕率 |
|------|----------|
| 逮捕指令 | ~80%（有约 20% 未执行） |
| 劝离指令 | ~10%（警察自主决定逮捕） |
| 调解指令 | ~5%（警察自主决定逮捕） |

→ ITT 比较（逮捕指令 vs 其他指令）会低估逮捕的因果效应 → 需要 IV。

## 核心发现

- **ITT 估计**：逮捕指令减少再犯（但与"不是逮捕"的差距不大）
- **IV 估计**：实际逮捕显著减少再犯
- IV 调整后效应约为 ITT 效应的 1.25×（因为 compliance 较高）

## 方法论贡献

- **"鼓励设计" (Encouragement Design)**：随机化的是"处理建议"而非"处理"——IV 恢复处理本身对依从者的效应
- **现场实验中的 IV 必要性**：即使有随机化，不依从也需要 IV 调整——否则低估处理效应
- **与 Oregon OHP 的平行**：Ch 1 的 Oregon OHP 有相同结构——随机彩票（鼓励）→ 部分参保 → IV 恢复参保效应

## 反面论点与数据空白

- **复现问题**：Sherman & Berk 的后续多城复现（NIJ 资助的六城研究）未能一致重复 Minneapolis 的发现——在某些城市逮捕反而**增加**再犯（特别是失业施暴者）。因果效应因地/人而异——LATE 在此处的"局部性"至关重要。
- **伦理问题**：随机分配警察反应涉及伦理——被捕对家暴受害者的影响可能超出"再犯率"这个单一指标。
- **数据质量**：再犯率通过官方报警记录测算——许多家暴未报警，真实再犯率可能被低估。

## 相关页

- [[工具变量IV]] / [[局部平均处理效应LATE]] / [[第一阶段与简约式]]
- [[随机对照试验RCT]] / [[俄勒冈健康保险实验]] — 相同的不依从 IV 结构
- [[Mastering-Metrics]]
