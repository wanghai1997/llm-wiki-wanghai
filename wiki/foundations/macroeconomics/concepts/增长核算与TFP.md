---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 9-2 隐含"]
tags: [concept, macroeconomics, batch4, growth]
confidence: medium
decay_category: medium
status: completed
---

# 增长核算与TFP

**Growth accounting** is the empirical framework—pioneered by [[Robert Solow]] (1957) and anticipated by [[Moses Abramovitz]] (1956)—for decomposing observed output growth into contributions from measurable input growth and a residual term representing technological progress and other unexplained factors. The residual is called **total factor productivity (TFP)** or the "Solow residual."

## The Growth Accounting Equation

For a general production function $Y = F(K, L, A)$ where $A$ represents technology:

$$\frac{\Delta Y}{Y} = \alpha_K \frac{\Delta K}{K} + \alpha_L \frac{\Delta L}{L} + \frac{\Delta A}{A}$$

where:
- $\alpha_K = (\partial F/\partial K)(K/Y)$ = elasticity of output with respect to capital (= capital share under perfect competition)
- $\alpha_L = (\partial F/\partial L)(L/Y)$ = elasticity of output with respect to labor (= labor share)
- $\Delta A/A$ = TFP growth (the "residual")

For a Cobb-Douglas production function $Y = AK^{\alpha}L^{1-\alpha}$:

$$\frac{\Delta Y}{Y} = \alpha \frac{\Delta K}{K} + (1-\alpha) \frac{\Delta L}{L} + \frac{\Delta A}{A}$$

### Interpreting TFP

TFP growth captures everything that raises output without increasing measured inputs:
- **True technological progress**: New inventions, better processes
- **Human capital improvements**: Education, skills (if not separately measured)
- **Resource reallocation**: Labor/capital moving from low-productivity to high-productivity uses
- **Economies of scale**: Efficiency gains from larger scale
- **Institutional improvements**: Better property rights, reduced corruption
- **Measurement error**: Mismeasured capital or labor quality

Abramovitz (1956) famously called TFP **"a measure of our ignorance"**—the larger the residual, the more we don't understand about growth's true sources.

## Growth Accounting in Practice

### US Postwar Growth (Example)

| Period | Output Growth | Capital Contribution | Labor Contribution | TFP Growth |
|---|---|---|---|---|
| 1948–1973 | 3.5% | 1.0% | 1.0% | 1.5% |
| 1973–1995 | 2.4% | 0.9% | 1.1% | 0.4% |
| 1995–2005 | 3.2% | 1.0% | 0.7% | 1.5% |
| 2005–2019 | 1.7% | 0.7% | 0.5% | 0.5% |

**Key observations**:
- The 1973–95 "productivity slowdown": TFP growth fell by ~1 percentage point
- The 1995–2005 "New Economy" revival: IT-driven TFP acceleration
- The post-2005 "secular stagnation": TFP growth again fell to ~0.5%

### Cross-Country Decomposition

Growth accounting has been applied extensively to explain cross-country income differences. The key finding: **TFP differences, not factor accumulation differences, explain most of the variation in income per capita across countries**.

For example, Hall and Jones (1999) and Klenow and Rodríguez-Clare (1997) found that:
- Differences in physical and human capital per worker explain roughly 1/3 of cross-country income variation
- Differences in TFP explain roughly 2/3

This result is central to the [[要素积累vs生产效率]] debate.

## The East Asian Miracle Decomposition

[[Alwyn Young]] (1992, 1995) applied rigorous growth accounting to the fast-growing East Asian economies:

| Economy | Output Growth | Capital Deepening | Labor Growth | TFP Growth |
|---|---|---|---|---|
| Singapore | 8.7% | 5.5% | 3.4% | ~0% |
| Hong Kong | 7.8% | 3.7% | 3.3% | 0.8% |
| Taiwan | 8.0% | 4.3% | 2.7% | 1.0% |
| South Korea | 9.3% | 4.5% | 3.2% | 1.6% |

Young's finding that TFP growth was modest—especially in Singapore—sparked the debate about whether the "East Asian miracle" was sustainable (see [[Alwyn Young]] and [[要素积累vs生产效率]]).

## Limitations of Growth Accounting

1. **TFP is a residual, not a causal factor**: It measures correlation, not causation. A country with good institutions may have high TFP, but growth accounting does not prove institutions cause growth.

2. **Input quality matters**: Standard growth accounting uses raw labor hours and physical capital stock. Adjusting for education, health, capital utilization, and capital composition (computers vs structures) significantly changes the decomposition.

3. **Endogeneity of inputs**: Firms choose $K$ and $L$ in response to technology shocks, so the "contribution" of capital may partly reflect reverse causality.

4. **Externalities are missed**: Knowledge spillovers, agglomeration effects, and network externalities raise output but are not captured in measured TFP.

## 反面论点与数据空白

### [CONTRADICTION] TFP = "无知度量" vs "效率度量"
教材将 TFP 呈现为"生产效率"的代理变量，暗示高 TFP 国家"使用资本更高效"。但 Abramovitz 的原意是相反：TFP 是**我们无法解释的部分**。将 TFP 重新包装为 "efficiency" 是一种概念偷换，掩盖了增长来源的不确定性。

### [regional-bias] 东亚奇迹的轻描淡写
教材 Ch 9-2 将 Young-Krugman 关于东亚增长可持续性的 debate 轻描淡写为 "recent studies have found that international variation in standards of living is attributable to a combination of capital accumulation and the efficiency with which capital is used"。这一表述：
- 回避了 debate 的政策含义（东亚模式是否可持续）
- 未提及 Young 的 TFP 估计对新加坡等国的严厉结论
- 将复杂的实证争议简化为"两者都重要"的模糊结论

### [BIAS] TFP 作为万能解释变量
教材频繁使用"TFP/效率"解释跨国收入差异，但不解释 TFP 本身由什么决定。这种处理方式将制度、地理、历史等深层因素压缩为一个黑箱残差，然后把这个黑箱当作解释变量使用。

### 数据空白
- **2010s 生产率减速**：教材 2016 年版无法涵盖 2008 危机后发达经济体 TFP 的持续放缓。Robert Gordon (*The Rise and Fall of American Growth* 2016) 认为美国 TFP 减速是结构性的，而非周期性
- **AI 与增长核算**：AI 作为通用目的技术（GPT）是否已进入生产函数？Brynjolfsson 等提出 "GDP-B" 框架，试图捕捉免费数字服务的价值。标准增长核算可能系统性地低估数字经济的贡献
- **气候变化与 TFP**：极端天气事件、资源枯竭可能以 TFP 下降的形式表现，但标准框架不区分"技术退步"和"环境约束收紧"

## See Also

- [[Robert Solow]] / [[Moses Abramovitz]] — Pioneers of growth accounting
- [[要素积累vs生产效率]] — Decomposition of cross-country income differences
- [[Alwyn Young]] — East Asian growth accounting
- [[Mankiw-Romer-Weil模型]] — Adding human capital to reduce the "ignorance" residual
- [[Solow增长模型]] — Theoretical framework underlying growth accounting
- [[管理实践与生产率]] — Management quality as a specific TFP determinant
