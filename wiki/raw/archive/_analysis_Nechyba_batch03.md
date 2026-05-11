---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [analysis, ingest, nechyba, batch3]
status: draft
---

# Batch 3 摄入分析 — Nechyba 微观经济学 Part 3（Ch 14-17）

> **Stage 1 产物**。本文给出 Batch 3 计划摄入的范围 / 概念清单 / 跨域链接 / 决策点；**不**写入正式 wiki/，等用户回复"继续 / 跳过 / 修改"后进入 Stage 2。
> 模板沿用 [[_analysis_Nechyba_batch02|Batch 2 分析文档]]§0–§10 结构,确保用户验收语境一致。

## 0. 范围与首要决策

### 0.1 [范围确认] Batch 3 = Ch 14-17（完整 Part 3，**4 章**）

用户在选项中写"Ch 14-16(竞争性市场均衡 / 部分均衡 / 国际贸易)",这是 6-batch 计划的最初框架。但 Batch 2 §0.1 [CORRECTION] 已经对照 PDF 实际目录纠正过：

| Part | 实际章数 | 主题 | Batch |
|---|---|---|---|
| 3 | **Ch 14-17（4 章）** | Competitive Markets and the "Invisible Hand" | **本批** |
| 4 | Ch 18-22（5 章） | Distortions / Externalities / Asymmetric Info | 4 |
| 5 | Ch 23-28（6 章） | Imperfect Competition / Game Theory | 5 |
| 6 | Ch 29-30（2 章） | General Equilibrium 进阶 / Political Economy | 6 |

实际 Part 3 = Ch 14–17：
- Ch 14：Competitive Market Equilibrium（短期/长期；进入退出）
- Ch 15：The "Invisible Hand" and the First Welfare Theorem（部分均衡 / 税 / 价格管制 / 国际贸易）
- Ch 16：General Equilibrium（Edgeworth Box / Walras / 福利定理 / Robinson Crusoe）
- Ch 17：Choice and Markets in the Presence of Risk（状态相依商品 / 期望效用 / 保险均衡）

**首要决策点**：将 Batch 3 范围确认为 **Ch 14-17（推荐）** 还是收回 **Ch 14-16**（把 Ch 17 推迟到 Batch 4 与 Ch 18-22 一起）？详见 §9 决策点 1。

### 0.2 与 Batch 1-2 的位置关系

```
                      Batch 3 = 汇合点
       ┌─────────────────────┴─────────────────────┐
       ↓                                            ↓
   消费者侧（B1 Ch 1-10）                         厂商侧（B2 Ch 11-13）
   Marshallian/Hicksian 需求                      条件投入需求 / 供给曲线
   消费者剩余 CS                                  生产者剩余 PS
       │                                            │
       └────────────→ 市场需求 + 市场供给 ←────────┘
                            ↓
              Ch 14：均衡（SR / LR / 进入退出 / 零利润）
                            ↓
              Ch 15：第一福利定理（部分均衡）
                            ↓
              Ch 16：一般均衡（Edgeworth + Walras + Robinson Crusoe）
                            ↓
              Ch 17：风险与状态相依商品（保险均衡）
```

Batch 3 的角色：把 B1 + B2 工具集**汇总**为均衡分析,并把单一商品市场的福利定理推广到一般均衡 + 风险情境。

## 1. 核心实体（Stage 2 拟建的人物 / 案例页）

### 1.1 历史人物（教材显式致敬）

教材明确提到生卒年与贡献的历史人物——本 Wiki 为他们建立独立实体页：

| 人物 | 生卒 | 贡献 | 教材位置 | 拟建页位置 |
|---|---|---|---|---|
| [[Léon Walras]] | 1834-1910（**注**：教材写"1934-1910"显然为笔误,应为 1834-1910） | Walras 定律；一般均衡理论之父 | 16B 脚注 8 | `entities/` |
| [[Vilfredo Pareto]] | 1848-1923 | 帕累托效率；福利经济学奠基者之一 | Ch 16 全章使用"Pareto efficient" | `entities/` |
| [[Francis Edgeworth]] | 1845-1926 | Edgeworth Box（1881 *Mathematical Psychics*） | Ch 16 全章 | `entities/` |
| [[John von Neumann]] | 1903-1957 | vN-M 期望效用（1944 *Games and Economic Behavior*） | 17B 脚注 5 | `entities/` |
| [[Oskar Morgenstern]] | 1902-1977 | 同上,vN-M 合著者 | 17B 脚注 5 | `entities/` |

