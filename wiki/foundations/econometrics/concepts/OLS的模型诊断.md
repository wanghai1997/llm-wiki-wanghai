---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, OLS, diagnostics, specification, foundations, Wooldridge, 技术]
confidence: medium
decay_category: slow
status: foundation
---

# OLS 的模型诊断

## 一句话定义

> **模型诊断** = 在 OLS 估计完成后，用**残差分析**和**模型设定检验**评估关键假设（正态性、函数形式、同方差）是否合理——不通过诊断的模型不应被信任。

## 残差分析

### 残差 vs 拟合值图
- 如果残差无模式地随机散布 → 函数形式可能正确
- 如果残差呈 U 形或漏斗形 → 函数形式错误 或 异方差

### 正态性检验
- **QQ 图**：残差分位数 vs 理论正态分位数
- **Jarque-Bera 检验**：基于偏度和峰度的联合检验
- **注意事项**：大样本下正态性不如一致性重要——CLT 使推断对非正态性稳健

## RESET 检验——模型设定检验

**Regression Specification Error Test (Ramsey 1969)**：

1. 估计 $y = \mathbf{x}\hat{\beta} + \hat{u}$
2. 将 $\hat{y}^2, \hat{y}^3$（拟合值的二次和三次方）加入模型
3. 检验这些高阶项的联合显著性（F 检验）
4. 如果显著 → 函数形式错误（遗漏了非线性项或交互项）

**RESET 不是一般化的"遗漏变量检验"**——它只检验函数形式错误，不对遗漏变量（与已包含变量不高度相关的遗漏变量）敏感。

## 影响点与离群值诊断

- **杠杆值 (Leverage)**：$h_{ii} = \mathbf{x}_i(\mathbf{X}'\mathbf{X})^{-1}\mathbf{x}_i'$——观测值 $i$ 在解释变量空间的"极端程度"
- **学生化残差**：标准化后的残差——$> 2$ (或 $> 3$) 时标记为潜在离群值
- **DFBETAS / Cook's Distance**：度量删除一个观测值后系数估计的变化

## 诊断的优先级

| 优先级 | 诊断 | 为什么重要 |
|--------|------|-----------|
| 1 | **函数形式 (RESET)** | 错误=所有系数都有偏 |
| 2 | **异方差 (White 检验)** | 影响推断（SE 不可靠） |
| 3 | **正态性** | 大样本下最不重要 |
| 4 | **离群值** | 在特定情况下重要 |

## 反面论点与数据空白

- **RESET 通过了 ≠ 模型正确**：RESET 只检验特定的非线性模式——其他形式的错误设定（如遗漏交互项）可能被遗漏。
- **"诊断-修正"循环的问题**：根据诊断结果修改模型然后报告结果 → 实质上是"数据窥探"(data snooping) → 标准误和 p 值不再有效。预注册和样本分割是部分解决方案。

## 相关页

- [[OLS估计量的统计性质]] / [[OLS渐近理论]] / [[异方差]]
- [[Introductory-Econometrics-Wooldridge-8e]]
