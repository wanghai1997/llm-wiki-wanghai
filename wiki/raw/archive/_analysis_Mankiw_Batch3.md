---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw) .pdf"]
tags: [analysis, ingest-stage1, mankiw, macroeconomics]
status: stage1-approved-stage2-completed
---

# Mankiw 9e Batch 3 — Stage 1 分析

## 摄入范围

- **教材**：Mankiw, *Macroeconomics* (Ninth Edition), Worth Publishers 2016
- **章节**：Part II 古典(长期) **Ch 6-7**（共两章约 40 页正文）
  - **Ch 6** "The Open Economy"（开放经济）
  - **Ch 7** "Unemployment and the Labor Market"（失业与劳动力市场）
- 衔接 Batch 2（Ch 3-5 古典核心三部曲），完成 Part II 古典长期理论全部七章

> **范围决策**：Batch 2 处理 Ch 3-5（实物 → 货币 → 通胀），Batch 3 处理 Ch 6-7（开放经济 + 失业）。两章在分析框架上均延续古典市场出清假设，且共享"长期"视角，自然成组。Part III（Ch 8-9 增长理论）留待 Batch 4。

## 1. 核心实体（建议入库 / 更新）

### 历史人物（新建）

| 实体 | 类型 | 关键事实 | 优先级 |
|---|---|---|---|
| **David Hume** (1711-1776) | entity | 已在 Batch 2 入库（货币数量论），Ch 6 PPP 再次引用其价格-铸币流动机制 | 已存在 |
| **David Card** (1956-) | entity | 1994 与 Krueger 新泽西-宾州最低工资自然实验，获 2021 诺奖 | 中 |
| **Alan Krueger** (1960-2019) | entity | 与 Card 合著最低工资研究，Obama 总统经济顾问委员会主席 | 中 |
| **George Akerlof** (1940-) | entity | 已在 micro/entities 存在（信息不对称），Ch 7 效率工资引用其"效率工资理论" | 已存在 |
| **Janet Yellen** (1946-) | entity | Ch 7 效率工资理论研究者（Yellen 1984 综述），后任 Fed 主席 | 低 |
| **Carl Shapiro** / **Joseph Stiglitz** | entity | Shapiro-Stiglitz 1984 效率工资模型（不偷懒约束），Stiglitz 已在 entities 存在 | 低 |
| **Arthur Okun** (1928-1980) | entity | "奥肯定律"（Okun's Law）关联失业与 GDP 缺口，Ch 9 详述，此处伏笔 | 低(占位) |
| **Edmund Phelps** (1933-2023) | entity | 1968 "自然失业率"概念独立提出者（与 Friedman 同时），2006 诺奖 | 中 |
| **Peter Diamond** (1940-) | entity | 搜索与匹配理论，2010 诺奖（与 Mortensen/Pissarides），Ch 7 搜索模型基础 | 低(占位) |
| **Dale Mortensen** (1939-2014) / **Christopher Pissarides** (1948-) | entity | DMP 搜索匹配模型，2010 诺奖，Ch 7 摩擦性失业微观基础 | 低(占位) |

> **注**：Batch 3 历史人物较 Batch 2 少，因 Ch 6-7 多为"模型 + 实证"而非"学派创始人"叙事。Card/Krueger 是 Ch 7 最低工资辩论的核心。Mundell / Fleming / Dornbusch 等开放经济代表人物主要在 Ch 12（Mundell-Fleming 模型）出场，本 Batch 仅提及 Mundell-Fleming 模型"将在 Ch 12 讨论"。

### 机构 / 概念性实体（新建或更新）

| 实体 | 类型 | 处理方式 |
|---|---|---|
| **IMF** (International Monetary Fund) | entity | Ch 6 国际收支 / 汇率危机案例引用;简述其"汇率制度分类" | 低 |
| **The Economist** | entity | Big Mac Index 发布者 | 低 |
| **BLS** (Bureau of Labor Statistics) | entity | 已在 Batch 1 存在（CPI / 失业率数据来源） | 已存在 |
| **JOLTS** (Job Openings and Labor Turnover Survey) | entity | BLS 职位空缺调查，Ch 7 Beveridge 曲线数据来源 | 中 |