**待用户决策**：是否给 5 人**全部**建独立页,还是合并 vN-M 为一页 / 暂不建 Edgeworth?见 §9 决策点 5。

**默认推荐**：5 人**全部**独立建页（与 Batch 1 的 6 人独立 + Batch 2 的 1 人独立保持口径一致）。

### 1.2 案例页

Ch 14-17 不增加新的"企业 / 机构"案例（不像 Batch 1-2 涉及具体公司）;教材的例子（Robinson Crusoe / 我和我妻子的橘子-香蕉交易 / 我妻子的人寿保险）是**抽象模型**而非真实主体。

## 2. 核心概念（按章节列出）

> 所有概念页位于 `wiki/foundations/microeconomics/concepts/`。`tags: [concept, microeconomics, foundations, batch3]`,`status: foundation`（教材政策示例若涉及具体国别 → `draft` + `regional-bias`）。

### 2.1 Ch 14 概念（市场均衡，预计 8 页）

- [[市场需求曲线]]（个体 Marshallian 需求水平加总;接续 [[Marshallian需求曲线]]）
- [[市场供给曲线]]（个体厂商 [[输出供给曲线]] 水平加总;接续 [[输出供给曲线]]）
- [[短期均衡]]（市场需求 = 市场供给,固定厂商数）
- [[长期均衡]]（自由进入退出 → 零经济利润）
- [[自由进入退出]]（LR 调整机制）
- [[长期零利润条件]]（$\pi^* = 0$；$p = \min LAC$）
- [[长期供给曲线]]（行业 LR 供给:常数成本 / 递增成本 / 递减成本三种行业类型）
- [[完全竞争行业类型]]（constant-cost / increasing-cost / decreasing-cost industry）

### 2.2 Ch 15 概念（部分均衡福利分析,预计 9 页）

- [[第一福利定理-部分均衡]]（图形 + 直觉版,严格版留 Ch 16）
- [[社会剩余]] = CS + PS（接续 [[消费者剩余]] + [[生产者剩余]]）
- [[价格上限]]（rent control / shortage / DWL）
- [[价格下限]]（minimum wage / surplus / DWL）
- [[税收归宿]]（statutory vs economic incidence;弹性规则）
- [[贸易税与配额]]（关税 / 配额 / 出口补贴的福利损失）
- [[国际贸易福利]]（生产者 vs 消费者赢家输家;开放经济下的 CS+PS）
- [[小国-大国贸易模型]]（terms of trade 内生 vs 外生）
- [[市场扭曲下的福利损失公式]]（DWL ≈ ½ × Δp × Δq;接续 [[DWL几何增长]]）

### 2.3 Ch 16 概念（一般均衡,预计 11 页）

- [[Edgeworth盒]]（2×2 交换经济的几何表示）
- [[互惠交易集MB]]（mutually beneficial trades；reservation utility）
- [[契约曲线]]（Pareto efficient set PE,MRS 相等的轨迹）
- [[核Core]]（Core = MB ∩ PE 在 2 人下;一般 N 人定义为"无联盟可阻断"）
- [[阻断联盟]]（blocking coalition,核的对偶定义）
- [[核收敛定理]]（Core Convergence:经济变大 → 核收敛到竞争均衡集;Edgeworth-Debreu-Scarf）
- [[一般均衡-Walras版]]（GE = 价格集 + 配置;每人优化 + 各市场出清）
- [[Walras定律]]（M-1 个市场出清 → 第 M 个自动出清;同次 0 度需求函数）
- [[第一福利定理]]（GE → Pareto efficient;反证法）
- [[第二福利定理]]（任意 PE 配置可作为某禀赋下的 GE 支撑;需要凸偏好）
- [[Robinson Crusoe经济]]（一人生产-消费经济:厂商 PMP + 消费者 UMP 解 = 计划者最优解）

### 2.4 Ch 17 概念（风险与状态相依商品,预计 12 页）

