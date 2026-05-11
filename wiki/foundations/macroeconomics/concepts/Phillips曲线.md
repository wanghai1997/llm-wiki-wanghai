---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 14-2"]
tags: [concept, macroeconomics, batch6, phillips-curve, inflation, unemployment]
confidence: medium
decay_category: medium
status: completed
---

# Phillips曲线

The **Phillips curve** is the empirical and theoretical relationship between inflation and unemployment. It is one of the most consequential concepts in macroeconomics, shaping monetary policy design, central bank mandates, and academic debates for over six decades.

## The Original Phillips Curve (1958)

[[A.W. Phillips]] (1958) discovered a remarkably stable inverse relationship between the rate of change of money wages and unemployment in the United Kingdom (1861–1957):

$$\frac{\Delta W}{W} = f(u), \quad f' < 0$$

Key finding: when unemployment was low, wages rose rapidly; when unemployment was high, wages grew slowly or fell.

The relationship was quickly extended to **price inflation** (assuming constant markups):

$$\pi = f(u), \quad f' < 0$$

## The Keynesian Era: A Stable Tradeoff

In the 1960s, Keynesian economists interpreted the Phillips curve as a **menu of policy choices**:
- Policymakers could choose any point on the curve
- Accept higher inflation for lower unemployment (expansionary policy)
- Or accept higher unemployment for lower inflation (contractionary policy)
- Samuelson and Solow (1960) popularized this interpretation in the US context

This view underpinned the "fine-tuning" approach to demand management in the 1960s.

## The Friedman-Phelps Critique (1968)

[[Milton Friedman]] (1968 AEA presidential address) and [[Edmund Phelps]] (1967–68) independently delivered a devastating critique:

**The natural rate hypothesis**: The tradeoff is only **short-run**. In the long run, the Phillips curve is **vertical** at the natural rate of unemployment ($u^n$).

**The mechanism**:
- Expansionary policy initially raises output and reduces unemployment below $u^n$
- But as workers and firms adjust their expectations, they demand higher wages and prices
- Real wages return to equilibrium; employment falls back to the natural rate
- Result: higher inflation with no permanent reduction in unemployment

**The expectations-augmented Phillips curve**:

$$\pi = \pi^e - \beta(u - u^n)$$

- If $\pi^e$ is fixed (short run): tradeoff exists
- If $\pi^e$ adjusts (long run): $u = u^n$, regardless of $\pi$

## The Rational Expectations Revolution (1970s)

[[Robert Lucas Jr]] (1972) and [[Thomas Sargent]] (1982) delivered an even stronger critique:

- Under **rational expectations**, even the **short-run** tradeoff disappears if policy is **anticipated**
- Only **unanticipated** policy changes can affect real variables
- Systematic demand management is therefore **ineffective**

**Lucas's signal extraction model**: Producers confuse aggregate price changes with relative price changes. But if they rationally anticipate monetary policy, they no longer make this confusion.

**Sargent's "Four Big Inflations"**: Credible regime changes could end hyperinflation without output costs—if expectations adjust rapidly.

## The Modern Phillips Curve: New Keynesian

The Phillips curve was "resurrected" in the 1990s as the **New Keynesian Phillips curve (NKPC)**:

$$\pi_t = \beta E_t\pi_{t+1} + \kappa (y_t - \bar{y}_t) + \varepsilon_t$$

Features:
- **Forward-looking**: Current inflation depends on expected future inflation
- **Microfounded**: Derived from Calvo pricing and firm optimization
- **Output gap-driven**: Inflation rises when the economy is "overheating"
- **Cost-push shocks**: $\varepsilon_t$ captures supply shocks (oil, exchange rates)

This version is the workhorse of modern central bank DSGE models.

## The Phillips Curve "Missing" (2008–2020)