## 2. 核心概念（建议入库 / 更新）

### Ch 6 — 开放经济

| 概念 | 是否新建 | 关键内容 |
|---|---|---|
| **净出口(NX)** | 新建 | $NX = EX - IM$；与 GDP 核算恒等式 $Y = C + I + G + NX$ 的衔接 |
| **净资本流出(NCO)** | 新建 | net capital outflow；$NCO = S - I$；$NX = NCO$ 恒等式 |
| **贸易余额** | 新建 | trade balance；顺差/逆差/平衡；与储蓄-投资缺口的关系 |
| **小型开放经济模型** | 新建（核心）| 世界利率 $r^*$ 外生；$S$ 由国内因素决定，$I = I(r^*)$；NX 调节 $S-I$ 缺口 |
| **世界利率** | 新建 | world interest rate；小型开放经济的关键外生变量 |
| **名义汇率** | 新建 | nominal exchange rate；direct vs indirect quote；升值/贬值 |
| **实际汇率** | 新建 | real exchange rate；$\epsilon = e \cdot P / P^*$；贸易竞争力指标 |
| **购买力平价(PPP)** | 新建（核心）| 一价定律 → 绝对 PPP → 相对 PPP；长期汇率决定理论 |
| **一价定律** | 新建 | law of one price；同一商品在不同国家以同一货币计价价格相同 |
| **Big Mac Index** | 新建 | 《经济学人》PPP 经验检验；汇率高估/低估的通俗度量 |
| **贸易方程（实际汇率决定）** | 新建 | $NX = NX(\epsilon)$；$S-I$ 垂直线 + $NX(\epsilon)$ 向下倾斜 → 决定 $\epsilon$ |
| **汇率制度** | 新建 | 固定汇率 vs 浮动汇率；Mankiw 简述 IMF 分类 |
| **资本管制** | 新建 | capital controls；小型开放经济模型的偏离；中国案例 |

### Ch 7 — 失业与劳动力市场

| 概念 | 是否新建 | 关键内容 |
|---|---|---|
| **自然失业率** | 新建（核心）| natural rate of unemployment；长期趋近的失业率；Frictional + Structural |
| **摩擦性失业** | 新建 | frictional unemployment；正常流动；缩短 vs 消除 |
| **结构性失业** | 新建 | structural unemployment；实际工资刚性 > 均衡工资；劳动力市场错配 |
| **实际工资刚性** | 新建 | real-wage rigidity；最低工资 / 工会 / 效率工资三种来源 |
| **效率工资** | 新建 | efficiency wage；Akerlof / Shapiro-Stiglitz；支付高于市场工资以提高生产率 |
| **最低工资** | 新建 | minimum wage；Card-Krueger 1994 自然实验 vs 标准竞争模型 |
| **工会与集体谈判** | 新建 | unions / collective bargaining；insider-outsider 理论 |
| **工作搜寻模型** | 新建 | job search；保留工资；失业保险对搜寻激励的影响 |
| **部门转移** | 新建 | sectoral shifts；Lilien 1982；结构性失业来源之一 |
| **Beveridge曲线** | 新建 | 失业率 vs 职位空缺率；沿曲线移动（周期）vs 曲线外移（结构） |
| **劳动力市场政策** | 新建 | 就业服务 / 工作培训 / 最低工资 / 失业保险设计 |
| **入职率与离职率** | 新建 | job finding rate $f$ / separation rate $s$；自然率 $U/L = s/(s+f)$ |
| **失业保险(UI)** | 新建 | unemployment insurance；道德风险 vs 消费保险权衡 |

### 其他附属概念