- [[状态相依商品]]（state-contingent good $x_s$;Arrow-Debreu 商品的雏形）
- [[期望效用函数]]（expected utility $U(x_G, x_B) = \delta u(x_B) + (1-\delta) u(x_G)$）
- [[vN-M期望效用]]（von Neumann-Morgenstern;独立性公理）
- [[独立性公理]]（Independence Axiom;附录 1 详细;Allais 悖论标注）
- [[风险厌恶]]（risk aversion;$u(E(x)) > E(u(x))$）
- [[u(x)凹性]]（concavity ↔ risk aversion;Jensen 不等式）
- [[确定性等价]]（certainty equivalent $x_{ce}$;$u(x_{ce}) = E(u(x))$）
- [[风险溢价]]（risk premium $RP = E(x) - x_{ce}$）
- [[精算公平保险]]（actuarially fair insurance；$b = p/\delta$）
- [[完全保险]]（full insurance;状态独立偏好下的最优）
- [[状态相依偏好]]（state-dependent preferences;过度保险 vs 保险不足）
- [[一般均衡-风险版]]（state-contingent 商品市场的 GE;个体风险 vs 总体风险 / 信念差异）

### 2.5 概念总数

| 章 | 概念数 | 累计 |
|---|---|---|
| Ch 14 | 8 | 8 |
| Ch 15 | 9 | 17 |
| Ch 16 | 11 | 28 |
| Ch 17 | 12 | 40 |
| **合计** | **40** | — |

加上 5 个人物实体 + 1-3 个主题页 + 镜像页扩展 + 跨域 see-also + 索引/状态/教材主页/log → 预计 **55-65 个页面变动**（与 Batch 1 的 61、Batch 2 的 35 量级一致）。

## 3. 链接点（Stage 2 拟建的跨页链接）

### 3.1 镜像页扩展（在 Batch 1-2 既有页上追加新段）

> 与 Batch 2 的"生产侧镜像"段平行：在已有概念页上追加"市场均衡 / 一般均衡 / 风险情境"扩展。

| 既有页 | 拟追加段 | 新内容核心 |
|---|---|---|
| [[消费者剩余]] | "市场均衡聚合" | CS 在市场需求曲线下的几何;Ch 15 福利公式 |
| [[生产者剩余]] | "市场均衡聚合" | PS 在市场供给曲线下的几何;LR 自由进入下 PS 退化 |
| [[消费者对偶性]] | "状态相依扩展" | $x_s$ 视角下,Marshallian/Hicksian 镜像继续成立 |
| [[偏好类型]] | "vN-M 期望效用类" | 期望效用函数作为偏好的特殊形式;Allais 悖论 [BIAS] |
| [[替代效应]] | "状态相依扩展" | 价格 $p_s$ 变化下的 SE-IE;接续 [[禀赋经济中的SE-IE]] |
| [[包络定理]] | "Walras 定律链接" | Walras 定律是预算约束在均衡下的总量版本 |
| [[关闭条件]] | "LR 进入退出对称" | 关闭决策的 LR 镜像 = 进入决策;$p = \min LAC$ |
| [[规模报酬]] | "行业供给曲线" | 三种行业类型（CR / IR / DR）与 LR 行业供给斜率 |

**默认推荐**：8 页扩展（与 Batch 2 的 5 页扩展量级匹配）。

### 3.2 跨域 see-also（单向链接到 AI / 管理叙事）

> 与 Batch 1-2 同口径：**单向**追加,不改写 AI/管理页主线。

| 跨域页 | 拟追加段 | 内容定位 |
|---|---|---|
| [[NVIDIA]] | "市场均衡 / 一般均衡视角" | 算力市场的供需汇总;NVIDIA 是垄断厂商而非完全竞争（[BIAS] 显式标注） |
| [[Token工厂经济学]] | "市场均衡视角" | Token 价格分层定价 vs 完全竞争模型的偏离;CS+PS 在 Token 市场的解读 |
| [[美团骑手管理平台]] | "价格管制视角" | 平台抽成 / 最低单价 ↔ 价格上限 / 下限的工资版本;DWL 与算法权力 |
| [[AI重塑企业组织]] | "一般均衡基底" | Batch 3 提供"完全竞争 + GE + 风险"的标准基底,与 AI 叙事的偏离条件 |

