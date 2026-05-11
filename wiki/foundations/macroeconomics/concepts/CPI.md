---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw) .pdf, Ch 2"]
tags: [concept, macroeconomics, price-index, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# CPI

> **一句话定义**:**Consumer Price Index**(消费者价格指数),衡量典型城市消费者购买固定商品篮子的成本变化,是美国官方"通胀率"的主要来源。

## 在教材中的位置

- 来源:[[Macroeconomics-Mankiw-9e]] Ch 2.2 *Measuring the Cost of Living*
- 制度:[[美国劳工统计局BLS]] 编制并每月发布

## 公式

$$
\text{CPI}_t = \frac{\sum_i p_{i,t} \cdot q_{i,b}}{\sum_i p_{i,b} \cdot q_{i,b}} \times 100
$$

其中:
- $p_{i,t}$:商品 $i$ 在时期 $t$ 的价格;
- $q_{i,b}$:商品 $i$ 在**基期 $b$** 的数量(权重);
- 基期 CPI = 100。

注意分子分母都用**基期数量** $q_{i,b}$,只有价格不同——CPI 是 [[拉氏指数与帕氏指数|拉氏指数]]。

## 与 GDP 平减指数的差异

详见 [[GDP平减指数与CPI比较]]。三大差异:

| 差异 | CPI | [[GDP平减指数]] |
|---|---|---|
| 篮子构成 | 城市消费者典型购物篮 | 所有国内最终生产 |
| 权重类型 | 基期权重(拉氏) | 当期权重(帕氏) |
| 进口品 | 含 | 不含 |

## CPI 的多个版本

| 指数 | 全称 | 用途 |
|---|---|---|
| **CPI-U** | Consumer Price Index for All Urban Consumers | 媒体最常引用的"通胀率" |
| **CPI-W** | CPI for Urban Wage Earners and Clerical Workers | 社保福利、工会工资指数化 |
| **C-CPI-U** | Chained CPI for All Urban Consumers | 反映替代行为(Tornqvist 指数);通胀读数低 0.2-0.3pp |
| **PCE Price Index** | Personal Consumption Expenditures Price Index | Fed 偏好的通胀目标(虽不属 BLS) |

## 篮子结构(2014 美国 CPI-U)

| 类别 | 权重 |
|---|---|
| 住房 | 42% |
| 交通 | 17% |
| 食品 / 饮料 | 14% |
| 医疗 | 8% |
| 娱乐教育 | 7% |
| 服装 | 3% |
| 其他 | 9% |

权重每两年更新一次(基于 *Consumer Expenditure Survey*)。

## 与 [[GDP]] 测度三件套

CPI 与 [[GDP平减指数]] 是宏观分析的两大通胀指标,与 [[失业率]] 共同构成"三件套":
- **GDP** 测产出;
- **CPI** 测通胀;
- **失业率** 测就业。

后续宏观模型(Phillips 曲线、AD-AS、Okun 法则)的所有变量都从这三件套衍生。

## 反面论点与数据空白

- **CPI 偏差**:[[Boskin委员会]] 1996 估计 CPI 高估通胀约 1.1pp,涵盖替代偏差、新商品偏差、质量变化偏差。详见 [[CPI偏差]]。
- **政治化变量**:CPI 与社保福利、退休金、税阶门槛挂钩,使其成为美国财政最敏感的变量之一。Boskin 委员会的"技术修正"建议被批评为"披着学术外衣的紧缩工具"。[BIAS]
- **2020-22 大流行的篮子失效**:消费结构剧变(出行 / 餐饮 / 实物零售 ↓,居家 / 数字消费 ↑),BLS 2017-18 权重失真;Cavallo 2020 估算"实时篮子"通胀比公布 CPI 高 0.5-1pp。
- **住房权重的争议**:CPI 用"自有住房等价租金"(OER)估算,2021-22 美国房价大涨与租金温和涨幅之间的滞后,使 CPI 在通胀回潮时低估约 0.3-0.5pp(后又因滞后高估)。
- **regional-bias**:本页全部基于美国 CPI-U;欧盟 HICP(协调消费者物价指数)、日本总务省 CPI、中国 NBS CPI 的篮子结构、权重更新频率不同,国际比较存在系统差异。

## 相关页

- 关联:[[GDP平减指数]] / [[GDP平减指数与CPI比较]] / [[拉氏指数与帕氏指数]] / [[CPI偏差]] / [[Boskin委员会]] / [[PPI]]
- 制度:[[美国劳工统计局BLS]]
- 教材:[[Macroeconomics-Mankiw-9e]] Ch 2.2
