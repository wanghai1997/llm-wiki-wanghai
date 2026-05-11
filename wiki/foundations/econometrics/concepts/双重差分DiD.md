---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, differences-in-differences, causal-inference, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# 双重差分 DiD

## 一句话定义

> **双重差分** = 比较**处理组在处理前后的变化**减去**控制组在同期内的变化**——通过"减去趋势"来消除不随时间变化的混淆因素。

## 直觉

DiD 的逻辑：
1. 处理组在政策后的结果变化 = 处理效应 + 时间趋势
2. 控制组在同期内的结果变化 = 时间趋势（假设无政策影响）
3. 两者相减 = 处理效应

$$\text{DiD} = (\bar{Y}_{\text{treated}, \text{post}} - \bar{Y}_{\text{treated}, \text{pre}}) - (\bar{Y}_{\text{control}, \text{post}} - \bar{Y}_{\text{control}, \text{pre}})$$

## 关键假设：平行趋势

**平行趋势假设** = 在没有处理的情况下，处理组和控制组的结果变量会**以相同的趋势变化**。

> 这是 DiD 的核心识别假设——不可直接检验，但可以通过检查**处理前**的趋势是否平行来间接支持。

## 与 RCT 的关系

- RCT：随机化消除**水平差异**（处理组 vs 控制组的基线差异）
- DiD：差分消除**趋势差异**（不随时间变化的处理-对照差距）
- 两者结合：Randomized DiD → 既消除水平差异又消除趋势差异

## 在 Mastering 'Metrics 中的位置

Ch 5 使用两个旗舰案例：
- [[大萧条银行危机DD案例|大萧条银行危机]]：美联储第六区（干预区）vs 第八区（未干预区）的银行破产率
- [[MLDA双重差分案例|MLDA DiD]]：利用不同州在不同年份改变法定饮酒年龄的"交错"处理

## 回归 DiD 模型

$$Y_{it} = \alpha + \beta \cdot \text{Treat}_i + \gamma \cdot \text{Post}_t + \delta \cdot (\text{Treat}_i \times \text{Post}_t) + \varepsilon_{it}$$

- $\beta$：处理组与对照组的基线差异（水平）
- $\gamma$：两组共同的时间趋势
- $\delta$ = **DiD 估计量** = 因果效应

加入控制变量和固定效应后的推广：
$$Y_{it} = \alpha_i + \lambda_t + \delta \cdot D_{it} + \varepsilon_{it}$$

其中 $\alpha_i$ 是个体/地区固定效应，$\lambda_t$ 是时间固定效应。

## 反面论点与数据空白

- **平行趋势不可检验**：只能用处理前的趋势来间接论证——但如果处理前趋势平行≠处理后趋势平行（如处理引发行为改变），结论可能有偏。
- **时变混淆**：如果处理同时有其他事件发生（如银行危机时也发生了干旱/罢工），DiD 会错误归因。
- **交错处理的翻车问题**：Goodman-Bacon (2021) 证明在交错处理设计中（不同个体在不同时间接受处理），传统双向固定效应 DiD 可能产生严重偏误——它是"已经在处理的组 vs 还没处理的组"的加权平均，后期处理组作为控制组时可能产生负权重。
- **新 DiD 方法**：Sun-Abraham (2021)、Callaway-Sant'Anna (2021)、Borusyak-Jaravel-Spiess (2024) 等提供了更稳健的交错处理估计量——本 Wiki 标注但留待进阶文献。

## 相关页

- [[平行趋势假设]] / [[大萧条银行危机DD案例]] / [[MLDA双重差分案例]]
- [[John-Snow霍乱地图]] / [[John-Snow]]
- [[Mastering-Metrics]]
