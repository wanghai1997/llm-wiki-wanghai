---
created: 2026-05-03
updated: 2026-05-03
source: "Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 15-20 + Epilogue, pp.441-600"
status: stage1-pending-approval
---

# Mankiw Batch 7 Stage 1 Analysis: Ch 15-20 + Epilogue — Microfoundations, Policy, and Finance

## Executive Summary

Batch 7 is the **final batch** of the Mankiw 9e ingestion, covering Part V (Ch 15-19: microfoundations of consumption, investment, money demand, and policy debates) and Part VI (Ch 20: financial system and crisis), plus the Epilogue. This batch "backfills" the theoretical foundations that Part IV (Ch 10-14) used heuristically—explicitly modeling consumer intertemporal optimization, firm investment decisions, and money demand from first principles. It also presents the major methodological divide in modern macroeconomics: Real Business Cycle (RBC) vs. New Keynesian models, and the rules-vs-discretion debate. Ch 20 and the Epilogue bring the narrative to the 2008 financial crisis and the state of macroeconomic consensus (or lack thereof).

---

## §1 Core Entities (Historical Figures)

| # | 建议页面名 | 身份 / 贡献 | 教材出现位置 | 批注 |
|---|---|---|---|---|
| E1 | [[Franco Modigliani]] | MIT, life-cycle hypothesis of consumption (1954), 1985 Nobel | Ch 16 | 消费理论三大支柱之一(与Friedman永久收入、Keynes消费函数并列) |
| E2 | [[James Tobin]] | Yale, Tobin's q theory of investment (1969), portfolio selection, 1981 Nobel | Ch 17 | 投资理论的核心人物;q理论将金融市场与实物投资连接 |
| E3 | [[Ben Bernanke]] | Fed Chair 2006-14, financial accelerator (Bernanke-Gertler-Gilchrist 1999), Great Depression banking research | Ch 20 | 2008金融危机的核心决策者;金融加速器理论是Ch 20的理论 backbone |
| E4 | [[Finn Kydland]] | Carnegie Mellon/Santa Barbara, RBC model (1982 with Prescott), time inconsistency (1977 with Prescott), 2004 Nobel | Ch 19 | RBC革命的核心人物;时间不一致性理论直接支撑规则vs相机抉择辩论 |
| E5 | [[Edward Prescott]] | Arizona State, RBC model (1982 with Kydland), 2004 Nobel | Ch 19 | 与Kydland共同开创RBC;"政策无效"命题 |
| E6 | [[David Laibson]] | Harvard, hyperbolic discounting / quasi-hyperbolic preferences in macro consumption, behavioral macro pioneer | Ch 16 (隐含) | Mankiw教材提及"即时满足"(instant gratification)倾向,隐含Laibson框架 |
| E7 | [[Hyman Minsky]] | Washington University, financial instability hypothesis (1975, 1986), "Minsky moment" | Ch 20 (隐含) | 教材未直接命名但Ch 20的金融脆弱性分析深受Minsky影响;作为补充人物 |

**Entity page count estimate:** 5-6 new entity pages (Modigliani, Tobin, Bernanke, Kydland, Prescott, possibly Laibson/Minsky). Friedman/Keynes/Lucas are expansions.

---

## §2 Core Concepts (Suggested Hierarchy)

### Ch 15: Stabilization Policy

| # | 建议页面名 | 核心内容 | 子概念 / 公式 | 教材位置 |
|---|---|---|---|---|
| C1 | [[稳定化政策]] *(扩展)* | 政策时滞(认识/决策/执行)、预测困难、卢卡斯批判的政策含义、自动稳定器 | 已有Batch 5页面,需扩展Ch 15深度 | Ch 15 |
| C2 | [[政府债务与赤字]] | 政府预算约束;债务/GDP比率;Ricardian等价性;代际负担;债务可持续性 | $G + rB = T + \Delta B$; 债务动态方程 | Ch 15 |
| C3 | [[Ricardian等价性]] | Barro (1974): 减税→未来增税预期→储蓄抵消→总需求不变 | 政府债务中性命题 | Ch 15 Case Study |
| C4 | [[政策时滞与预测困难]] | 认识时滞、决策时滞、执行时滞;经济预测的系统性偏差 | 美联储预测误差;Greenbook | Ch 15 |

