---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw) .pdf, Ch 2"]
tags: [concept, macroeconomics, national-accounts, price-index, foundations]
confidence: medium
decay_category: medium
status: foundation
---

# GDP 平减指数

> **一句话定义**:**GDP Deflator**,衡量经济整体价格水平的指数,等于 名义 GDP / 实际 GDP × 100;是 [[帕氏指数]](当期权重)的典型代表。

## 在教材中的位置

- 来源:[[Macroeconomics-Mankiw-9e]] Ch 2.1.4 + Ch 2.2(与 [[CPI]] 比较)
- 制度:[[美国经济分析局BEA]] 与 GDP 同步发布

## 公式

$$
\text{GDP 平减指数}_t = \frac{\text{名义 GDP}_t}{\text{实际 GDP}_t} \times 100
$$

或等价地:

$$
\text{GDP 平减指数}_t = \frac{\sum_i p_{i,t} \cdot q_{i,t}}{\sum_i p_{i,b} \cdot q_{i,t}} \times 100
$$

注意分子分母**都用当期数量** $q_{i,t}$,只有价格不同——因此 GDP 平减指数是 [[拉氏指数与帕氏指数|帕氏指数]]。

## 使用 2014 年基期的数值例

延续 [[名义GDP与实际GDP]] 的苹果 / 香蕉例子:
- 名义 GDP 2015 = 600,实际 GDP 2015(2014 基期) = 350
- GDP 平减指数 2015 = 600 / 350 × 100 = 171.4(基期 2014 = 100)
- 通胀率 = (171.4 − 100) / 100 = 71.4%

## 与 CPI 的差异(三大差异)

详见 [[GDP平减指数与CPI比较]]。三个核心差异:

1. **篮子构成**:GDP 平减指数包含**所有国内生产**的最终品;CPI 仅包含**典型城市消费者**购买的商品;
2. **权重类型**:GDP 平减指数 = 当期权重(帕氏);CPI = 基期权重(拉氏);
3. **进口品处理**:GDP 平减指数**不**含进口(只算国内生产);CPI **含**进口品(消费者实际购买)。

## PCE 价格指数(联储偏好)

虽然 Mankiw Ch 2 主要用 GDP 平减指数与 CPI,但**美联储**自 2000 起将 *Personal Consumption Expenditures Price Index*(PCE)作为通胀目标的主要指标。PCE:
- 篮子比 CPI 更广(包含医保第三方支付);
- 权重每月更新(费雪指数,介于拉氏与帕氏之间);
- 通胀读数通常比 CPI 低 0.3-0.5pp。

## 反面论点与数据空白

- **平减指数对结构性变化的滞后**:由于使用当期权重,但与基期价格挂钩,GDP 平减指数在产业结构急剧变化时(如 1990s 信息技术革命)可能扭曲;
- **不含进口的双面性**:不含进口意味着 GDP 平减指数不反映"输入性通胀"——2022 全球通胀回潮时,美国 GDP 平减指数(主要受国内服务通胀驱动)与 CPI(含能源与商品进口)读数显著背离;
- **链式加权下 GDP 平减指数与隐含价格指数(IPD)的概念混淆**:1996 后 BEA 实际 GDP 链式加权,GDP 平减指数实际计算是费雪型而非简单帕氏。Mankiw 9e 在脚注简单交代,未充分明示。
- **regional-bias**:中国 NBS 公布"GDP 缩减指数"概念上等价,但实际编制使用三大产业的不同基期物价指数,与美国 BEA 不严格可比。

## 相关页

- 父概念:[[GDP]] / [[名义GDP与实际GDP]]
- 关联:[[GDP平减指数与CPI比较]] / [[CPI]] / [[拉氏指数与帕氏指数]] / [[链式加权]]
- 制度:[[美国经济分析局BEA]]
- 教材:[[Macroeconomics-Mankiw-9e]] Ch 2.1.4 + Ch 2.2
