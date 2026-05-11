---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [concept, microeconomics, foundations, externality, taxation, DWL]
confidence: medium
decay_category: medium
status: foundation
---

# Pigou税与DWL

> Pigouvian Taxes and Deadweight Loss

Pigou 税与扭曲税在 DWL 效应上**截然相反**：扭曲税**创造** DWL，Pigou 税**消除** DWL。这是理解税收效率性质的关键分水岭。

## 扭曲税创造 DWL（回顾 Batch 3）

在完全竞争市场（无外部性）中：
- 税前均衡：$P^*, Q^*$（社会最优）。
- 征收从量税 $t$ → 消费者支付 $P_d = P_s + t$，生产者获得 $P_s$。
- 交易量降至 $Q_t < Q^*$。
- **DWL** = 需求曲线与供给曲线之间、从 $Q_t$ 到 $Q^*$ 的三角形 = 因税收而"消失"的互惠交易。

## Pigou 税消除 DWL

在存在负外部性的市场中：
- **无税市场均衡**：$P_{\text{市场}}, Q_{\text{市场}}$，由 $P = PMC$ 决定。
- 但 $PMC < MSC$ → $Q_{\text{市场}} > Q_{\text{社会最优}}$ → **已有 DWL**（外部性导致的效率损失）。
- 征收 Pigou 税 $t^* = MEC(Q^*)$ → 厂商面对的 $PMC' = PMC + t^* = MSC$。
- 新均衡：$P' = MSC$ → $Q' = Q_{\text{社会最优}}$。
- **结果**：消除了外部性导致的 DWL，达到社会最优。

### 图形对照

```
扭曲税（无外部性）：          Pigou 税（有外部性）：

价格                            价格
 │     S                       │     MSC = PMC + MEC
 │      ╲                      │        ╱
 │  P_d  ╲                     │       ╱
 │──┼────╲                     │  P'  ╱ PMC
 │  │     ╲                    │──┼──╱
 │  │  P*  ╲                   │  │  ╱
 │──┼──────╲                   │  │ ╱
 │  │  P_s  ╲                  │  │╱
 │  │        ╲                 │  ├──────────
 │  └────┼───╲── D             │  │  Q*  Q_market
 │       Q_t Q*                │
 │                             │
```

- **左图（扭曲税）**：税把交易量从 $Q^*$ 压到 $Q_t$ → **创造** DWL（三角形 $Q_t$-$Q^*$）。
- **右图（Pigou 税）**：税把交易量从 $Q_{\text{market}}$ 压到 $Q^*$ → **消除** DWL（三角形 $Q^*$-$Q_{\text{market}}$）。

## 关键定性结论

| 情形 | 税收类型 | 对 DWL 的影响 | 对社会剩余的影响 |
|---|---|---|---|
| 无外部性 | 扭曲税 | 创造 DWL | 减少 |
| 有负外部性 | Pigou 税 | 消除 DWL | 增加 |
| 有正外部性 | Pigou 补贴 | 消除 DWL | 增加 |

## 信息要求与实施困难

Pigou 税的福利增益取决于税率是否精确等于 MEC：
- $t < MEC$：外部性仍过度，DWL 部分消除。
- $t = MEC$：完全消除 DWL（理论上）。
- $t > MEC$：过度矫正 → **反向 DWL**（生产/消费不足）。

Weitzman（1974）的经典论文证明：当 MEC 曲线陡峭而边际减排成本曲线平坦时，**数量管制**（quota）优于价格管制（tax）；反之则 tax 更优。这被称为"价格 vs 数量"之争。

## 反面论点与数据空白

- 教材 Ch 1-15 的"几乎所有税都低效"叙事到 Ch 21 才得到修正——读者可能在读到 Ch 21 之前已形成根深蒂固的"税收 = 低效"印象。这是 [[经济学六大教训]] / [[无谓损失DWL]] [BIAS] 的结构性后果。
- Pigou 税的"消除 DWL"结论依赖于**完全竞争**假设。若市场本身存在垄断势力，Pigou 税与垄断扭曲的交互复杂（双重扭曲问题）。
- 现实中最优 Pigou 税率随时间变化（技术进步改变 MEC）→ 静态税率无法持续最优。
- 缺乏大规模 Pigou 税的严格因果福利评估：碳税的环境效益（第一重红利）难以与经济增长、技术变革等混淆因素分离。

## 相关页

- [[Pigou税]] — Pigou 税的上位概念
- [[无谓损失DWL]] — Batch 3 建立的基本概念
- [[总额税与扭曲税]] — 税收分类框架
- [[土地税]] — 另一类 DWL ≈ 0 的税收
- [[外部性]] — Pigou 税要矫正的市场失灵