| 概念 | 优先级 | 备注 |
|---|---|---|
| **汇率风险** | 低 | Ch 6 简述，未深入 |
| **利率平价** | 低 | covered/uncovered interest parity；Mankiw 未详述，留教材脚注 |
| **内部人-外部人模型** | 低 | insider-outsider theory；工会议价；教材简述 |
| **滞后效应(Hysteresis)** | 低 | 短期失业→自然率上升；Mankiw 未详述，Olivier Blanchard/Summers 提出 |

## 3. 与现有 Wiki 链接点

### 3.1 Batch 1-2 已有宏观页 — 直接引用

| 已有页 | Batch 3 引用方向 |
|---|---|
| [[GDP]] | Ch 6 $Y = C + I + G + NX$；开放经济下的 GDP 恒等式 |
| [[GDP三种核算方法]] | Ch 6 支出法中的净出口 $NX$；国际收支恒等式 |
| [[GDP核算恒等式]] | Ch 6 $S - I = NX = NCO$ 的核心推导起点 |
| [[失业率]] | Ch 7 自然失业率、摩擦性失业、结构性失业的细分 |
| [[CPI]] | Ch 6 实际汇率中 $P$ 与 $P^*$ 的测度 |
| [[古典宏观长期模型]] | Batch 2 主题页；Ch 6-7 是其开放经济与劳动力市场扩展 |
| [[货币与通胀理论]] | Ch 6 PPP 与货币数量论的汇率版本（$e = P/P^*$） |
| [[储蓄-投资均衡]] | Ch 6 开放经济下 $S - I = NX$ 替代封闭经济的 $S = I$ |
| [[挤出效应]] | Ch 6 小型开放经济中：财政扩张 → $S \downarrow$ → $NX \downarrow$（非利率上升） |
| [[N. Gregory Mankiw]] | 作者主页 |
| [[Macroeconomics-Mankiw-9e]] | 教材主页，Batch 3 完成后更新表格 |
| [[宏观经济学foundations总览]] | Batch 3 行更新为"已完成" |

### 3.2 微观（Nechyba）已有页面 — 单向 see-also

| 微观已有页 | 宏观新建页对应 | 用途 |
|---|---|---|
| [[国际贸易的福利分析]] | Ch 6 [[净出口]] / [[小型开放经济模型]] | 微观贸易福利 vs 宏观 NX 流量；Nechyba Ch 15 关税/配额 vs Mankiw 开放经济宏观 |
| [[劳动供给]] | Ch 7 [[自然失业率]] / [[摩擦性失业]] | 微观个体劳动供给决策 vs 宏观失业总量 |
| [[劳动力市场均衡]] | Ch 7 [[结构性失业]] / [[实际工资刚性]] | 微观完全竞争劳动市场出清 vs 宏观工资刚性导致失业 |
| [[最低工资]] | Ch 7 [[最低工资]] | 微观供需分析 vs 宏观 Card-Krueger 经验证据 |
| [[工会]] | Ch 7 [[工会与集体谈判]] | 微观劳动垄断 vs 宏观失业结构来源 |
| [[效率工资]] | Ch 7 [[效率工资]] | 微观激励理论 vs 宏观结构性失业解释 |
| [[一般均衡]] | Ch 6 [[小型开放经济模型]] | 微观多市场均衡 vs 宏观开放经济一般均衡（国内 + 国际） |

### 3.3 关联议题 / 跨域

| 关联页 | 用途 |
|---|---|
| [[Token工厂经济学]] | Ch 6 开放经济：AI 芯片（NVIDIA GPU）贸易与全球 NX 格局；美国高科技出口管制→NX 变动 |
| [[NVIDIA]] / [[黄仁勋]] | AI 芯片出口管制（美国→中国）作为"资本管制"的当代案例；全球半导体供应链与贸易余额 |
| [[AI重塑企业组织]] | Ch 7 结构性失业：AI 替代导致的部门转移（sectoral shifts）是摩擦性/结构性失业的新来源 |
| [[GDP的局限性]] | Ch 6 贸易余额不能衡量"福利"：NX > 0 不等于国家更富（只是借出更多） |

