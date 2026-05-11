---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [analysis, ingest-stage1, microeconomics, foundations, batch01]
status: draft
---

# Stage-1 分析：Nechyba《Microeconomics: An Intuitive Approach with Calculus》Batch 1（Ch 1–10）

> 这是 Ingest 工作流第一阶段（分析→确认→生成）的分析稿。
> **生成阶段（Stage 2）须等用户确认本文档之后才会执行。**

---

## 0. 文档总体评估

### 0.1 文献基本信息

- **作者**：Thomas J. Nechyba（杜克大学经济学教授，曾任系主任）。
- **版本**：Cengage Learning, 2017 © 第二版（页脚版权页）。
- **体量**：约 1200 页，30 章，分为 6 个 Part。
- **设计特征**：每章双轨结构 **Part A（图形直觉版）+ Part B（微积分严格版）**——A、B 章节共享同一编号但角标不同（如 9A.3.1 vs 9B.3.1）。可独立读，也可合读。
- **教学定位**：中级微观经济学，适合"已学过初级宏微观、会用基础微积分"的本科二/三年级学生；约介于 Varian 中级与 MWG 高级之间，但具有"先建直觉再上数学"的独特双轨结构。

### 0.2 与本 Wiki 的契合度

- `purpose.md` 列出的覆盖领域含 **经济学**，目前 Wiki 的经济学条目为零（实体 9 条、概念 16 条全部位于 AI / 组织管理域）。
- Nechyba 的优点是**"微观经济学第一性原理"**，可作为 `wiki/foundations/microeconomics/` 的奠基层；其严格度足以支撑后续与 Mas-Colell、Varian 等高级教材交叉摄入。
- **建议**：本批次摄入的核心定理 / 模型采用 `status: foundation`；教材特有的应用 / 政策叙述（如 IRA 税收政策示例）采用 `status: draft`，等多源交叉验证后再升级。

### 0.3 Batch 1 章节范围与主题

> 本批次涵盖 **Part 1（消费者、工人、储蓄者的效用最大化选择）的全部 10 章**，构成"个人最优化决策"的完整闭环。

| 章 | 主题 | 关键工具 |
|---|---|---|
| Ch 1 | 实证 vs 规范 / 经济学六大教训 / 看不见的手 | 思想框架 |
| Ch 2 | 消费者经济环境：预算约束 | 外生收入预算 |
| Ch 3 | 跨期 / 劳动 / 金融预算 | 内生收入预算 |
| Ch 4 | 偏好与无差异曲线（5 公理） | 完备性 / 传递性 / 单调性 / 凸性 / 连续性 |
| Ch 5 | 偏好类型（CES / Cobb-Douglas / 完全替代/互补 / 准线性 / 同位） | 替代弹性 σ |
| Ch 6 | 最优选择（边际条件 / 角点解 / 拉格朗日 / 非凸偏好） | 切线法 + KKT |
| Ch 7 | 收入与替代效应：Hicks vs Slutsky 分解 | 补偿预算 / Giffen / 反向 SE |
| Ch 8 | 禀赋经济中的财富与替代效应（劳动 / 资本市场） | Laffer 曲线 / IRA |
| Ch 9 | 需求曲线与劳动 / 资本供给曲线的推导 | "切片"逻辑：固定其它变量 |
| Ch 10 | 消费者剩余与无谓损失（DWL） | MWTP / 补偿需求 / 对偶 / Slutsky 方程 / Shephard / Roy / 包络定理 |

### 0.4 总体教学线索（作者意图）

1. 先建立 **"经济环境"**（Ch 2–3）——什么是可负担集；
2. 再建立 **"偏好"**（Ch 4–5）——什么是被欲求；
3. 二者结合得 **"最优化选择"**（Ch 6）；
4. 让环境变化（价格 / 收入 / 利率 / 工资 / 禀赋）→ **比较静态分析**（Ch 7–8）；
5. 把比较静态结果"竖切"成 **需求与供给曲线**（Ch 9）；
6. 最后用这些曲线 **测度福利**（Ch 10）。

> 这一线索在 wiki 中可以转化为一个 **主题摘要页**："消费者最优化选择"，作为 Batch 1 的统一索引页。

---

## 1. 核心实体（拟新增）

### 1.1 人物