### Ch 16: Consumption

| # | 建议页面名 | 核心内容 | 子概念 / 公式 | 教材位置 |
|---|---|---|---|---|
| C5 | [[消费理论]] | 主题页:从Keynes到行为经济学的消费理论谱系 | 五大模型+微观-宏观桥接 | Ch 16 |
| C6 | [[Keynes消费函数]] *(扩展)* | $C = \bar{C} + cY$, MPC, 消费 puzzle | Kuznets发现长期MPC≈1,短期MPC≈0.9 | Ch 16-1 |
| C7 | [[Fisher跨期选择模型]] | 两期/多期预算约束;消费平滑;利率对储蓄的SE-IE分解 | $U(c_1,c_2)$ subject to $c_1 + c_2/(1+r) = y_1 + y_2/(1+r)$ | Ch 16-2 |
| C8 | [[生命周期假说]] | Modigliani (1954): 消费取决于终身收入而非当期收入;储蓄=收入-平滑消费 | $C = (W + RY)/T$ | Ch 16-3 |
| C9 | [[永久收入假说]] | Friedman (1957): 消费取决于永久收入;暂时性收入→储蓄;预期收入变化→消费调整 | $C = kY^p$; 已建[[古典消费函数]]可扩展或新建 | Ch 16-3 |
| C10 | [[随机游走假说]] | Hall (1978): 在PIH+理性预期下,消费变化不可预测;只有未预期信息改变消费 | $E_t[C_{t+1}] = C_t$; 对政策含义:可预测政策不影响消费 | Ch 16-4 |
| C11 | [[行为消费理论]] | Laibson双曲贴现、心理账户、即时满足;MPC对退税更高(2001/2008退税证据) | $\beta$-$\delta$模型; 时间不一致偏好 | Ch 16-5 |

### Ch 17: Investment

| # | 建议页面名 | 核心内容 | 子概念 / 公式 | 教材位置 |
|---|---|---|---|---|
| C12 | [[投资理论]] | 主题页:新古典投资模型、q理论、融资约束、住房投资、存货投资 | 三种投资类型+微观基础 | Ch 17 |
| C13 | [[新古典投资模型]] | 企业租赁资本至MPK = 资本成本($r + \delta$); 投资=资本存量变化 | $I = K^* - K_{-1} + \delta K_{-1}$ | Ch 17-1 |
| C14 | [[Tobin q理论]] | Tobin (1969): 投资取决于股票市场估值与重置成本之比; q>1→投资 | $q = $ 市场价值 / 重置成本; 连接金融市场与实物投资 | Ch 17-2 |
| C15 | [[融资约束]] | 内外部融资成本差异;信息不对称→投资受现金流影响;小企业尤其严重 | Fazzari-Hubbard-Petersen (1988) | Ch 17-2 |
| C16 | [[住房投资]] | 住房作为耐用消费品+投资品;利率敏感性;2000s房地产泡沫 | 住房市场与商业周期的关系 | Ch 17-3 |
| C17 | [[存货投资]] | 存货作为生产缓冲;加速模型($I_{inv} = a\Delta Y$); JIT革命降低存货/GDP | 已建[[存货投资]](Batch 1)为核算概念,需扩展为投资理论 | Ch 17-3 |

### Ch 18: Money Supply and Money Demand

| # | 建议页面名 | 核心内容 | 子概念 / 公式 | 教材位置 |
|---|---|---|---|---|
| C18 | [[货币需求理论]] | 从数量论到资产组合理论:交易动机、预防动机、投机动机(Baumol-Tobin模型) | $(M/P)^d = L(i, Y)$; 已建[[实际货币余额与货币需求]]可扩展 | Ch 18 |
| C19 | [[Baumol-Tobin模型]] | 最优货币持有量:交易成本与利息损失的权衡;"货币需求的存货理论" | $M^* = \sqrt{bY/2i}$; 平方根公式 | Ch 18-1 |
| C20 | [[货币需求投资组合理论]] | 货币作为资产组合的一部分;风险-收益权衡;预期通胀→减少货币持有 | Tobin (1958) 资产组合选择 | Ch 18-2 |
| C21 | [[货币需求的经验证据]] | 金融创新使货币需求函数不稳定;电子支付改变$L(i,Y)$;数字货币挑战 | 货币主义的衰落(1980s+) | Ch 18-2 |