## 4. 矛盾发现

### 内部矛盾（教材内部）

1. **小型开放经济模型的"小型"假设与现实不符**：
   - Ch 6 假设本国是世界利率 $r^*$ 的接受者（price taker）；
   - 但美国是全球最大经济体，其财政/货币政策显然影响全球 $r^*$；
   - 教材自承"大型开放经济"将在后续章节（Ch 12）处理，但全书未展开。
   - **标记**：`[CONTRADICTION] 小型开放经济的 price-taker 假设对美国不适用`

2. **PPP 理论与实际汇率的巨大偏离**：
   - Ch 6-4 给出 PPP 理论：$e = P/P^*$；
   - 但 Big Mac Index 显示实际汇率长期大幅偏离 PPP（如瑞士法郎高估 30%+）；
   - Mankiw 解释为"非贸易品 + 贸易壁垒 + 消费偏好差异"，但**未量化偏离幅度**也**未给出预测能力评估**；
   - Rogoff 1996 "购买力平价之谜"（PPP 偏离半衰期 3-5 年）未被提及。
   - **标记**：`[CONTRADICTION] PPP 长期成立但短期偏离极大，教材未处理"多久算长期"`

3. **自然失业率的"自然"是否自然**：
   - Ch 7 将自然失业率定义为 $U/L = s/(s+f)$，由入职率/离职率决定；
   - 但政策显然影响 $s$ 和 $f$（失业保险改变 $f$，培训改变 $f$）；
   - "自然"一词暗示外生/不可改变，实际高度内生于制度设计；
   - Friedman 1968 原话"自然率"(natural rate)借用自 Wicksell，是隐喻而非实证断言。
   - **标记**：`[CONTRADICTION] "自然失业率"名不副实——政策可改变其水平`

4. **最低工资的竞争模型 vs Card-Krueger 证据**：
   - Ch 7 先讲标准竞争模型：最低工资 ↑ → 失业 ↑（教材 Figure 7-4）；
   - 然后引用 Card-Krueger 1994：新泽西最低工资 ↑ 但就业未 ↓；
   - 教材的"解决"是："一些经济学家认为 Card-Krueger 结果不稳健"（教材第 200 页脚注），但**不深入 Monopsony 模型**（Stigler 1946 / Manning 2003），而 Monopsony 才是最低工资不增失业的完整理论解释；
   - 微观 Nechyba Ch 26 处理买方垄断，但宏观教材回避此框架。
   - **标记**：`[CONTRADICTION] 最低工资竞争模型预测与 Card-Krueger 证据矛盾，教材未引入买方垄断解释`

### 与 Batch 1-2 概念的对接矛盾

5. **古典模型中的"充分就业" vs Ch 7 的失业**：
   - Ch 3-5 古典模型默认劳动市场出清（$L$ = 充分就业）；
   - Ch 7 引入摩擦性失业 + 结构性失业，承认劳动市场**长期也存在失业**；
   - 古典"充分就业"是"自然率下的就业"而非"零失业"，但教材在两章之间的语义切换不够清晰；
   - 对读者而言，Ch 3 $L$ 是固定/外生，Ch 7 $L$ 受 $s,f$ 和工资刚性影响，模型不一致。
   - **标记**：`[CONTRADICTION] Ch 3 劳动市场出清 vs Ch 7 长期失业——模型假设不一致`

6. **Ch 6 $S-I = NX$ 与 Ch 3 可贷资金市场的断裂**：
   - Ch 3 封闭经济：$S$ 和 $I$ 通过 $r$ 在国内出清；
   - Ch 6 开放经济：$r = r^*$（外生），$S-I$ 缺口通过 $NX$ 出清；
   - 两套机制完全不同，教材未解释"封闭→开放"的过渡逻辑（大国情形是中间状态）。

### 与外部学派的矛盾