| 拟建页面 | 简介 | status |
|---|---|---|
| [[Thomas J. Nechyba]] | 教材作者，杜克大学；研究教育经济学、地方公共经济学。 | draft |
| [[John Hicks]] | "补偿需求曲线"提出者；Hicks 分解的 SE。Ch 7 / Ch 10 显式致敬。 | foundation |
| [[Eugen Slutsky]] | Slutsky 方程；Slutsky 分解的另一种 SE 定义。Ch 7 / Ch 10。 | foundation |
| [[Alfred Marshall]] | "Marshallian 需求"（无补偿需求）；1895 年 *Principles of Economics*。 | foundation |
| [[Ronald Shephard]] | Shephard's Lemma（1953 年）。 | foundation |
| [[René Roy]] | Roy's Identity（1947 年）。 | foundation |

> Margaret Thatcher（"head tax / 人头税"案例，Ch 10）——仅 wikilink 占位，本批次不为其建独立页（与微观经济理论非中心）。

### 1.2 机构 / 出版物

| 拟建页面 | 备注 |
|---|---|
| [[Microeconomics-Nechyba-2e]]（书页） | 教材索引页，含章节目录 / Part 划分 / A-B 双轨说明 / 后续 Batch 计划。 |

### 1.3 与现有 Wiki 实体的潜在交集

- **[[NVIDIA]] / [[黄仁勋]]**：Ch 10 的"DWL 几何增长 → 宽税基低税率"政策结论可以作为分析"Token 计费"等数字商品税的概念性参考（远期可考虑跨域链接，本批次不强求）。
- **[[美团]] / [[盒马]]**：Ch 8 的劳动 SE/IE 模型可以作为分析骑手 / 蓝领工时供给行为的理论镜片（远期跨域链接）。

---

## 2. 核心概念（拟新增）

> 概念按学习顺序与逻辑层级组织。**所有概念页须包含"反面论点与数据空白"小节**（CLAUDE.md 强制要求）。

### 2.1 经济学方法论（Ch 1）

| 拟建页 | 一句话定义 | status |
|---|---|---|
| [[实证经济学与规范经济学]] | Positive describes "what is"; normative prescribes "what ought"。 | foundation |
| [[看不见的手]] | 价格信号下的分散决策可逼近 Pareto-efficiency；Smith 1776。 | foundation |
| [[经济学六大教训]] | Nechyba 抽出的六条贯穿全书的核心信念。 | draft（教材主观抽提） |

### 2.2 经济环境：预算约束（Ch 2–3）

| 拟建页 | 关键点 | status |
|---|---|---|
| [[预算约束]] | 外生收入下 `p₁x₁ + p₂x₂ ≤ I`；斜率 = -p₁/p₂；机会成本 = 斜率绝对值。 | foundation |
| [[禀赋预算]] | 内生收入：禀赋 (e₁,e₂) 通过价格转化为购买力；价格变动旋转预算线**绕禀赋点**。 | foundation |
| [[跨期预算约束]] | `(1+r)c₁ + c₂ = (1+r)e₁ + e₂`；利率即跨期价格。 | foundation |
| [[劳动-闲暇预算]] | 闲暇禀赋 L 与工资 w；工资变动旋转预算线绕 (L,0)。 | foundation |
| [[折点预算]] | 数量折扣 / 累进税 / 配给制造成 kinky budget；用于解释边际激励的分段。 | draft |
| [[机会成本]] | 任一选择的代价 = 放弃的次优选择的价值；预算线斜率的核心含义。 | foundation |

### 2.3 偏好（Ch 4–5）

| 拟建页 | 关键点 | status |
|---|---|---|
| [[偏好五公理]] | 完备性 / 传递性 / 单调性 / 凸性 / 连续性；前三常被称作"理性"，后两为"几何良态"。 | foundation |
| [[无差异曲线]] | 等效用曲线；连续 + 单调 → 不交叉、向右下倾。 | foundation |
| [[边际替代率MRS]] | `MRS = -dx₂/dx₁ = MU₁/MU₂`；凸偏好 → MRS 沿 IC 递减。 | foundation |
| [[偏好类型]] | 完全替代 / 完全互补 / Cobb-Douglas / CES / 准线性 / 同位。 | foundation |
| [[替代弹性]] | `σ = d ln(x₂/x₁) / d ln(MRS)`；CES 中 σ = 1/(1+ρ)；σ→0 互补、σ→∞ 替代、σ=1 即 CD。 | foundation |
| [[同位偏好]] | 收入扩展路径为原点出发的射线；Engel 曲线为线性。 | foundation |
| [[准线性偏好]] | 一种商品无收入效应；MWTP = 普通需求；Ch 10 福利测量"特例"。 | foundation |

