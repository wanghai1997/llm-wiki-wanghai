---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, randomized-trial, case-study, health-insurance, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# RAND 健康保险实验

## 一句话定义

> **RAND HIE** (1974-1982) = 历史上规模最大、最具影响力的社会 RCT 之一——在六个美国城市随机将 ~2,000 个家庭分配到不同医保计划，研究"医保覆盖是否改善健康"。

## 研究设计

- **处理**：家庭被随机分配到不同成本的医保计划（免费医疗、25% 共付率、50% 共付率、95% 共付率、HMO 式预付制）
- **结果**：医疗支出、就医次数、健康状况（血压、胆固醇、视力等生理指标 + 自我报告健康）
- **人群**：六个美国城市（Dayton OH、Seattle WA、Fitchburg MA、Charleston SC、Georgetown County SC、Franklin County MA）

## 核心发现

| 发现 | 方向 | 显著性 |
|------|------|--------|
| 更高覆盖 → 更多就医 | ↑ | 显著 |
| 更高覆盖 → 更多医疗支出 | ↑ | 显著 |
| 更高覆盖 → **身体健康指标改善** | → | **总体不显著** |
| 免费医疗 → 最贫困群体血压改善 | ↑ | 局部显著 |

**核心教训**：医保覆盖增加使用率是确定性的，但额外医疗是否转化为更好的健康结果——平均而言不显著（对最贫困者有局部效果）。

## 在 Mastering 'Metrics 中的方法论意义

RAND HIE 是 Ch 1 的第一个旗舰案例，用于展示：
1. **成功的随机分配**：Table 1.3 显示各组基线高度平衡
2. **多组处理**：非简单 treated/control 二值——需要使用均值比较和 IV（Ch 3）
3. **意图处理分析（ITT）** vs 依从者效应：随机分配到不同计划 ≠ 实际使用量相等
4. **亚组分析**：最贫困者的健康改善提示因果效应不恒常

## 反面论点与数据空白

- **时代局限性**：RAND HIE 数据是 1970 年代末的——当时医疗技术、费用结构和疾病谱与今天差异巨大。
- **样本代表性问题**：排除 65 岁以上（Medicare 覆盖）和最高收入群体——结果不能推广到这些人群。
- **Hawthorne 效应**：参与实验本身可能改变行为（受试者知道自己被研究）。
- **统计效力问题**：某些亚组比较样本太小，"无显著差异"可能只是样本不够大。

## 相关页

- [[随机对照试验RCT]] / [[平衡性检验]] / [[俄勒冈健康保险实验]]
- [[工具变量IV]] — RAND HIE 的 IV 分析扩展
- [[Mastering-Metrics]]