7. **效率工资理论的微观基础争议**：
   - Mankiw 引用 Akerlof "礼物交换"和 Shapiro-Stiglitz "不偷懒约束"解释效率工资；
   - 但新古典批评者（如 Summers 1988 之后）认为效率工资是 ad hoc，缺乏稳健微观基础；
   - 实证上效率工资对失业的解释力有限（欧洲高失业更可能是制度因素）。

8. **搜索匹配模型 vs 古典代表行为人**：
   - Ch 7 摩擦性失业使用 $s,f$ 流量模型，本质仍是总量代表行为人；
   - Diamond-Mortensen-Pissarides 搜索匹配模型（2010 诺奖）需要异质性工人和职位，与 Mankiw 的简化框架不同；
   - 教材仅在脚注/案例研究提及 DMP，未纳入正文。
   - **标记**：`[BIAS] 搜索模型简化为代表行为人流量方程，回避异质性匹配`

9. **开放经济的国际收支账户 vs MMT 视角**：
   - Mankiw：$NX = NCO$，贸易顺差 = 资本净流出，是一种"约束"；
   - MMT / 后凯恩斯：主权货币国家的国际收支是会计恒等式而非约束，本国政策空间不受 NX 限制（浮动汇率下）；
   - 对非主权货币国家（欧元区成员国）确实受约束，但教材未区分。

## 5. 知识缺口

### 教材自身缺失

1. **大国开放经济模型**：美国显然不是 price taker，但全书未建立 $r$ 内生的两国模型；Ch 12 Mundell-Fleming 仍假设小型开放经济。
2. **汇率决定的资产市场方法**：货币主义汇率理论（$e = M/M^* \cdot ...$）仅简述，Dornbusch 超调模型（1976）未出现。
3. **2008 后全球储蓄过剩 / 安全资产稀缺**：Bernanke 2005 "全球储蓄过剩"假说、Caballero 安全资产短缺，解释美国长期贸易逆差——教材未涉及。
4. **贸易战与关税的宏观效应**：2018-2020 中美贸易战期间关税对 NX 的影响，教材 2016 出版自然未涵盖。
5. **远程工作与劳动力市场**：COVID-19 后远程工作对摩擦性失业、地理错配的影响——教材未涉及。
6. **中国的劳动力市场制度**：户籍制度、劳务派遣、农民工流动对摩擦性/结构性失业的影响——完全缺失。
7. **欧洲青年失业危机**：西班牙/希腊 2010s 青年失业率 >50%，是结构性失业的典型案例——教材未深入。
8. **AI / 自动化对失业的影响**：Autor / Acemoglu / Restrepo 的"任务模型"（routine-biased technical change）——教材未涉及。
9. **平台经济与零工就业**：Uber / 外卖骑手等"非标准就业"对失业统计的挑战（是否算失业？是否算劳动力？）

### 本 Wiki 跨域缺口

10. **[[Token工厂经济学]] 的全球供应链**：AI 芯片（台积电制造、NVIDIA 设计、全球消费）是开放经济宏观的典型截面，但 Token 工厂框架未用 NX/NCO 语言。
11. **算力作为"资本品"的跨境流动**：GPU 数据中心投资是 $I$ 还是资本进口？云服务出口是服务出口还是 "数字 NX"？

### 政策与制度缺口

12. **IMF 条件性(Conditionality)**：汇率危机时的 IMF 贷款条件（财政紧缩/结构性改革），教材未涉及。
13. **欧元区的不完全货币联盟**：Ch 6 提及 Euro 案例，但未分析"无独立货币政策 + 无财政转移"对成员国失业的影响。
14. **中国资本账户管制**：Ch 6 小型开放经济假设 $NCO$ 自由流动，但中国资本管制使模型完全不适用——教材未标注此 [regional-bias]。

## 6. 反面论点初稿（[BIAS] / [CONTRADICTION] 标注）

### 6.1 开放经济的批判视角

> `[BIAS]` Mankiw Ch 6 的开放经济模型是**新古典范式**的延伸：自由贸易总是最优（$NX$ 只是调节储蓄-投资缺口），汇率由基本面（PPP）决定。以下视角被边缘化：

