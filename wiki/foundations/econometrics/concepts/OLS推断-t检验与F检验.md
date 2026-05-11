---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, inference, OLS, t-test, F-test, foundations, Wooldridge, 技术]
confidence: medium
decay_category: medium
status: foundation
---

# OLS 推断——t 检验与 F 检验

## 一句话定义

> **OLS 推断** = 在 MLR.1-6（加正态性）下，$\hat{\beta}_j$ 的抽样分布是 $t$ 分布，多个约束的联合检验使用 $F$ 分布——构成"汇报标准误 + 显著性星号"的基础。

## t 检验

### 单个参数约束

$$H_0: \beta_j = a_j \quad \text{vs} \quad H_1: \beta_j \neq a_j$$

$$t = \frac{\hat{\beta}_j - a_j}{\text{se}(\hat{\beta}_j)} \sim t_{n-k-1}$$

- $|t| > c_{\alpha/2}$ → 拒绝 $H_0$（$\alpha$ 显著性水平）
- 最常见的检验：$H_0: \beta_j = 0$（"变量 $x_j$ 是否有显著效应？"）

### p 值

$$p = 2 \cdot P(T > |t| \mid H_0 \text{ 为真})$$

- p 值小 → 数据在 $H_0$ 下"不寻常" → 拒绝 $H_0$ 的证据
- **p 值不是** $H_0$ 为真的概率
- **p 值不是** 效应大小——在大样本中微小的效应也可能 p < 0.001

### 置信区间

$$\hat{\beta}_j \pm c_{\alpha/2} \cdot \text{se}(\hat{\beta}_j)$$

- 95% CI：在重复抽样中，95% 的置信区间会覆盖真实的 $\beta_j$
- **不是** "$\beta_j$ 有 95% 的概率落在这个区间内"

## F 检验

### 多重约束的联合检验

$$H_0: \beta_{k-q+1} = 0, ..., \beta_k = 0$$

（最后 $q$ 个变量都可排除）

$$F = \frac{(\text{SSR}_r - \text{SSR}_{ur}) / q}{\text{SSR}_{ur} / (n - k - 1)} \sim F_{q, n-k-1}$$

- SSR_r：受约束模型（排除 $q$ 个变量）的残差平方和
- SSR_{ur}：无约束模型（全部变量）的残差平方和
- $F$ 大 → 排除这些变量使拟合显著变差 → 拒绝 $H_0$

### 整体显著性检验

$$H_0: \beta_1 = \beta_2 = ... = \beta_k = 0$$

$$F = \frac{R^2 / k}{(1 - R^2) / (n - k - 1)}$$

## 汇报惯例

在实证论文中：
> $\ln(\text{wage}) = 0.584 + 0.083\,\text{educ} + ...$
> $\quad\quad(0.097)\;\;(0.007)$

括号中为标准误。系数旁标注星号：*** (1%), ** (5%), * (10%)。

## 反面论点与数据空白

- **p 值的误用与 ASA 声明**：Wasserstein-Lazar (2016) "ASA Statement on p-Values"——p 值不衡量效应大小、不衡量假说概率、不应被二分化为"显著/不显著"。
- **多重检验问题**：当进行多次 t/F 检验时，即使所有零假设为真，5% 的检验也会"显著"——需要 Bonferroni 或 FDR 修正。
- **"p-hacking"**：选择性报告显著结果、变换模型设定直到 p < 0.05——预注册 (pre-registration) 是部分解决方案。
- **功效 (Power)**：检验不显著未必是效应为零——也可能是样本量太小。报告置信区间比报告 p 值更有信息量。

## 相关页

- [[OLS估计量的统计性质]] / [[OLS渐近理论]]
- [[统计推断基础-计量]]（MM）— RCT 情境下的推断基础
- [[Introductory-Econometrics-Wooldridge-8e]]