**默认推荐**：4 处（与 Batch 1 一致;Batch 2 是 2 处）。

### 3.3 主题导览页（Stage 2 新建）

**默认推荐：3 个独立主题页**（详见 §9 决策点 2）：

- [[竞争性市场均衡]]（Ch 14-15 综合,部分均衡 + 福利分析）
- [[一般均衡]]（Ch 16 综合,Edgeworth + Walras + Robinson Crusoe + 福利定理）
- [[风险与状态偏好]]（Ch 17 综合,期望效用 + 保险 + 风险情境 GE）

**备选 A**：1 个综合主题页 [[竞争性市场与福利]]（4 章合并;最紧凑但损失各章独立性）。
**备选 B**：2 个主题页 [[竞争性市场均衡]] + [[一般均衡与风险]]（Ch 14-15 / Ch 16-17 二分）。

## 4. 矛盾发现 / 教学偏置 [BIAS]

### 4.1 与 Batch 1-2 的延续 [BIAS]

- **完全竞争假设的延续 [BIAS]**：Ch 14-17 全部假设价格接受。Ch 14-15 的市场需求-供给加总假定厂商无个体定价权;Ch 16 的 Walras 均衡仍是价格接受;Ch 17 的保险市场也是完全竞争。垄断 / 寡头 / 信息不对称 / 外部性留到 Ch 18-25。已在 Batch 2 [[利润最大化问题]] / [[价值边际产品VMP]] 标注的 [BIAS] 在 Batch 3 持续生效。
- **小政府叙事偏向的延续 [BIAS]**：Ch 15 把价格管制（rent control / minimum wage）和贸易壁垒一律作为 DWL 的源头讲;Pigou 矫正性税要到 Ch 21 才出现。已在 Batch 1 [[经济学六大教训]] / [[无谓损失DWL]] 的 [BIAS] 持续生效。

### 4.2 Batch 3 新增 [BIAS]

- **第一福利定理的"无前提乐观"叙事 [BIAS]**：Ch 15-16 在论证第一福利定理时,会列出"无外部性 / 无非凸 / 无信息不对称 / 无市场势力"等前提,但教材的修辞重心放在"在这些条件下市场是高效的",而非"这些条件多么严苛"。读者若止步 Part 3,会形成"市场配置默认高效"的失衡印象;Ch 17 结尾的 CONCLUSION 段已经预告"Ch 18 起将讲第一福利定理失败的情形",但前 4 章的语调依然偏正面。**拟在 [[第一福利定理]] / [[第一福利定理-部分均衡]] / [[竞争性市场均衡]] 主题页 §3 显式标注**。

- **国际贸易的"自由贸易默认正确"叙事 [BIAS]**：Ch 15 论证国际贸易时,几乎只展示"贸易增加总福利"（CS+PS 净增）,但分配后果（生产者输家 / 消费者输家）只作为附注,且**完全不**讨论:① 比较优势的动态形成（幼稚产业保护、技术外溢）;② 贸易调整成本（劳动力再配置、地区性失业);③ 国家安全 / 战略性产业 / 数字主权。读者若止步 Ch 15,会形成"自由贸易 = 帕累托改进"的过度乐观印象。**拟在 [[国际贸易福利]] [BIAS] 段标注**;同时和本 Wiki 的 AI/算力叙事（[[NVIDIA]] / [[Token工厂经济学]] 涉及出口管制）形成对话。

- **期望效用框架的"独立性公理无问题"叙事 [BIAS]**：Ch 17 + 附录 1 介绍 vN-M 期望效用,把独立性公理作为"不强的合理假设",仅在附录 2 简要提到 Allais 悖论作为"famous paradox"。但行为经济学（Kahneman-Tversky 1979 *Prospect Theory*；Allais 1953）已经证明独立性公理在实验中**系统性**被违反。Ch 17 的整套保险均衡分析（精算公平 / 完全保险 / 风险厌恶）都建立在 vN-M 之上;若该框架在描述层面失效,结论的描述效力受限（规范效力可保留）。**拟在 [[vN-M期望效用]] / [[独立性公理]] [BIAS] 段标注**;同时埋设 Batch 4 摄入 Kahneman 或 MWG Ch 6 时的接入点。