### 2.4 最优选择（Ch 6）

| 拟建页 | 关键点 | status |
|---|---|---|
| [[效用最大化问题]] | `max u(x₁,x₂) s.t. p₁x₁+p₂x₂=I`；解为 Marshallian 需求 `xᵢ(p,I)`。 | foundation |
| [[支出最小化问题]] | `min p₁x₁+p₂x₂ s.t. u(x₁,x₂)=u`；解为 Hicksian / 补偿需求 `hᵢ(p,u)`。 | foundation |
| [[内点最优条件]] | `MRS = -p₁/p₂`，即"心理换算率 = 市场换算率"。 | foundation |
| [[角点解]] | 内点条件失败 → 在轴上选择；准线性 / 完全替代常出现。 | foundation |
| [[拉格朗日法]] | 引入 λ 把约束并入目标函数；λ\* 即收入的边际效用。 | foundation |
| [[非凸偏好与多解]] | 凸偏好假设的失效 → 一阶条件给出极小或非全局最大；需要凹性或二阶条件。 | draft |

### 2.5 比较静态：收入与替代效应（Ch 7–8）

| 拟建页 | 关键点 | status |
|---|---|---|
| [[Hicks分解]] | 价格变化 = 替代效应（沿原 IC，到补偿预算）+ 收入效应（IC 移动）；保持效用不变。 | foundation |
| [[Slutsky分解]] | 替代效应 = 沿"维持原始消费束可负担"的预算移动；保持购买力不变。Hicks 与 Slutsky 在小变化下重合。 | foundation |
| [[补偿预算]] | 给消费者足够补偿以重达原 IC（Hicks）或原 bundle（Slutsky）。 | foundation |
| [[正常商品与劣等商品]] | `∂x/∂I` 符号决定；劣等商品的 IE 与 SE 反向。 | foundation |
| [[Giffen商品]] | 劣等且 IE 大于 SE → 价格上升时需求上升；理论可能但实证罕见。 | foundation |
| [[禀赋经济中的SE-IE]] | 禀赋点不动，价格变动同时改变购买力与相对价格；劳动 / 资本供给曲线后弯的根源。 | foundation |
| [[劳动供给后弯]] | 高工资段闲暇成为正常品时 IE 压过 SE；可来自 CES with ρ>0。 | draft（实证依赖） |
| [[Laffer曲线]] | 税率↑→ 行为响应使税基↓→ 税收先升后降；理论清晰，"拐点位置"实证争议。 | draft |
| [[IRA与跨期税收]] | 工资征税 + 储蓄补贴；Method 1（个人账户）vs Method 2（pay-as-you-go）效果差异。 | draft |

### 2.6 需求 / 供给曲线的推导（Ch 9）

| 拟建页 | 关键点 | status |
|---|---|---|
| [[Marshallian需求曲线]] | "切片"：固定 (I, p₂)，画 (p₁, x₁)；嵌入收入与替代两效应。 | foundation |
| [[劳动供给曲线]] | 来自闲暇-消费选择的 wage-leisure 切片。 | foundation |
| [[资本供给曲线]] | 来自跨期选择，利率为价格；储蓄函数 s(r)。 | foundation |
| [[借贷需求曲线]] | 同一跨期问题在另一边；与储蓄供给互为倒影。 | foundation |
| [[需求曲线斜率与商品类型]] | 正常商品 → 下行；劣等且 SE 占优 → 下行；Giffen → 上行。 | foundation |

### 2.7 福利测度（Ch 10）