### Ch 19: Advances in Business Cycle Theory

| # | 建议页面名 | 核心内容 | 子概念 / 公式 | 教材位置 |
|---|---|---|---|---|
| C22 | [[实际经济周期模型]] | Kydland-Prescott (1982): 技术冲击驱动波动;无货币/需求因素;市场始终出清 | 校准(calibration)而非估计;Solow残差作为技术冲击代理 | Ch 19-1 |
| C23 | [[新凯恩斯主义模型]] | 在RBC基础上加名义刚性(价格粘性);货币政策有真实效应;微基础+政策有效 | 新凯恩斯Phillips曲线;DSGE模型作为政策工具 | Ch 19-2 |
| C24 | [[规则与相机抉择]] | Friedman (1960) vs. Keynesian:固定规则(如Taylor规则)避免时间不一致;但规则缺乏灵活性 | Kydland-Prescott (1977)时间不一致性;Taylor (1993)规则 | Ch 19-3 |
| C25 | [[时间不一致性]] | 政策制定者的事前最优≠事后最优;导致通胀偏差(bias);需承诺机制(央行独立性) | 通胀偏差:$ar{\pi} > 0$ even when optimal is 0 | Ch 19-3 |

### Ch 20: The Financial System and the Financial Crisis

| # | 建议页面名 | 核心内容 | 子概念 / 公式 | 教材位置 |
|---|---|---|---|---|
| C26 | [[金融加速器]] | Bernanke-Gertler-Gilchrist (1999): 信贷市场摩擦放大经济波动;净值↓→外部融资成本↑→投资↓ | 资产价格→企业净值→杠杆率→信贷可得性 | Ch 20 |
| C27 | [[银行挤兑与存款保险]] | Diamond-Dybvig (1983): 银行期限转换的内在脆弱性;存款保险作为协调机制 | 已建[[存款保险与金融稳定]]可扩展 | Ch 20 |
| C28 | [[2008金融危机]] | 住房泡沫→次贷→证券化→CDS→雷曼→全球危机;政策应对:QE、救助、Dodd-Frank | 危机传播机制;大衰退(Great Recession) | Ch 20 Case Study |
| C29 | [[宏观审慎政策]] | 从微观审慎(单个机构安全)到宏观审慎(系统性风险);逆周期资本缓冲 | Basel III; 系统性重要金融机构(SIFI) | Ch 20 (隐含) |

### Epilogue: What We Know, What We Don't

| # | 建议页面名 | 核心内容 | 教材位置 |
|---|---|---|---|
| C30 | [[宏观经济学共识与分歧]] | 六大共识+四大分歧;新古典综合vs后凯恩斯vs奥地利;Mankiw的"我们知道了什么"清单 | Epilogue |

**Concept page count estimate:** 25-30 new or significantly expanded concept pages.

---

## §3 Links to Existing Wiki Pages

以下页面将在 Batch 7 生成后被更新或扩展:

1. **[[稳定化政策]]** (Batch 5): Ch 15 提供更深入的政策时滞、自动稳定器、预测困难分析
2. **[[古典消费函数]]** (Batch 2): 需扩展为Keynes消费函数的完整讨论,并与Fisher/Modigliani/Friedman对比
3. **[[实际货币余额与货币需求]]** (Batch 2): 需扩展Baumol-Tobin模型和投资组合理论
4. **[[货币乘数]] / [[量化宽松]] / [[美联储工具]]** (Batch 2): Ch 18-20提供更深层的货币需求/金融危机语境
5. **[[Milton Friedman]]** (已有): 扩展永久收入假说(1957)和消费理论贡献
6. **[[Robert Lucas Jr]]** (已有): 扩展Lucas批判对消费/投资政策评估的含义
7. **[[John Taylor]]** (Batch 6): 扩展Taylor规则在政策规则vs相机抉择辩论中的角色
8. **[[价格灵活性与价格粘性]]** (Batch 1): Ch 19 RBC vs 新凯恩斯直接涉及此核心假设
9. **[[微观基础]]** (Batch 1): Ch 16-19是微观基础的完整展开
10. **[[宏观经济学foundations总览]]**: 更新Part V-VI为"已完成",全书Mankiw摄入完毕
11. **[[Macroeconomics-Mankiw-9e]]**: 更新进度表,全书完成
12. **[[短期经济波动]]**: 扩展Ch 19-20内容,形成全书闭环

