---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, natural-experiment, epidemiology, history, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# John Snow 霍乱地图

## 一句话定义

> **John Snow 的霍乱地图** (1854) = 流行病学史上最著名的**自然实验**——通过绘制伦敦 Soho 区霍乱死亡病例的空间分布，Snow 证明了霍乱通过**污染的水**而非空气传播。

## 研究背景

1854 年 8-9 月，伦敦 Soho 区霍乱爆发，数日内数百人死亡。当时医学界的主流理论是**瘴气说**（miasma theory：霍乱通过"坏空气"传播）。Snow 持相反的水传播说。

## Snow 的因果推断策略

### 1. 空间断点分析

Snow 绘制了每例霍乱死亡的地理位置，发现：
- 病例**高度聚集**在 Broad Street 水泵周围
- 距离该水泵越远，死亡率越低
- 例外证实规则：附近一个修道院的修女几乎无人死亡——她们有自己的水井
- 例外证实规则：附近一个啤酒厂的工人无人死亡——他们只喝啤酒不喝水

### 2. "自然 IV"比较

Snow 注意到两家供水公司（Southwark & Vauxhall vs Lambeth）向相邻家庭供水——水来自泰晤士河的不同河段（污染 vs 较清洁）。这形成了**类似于随机分配的处理/对照比较**——住在同一街区的家庭，仅因供水公司不同而有不同的霍乱风险。

### 3. 干预实验

Snow 说服地方当局拆除 Broad Street 水泵的把手——霍乱随即消退。

## 方法论遗产

Mastering 'Metrics Ch 5 将 Snow 定位为 DiD 方法的思想先驱：

| Snow 的做法 | 现代计量对应 |
|-------------|------------|
| 比较水泵拆除前后的死亡率 | 处理前-后差分 |
| 比较"供水的不同来源" | 处理组 vs 控制组 |
| 地图上标注每例死亡 | 微观数据的空间分析 |
| 拆除水泵把手 = 关闭处理 | 干预实验 |

Mastering 'Metrics 的 Figure 5.7 用现代计量语言重述了 Snow 的 DD 配方。

## 反面论点与数据空白

- **Snow 的结论在当时遭到反对**：医学界的主流意见拒绝水传播说——甚至 Snow 自己的同事也持怀疑态度。直到 1866 年霍乱再次爆发后，他的理论才逐渐被接受。这一延迟说明：即使有清晰的因果证据，制度和社会接受也需要时间。
- **"自然实验"的幸运成分**：两家供水公司的供水区域交错是历史的偶然——Snow 乘势而为，而非事先设计。并非所有因果问题都有这种幸运的自然变异。
- **现代流行病学的局限**：Snow 的方法是"单因素"因果模型（水泵 → 霍乱）——现代公共卫生问题（如肥胖、心理健康）往往涉及复杂的多因素因果网络，单个"水泵"式的自然实验难以解答。

## 相关页

- [[双重差分DiD]] / [[John-Snow]]
- [[因果推断]] / [[理想实验基准]]
- [[Mastering-Metrics]]
