---
created: 2026-05-04
updated: 2026-05-04
sources: ["Introductory Econometrics A Modern Approach, 8e (Jeffrey M. Wooldridge) .pdf"]
tags: [concept, econometrics, sample-selection, Heckman, inverse-Mills-ratio, foundations, Wooldridge]
confidence: medium
decay_category: slow
status: foundation
---

# 样本选择修正——Heckman 两步法

## 一句话定义

> **Heckman 两步法** = 当因变量仅对**自选择**的样本可观测时（如工资仅对有工作的人可见），通过**逆 Mills 比率**修正选择偏差——两步：Probit（选择方程）→ OLS（结果方程 + 修正项）。

## 样本选择问题

工资回归 $wage = x\boldsymbol{\beta} + u$ 只能对有工作的人估计——但**是否工作**本身是内生选择：

$$work^* = z\boldsymbol{\gamma} + v$$

只当 $work^* > 0$ 时工资可观测。如果 $u$ 和 $v$ 相关（决定工作的人与不工作的人在工资潜力上系统性不同）→ OLS 在选定样本上**不一致**。

## Heckman 两步法（Heckit）

### 步骤 1：选择方程（Probit）

$$P(work=1|z) = \Phi(z\boldsymbol{\gamma})$$

获得 $\hat{\boldsymbol{\gamma}}$，计算**逆 Mills 比率**：

$$\hat{\lambda}_i = \frac{\phi(z_i\hat{\boldsymbol{\gamma}})}{\Phi(z_i\hat{\boldsymbol{\gamma}})}$$

$\hat{\lambda}_i$ 捕捉了"这个人被选入样本的统计倾向"。

### 步骤 2：结果方程 + 修正项

$$wage_i = x_i\boldsymbol{\beta} + \rho \hat{\lambda}_i + \varepsilon_i$$

- 如果 $\hat{\rho}$ 显著 ≠ 0 → 存在样本选择偏差 → 需要修正
- 加入 $\hat{\lambda}$ 后 $x_i\boldsymbol{\beta}$ 的解释：**在控制了选择偏差后**，$x$ 对工资的因果效应

## 识别条件——排他性约束

选择方程 $z$ 中至少有一个变量**不出现**在结果方程 $x$ 中——即有一个变量影响"是否工作"但不直接影响"工资多少"。

常用排他性变量：
- 家庭结构（是否有小孩、配偶收入）
- 非劳动收入（遗产、投资收益）
- 政策规则（领取福利的资格条件）

> 没有排他性约束 → Heckman 模型仅通过非线性函数形式识别——在实践中非常脆弱。

## Heckman 两步法的替代方法

- **MLE**：同时估计选择和结果方程——更有效但更依赖分布假设
- **控制函数方法**（Ch 19）：更一般的处理选择偏差框架
- **IPW**（Ch 19）：通过重新加权未受选择的观测来恢复代表性

## 反面论点与数据空白

- **排他性约束在实际中很难找到**：许多影响选择的变量也直接影响结果——弱的排他性约束导致 Heckman 估计不稳定（多重共线性 + 识别仅来自函数形式）。
- **Heckman 两步法对正态性假设敏感**：如果误差不是联合正态的 → MLE/两步法不一致。部分解决方案：半参数样本选择模型。

## 相关页

- [[截取与截断回归]] / [[Tobit模型-角点解]] / [[缺失数据与非随机样本]]
- [[Introductory-Econometrics-Wooldridge-8e]]
