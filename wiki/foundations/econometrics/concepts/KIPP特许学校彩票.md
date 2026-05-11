---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, instrumental-variables, case-study, education, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# KIPP 特许学校彩票

## 一句话定义

> **KIPP Lynn 彩票研究** = [[Joshua-Angrist|Angrist]] et al. (2012, *JPAM*) 利用 KIPP 特许学校的**入学抽签**作为工具变量——识别在贫困/少数族裔社区中"No Excuses" 特许学校模式对学生成绩的因果效应。

## 研究背景

KIPP (Knowledge Is Power Program) 是美国最大的特许学校网络之一，以"No Excuses"模式著称：
- 长学时（每天 7:30-17:00，部分周末上课）
- 严格的纪律和行为规范
- 选择性教师招聘（非工会合同）
- 95% 黑人/拉丁裔学生，80%+ 享受联邦免费午餐（贫困线以下）

批评者认为 KIPP 的"成功"来自**选择偏差**——KIPP 招收的是更积极参与的家长和更有潜力的学生。

## 研究设计

- **工具变量 $Z_i$**：KIPP 入学彩票是否中签（赢/输）
- **处理 $D_i$**：是否实际入学 KIPP
- **结果**：MCAS 标准化数学和英语考试成绩
- **Compliance**：~74% 中签者入学，~3.5% 未中签者也设法入学

## 核心发现

| 估计量 | 数学成绩效应 | 英语成绩效应 |
|--------|------------|------------|
| ITT（赢 vs 输） | +0.36σ | +0.12σ（不显著） |
| IV/LATE | +0.48σ | +0.16σ（不显著） |
| OLS（入学 vs 未入学） | +0.47σ | - |

**结论**：KIPP 显著提高数学成绩（效果量 ~0.5σ，相当于将一个平均学生从中位数提升到约 70 百分位），但英语成绩提升不显著。OLS 和 IV 估计接近——说明选择偏差在此案例中不大（可能是因为彩票 + 高遵从率 + KIPP 的独特吸引力的组合）。

## 方法论贡献

- **IV 的教科书级应用**：三条件（第一阶段强 [0.74] + 独立性 [彩票随机] + 排他性 [彩票唯一通过入学影响成绩]）全部清晰可辩护
- **LATE 的直观解读**：compliers 的因果效应——"被彩票推动才去 KIPP 的学生"
- **OLS 和 IV 一致**：两个估计量接近 → 增强了结论的可信度（即使不用 IV 方法，结果也类似）
- **平衡性检验的展示**：Table 3.1 Panel A 展示了完美的基线平衡——论证了彩票的随机性

## 反面论点与数据空白

- **仅一个学区的一所学校**：KIPP Lynn 的结果不能推广到所有 KIPP 学校——更不用说所有特许学校。
- **短期效应 vs 长期效应**：仅追踪到第一次 MCAS 考试后的变化——更长期效应（高中毕业率、大学入学）在后续文献中有所追踪但结论不一。
- **"No Excuses"模式的伦理辩论**：KIPP 的高度纪律化是否过度压抑？这种教育模式的长期心理效应缺乏随机化证据。
- **教师流失率**：KIPP 教师的高流失率（每年约 30%）可能影响学校质量的可持续性——随机实验不能回答此问题。

## 相关页

- [[工具变量IV]] / [[局部平均处理效应LATE]] / [[第一阶段与简约式]]
- [[Joshua-Angrist]]
- [[Mastering-Metrics]]
