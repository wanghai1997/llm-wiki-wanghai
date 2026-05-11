---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [概念, microeconomics, foundations, batch3, 一般均衡, BIAS]
confidence: medium
decay_category: slow
status: foundation
---

# Robinson Crusoe经济

> 1 人 + 1 厂商的极简一般均衡。Crusoe 既是消费者(选休闲与产品)也是厂商(选生产)。生产可能边界 + 无差异曲线相切 → 唯一最优配置。教材用其引入"分散决策 = 集中决策"的同构。[BIAS:鲁滨逊"无社会"抽象]

## 形式

设 Crusoe 有时间禀赋 $\bar L$,可以分为休闲 $\ell$ 和劳动 $L = \bar L - \ell$。劳动通过生产函数 $f(L)$ 生产消费品 $C$。

**Crusoe 集中决策**:
$$
\max_{\ell, C} U(\ell, C) \quad \text{s.t.} \quad C = f(\bar L - \ell)
$$

最优条件:$MRS_{\ell, C} = MP_L$ → 边际替代率 = 边际产量。

## 分散决策版本(Walras 隐喻)

设 Crusoe 把自己分裂为两个角色:
- **消费者 Robinson**:选 $(\ell, C)$ 使 $U$ 最大化,预算 $w \ell + p C \le w \bar L + \pi$。
- **厂商 Crusoe Inc.**:选 $L$ 使 $\pi = p f(L) - w L$ 最大化。

完全竞争下,$w$ 与 $p$ 调整使两人决策同时一致 + 市场出清:$L^{需求} = \bar L - \ell^{供给}$,$C^{需求} = f(L^{供给})$。

> **关键洞察**:分散决策与集中决策得到**相同**的 $(\ell^*, L^*, C^*)$。这是第一福利定理在 1 人 1 厂商情形的最简版本。

## 几何

教材 16A 给出经典图:
- 横轴 $\ell$(休闲),纵轴 $C$(消费)。
- 生产可能边界 $C = f(\bar L - \ell)$ 凸向原点(MP 递减,递增机会成本)。
- 无差异曲线 $U(\ell, C)$ = 常数。
- **最优**:无差异曲线与生产可能边界相切。
- **价格 $w/p$**:斜率 $-w/p$ = 切线斜率(同时是消费者预算线 + 厂商生产决策的"等利润线")。

## 教学功能

Robinson Crusoe 经济是一般均衡的"原型简化":
1. 引入"价格 = 边际生产率"概念。
2. 演示分散 / 集中决策同构(Walras vs 集体规划)。
3. 第一福利定理的 1 人版(无外部性时显然成立)。
4. 引入 PPF + 无差异曲线相切的几何。

## Robinson Crusoe + Friday 经济

教材 16B 扩展:加入第二人 Friday(劳动 / 偏好不同),Crusoe 与 Friday 通过分工 + 交换实现共同最优。这是从"鲁滨逊"到完整 Edgeworth 盒的过渡。

## [BIAS:鲁滨逊"无社会"抽象]

> **教材立场**:Robinson Crusoe 模型把"社会"还原为"孤立个体的选择"——经济学的基本单位是个人偏好 + 个人禀赋。

> **反面立场**:
> 1. **方法论个体主义批评**:Bowles-Gintis 2011 *A Cooperative Species* 等论证,人类经济行为本质上是社会性的——偏好、规范、信任都在社会互动中形成。Robinson Crusoe 模型从源头上抹去这一维度。
> 2. **Crusoe 的"无社会"是文学虚构**:历史上,Defoe 的 Crusoe 实际上携带着大量先在社会知识(语言、技艺、价值观),并非"原子个人"。模型把社会内容隐藏后,得出的"个人选择"结论暗含社会假设。
> 3. **跨文化偏好差异**:Henrich et al. 2010 *"The weirdest people in the world?"* 显示偏好高度依赖文化,WEIRD 国家(Western, Educated, Industrialized, Rich, Democratic)的偏好不能代表人类一般。Robinson Crusoe 假设偏好普适使理论应用范围受限。
> 4. **集体生产形式被忽略**:合作社、家庭、公共组织等非市场化生产形式在 Robinson Crusoe 模型中无对应。Ostrom 1990 *Governing the Commons* 系统讨论这些形式,Nechyba 完全市场化分析不展开。

## 反面论点与数据空白

- **方法论个体主义的本体论问题**:经济学是否应该假设社会可还原为个体选择?Sen 1977 *"Rational Fools"* / Bowles-Gintis 2011 / Nelson 2006 *Economics for Humans* 都给出反方观点。
- **生产函数的可加性 / 凸性假设**:Robinson Crusoe 模型假设 $f$ 凸 / 边际递减;现实中规模经济(IRS)使 $f$ 不凸 → 第一福利定理失效。教材假设凸技术回避此问题。
- **跨期 / 风险忽略**:Robinson Crusoe 静态;Ch 17 引入风险,但仍无跨期(Ch 18 才系统跨期)。
- **环境约束失踪**:Robinson Crusoe 把"自然"作为外生约束,不考虑生产对环境的影响。21 世纪气候 / 生态危机使这一假设不可持续。
- **数据空白**:Robinson Crusoe 是教学工具,无直接实证;但实验经济学(Smith 1962-2000s 系列)展示真实主体在 Crusoe-like 实验中行为偏离理论预测——损失厌恶、互惠、公平等社会维度普遍涌现。
- **AI 时代的"非人"经济**:21 世纪 AI 生产力变革使"人 + 工具" 经济结构重构,Robinson Crusoe 假设的"人 = 唯一决策者"显得过时。详见 [[AI重塑企业组织]] 跨域链接。

## 相关页

- 上游:[[一般均衡-Walras版]] / [[第一福利定理]]
- 邻近:[[Edgeworth盒]](2 人扩展)
- 跨期 / 风险:Ch 17-18 / [[状态相依商品]]
- 反面:[[共同治理]] [Batch 5] / [[AI重塑企业组织]] 跨域链接
- 主题:[[一般均衡]]
