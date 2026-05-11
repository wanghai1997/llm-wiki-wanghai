---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [人物, 经济学家, 数学家, 微观经济学, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Harold Hotelling（1895–1973）

## 简介

美国数理经济学家、统计学家。普林斯顿数学博士（1924），先后任教 Stanford、Columbia、University of North Carolina。横跨数理统计与微观经济学两域，既是 [[Hotelling引理]] 的提出者，也奠基了多元统计中的 Hotelling T² 与主成分分析。

## 在 Nechyba 中的引用脉络

Nechyba 在 Ch 12B "Duality in Producer Theory"（pp. 399 起）与 Ch 13B 显式致敬 Hotelling，作为 [[厂商对偶性]] 的另一支柱（与 Batch 1 的 [[Shephard引理]] / [[Roy恒等式]] 并列）。

## 核心贡献（与本 Wiki 相关）

| 年份 | 贡献 | 本 Wiki 对应页 |
|---|---|---|
| 1929 | "Stability in Competition"——空间区位选择模型（海滩冰淇淋摊问题），后衍生出中位选民定理 | 留待 Batch 5 Ch 28（[[政治经济学]]）|
| 1931 | "The Economics of Exhaustible Resources"——Hotelling 规则：可耗竭资源价格沿利率增长 | 留待未来资源经济学摄入 |
| 1932 | "Edgeworth's Taxation Paradox and the Nature of Demand and Supply Functions"——Hotelling 引理 | [[Hotelling引理]] |
| 1933 | "Analysis of a Complex of Statistical Variables into Principal Components" | 不在本 Wiki 微观范围 |
| 1947 | Hotelling T² 检验 | 不在本 Wiki 微观范围 |

## Hotelling 引理（口语版）

> "对利润函数关于价格求偏导，得到输出供给；关于工资求偏导，得到劳动需求的负值。"
>
> 形式化：$\frac{\partial \pi^*(p,w,r)}{\partial p} = x^*(p,w,r)$；$\frac{\partial \pi^*(p,w,r)}{\partial w} = -L^*(p,w,r)$。

由 [[包络定理]] 直接证明——见 [[Hotelling引理]] 详情页。

## 与同代经济学家的关系

- **与 [[John Hicks]]**：Hicks 1939 *Value and Capital* 在福利测度框架上扩展 Hotelling 1932 的思想。
- **与 [[Eugen Slutsky]]**：消费者侧 [[Slutsky方程]] 与生产者侧 Hotelling 引理共享"包络定理"基底，但 Slutsky（1915）与 Hotelling（1932）并未直接互引。
- **与 [[Ronald Shephard]]**：Shephard 1953 引理是 Hotelling 1932 思路在成本函数侧的镜像；二者通常成对教学。

## 反面论点与数据空白

- **引理失效条件**：要求生产集**凸**且 PMP 有**内点最优解**——角点解（关闭、零投入）下 Hotelling 引理不直接适用，须改用 Clarke 次梯度或 KKT 条件。Nechyba 不展开非光滑分析。
- **空间竞争模型的实证**：1929 年海滩模型预言"两家厂商都聚集在中点"，但现实的零售选址（沃尔玛 vs Costco）受人口密度、土地价格、成本曲线异质性主导，原始模型不直接适用。Hotelling 本人在 1937 年承认模型对"均衡稳定性"有过度乐观估计。
- **可耗竭资源 Hotelling 规则**：实证中油价并不严格沿利率增长（开采成本下降、替代品出现、需求弹性变化）；DasGupta-Heal 1979 给出更复杂的修正。本 Wiki 暂不展开。

## 相关页

- [[Hotelling引理]] / [[包络定理]] / [[厂商对偶性]] / [[利润函数]]
- 同代人物：[[John Hicks]] / [[Eugen Slutsky]] / [[Ronald Shephard]] / [[René Roy]]
- 教材：[[Microeconomics-Nechyba-2e]]
- 主题：[[厂商最优化选择]]