- **贸易保护主义者 / 战略贸易理论**（Krugman / Brander-Spencer）：战略性产业（半导体、AI 芯片）的贸易限制有福利改进可能；Mankiw 只在脚注简述"战略性贸易理论"，未展开。
- **依赖理论 / 结构主义**（Prebisch, Singer）：发展中国家出口初级产品、进口制成品的贸易结构导致长期贸易条件恶化；PPP 和一价定律假设全球同质商品，忽略南北不平等交换。
- **MMT / 后凯恩斯开放经济**：浮动汇率主权货币国家不受 NX 约束；固定汇率（如欧元区）才是问题根源。Mankiw 默认 NX 是"需要平衡"的变量，而非会计恒等式。

### 6.2 失业理论的方法论争议

> `[BIAS]` Mankiw Ch 7 的失业框架是**新古典综合**的：自然失业率由摩擦 + 结构组成，需求侧（周期性失业）是短期现象。这一框架在以下视角下有问题：

- **后凯恩斯派（Robinson, Davidson）**：拒绝"自然率"概念——失业主要是有效需求不足，而非摩擦/结构；"自然率"是为放任政策辩护的意识形态构造。
- **Marxist / 激进经济学（Bowles, Weisskopf）**：失业是资本控制劳动的系统性工具（"失业后备军"），效率工资/工会压制只是表象；自然失业率理论掩盖了阶级结构。
- **行为派劳动经济学（Kahneman, Thaler）**：失业的心理成本、搜寻行为中的非理性（过度自信、现状偏见）使 $s,f$ 模型过于简化；保留工资不是理性计算的结果。
- **女性主义经济学**：自然失业率模型以"男性面包winner"为默认主体，忽略女性非正式劳动、无偿家务劳动对"劳动力"定义的影响；BLS U-1~U-6 统计框架本身有性别偏置。

### 6.3 最低工资争议的偏置

- Mankiw 呈现 Card-Krueger 结果但快速以"方法争议"消解，**未呈现买方垄断(monopsony)模型**——后者是最低工资不增失业的完整理论解释；
- 买方垄断在 Nechyba 微观 Ch 26 有详述，但宏观教材回避，造成"微观-宏观知识断裂"；
- 2019 年后 Cengiz-Dube-Lindner-Zimmerman 等利用更多州级边界数据的最低工资研究确认 Card-Krueger 结论，教材当然未涵盖。
- **标记**：`[BIAS] 最低工资竞争模型占主导，买方垄断解释被边缘化`

### 6.4 区域偏置

- **regional-bias 标记**：Ch 6 汇率案例以美国/欧元区为主，新兴市场汇率危机（1997 亚洲、2001 阿根廷、2018 土耳其）仅简述；
- Ch 7 失业数据全部美国（CPS / JOLTS / Beveridge 曲线），欧洲（Eurostat）、日本（总务省）、中国（NBS 城镇调查失业率）的制度差异未对比；
- 中国 2023 青年失业率 >20% 的案例、印度就业弹性低下、拉美非正规就业等完全缺失。

### 6.5 模型简化与当代议题的脱节

- **AI 与自动化失业**：Acemoglu-Restrepo "任务模型"（routine-biased technical change）指出 AI 替代常规任务、创造非常规任务；Mankiw 仅提及 "sectoral shifts" 是摩擦性失业来源，未分析 AI 带来的结构转型规模；
- **零工经济与失业统计**：Uber 司机在 BLS 统计中算"就业"还是"非正规"？平台经济模糊了"失业/就业"二元；
- **远程工作对地理错配的影响**：COVID-19 后远程工作降低摩擦性失业（搜寻范围扩大），但也可能导致新的结构性错配（"超级明星城市"集中）。

## 7. 拟新建页面清单（Stage 2 候选）

> 共 **~20** 个新页；具体取舍待用户批准 Stage 1 后定稿。