| 拟建页 | 关键点 | status |
|---|---|---|
| [[边际支付意愿MWTP]] | 沿单一 IC 的 MRS 在不同消费量上的轨迹；本质即补偿需求曲线。 | foundation |
| [[消费者剩余]] | 总支付意愿 - 实际支付；**仅在准线性偏好下沿 Marshallian 曲线测度才正确**，否则要沿 MWTP。 | foundation |
| [[补偿需求曲线]] | Hicksian h(p,u)；只含 SE，不含 IE。 | foundation |
| [[Marshallian需求与Hicksian需求关系]] | 正常品：D 比 H 平缓；劣等品：D 比 H 陡；准线性：两者重合。 | foundation |
| [[无谓损失DWL]] | DWL = L - T（同效用的总额税 - 实际税收）；根源是 SE 改变机会成本。 | foundation |
| [[总额税与扭曲税]] | Lump-sum tax 不变机会成本 → 无 DWL；Thatcher 人头税案例。 | foundation |
| [[DWL几何增长]] | 准线性 + 线性需求下，DWL ∝ t²；推论：宽税基低税率优于窄税基高税率。 | foundation |
| [[消费者对偶性]] | UMP 与 EMP 互为对偶；4 个对象（u,V,E,h,x）的连接图。 | foundation |
| [[Slutsky方程]] | `∂xᵢ/∂pⱼ = ∂hᵢ/∂pⱼ - (∂xᵢ/∂I)(∂E/∂pⱼ)`；将 Marshallian 斜率分解为 SE + IE。 | foundation |
| [[Shephard引理]] | `∂E(p,u)/∂pᵢ = hᵢ(p,u)`。 | foundation |
| [[Roy恒等式]] | `xᵢ(p,I) = -[∂V/∂pᵢ]/[∂V/∂I]`。 | foundation |
| [[间接效用函数]] | `V(p,I) = u(x*(p,I))`。 | foundation |
| [[支出函数]] | `E(p,u) = p·h*(p,u)`；凹于 p。 | foundation |
| [[包络定理]] | `∂F\*/∂α = ∂L/∂α│at optimum`；用于推导 Shephard / Roy。 | foundation |

> 注：**CV / EV（补偿变差 / 等价变差）** 在 Nechyba 中以"用 V 求 u\*，再用 E 求 L"的形式隐式出现，但**没有显式命名 CV / EV**。下批次（或在 Mas-Colell 摄入时）应补足显式定义页 [[补偿变差CV]]、[[等价变差EV]]，并指明 Nechyba 的 L 在哪种情形等价于 EV / CV。

---

## 3. 与现有 Wiki 的链接点

> Batch 1 与现有 AI / 组织管理域基本正交，但以下 4 处可建立**远期跨域伏笔**：

1. **[[Token工厂经济学]] ↔ [[DWL几何增长]]**：Token 分层定价的"宽基低率"含义 vs 微观税收"broad base, low rate"原则；可在 Token 工厂经济学页加一句"参考 [[DWL几何增长]] 中的几何增长结论"。
2. **[[美团骑手管理平台]] ↔ [[禀赋经济中的SE-IE]] / [[劳动供给后弯]]**：算法压榨/激励对骑手时间分配的经济学解读，远期可在主题页 [[AI重塑企业组织]] 增补一节。
3. **[[Laffer曲线]] ↔ [[NVIDIA]] / [[黄仁勋]]**：算力税 / 数字服务税讨论可援引 Laffer 直觉；本批次仅作页内 see-also。
4. **[[实证经济学与规范经济学]] ↔ 已有 [CONTRADICTION] 标注的 [[AI重塑企业组织]] 主题页**：可在 AI 主题页脚注引一句"本主题混合了 positive 与 normative 论断"作为方法论提醒。

> 上述跨域链接**仅在 see-also 段以单向引用方式建立，不强求双向回链**，避免破坏 AI/组织页的主线。

---

## 4. 内部矛盾与教学偏见

### 4.1 教材内部张力

- **[BIAS] 准线性偏好的"特殊性"**：Nechyba 反复强调"消费者剩余仅在准线性下可信"，但全书前 9 章的几乎所有教学示例都用 Cobb-Douglas（σ=1，非准线性）。**初学者可能被反复使用的 CD 示例误导，以为 D 与 H 总是接近。** Wiki 摄入时应在 [[消费者剩余]] 页显著提示该陷阱。
- **[BIAS] "几乎所有现实税都低效"** 的政策叙事 (10A.3.4)：作者立场倾向于偏小 / 偏中性的政府干预，未充分讨论 Pigou 税 / 矫正性税在外部性下的效率改进作用（Ch 21 才讨论）。本 wiki 在 [[总额税与扭曲税]] 页应补一句"该结论假设无外部性"。
- **[BIAS] 美式政策案例**：IRA、401(k)、Bush/Obama 减税、慈善捐赠抵扣均为美国制度；中国 / 欧洲读者直接套用须谨慎。Wiki 在 [[IRA与跨期税收]] 等页加 `regional-bias` 标签。

### 4.2 与 Wiki 现有论断的潜在冲突

