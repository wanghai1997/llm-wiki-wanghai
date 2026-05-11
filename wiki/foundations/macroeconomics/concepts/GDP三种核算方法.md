---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw) .pdf, Ch 2"]
tags: [concept, macroeconomics, national-accounts, gdp, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# GDP 三种核算方法

> **一句话定义**:[[GDP]] 在理论上等价的三种核算视角——生产法、收入法、支出法,在理想测量下完全相等。

## 在教材中的位置

- 来源:[[Macroeconomics-Mankiw-9e]] Ch 2.1.3
- 制度:[[美国经济分析局BEA]] NIPA 表 1.7.5

## 三种方法

### 1. 生产法(Production Approach / 增加值法)

GDP = 各行业增加值之和

**增加值**(value added)= 行业总产出 − 中间投入。该方法避免重复计算 [[中间品与最终品]]——只计入每环节的"新增"价值。

**例**:面包行业
- 农民产麦 100,卖给磨坊增加值 100;
- 磨坊磨粉 250,中间品 100,增加值 150;
- 面包房做面包 400,中间品 250,增加值 150;
- 总 GDP 贡献 = 100 + 150 + 150 = 400(等于最终面包售价)。

### 2. 收入法(Income Approach)

GDP = 所有要素收入之和

具体项目:
- **雇员报酬**(Compensation of employees):工资 + 福利;
- **企业利润**(Corporate profits):公司税前利润;
- **业主收入**(Proprietors' income):非公司业主收入;
- **租金收入**(Rental income):净租金;
- **净利息**(Net interest):利息收入 − 利息支出;
- **生产税**(Taxes on production and imports):销售税、消费税等;
- **折旧**(Depreciation / Consumption of fixed capital):资本耗用。

### 3. 支出法(Expenditure Approach)

$Y = C + I + G + NX$,见 [[GDP核算恒等式]]。

## 三法的等价性

三种方法在**理论上**完全相等,因为:
- 每件最终产品的售价 = 增加值之和(生产 = 支出);
- 每件最终产品的售价 = 用于支付要素的总额(支出 = 收入)。

实际数据中,统计误差导致差距,BEA 公布"统计误差"项(*statistical discrepancy*)以平衡。该项通常在 $\pm 1\%$ GDP 之内。

## 教材的方法选择

Mankiw Ch 2 主要用**支出法**讲解,因为:
- 直接对应宏观模型(IS-LM、AD-AS、开放经济);
- $C, I, G, NX$ 各自有独立行为方程;
- 易与凯恩斯主义"总需求"叙事衔接。

教材在 Ch 3 末提及收入法用于推导要素收入分配。生产法在中级教材中最少使用,但在行业分析、产业政策中是核心工具。

## 与微观经济学的关系

微观经济学侧也有三种"价值"视角:
- **生产法 ↔ 厂商最优化**(Nechyba Ch 11-13):增加值对应厂商利润 + 工资 + 利息;
- **收入法 ↔ 要素市场**(Nechyba Ch 14):工资率 × 劳动 + 资本租金 × 资本;
- **支出法 ↔ 消费者支出**(Nechyba Ch 1-10):预算约束的总和。

但宏观加总不等于微观加总——一般均衡中各市场出清的总价值即是 GDP,这一逻辑由 [[Walras定律]] 保证。

## 反面论点与数据空白

- **生产法在数字经济中的失灵**:开源软件、维基百科等没有市场价格的"中间投入",生产法增加值无法计算。BEA 2018 *Digital Economy Satellite Account* 使用替代估算,但仍不完整。
- **收入法的功能性收入分配偏置**:收入法把"工资 vs 利润 vs 租金"明确化,但不直接显示个人之间的不平等(基尼系数);Mankiw Ch 2 不深入这一维度。
- **三法不一致的隐含信息**:统计误差项(statistical discrepancy)长期偏向某一方向,可能反映系统性测度问题。例:1990s 美国统计误差长期为正,提示生产 / 收入侧高估或支出侧低估。
- **regional-bias**:中国 NBS 长期主要用生产法发布 GDP,2018 改革后逐步引入支出法。各国方法差异可影响国际比较。

## 相关页

- 父概念:[[GDP]]
- 子方法:[[GDP核算恒等式]](支出法)
- 子项:[[中间品与最终品]] / [[国民收入核算衍生指标]]
- 制度:[[美国经济分析局BEA]]
- 教材:[[Macroeconomics-Mankiw-9e]] Ch 2.1.3