- **Robinson Crusoe 模型的"无社会"假设 [BIAS]**：Ch 16B.3 用 Robinson Crusoe 经济（一人扮演消费者 + 厂商 + 土地所有者）证明"GE = 计划者最优"。这一抽象的代价是把**分工 / 市场 / 价格**这三个概念全部重叠到一个人身上;它能简化数学,但模糊了价格在协调 *分散决策* 中的核心作用——而正是后者构成了"看不见的手"的实证内容。读者若把 Robinson Crusoe 模型当成"市场协调"的代表,会错失市场机制的本体论功能。**拟在 [[Robinson Crusoe经济]] [BIAS] 段标注**。

### 4.3 与 [CONTRADICTION] 主线的对话

Batch 3 暂**不**直接回应 Wiki 已有的 [CONTRADICTION] 主线（"个体自由 vs 算法压榨"、"管理思想滞后 vs 技术驱动"）;但 Ch 15 价格管制工具集（[[价格上限]] / [[价格下限]] / DWL）与 [[美团骑手管理平台]] 的"算法定价 = 实质工资下限/上限"形成桥接。完整回应仍要到 Batch 5（Ch 23-25 不完全竞争 + 议价博弈论）。

## 5. 知识缺口（拟补 / 留待后续）

### 5.1 Batch 3 内能补的（无需新材料）

- [[补偿变差CV]] / [[等价变差EV]]：原计划 Batch 4 / MWG 摄入。但 Ch 15 的福利分析使用 [[消费者剩余]] / [[社会剩余]] 也能完成,且 Ch 17 的"确定性等价 + 风险溢价"在精神上接近 EV/CV 的风险情境版本。**可选**:在 Ch 17 触及保险一般均衡时,顺势补 [[补偿变差CV]] / [[等价变差EV]] 两页（详见 §9 决策点 6）。
- 行业供给弹性差异（Goulder-Williams 2012 综述）：Batch 2 [[规模报酬]] 已埋设,Ch 14 的"行业类型"为这块文献提供概念框架。

### 5.2 Batch 3 内**不**能补的（留待后续）

- 比较优势 + 贸易调整成本（Ricardo / Heckscher-Ohlin / Stolper-Samuelson）：教材 Ch 15 仅给出最简化的 2-good / 2-country 模型,完整 HO 框架要到本科国际贸易专项教材（Krugman-Obstfeld）才有。
- 第一福利定理失败模式的完整目录（外部性 / 公共品 / 信息不对称 / 市场势力 / 非凸）：留 Ch 21-25（Batch 5）。
- Allais / Ellsberg 悖论 + Prospect Theory 的实验证据：留 Batch 4 摄入或 MWG。
- 不动产市场 / 劳动力市场 / 金融市场的 Walras 一般均衡校准：留计算 GE / Hertz-Sommer-Hau / Auerbach-Kotlikoff 等专题。
- 核收敛定理的严格证明（Edgeworth-Debreu-Scarf）：留 MWG Ch 18。

## 6. 反面论点与数据空白（每个概念页"反面论点与数据空白"小节的初稿要点）

CLAUDE.md 强制要求每个概念页含此小节。Stage 2 生成时按下表准备：

### 6.1 Ch 14（市场均衡）

- [[长期零利润条件]] 反面论点：现实长 LR 可能不存在；"僵尸企业"（Caballero-Hoshi-Kashyap 2008）违反退出条件;数字平台行业的 IRS 使 $\min LAC \to 0$,LR 均衡退化为垄断。
- [[完全竞争行业类型]] 反面论点：constant-cost 行业实证罕见;农业季节性 + 储存技术使供给曲线非单调;软件行业实际上是 0 边际成本（Decreasing-cost 极端）。
- [[市场需求曲线]] 反面论点：Slutsky 对称性的实证违反（Browning, Deaton, Hausman）→ 个体加总到市场可能掩盖系统性偏差。

### 6.2 Ch 15（福利分析 + 国际贸易）