### entities/（3-4 个）
1. `David-Card.md`
2. `Alan-Krueger.md`
3. `Edmund-Phelps.md`（可选，自然失业率概念共同提出者）
4. `Peter-Diamond.md`（可选，搜索匹配理论，DMP 模型）

### concepts/（主线 ~16 个）

**Ch 6 开放经济组（8 个）**：
- 净出口与净资本流出.md（$NX = NCO = S-I$ 恒等式）
- 小型开放经济模型.md（核心：世界利率 + S-I 缺口 + NX 调节）
- 名义汇率与实际汇率.md（含升值/贬值定义）
- 实际汇率与贸易余额.md（$NX(\epsilon)$ 函数）
- 购买力平价.md（PPP；一价定律；Big Mac Index）
- 开放经济中的财政政策.md（小型开放经济下的挤出 → 贸易余额下降）
- 开放经济中的储蓄变动.md（$S$ 变动对 NX 的影响）
- 汇率制度.md（固定 vs 浮动；IMF 分类简述）

**Ch 7 失业组（8 个）**：
- 自然失业率.md（核心：$U/L = s/(s+f)$；摩擦 + 结构）
- 摩擦性失业.md（工作搜寻；保留工资；入职率/离职率）
- 结构性失业.md（实际工资刚性；劳动力市场错配）
- 实际工资刚性.md（最低工资 / 工会 / 效率工资三种机制）
- 效率工资.md（Akerlof 礼物交换；Shapiro-Stiglitz 不偷懒约束）
- 最低工资.md（标准模型 vs Card-Krueger 证据；买方垄断伏笔）
- 工会与集体谈判.md（insider-outsider；对工资/失业的影响）
- Beveridge曲线.md（失业率-职位空缺率；周期 vs 结构移动）

### topics/（1 个汇总页）
- 开放经济与失业理论.md（Part II 总览页，整合 Ch 6-7；或拆分为两个主题页）

> **替代方案**：Ch 6 和 Ch 7 主题差异大，可建两个主题页：
> - `开放经济理论.md`（Ch 6 整合）
> - `失业与劳动力市场理论.md`（Ch 7 整合）

### 教材主页 / 索引更新
- `Macroeconomics-Mankiw-9e.md` 的 Batch 表 + 历史人物索引；
- `宏观经济学foundations总览.md` Batch 3 行更新为已完成；
- `wiki/log.md` 追加 Batch 3 入口；
- `wiki/index.md` 追加 Batch 3 页面。

## 8. 关键决策待用户确认

请用户确认 / 调整以下决策：

1. **主题页结构**：Ch 6-7 合并为一个主题页 `开放经济与失业理论.md`，还是拆分为两个（`开放经济理论.md` + `失业与劳动力市场理论.md`）？
2. **历史人物深度**：Card / Krueger 本 Batch 入库（最低工资核心）；Phelps / Diamond 是否纳入（他们的核心贡献分别在自然率和搜索匹配，但 Mankiw 正文未深入 DMP）？
3. **PPP 深度**：是否引入 Rogoff 1996 "PPP 之谜"（偏离半衰期 3-5 年）作为教材外部知识补充？
4. **买方垄断模型**：最低工资页是否引入 monopsony 模型解释 Card-Krueger 结果？还是严格只追溯 Mankiw 文本（文本回避了 monopsony）？
5. **Beveridge 曲线**：是否引入 2008 后美国 Beveridge 曲线外移（结构变化）的实证？
6. **Card-Krueger 后续研究**：是否补充 2019 年后 Cengiz-Dube 等大数据最低工资研究（确认 Card-Krueger 结论）？
7. **AI / 自动化失业**：Ch 7 "部门转移"页是否加入 Acemoglu-Restrepo "任务模型"作为当代扩展？
8. **中国资本管制**：小型开放经济模型页是否加 [regional-bias] 标注（模型对中国完全不适用）？

---

> Stage 1 分析完成。**请用户回复"继续"或具体修改意见**，经批准后进入 Stage 2 页面生成。
