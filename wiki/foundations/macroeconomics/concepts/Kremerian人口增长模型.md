---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw), Ch 8-3"]
tags: [concept, macroeconomics, batch4, growth]
confidence: medium
decay_category: medium
status: completed
---

# Kremerian人口增长模型

The **Kremerian model** (Kremer 1993) proposes that **population size drives technological progress**, creating a positive feedback loop between population and economic growth. It stands in direct contrast to both the [[Solow增长模型]] (where higher population growth lowers per-capita income) and the [[Malthusian增长模型]] (where population growth keeps income at subsistence).

## Core Mechanism

Kremer's model rests on two key assumptions:

### Assumption 1: Population Drives Innovation

The rate of technological progress is proportional to population:

$$\dot{A}/A = g(L) = g_0 L$$

where $A$ is the stock of technology/ideas and $L$ is population.

**Intuition**: More people means more potential innovators, researchers, and problem-solvers. Ideas are nonrival—once created, they benefit everyone—so a larger population generates more ideas per capita.

### Assumption 2: Technology Raises Carrying Capacity

Better technology (agriculture, medicine, public health, economic organization) raises the maximum population that can be sustained at subsistence:

$$L_{max} = f(A)$$

where $f'(A) > 0$.

### The Positive Feedback Loop

These two assumptions create a self-reinforcing dynamic:

$$L \uparrow \Rightarrow \dot{A}/A \uparrow \Rightarrow A \uparrow \Rightarrow L_{max} \uparrow \Rightarrow L \uparrow$$

Larger population → faster innovation → higher carrying capacity → larger population.

## Historical Evidence

Kremer tests the model using data from 1 million B.C. to 1990:

### Prediction: Population Growth Should Accelerate Over Time

If $\dot{A}/A \propto L$, then as world population grows, the rate of technological progress accelerates, which in turn allows faster population growth. Over the very long run, both population and its growth rate should increase.

**Empirical fit**:
- For most of human history, world population grew extremely slowly (~0.001% per year)
- Around 10,000 B.C. (agricultural revolution), growth accelerated modestly
- Around 1800 (industrial revolution), growth accelerated dramatically
- In the 20th century, world population growth reached ~1.5% per year
- The *rate* of population growth itself has been increasing over time

### The "Empty Planet" Counterfactual

Kremer notes that regions with larger populations (Eurasia-Africa) developed more advanced technologies than isolated regions with small populations (Australia, Tasmania, pre-Columbian Americas). This is consistent with the scale effect: more people → more ideas.

## Contrast with Competing Models

| Model | Population→Growth | Core Mechanism | Historical Domain |
|---|---|---|---|
| **Malthus** | Negative | Population absorbs surplus | Pre-industrial agrarian |
| **Solow** | Negative (higher $n$ lowers $k^*$) | Capital dilution | Industrial with exogenous tech |
| **Kremer** | Positive | Scale effects in innovation | Very long run; global scale |

## Modern Relevance and Limitations

### Where Kremerian Logic Applies Today

1. **Innovation clusters**: Silicon Valley, Shenzhen, Boston-Cambridge benefit from dense concentrations of talent—scale effects in localized innovation
2. **Global R&D**: The total stock of scientists and engineers worldwide is a key input to global technological progress
3. **Urbanization**: Cities generate agglomeration effects that accelerate idea production (Glaeser 2011)

### Limitations and Critiques

1. **"Race to the bottom" on scale effects**: Jones (1995) showed that if R&D productivity depends on the *stock* of ideas ("fishing out" effect), then population growth need not accelerate innovation. In the "semi-endogenous growth" framework, long-run growth depends on the growth rate of population, not its level.

2. **Quality vs quantity**: Modern fertility decline suggests that human capital per person (education, skills) matters more than raw numbers. The transition from "more people" to "better-educated people" as the driver of innovation is not captured in the basic Kremer model.

3. **Institutional prerequisites**: Scale effects only operate if institutions permit free exchange of ideas. A large population under authoritarian control may not generate proportionally more innovation.

## In Mankiw's Textbook

Mankiw Ch 8-3 presents Kremer as a third "perspective" on population and growth, alongside Solow and Malthus. The textbook emphasizes Kremer's historical evidence but does not:
- Explain the model's modern limitations (Jones 1995 critique)
- Delineate when Kremerian vs Solowian logic applies
- Address the policy implications (should countries encourage larger populations?)

## 反面论点与数据空白

### [CONTRADICTION-2] 三种模型边界未标注
教材将 Kremer、Solow、Malthus 并置在同一节，却不明确各自的适用边界。Kremer 描述的是百万年级别的全球长期趋势；Solow 描述的是工业经济体的中期资本积累；Malthus 描述的是前工业时代的农业社会。三者不是对同一现象的竞争性解释，而是不同时间尺度和制度环境下的不同 regime。

### [BIAS] "人口=进步"的简化叙事
Kremer 模型暗示更大的人口总是更好（更多创新者）。但：
- 非洲人口增长并未自动转化为快速技术进步（制度约束）
- 中国的人口规模优势在计划经济时期被制度压抑，1978年后才释放
- 人口质量（教育、健康）可能比数量更重要（Becker 的人力资本理论）

### 数据空白
- **Jones (1995) 半内生增长**：Jones 的 "R&D-based models of economic growth" 修正了 Kremer 的 scale effect，提出长期增长率取决于人口增长率而非人口水平。教材未涉及这一重要修正
- **人口转型与增长**：全球生育率下降（UN 预测 2100 年世界人口达峰后下降）对 Kremerian 机制的挑战：如果全球人口最终萎缩，技术进步是否会停滞？
- **AI 与自动化**：如果 AI 可以替代人类创新者，人口规模对创新的重要性可能下降。这一前沿议题完全超出教材范围

## See Also

- [[Michael Kremer]] — Model originator
- [[人口增长与索洛模型]] — Three-way comparison of population-growth theories
- [[Malthusian增长模型]] — Opposing view: population growth keeps income at subsistence
- [[Solow增长模型]] — Standard view: population growth dilutes capital
- [[内生增长理论]] — Modern frameworks for endogenous technological progress