- [[第一福利定理-部分均衡]] 反面论点：定理仅在"无外部性 + 无信息不对称 + 完全竞争"下成立;现实市场至少违反一个条件 → 定理为基准而非描述。
- [[价格上限]] / [[价格下限]] 反面论点：教材的 DWL 分析忽略**分配**后果;低收入消费者从 rent control 受益 / 工人从 minimum wage 受益的实证（Card-Krueger 1994 minimum wage paradox）。
- [[国际贸易福利]] 反面论点：贸易调整成本（Autor-Dorn-Hanson 2013 China shock）使 LR CS+PS 增加掩盖 SR 地区性失业;比较优势的动态演化（韩国 / 台湾电子产业幼稚产业保护）违反静态模型。
- [[税收归宿]] 反面论点：长 LR 资本流动性使资本税归宿落在劳动（Harberger 1962）；增值税 / 消费税的累退性（Gruber-Saez）。

### 6.3 Ch 16（一般均衡）

- [[第一福利定理]] 反面论点：所有"正"前提（无外部性 / 凸偏好 / 完美信息 / 完全竞争）的现实违反;Greenwald-Stiglitz 1986 证明"几乎所有"实际经济不满足前提。
- [[第二福利定理]] 反面论点：lump-sum 转移在现实中**不存在**（信息不对称 + 政治可行性);Mirrlees 1971 最优所得税理论给出现实的最佳替代。
- [[Walras定律]] 反面论点：在不完全市场（缺失市场 / 信息不对称）下,Walras 定律的均衡可能不存在或不唯一（Hahn 1958、Sonnenschein-Mantel-Debreu 1972-74）。
- [[Robinson Crusoe经济]] 反面论点：去除分工和市场后,模型失去对"价格作为协调机制"的解释力;参见 Hayek 1945 *The Use of Knowledge in Society*——价格的认识论功能在 RC 模型中完全消失。

### 6.4 Ch 17（风险与保险）

- [[期望效用函数]] / [[独立性公理]] 反面论点：Allais 1953 / Kahneman-Tversky 1979 *Prospect Theory* 的实验违反;Ellsberg 1961 模糊厌恶悖论;现实人面对保险决策的系统性"过度保险"或"保险不足"无法用 EU 解释（参见 Sydnor 2010 房屋保险研究）。
- [[精算公平保险]] 反面论点：现实保险存在加载费用（loading factor)、逆向选择（Akerlof 1970）和道德风险;真实精算公平保险**不存在**。
- [[一般均衡-风险版]] 反面论点：完整状态相依商品市场（Arrow-Debreu）需要"完美 + 完整 + 无限"的市场结构;现实金融市场是"不完全"的（Hart 1975）;2008 金融危机展示状态相依商品定价机制可整体失效。

## 7. 主题页（拟建的 1-3 个综合导览页结构）

按默认推荐（3 个独立主题页）准备：

### 7.1 [[竞争性市场均衡]]（Ch 14-15 综合）

七段式（与 [[消费者最优化选择]] / [[厂商最优化选择]] 同构）：
1. 全章拓扑（市场需求 + 市场供给 → SR / LR 均衡 → 福利测度 → 政策扭曲）
2. 三条贯穿红线（个体加总;CS+PS = 社会剩余;DWL ≈ ½ × Δp × Δq）
3. 教学偏置 [BIAS]（小政府叙事延续 + 自由贸易默认 + 完全竞争假设）
4. 数据空白（行业弹性 / 贸易调整成本 / Card-Krueger 等实证）
5. 跨域 see-also（NVIDIA / Token工厂 / 美团骑手 / AI重塑企业组织）
6. 后续 Batch 衔接（Ch 16 GE / Ch 18-22 失败模式 / Ch 23-25 不完全竞争）
7. 推荐阅读路径

### 7.2 [[一般均衡]]（Ch 16）

同构七段式,重点：
- §1 拓扑（Edgeworth → 契约曲线 → 核 → Walras 均衡 → 福利定理 → Robinson Crusoe）
- §2 红线（个体优化 → 总量约束 → Pareto 高效 → 第一/第二福利定理）
- §3 [BIAS]（无前提乐观 + RC 模型抽象代价）
- §5 跨域（[[AI重塑企业组织]] 的"算法平台 = 微型 GE"类比的边界）

