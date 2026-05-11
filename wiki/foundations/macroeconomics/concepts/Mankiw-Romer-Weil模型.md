---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 9-2 隐含"]
tags: [concept, macroeconomics, batch4, growth]
confidence: medium
decay_category: medium
status: completed
---

# Mankiw-Romer-Weil模型

The **Mankiw-Romer-Weil (MRW) model** (1992) extends the [[Solow增长模型]] by adding **human capital** as a third factor of production. It is arguably the most influential empirical growth paper of the 1990s, demonstrating that an augmented Solow framework can explain roughly 80% of cross-country income variation and successfully predicts **conditional convergence**.

## The Augmented Production Function

MRW specify a Cobb-Douglas production function with three inputs:

$$Y = K^{\alpha} H^{\beta} (AL)^{1-\alpha-\beta}$$

where:
- $K$ = physical capital
- $H$ = human capital
- $L$ = raw labor
- $A$ = technology (labor-augmenting, growing at rate $g$)

Human capital is accumulated analogously to physical capital:
$$\dot{H} = s_h Y - \delta H$$

where $s_h$ is the fraction of output devoted to human capital accumulation (proxied by school enrollment rates).

## Key Results

### 1. Explaining Cross-Country Income Differences

In steady state, output per effective worker is:

$$\ln(\tilde{y}^*) = \frac{\alpha}{1-\alpha-\beta} \ln(s_k) + \frac{\beta}{1-\alpha-\beta} \ln(s_h) - \frac{\alpha+\beta}{1-\alpha-\beta} \ln(n + g + \delta)$$

MRW estimate this equation using cross-country data:
- **Without human capital**: The basic Solow model explains ~60% of income variation; estimated $\alpha \approx 0.60$ (too high relative to factor share evidence)
- **With human capital**: The augmented model explains ~80% of income variation; estimated $\alpha \approx 0.30$, $\beta \approx 0.50$ (consistent with micro evidence on capital and schooling returns)

### 2. Restoring Conditional Convergence

The augmented model predicts that countries converge to their own steady states at rate:

$$\lambda = (1-\alpha-\beta)(n + g + \delta)$$

With $\alpha + \beta \approx 0.80$, the implied convergence speed is roughly **2% per year**—matching observed patterns.

The basic Solow model (without human capital) implies faster convergence (~4–5% per year), which is rejected by the data. Adding human capital slows predicted convergence because human capital accumulation takes time.

### 3. The Role of Human Capital

MRW find that human capital is quantitatively important:
- Differences in schooling explain a substantial portion of cross-country income differences
- Countries that invest heavily in education (East Asia) tend to have higher steady-state incomes
- Human capital acts as a "complement" to physical capital: educated workers are more effective at using physical capital

## Empirical Specification

MRW estimate:

$$\ln(Y_i/L_i) = a + b_1 \ln(s_{k,i}) + b_2 \ln(s_{h,i}) + b_3 \ln(n_i + g + \delta) + \epsilon_i$$

Using:
- $s_k$ = investment/GDP ratio (physical capital investment)
- $s_h$ = secondary school enrollment rate (human capital investment proxy)
- $n$ = population growth rate
- $g + \delta$ = assumed constant at 0.05

## Critiques and Extensions

### 1. Measurement of Human Capital

MRW proxy human capital by school enrollment, which is imperfect:
- Does not capture **quality** of schooling (teacher quality, curriculum, learning outcomes)
- Does not capture **on-the-job training** or informal learning
- Does not capture **health** as a component of human capital

Subsequent work (e.g., Hanushek-Woessmann) shows that **test scores** (PISA, TIMSS) predict growth better than years of schooling.

### 2. Endogeneity of Investment Rates

Countries with good institutions may both invest more and grow faster, causing omitted variable bias. Instrumental variable strategies (e.g., using colonial history, geographic variables) partially address this but remain contested.

### 3. TFP Still Matters

Even the augmented Solow model leaves ~20% of income variation unexplained. This residual is likely related to TFP differences driven by institutions, geography, and policy—leading to the [[要素积累vs生产效率]] debate.

## In Mankiw's Textbook

The textbook draws heavily on the MRW framework in Ch 9-2's empirical discussion:
- The conditional convergence result
- The role of human capital in explaining cross-country differences
- The regression evidence on savings, population growth, and schooling

However, the textbook does not prominently credit Weil as a coauthor, nor does it discuss the paper's methodological innovations and limitations.

## 反面论点与数据空白

### [CONTRADICTION] 人力资本测度的粗糙性
教材呈现 MRW 结果时，将学校入学率作为人力资本的可靠代理。但 Hanushek-Woessmann (2008, 2012) 的开创性研究表明：
- **教育质量**（认知技能测试分数）比**教育数量**（入学年限）更能预测经济增长
- 许多国家（尤其是发展中国家）存在严重的"学习危机"：学生上学多年却未获得基本识字算数能力
- MRW 的 $s_h$ 代理变量可能高估了部分国家的人力资本，低估了另一些国家

### [regional-bias] 回归框架的隐含假设
MRW 的跨国家回归假设所有国家共享相同的生产函数参数（$\alpha$, $\beta$）。但：
- 发展中国家可能因技术采用滞后而有不同的有效 $\alpha$
- 制度差异可能改变生产函数的函数形式
- 将不同制度 regime（民主 vs 专制、市场 vs 计划）的国家放在同一回归中，假设它们共享相同的 steady-state 结构，是一种强假设

### 数据空白
- **微观-宏观张力**：微观研究（Mincer 回归）估计教育回报率为 8–10%，但 MRW 的宏观估计暗示更高的教育贡献。这种"微观-宏观张力"未在教材中讨论
- **无形资本**：MRW 框架只包含物质和人力资本。现代经济中，无形资本（R&D、软件、组织资本）可能同样重要，甚至更重要 (Corrado-Hulten 2010)
- **中国经验**：中国的高储蓄+高投资+人口红利在 MRW 框架中可部分解释，但其制度因素（地方政府竞争、土地财政）完全超出模型范围

## See Also

- [[N. Gregory Mankiw]] / [[Paul Romer]] / [[David Weil]] — Model originators
- [[Solow增长模型]] — Base model that MRW extends
- [[收敛假说]] — Conditional convergence prediction and evidence
- [[要素积累vs生产效率]] — Decomposition of income differences
- [[增长核算与TFP]] — Growth accounting including human capital
- [[促进增长的政策]] — Policy implications of human capital accumulation