---

## §4 Contradictions / Tensions with Existing Wiki Content

### [CONTRADICTION-1] Ricardian等价性的经验失效

Barro (1974)预测减税→储蓄增加→总需求不变。但:
- **2001/2008美国退税**:JPS (2006) 发现退税的MPC高达0.2-0.4(短期),与Ricardian等价矛盾
- ** liquidity-constrained households**: 约1/3美国家庭无法借贷,减税直接增加消费
- ** myopia**: 消费者可能不理解未来税收负担

教材呈现Ricardian等价为"重要理论"但承认"可能不完全成立",未充分讨论经验反驳。

### [CONTRADICTION-2] RBC模型的经验脆弱性

Kydland-Prescott (1982) RBC模型假设:
- **技术冲击驱动波动**: Solow残差作为技术冲击代理,但残差包含测量误差、要素利用变化、需求冲击
- **市场始终出清**: 无法解释失业(模型中无失业概念)
- **无货币效应**: 与大量实证文献矛盾(Bernanke-Blinder 1992等)
- **校准方法的争议**: 不估计而是"校准"参数,逃避统计检验

教材将RBC呈现为"另一种视角",但实际上RBC在2008后已被边缘化。

### [CONTRADICTION-3] 行为经济学在宏观中的边缘化

Ch 16-5引入Laibson式行为消费理论,但:
- **仅限消费**: 投资、货币需求、劳动供给等行为修正缺失
- **无DSGE整合**: 主流新凯恩斯DSGE仍假设完全理性;行为DSGE(Angeletos et al.)未进入教材
- **政策含义未展开**: 若消费者有时间不一致偏好,"助推"(nudge)可能比利率/税收政策更有效——教材未讨论

### [CONTRADICTION-4] 2008危机的教材叙事局限

Ch 20对2008危机的描述:
- **侧重住房泡沫**: 但忽略金融部门结构性问题(影子银行、回购协议市场、CDS)
- **忽略分配维度**: 危机后果(失业、财富损失、不平等加剧)轻描淡写
- **政策评估不完整**: QE的效果(财富不平等加剧)未充分讨论;Dodd-Frank的有效性存疑
- **Minsky视角缺失**: 金融内生不稳定性(投机→庞氏→崩溃)未被系统呈现

### [CONTRADICTION-5] 宏观共识的"虚假中和"

Epilogue声称宏观经济学已达成"广泛共识",但:
- **后凯恩斯主义**: Minsky金融不稳定、Kalecki利润驱动增长完全缺席
- **MMT**: 政府赤字不危险、央行独立性是迷思——与教材根本矛盾
- **生态经济学**: 增长极限、去增长(degrowth)——教材未涉及
- **AI与自动化**: 对就业和增长的长期影响——2016年版完全未预见

---

## §5 Knowledge Gaps (Beyond the Textbook)

1. **异质性代理人模型(HANK)**: 2010s后发展,考虑不同收入/财富群体的差异化消费/储蓄行为,对财政乘数估计产生革命性影响(Kaplan-Moll-Violante 2018)
2. **现代货币理论(MMT)**: Wray/Kelton框架——货币主权政府不受预算约束,通胀是唯一限制。与教材的政府债务可持续性分析直接矛盾。
3. **绿色宏观经济学**: 气候变化作为宏观经济冲击(碳预算、搁浅资产、绿色投资需求)。2016年版完全未涉及。
4. **数字货币与CBDC**: 比特币、稳定币、央行数字货币对货币需求、货币政策传导、银行脱媒的影响。
5. **长期停滞(Secular Stagnation)**: Summers (2013) 提出;r*持续下降导致的货币政策空间枯竭。
6. **不平等与宏观**: Piketty (2014) 财富不平等动态;财富效应对消费的影响;分配对总需求的非线性效应。
7. **中国模式**: 中国宏观政策框架(多目标制、MLF/LPR/存款准备金率工具、政府隐性债务)与教材的美式框架差异巨大。