### 7.3 [[风险与状态偏好]]（Ch 17）

同构七段式,重点：
- §1 拓扑（状态相依商品 → 期望效用 → 风险厌恶 → 保险 → 一般均衡）
- §2 红线（u 凹性 ↔ 风险厌恶 ↔ 完全保险偏好;状态独立 vs 状态相依;个体 vs 总体风险）
- §3 [BIAS]（vN-M 描述失效 + 精算公平假设 + 完整市场假设）
- §5 跨域（NVIDIA 长期供货合同 = 状态相依商品的远期版本;算法风险定价）

## 8. Stage 2 拟生成的页面清单（汇总）

| 类别 | 数量 | 详情 |
|---|---|---|
| 实体（人物） | 5 | [[Léon Walras]] / [[Vilfredo Pareto]] / [[Francis Edgeworth]] / [[John von Neumann]] / [[Oskar Morgenstern]] |
| 概念（Ch 14） | 8 | 见 §2.1 |
| 概念（Ch 15） | 9 | 见 §2.2 |
| 概念（Ch 16） | 11 | 见 §2.3 |
| 概念（Ch 17） | 12 | 见 §2.4 |
| 主题页 | 3 | [[竞争性市场均衡]] / [[一般均衡]] / [[风险与状态偏好]]（默认推荐） |
| 镜像页扩展 | 8 | 见 §3.1 |
| 跨域 see-also 编辑 | 4 | 见 §3.2 |
| 教材主页编辑 | 1 | [[Microeconomics-Nechyba-2e]] 新增 Batch 3 段 + 人物索引 + [BIAS] 段 |
| 索引 / 状态 / 日志 | 3 | `wiki/index.md` / `wiki/state.md` / `wiki/log.md` |
| **合计** | **64** | 与 Batch 1（61）/ Batch 2（35）量级匹配 |

## 9. 决策点（请用户回复"continue"采用默认,或单独修改某项）

| # | 决策项 | 默认推荐 | 备选方案 |
|---|---|---|---|
| 1 | **Batch 3 范围** | **Ch 14-17（4 章,完整 Part 3）** | Ch 14-16（把 Ch 17 推迟到 Batch 4）|
| 2 | **主题页粒度** | **3 页**（[[竞争性市场均衡]] + [[一般均衡]] + [[风险与状态偏好]]） | 1 页综合 / 2 页（Ch 14-15 + Ch 16-17）|
| 3 | **镜像页扩展数量** | **8 页**（见 §3.1）| 5 页（删 [[关闭条件]] / [[规模报酬]] / [[替代效应]] 中 3 页）|
| 4 | **跨域 see-also 数量** | **4 处**（NVIDIA / Token工厂 / 美团骑手 / AI重塑企业组织）| 2 处（去掉 [[NVIDIA]] / [[Token工厂经济学]]）|
| 5 | **新增人物实体页** | **5 人独立**（Walras / Pareto / Edgeworth / vN / Morgenstern）| 4 人（合并 vN-M 为单页）/ 3 人（去 Edgeworth）|
| 6 | **CV / EV 是否在本批补足** | **不补,留 Batch 4 / MWG**（与原计划一致） | 在 Ch 17 触及保险时**补 [[补偿变差CV]] / [[等价变差EV]]** 两页 |
| 7 | **PDF 归档** | **保持 Plan B**（Batch 6 全部完成后再归档,本批 3/6） | 现在归档（Plan A）|

**预计页面变动**：默认决策下 64 页（与 §8 一致）;若决策点 6 选择"补 CV/EV"则增至 66 页。

## 10. PDF 留存说明

按 Plan B,本批继续保留 PDF 在 `raw/inbox/` 下不动。Batch 6 全部完成后再统一归档至 `raw/archive/`。本批为 6-batch 计划的 **3/6**。

---

> **Stage 1 输出结束**。等待用户回复:
> - **"continue" 或 "继续"**：采用 §9 全部默认决策,进入 Stage 2 生成;
> - **"修改 #N: ..."**：单独修改某决策点（其他默认）后进入 Stage 2;
> - **"跳过"**：终止 Batch 3,不进入 Stage 2。