- 现 Wiki 的 [[让听见炮声的人呼唤炮火]]、[[组织三大内生矛盾]] 等概念基于"实践经验"和"管理学叙事"，而 Nechyba 的微观逻辑基于"理性 + 公理化"。**两条路径回答的问题不同**（前者：组织内部决策权下放；后者：分散市场如何聚合信息）——并非冲突，但应在 [[看不见的手]] 页加 see-also 提示，避免读者把"哈耶克分散决策"和"任正非 ENPS 听炮声"等同。

### 4.3 待用户决策的命名歧义

- 本 wiki 已有 [[组织三大内生矛盾]]。本批次拟建 [[偏好五公理]]——名称风格一致，无冲突。
- "替代效应"在 wiki 中尚未出现，但 Nechyba 给出 **Hicks vs Slutsky 两种定义**——拟建 **单页 [[替代效应]]** 内含两种分解的对比，而非分两页，避免读者混淆。**待用户确认是否合并。**

---

## 5. 知识缺口（Batch 1 自身遗留）

> 这些缺口将在 Batch 2–6 或后续 Mas-Colell 摄入时填补：

1. **CV / EV 的显式定义**——Nechyba 用 L 隐式表达，缺独立讨论。
2. **显示偏好理论（Revealed Preference, Samuelson 1938）**——Nechyba 全书几乎不提。
3. **Engel 曲线 / 收入扩展路径**——Ch 9 仅以"income-demand relationship"形式简提，未独立成节。
4. **聚合需求 vs 个体需求**——Ch 9 局限在个体层面。
5. **行为经济学偏离**（损失厌恶、双曲贴现、菜单效应）——Nechyba 只在末尾应用章节零星提及。
6. **风险与不确定性下的选择**（期望效用、风险溢价）——属于 Ch 17（Batch 4），未在本批。
7. **博弈论作为微观工具**——Ch 24（Batch 5），需要决定是否提前到 foundations 层。
8. **生产理论与厂商**（Ch 11–13 = Batch 2）。

---

## 6. 反面论点 / 数据空白草稿

> 以下条目将作为各概念页"反面论点与数据空白"小节的种子文本（Stage 2 时按页分散写入）。

| 概念 | 反面论点要点 | 数据空白 |
|---|---|---|
| [[偏好五公理]] | Allais paradox / Ellsberg paradox / 偏好反转实验对**传递性**的实证挑战；**完备性**对未经验场景失效（Sen 的"理性傻瓜"）。 | Nechyba 未引用任何行为实验数据。 |
| [[效用最大化问题]] | Simon 的 bounded rationality / Kahneman 的"系统 1"；现实决策更接近启发式而非显式优化。 | 无神经经济学证据引用。 |
| [[Giffen商品]] | Jensen & Miller (2008) 中国湖南米饭实验是**唯一**广受认可的实证；理论可能 ≠ 经验普遍。 | Nechyba 仅承认"罕见"，未量化。 |
| [[Laffer曲线]] | 拐点税率的实证估计在 30–70% 之间，跨度极大（Trabandt-Uhlig 2011 vs Saez 2001）。 | Nechyba 未给具体估计。 |
| [[消费者剩余]] | Marshallian 测度在大价格变动下偏差可达 10%+（Hausman 1981）；CV/EV 才是理论上正确的。 | Nechyba 未给偏差量级表（仅 Table 10.1 关于 DWL/T）。 |
| [[DWL几何增长]] | "broad base, low rate"前提是无外部性、无再分配偏好；Mirrlees 最优税理论给出更细的 trade-off。 | Nechyba 把分配问题推给 Ch 29，本批次不展开。 |
| [[看不见的手]] | 第一福利定理需要完全竞争 + 无外部性 + 完备市场——Stiglitz 等指出现实条件几乎不满足。 | Nechyba 在 Ch 1 给出强叙事，矛盾留到 Ch 21+ 处理。 |
| [[实证经济学与规范经济学]] | Hilary Putnam / Amartya Sen 论证"价值-事实二分"在经济学中无法严格区分。 | 哲学层面争议，本 wiki 在该页脚注列两条对立文献即可。 |

---

## 7. 主题摘要页（拟建）

| 页面 | 范围 | 关系 |
|---|---|---|
| [[消费者最优化选择]] | 把 Ch 1–10 的 6 步逻辑链（环境→偏好→优化→比较静态→曲线→福利）串成一篇导览。 | 索引性主题页；引用上面所有 foundations 概念。 |