---

## §6 Bias / Divergence Markers

### [BIAS-1] 消费理论的"美国中产阶级"默认

消费理论以美国中产阶级生命周期(青年借贷→中年储蓄→老年消耗)为默认模型,但:
- **发展中国家**: 信贷市场不发达→无法借贷平滑消费
- **欧洲福利国家**: 养老金替代率高→储蓄动机弱
- **中国**: 高储蓄率(预防性动机、住房购买、教育支出)无法用标准模型解释

### [BIAS-2] RBC vs 新凯恩斯的"虚假对称"

教材将RBC和新凯恩斯并置为"两种互补方法",但:
- **学术影响力**: RBC在2008后急剧衰落;新凯恩斯DSGE dominates央行模型
- **经验支持**: RBC无法解释失业和货币效应;新凯恩斯可以
- **政策相关性**: RBC的政策含义是"政府不应干预";新凯恩斯支持稳定化政策

教材的"对称呈现"掩盖了两者的实际不对等地位。

### [BIAS-3] 2008危机的"技术性"叙事

教材将2008危机呈现为"住房泡沫+金融传染"的技术性问题,但:
- **忽略结构性根源**: 1980s以来金融去监管、收入分配恶化、全球失衡
- **忽略政治经济学**: 金融行业的政治影响力推动去监管
- **忽略跨国差异**: 欧洲主权债务危机、中国4万亿刺激、新兴市场资本流动——教材以美国为中心

### [regional-bias] 金融危机案例的美国中心主义

Ch 20的Case Study几乎全部是美国视角:
- 美国住房泡沫、雷曼兄弟、AIG、TARP
- 欧洲(爱尔兰/西班牙房地产泡沫、希腊主权危机)仅简要提及
- 新兴市场(东亚1997、拉美1980s债务危机)缺失
- 中国(4万亿刺激、地方债平台、影子银行)完全缺席

---

## §7 Estimated Page Generation Load

| 类别 | 数量 | 说明 |
|---|---|---|
| entities/ | 5-6 | Modigliani, Tobin, Bernanke, Kydland, Prescott, possibly Laibson |
| concepts/ | 25-30 | 见 §2 详表 |
| 更新现有页 | 8-10 | Friedman, Keynes, Lucas, Taylor, 稳定化政策, 货币需求, 总览, Macro教材主页, index, state, log |

**总计: ~35 新页面 + 10 更新页面**

---

## §8 Recommended Wikilink Architecture

```
微观基础回填 (Batch 7 主题)
├── Ch 15 稳定化政策
│   ├── 稳定化政策 (扩展)
│   ├── 政府债务与赤字
│   ├── Ricardian等价性
│   └── 政策时滞与预测困难
├── Ch 16 消费理论
│   ├── 消费理论 (主题页)
│   ├── Keynes消费函数 (扩展)
│   ├── Fisher跨期选择模型
│   ├── 生命周期假说 (Modigliani)
│   ├── 永久收入假说 (Friedman)
│   ├── 随机游走假说 (Hall)
│   └── 行为消费理论 (Laibson)
├── Ch 17 投资理论
│   ├── 投资理论 (主题页)
│   ├── 新古典投资模型
│   ├── Tobin q理论
│   ├── 融资约束
│   ├── 住房投资
│   └── 存货投资 (扩展)
├── Ch 18 货币供给与需求
│   ├── 货币需求理论 (扩展)
│   ├── Baumol-Tobin模型
│   ├── 货币需求投资组合理论
│   └── 货币需求的经验证据
├── Ch 19 商业周期理论前沿
│   ├── 实际经济周期模型
│   ├── 新凯恩斯主义模型
│   ├── 规则与相机抉择
│   └── 时间不一致性
└── Ch 20 金融危机
    ├── 金融加速器
    ├── 银行挤兑与存款保险 (扩展)
    ├── 2008金融危机
    └── 宏观审慎政策
```

---

*本分析文件等待用户确认。确认后进入 Stage 2 页面生成。*
