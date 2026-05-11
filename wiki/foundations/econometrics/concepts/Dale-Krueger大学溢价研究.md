---
created: 2026-05-04
updated: 2026-05-04
sources: ["Mastering Metrics The Path From Cause to Effect (Joshua David Angrist, Jörn-Steffen Pischke).pdf"]
tags: [concept, econometrics, regression, case-study, education, foundations]
confidence: medium
decay_category: slow
status: foundation
---

# Dale-Krueger 大学溢价研究

## 一句话定义

> **Dale & Krueger (2002, QJE)** = 利用大学申请和录取数据（College and Beyond Survey）研究"上精英私立大学是否提高收入"——通过控制**申请-录取选择度群组**（Barron's selectivity groups）来消除选择偏差。

## 研究设计

- **数据**：College and Beyond (C&B) Survey——1976 年入学群体，追踪至 1995 年收入
- **处理**：就读私立大学 (Private) vs 公立大学 (Public)
- **关键创新**：控制学生**申请并被录取的大学集合**的选择度类别（Barron's 分类），而非仅控制学生自身特征

## 核心发现

| 回归模型 | 私立大学溢价 (log points) | 标准误 |
|---------|------------------------|--------|
| (1) 无控制 | +0.212 | — |
| (2) 控制自身 SAT | +0.152 | — |
| (3) 控制申请-录取选择度组 | **~0.000** | ~0.04 |
| (4) 再加能力/家庭背景控制 | 仍然 ~0.000 | — |

**结论**：一旦控制"你申请了什么水平的大学"（revealed ambition + 能力信号），就读私立大学的额外收入效应约等于零。

## 方法论意义

Mastering 'Metrics Ch 2 将此作为回归方法的旗舰案例：

1. **系数稳定性论证**：加了选择度组（columns 1-3）→ 系数从 +0.212 崩塌到 ~0 → 再加其他控制（columns 4-6）→ 系数稳定 → 暗示选择度组已经吸收了大部分选择偏差
2. **"自我揭示"的控制变量**：申请-录取群组比 SAT 分数更丰富——它综合了学生的抱负、对自己能力的认知、高中辅导员评价等不可直接观测的信息
3. **OVB 公式教学**：从 column (1) 到 (3) 的变化 → 直观展示 OVB 公式的作用机制

## 反面论点与数据空白

- **C&B 数据的代表性问题**：仅覆盖 30 所 selective colleges——结论对非精英大学、社区学院、未上大学的人不适用。
- **马太效应 (Matthew Effect) 证据**：Dale-Krueger 发现对**低收入家庭学生**，精英大学仍有正溢价——与"平均零效应"形成重要补充（但该交互效应在原始论文中样本量较小）。
- **年龄截断**：数据追踪至 1995 年（1976 年入学群体约 40 岁）——无法捕捉职业生涯**后期**的溢价分化（可能后期才显现）。
- **"选择度组"的测度误差**：Barron's 分类是粗粒度的（6 或 7 类），同一类内大学的真实差异可能被平均掉。
- **反向因果疑虑**：某些学生本就有更高的收入潜力，但选择度组控制是否完全捕捉了这一点——没有实验，无法确证。

## 相关页

- [[回归作为自动匹配]] / [[遗漏变量偏差公式]] / [[条件独立假设CIA]]
- [[教育回报率-因果估计]]
- [[Mastering-Metrics]]
