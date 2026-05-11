---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 10", "Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 14-1"]
tags: [concept, macroeconomics, batch5, batch6, core-model]
confidence: medium
decay_category: slow
status: completed
---

# AD-AS模型

The **AD-AS model** (Aggregate Demand–Aggregate Supply model) is the foundational framework for analyzing short-run economic fluctuations. It combines the [[总需求曲线]] (downward-sloping) with the [[总供给曲线]] (upward-sloping in the short run, vertical in the long run) to determine the equilibrium price level and output.

## Model Structure

```
Price Level (P)
    │
    │   LRAS
    │     │
    │     │    SRAS
    │     │     /
    │     │    /
    │     │   /  AD
    │     │  /  /
    │     │ /  /
    │     │/  /
    └─────┼──/──────────→ Output (Y)
          │ /
          Ȳ
```

**Short-run equilibrium**: Intersection of AD and SRAS determines $Y$ and $P$. Output may deviate from potential ($\bar{Y}$).

**Long-run equilibrium**: AD, SRAS, and LRAS all intersect at the same point. $Y = \bar{Y}$ and expectations are fulfilled ($P = P^e$).

## Demand Shocks

A **demand shock** shifts the AD curve. Examples:

**Positive demand shock** (AD shifts right):
- Stock market boom increases consumer wealth
- Government increases defense spending
- Central bank expands money supply
- Foreign economies boom, increasing exports

**Short-run effect**: $Y \uparrow$, $P \uparrow$ — boom with inflation
**Long-run adjustment**: Tight labor market → wages rise → SRAS shifts left → $Y$ returns to $\bar{Y}$, $P$ permanently higher

**Negative demand shock** (AD shifts left):
- 1929 stock market crash
- 2008 financial crisis
- Fiscal austerity

**Short-run effect**: $Y \downarrow$, $P \downarrow$ — recession with deflationary pressure
**Long-run adjustment**: Slack labor market → wages fall (slowly) → SRAS shifts right → $Y$ returns to $\bar{Y}$

## Supply Shocks

A **supply shock** shifts the SRAS (and possibly LRAS). Examples:

**Adverse supply shock** (SRAS shifts left):
- Oil price increase (1973 OPEC embargo, 1979 Iranian revolution)
- Natural disasters destroying capital
- Wage push from unionization

**Effect**: $Y \downarrow$, $P \uparrow$ — **stagflation** (stagnation + inflation)

This combination is particularly painful because stabilization policy faces a dilemma: stimulating AD to raise $Y$ worsens inflation; restricting AD to fight inflation deepens the recession.

**Favorable supply shock** (SRAS shifts right):
- Technological breakthrough (IT revolution 1990s)
- Oil price collapse (1986, 2014)
- Deregulation reducing business costs

**Effect**: $Y \uparrow$, $P \downarrow$ — the ideal scenario of non-inflationary growth

## Stabilization Policy

Policymakers can use **fiscal policy** (shifting AD via $G$ or $T$) and **monetary policy** (shifting AD via $M$) to offset shocks:
- **Counter demand shock**: If AD falls, expand fiscal/monetary policy to shift AD back right
- **Counter supply shock**: No clean solution—facing the stagflation tradeoff

However, stabilization policy faces practical challenges: [[稳定化政策]] discusses recognition lags, decision lags, implementation lags, and the difficulty of forecasting.

## 反面论点与数据空白

### [CONTRADICTION-1] AD-AS作为"教学模型" vs "政策工具"的张力

AD-AS是本科教学的核心模型,但现代央行几乎不使用它:
- **美联储**:决策基于DSGE模型(如FRB/US)、Taylor rule、大量实时数据
- **欧央行**:使用NAWM、双支柱框架
- **中国人民银行**:多目标、多工具的复杂框架

AD-AS的二维简化(P-Y空间)无法捕捉:
- 金融部门的角色
- 预期和前瞻指引
- 多期动态和滞后效应
- 收入分配和不平等

教材将AD-AS呈现为"宏观经济学的主模型",但实际是"教学入门模型",这一差距未向学生说明。

### [CONTRADICTION-2] "长期调整"的速度问题

教材反复说"长期中经济回到LRAS",但:
- **日本**:1990-2020年"失去的二十年",长期低于潜在产出
- **欧元区**:2008后南部成员国持续萧条
- **大萧条**:美国用了10年才回到趋势产出

如果"长期"是10-20年,那么"短期波动"框架本身就是不足的。需要引入滞后效应(hysteresis)概念——短期衰退会永久性地降低潜在产出。

### [CONTRADICTION-3] 忽略分配维度

AD-AS将产出Y作为单一变量,但:
- 同一GDP水平下,收入分配可能截然不同
- 需求冲击对低收入群体的影响远大于高收入群体
- 供给冲击(如能源价格上涨)对穷人的实际收入冲击更大

Stiglitz-Sen-Fitoussi 2009指出,GDP无法捕捉福祉分配,AD-AS继承了这一盲点。

### 数据空白

1. **实时LRAS估计**:我们不知道\bar{Y}的实时值,只能在事后估计——这使得"产出缺口"(Y - \bar{Y})的测度充满争议
2. **自然利率 r* 的估计**:Laubach-Williams (2003) 方法显示r*的估计误差极大,直接影响货币政策立场判断
3. **2008后的"新常态"**:潜在产出增速可能结构性下降(Gordon 2016),LRAS右移速度放缓

## See Also

- [[总需求曲线]] — 需求侧
- [[总供给曲线]] — 供给侧
- [[需求冲击]] — AD曲线的移动
- [[供给冲击]] — AS曲线的移动
- [[稳定化政策]] — 政策应对
- [[IS-LM模型]] — AD-AS的微基础(Ch 12推导)
- [[短期经济波动]] — 本模型的应用场景
- [[总供给的微观基础]] — SRAS向上倾斜的三种理论解释(Ch 14-1)
- [[粘性工资理论]] / [[粘性价格理论]] / [[不完全信息理论]] — 三种微观机制
- [[Phillips曲线]] — SRAS的通胀-失业表达形式(Ch 14-2)
