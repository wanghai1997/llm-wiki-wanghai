---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, labor-economics, human-capital, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Mincer 方程

## 一句话定义

> **Mincer 方程** = 劳动经济学中估计教育回报的基准工资方程——将 $\ln$（收入）回归于教育年限 + 潜在经验 + 潜在经验的平方——由 Jacob Mincer (1974) 系统化。

## 标准形式

$$\ln Y_i = \alpha + \rho S_i + \beta_1 X_i + \beta_2 X_i^2 + \varepsilon_i$$

其中：
- $Y_i$：年收入（或小时工资）
- $S_i$：受教育年限
- $X_i$：**潜在经验** = $\text{age} - S_i - 6$（即从结束教育到当前的年数）
- $\rho$：**教育回报率**（每增加一年教育 → $\ln$ 收入增加 $\rho \times 100\%$）

## Mincer 的原始估计

Mincer (1974) 使用 1960 年美国人口普查数据（约 31,000 名白人男性）：
- 无经验控制：$\hat{\rho} \approx 7\%$
- **有经验控制**：$\hat{\rho} \approx 11\%$

加入经验控制后教育系数**上升**——原因是教育和经验负相关（多受教育的人经验少），而 OVB 公式表明遗漏经验的偏差向下。

## Mincer 方程的因果困境

Mincer 方程是**最著名的劳动经济学回归模型**——但 $\rho$ 的因果解释面临三个挑战：

1. **能力偏差**：教育年限与能力正相关 → $\rho$ 可能高估因果效应
2. **测量误差**：自报教育年限有误差 → $\rho$ 向零衰减（低估）
3. **异质回报**：不同人的教育回报不同 → OLS 给出的 $\rho$ 是某种加权平均——但不一定是政策相关的参数

三个偏误方向不同——不能简单说"Mincer 高估了教育回报"。

## Mincer 方程在 Furious Five 检验下的表现

Mastering 'Metrics Ch 6 用四种方法检验 Mincer 方程的教育系数：

| 方法 | 估计的 $\rho$ | 与 Mincer 的偏差 |
|------|-------------|----------------|
| Mincer OLS | ~0.11 | 基准 |
| 双胞胎差分 IV | ~0.108 | 几乎相同（能力偏差不大） |
| QOB IV (2SLS) | ~0.07-0.10 | 略低但差异不显著 |
| 成人法律 IV | 类似范围 | 一致 |

> **总的结论**：Mincer 的 OLS 估计 ~11% 可能**并没有严重偏误**——多种因果方法给出的估计在相似范围内。这是一个令人安心的发现。

## 反面论点与数据空白

- **潜在经验的代理粗糙**：$X = \text{age} - S - 6$ 假设所有人结束教育后连续工作——对女性、少数民族和自我雇佣者不成立。
- **"加入经验控制后教育系数上升"未必是因果改进**：经验本身可能是内生的（与教育选择相关）。
- **线性教育回报假设**：Mincer 模型假设每年教育有相同的回报——但"羊皮纸效应"（文凭断点）表明某些年份（毕业年）的回报可能不成比例地大。
- **"能力偏差不大"的发现可能局限于美国白人男性**：在其他人群（移民、少数族裔、发展中国家）中，能力偏差可能更大——因为教育获取的公平性更弱。

## 相关页

- [[教育回报率-因果估计]] / [[能力偏差]] / [[测量误差偏差]]
- [[Bad-Controls问题]]
- [[Texas羊皮纸效应]] — 检验 Mincer 的线性回报假设
- [[Mastering-Metrics]]