> 本主题页**不与 [[AI重塑企业组织]] 合并**，二者相互独立。

---

## 8. 待生成页清单（Stage 2 候选）

汇总：**6 实体 + 1 书页 + 51 概念 + 1 主题 + 1 章节书签更新 = 60 个新页 + 多个索引更新**。

> 概念数 51 看似多，但其中 Ch 9–10 的对偶性与定理（约 12 个）粒度细但内容短（每页约 80–150 字 + 公式 + 反面论点）。如用户认为粒度过细，可合并：
> - 选项 A（细粒度，推荐）：保持每个对偶定理独立页，便于其它教材交叉引用。
> - 选项 B（粗粒度）：将 [[Slutsky方程]] / [[Shephard引理]] / [[Roy恒等式]] / [[包络定理]] 合并入 [[消费者对偶性]] 单页。
> - **请用户在确认本分析时一并指示偏好。**

### 8.1 索引 / 状态文件更新计划

- 新建 `wiki/foundations/microeconomics/`（首次启用 foundations 目录）。
- 更新 `wiki/index.md`：新增 "经济学（微观）" 顶级分类，含子分类"方法论 / 预算 / 偏好 / 最优化 / 比较静态 / 曲线推导 / 福利测度"。
- 更新 `wiki/state.md`：新增 "微观经济学（消费者理论）" 共识段；标注 status: foundation 的方法论原则。
- 写入 `wiki/log.md`：本批次 ingest 条目；并按方案 B 记录"PDF 暂留 inbox，archive 推迟到 Batch 6 完成后"。

### 8.2 文件命名约定（建议）

- `wiki/foundations/microeconomics/concepts/Slutsky方程.md`
- `wiki/foundations/microeconomics/entities/John_Hicks.md`
- `wiki/foundations/microeconomics/topics/消费者最优化选择.md`
- `wiki/foundations/microeconomics/books/Microeconomics-Nechyba-2e.md`

> 中文页名 + 英文人名 / 西方术语保留原文，与现有 wiki 风格保持一致（参考 [[Token工厂经济学]] / [[Agent与AaaS]] 的混合风格）。

---

## 9. 用户须确认事项（Stage-1 拦截点）

请就以下 5 项给出指示，以便进入 Stage 2 生成：

1. **粒度选择**：对偶定理采用"细粒度（A）"还是"粗粒度（B）"？
2. **替代效应合并**：是否同意 [[替代效应]] 单页内含 Hicks 与 Slutsky 两种分解（而非分两页）？
3. **跨域伏笔**：是否同意按 §3 在 4 处现有 AI/管理页加单向 see-also（不改原页主线）？
4. **CV / EV 推迟**：是否同意将 [[补偿变差CV]] / [[等价变差EV]] 推迟到 Batch 4（含风险与福利综合）或 Mas-Colell 摄入时再补？
5. **教学偏见标签**：是否同意在 [[IRA与跨期税收]] 等美式政策示例页加 `regional-bias` 标签？

---

## 10. 关于 inbox 之外新出现的 PDF 的提醒

- 在阅读 Ch 10 期间，发现 `wiki/raw/` 目录（**inbox 之外**）出现两份新 PDF：
  - `Microeconomic theory (Mas-Colell, Andreu, Whinston etc.).pdf`（英文原版，68.7 MB）
  - `微观经济理论 (安德鲁·马斯-克莱尔 迈克尔·D·温斯顿 杰里·R·格林 曹乾) .pdf`（中文版，22.8 MB）
- 二者**未在 inbox**，按 CLAUDE.md "raw/inbox/ 是待处理入口" 的规则，**本批次不处理**。
- **建议**：在 Nechyba 全 6 批摄入完成后，再将 MWG（Mas-Colell 等三人）作为"高级教材交叉验证层"摄入；届时 [[CV]]/[[EV]]、Aumann 表征、Afriat 不等式等 Nechyba 缺项可一次补齐。
- **请用户决定**：是按上述次序（先 Nechyba 全摄入再 MWG），还是用 MWG 与 Nechyba 并行交叉？两种方式各有利弊：
  - 顺序处理 → 知识库迭代清晰，结论稳定；
  - 并行交叉 → 一次性建立"中级 + 高级"双层 foundations，节省返工。

---

> **本文件状态：Stage-1 分析草稿。等待用户确认后进入 Stage-2 生成。**
> **生成阶段将分小节提交，便于用户中途中止或调整。**