After the 2008 financial crisis, the Phillips curve appeared to break down in advanced economies:
- US unemployment fell from 10% to 3.5% (2010–2019)
- But inflation remained persistently below the 2% target
- Possible explanations:
  - **Globalization**: Cheap imports from China and elsewhere suppressed wage growth
  - **Amazon effect**: Online competition reduced pricing power
  - **Gig economy**: Weak worker bargaining power
  - **Anchored expectations**: Inflation expectations became firmly anchored at 2%
  - **Mismeasurement**: Output gap estimates may have been wrong

## The Phillips Curve Reappears (2021–2022)

During the post-COVID recovery:
- Unemployment fell rapidly
- Inflation surged to 9% in the US, 11% in the Eurozone
- The Phillips curve seemed to steepen again
- But this episode was complicated by:
  - Supply chain disruptions
  - Massive fiscal stimulus
  - Energy price shocks
  - Pent-up demand

Whether the Phillips curve has truly "returned" or whether this was a temporary supply-demand imbalance remains debated.

## 反面论点与数据空白

### [CONTRADICTION-1] Phillips曲线的"死亡"与"复活":教材叙事张力

Ch 14-2呈现Phillips曲线从"经验规律→被Friedman-Phelps证伪→被Lucas理性预期消解→以新凯恩斯主义形式复活"的谱系。但教材未明确回答:**Phillips曲线在现代央行决策中究竟是什么地位?**
- 美联储明确使用"产出缺口-通胀"关系(本质就是Phillips曲线)进行政策评估
- 但新凯恩斯DSGE中的Phillips曲线是结构方程(由厂商最优化推导),而非历史经验关系
- 2008后Phillips曲线"失踪"(低失业未引发高通胀)使原始经验版本再度受质疑

教材将Phillips曲线呈现为"已被理性预期超越"的教学工具,但现代央行从未放弃使用它。

### [CONTRADICTION-2] "大缓和"(Great Moderation)的教材叙事

教材将1990s-2000s的低波动归功于"更好的货币政策"(基于Taylor规则和通胀目标)。但:
- **好运气假说** (Stock-Watson 2002):波动下降主要归因于更小的冲击,而非政策改善
- **金融泡沫积累**:大缓和期间积累的巨大金融风险在2008爆发,说明低波动不等于低风险
- **全球储蓄过剩** (Bernanke 2005):外部因素压制利率和通胀,与货币政策无关

教材选择性呈现"货币政策成功"叙事,忽略结构性因素。

### [CONTRADICTION-3] 牺牲率估计的美国中心主义

教材的牺牲率估计几乎全部来自美国经验。但:
- 欧洲反通胀(如德国1980s)的牺牲率可能更高
- 新兴市场反通胀往往伴随剧烈社会动荡
- 日本"失去的三十年"显示,试图降低低通胀的"代价"可能是长期停滞

### 数据空白

1. **NKPC vs 传统Phillips曲线**:现代央行模型使用NKPC,但教材仍主要讲授适应性预期版本
2. **Phillips曲线的平坦化**:2008-2020年的"失踪"尚无定论——是数据问题、模型问题还是结构性变化?
3. **中国的Phillips曲线**:CPI通胀与城镇失业率关系微弱,标准Phillips曲线不适用
4. **平均通胀目标制(AIT)**:Powell 2020年引入的新框架允许通胀暂时超调——挑战传统对称性假设

## See Also

- [[自然率假说]] — Friedman-Phelps对原始Phillips曲线的修正
- [[适应性预期]] — 短期Phillips曲线的维持机制
- [[理性预期]] — Lucas对Phillips曲线的消解
- [[牺牲率]] — 降低通胀的产出代价
- [[滞后效应]] — 短期失业可能永久改变自然率
- [[A.W. Phillips]] — 原始发现者
- [[Milton Friedman]] / [[Edmund Phelps]] — 自然率假说
- [[Robert Lucas Jr]] / [[Thomas Sargent]] — 理性预期革命
- [[总供给的微观基础]] — Phillips曲线的现代微基础
