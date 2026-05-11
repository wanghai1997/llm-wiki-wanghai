---
created: 2026-05-03
updated: 2026-05-03
sources: ["Macroeconomics (Ninth Edition) (N. Gregory Mankiw) .pdf, Ch 5 Appendix"]
tags: [entity, person, economist, monetary-economics, hyperinflation]
confidence: medium
decay_category: medium
status: foundation
---

# Phillip Cagan

> **一句话画像**:Phillip Cagan(1927-2012),哥伦比亚大学经济学家,NBER 货币史学者。其 1956 论文 *The Monetary Dynamics of Hyperinflation* 首次以严谨数据建模研究 7 次恶性通胀(德国、奥地利、匈牙利、波兰、苏联、希腊、中国国统区),提出 **Cagan 货币需求函数**,成为 [[恶性通胀]] 与 [[铸币税与通胀税]] 研究的奠基之作。

## 在教材中的位置

- 来源:[[Macroeconomics-Mankiw-9e]] Ch 5 附录 *The Cagan Model: How Current and Future Money Affect the Price Level*
- Mankiw 直接以 Cagan 模型作为理性预期下价格水平决定的标准展示

## 核心学术贡献

### 1. Cagan 货币需求函数(1956)

$$ \ln(M/P)_t = -\gamma \cdot \pi_t^e + \text{const} $$

- 实际货币余额需求随**预期通胀**指数下降
- $\gamma$ 是通胀半弹性,Cagan 在七次恶性通胀样本中估计为 5-50
- 此函数+理性预期使 Mankiw Ch 5 附录得到:
$$ p_t = \frac{1}{1+\gamma} \sum_{s=t}^{\infty} \left(\frac{\gamma}{1+\gamma}\right)^{s-t} \mathbb{E}_t m_s $$
- 即**当前价格 = 当前及未来预期货币供给的加权平均**
- 这是现代理性预期 + 货币模型的雏形,直接影响 [[Robert Lucas]] 1972

### 2. 七次恶性通胀样本

Cagan 1956 研究的七次案例:
| 国家 | 时期 | 月度通胀峰值 |
|---|---|---|
| 奥地利 | 1921-22 | ~134% |
| 德国 | 1922-23 | ~32,400% |
| 匈牙利 1 | 1923-24 | ~98% |
| 匈牙利 2 | 1945-46 | ~$4.19 \times 10^{16}\%$(史上最高) |
| 波兰 | 1923 | ~275% |
| 俄罗斯 | 1921-24 | ~213% |
| 希腊 | 1944 | ~85,500% |

后续研究扩展样本:1985 Bolivia / 1989 阿根廷 / 1990s 巴西 / 2008-09 津巴布韦 / 2018+ 委内瑞拉。详见 [[恶性通胀]]。

### 3. 通胀税收益曲线

- 在 Cagan 模型中,政府通胀税收入 = $\pi \cdot M/P$
- 由于 $M/P$ 随 $\pi^e$ 下降,收入存在峰值——这是 [[铸币税与通胀税]] 的拉弗曲线雏形
- 政策含义:试图用印钞融资过头会陷入"通胀税收入下降"的恶性循环

## 与"理性预期革命"的关系

- Cagan 1956 假设**适应性预期**(adaptive expectations):$\pi^e_{t+1} = \lambda \pi_t + (1-\lambda)\pi^e_t$
- [[Robert Lucas]] / [[Thomas Sargent]] 1970s 用**理性预期**重做 Cagan 模型,得到不同的政策含义(Sargent 1982 *The Ends of Four Big Inflations* 分析德、奥、匈、波四次恶性通胀终结,论证可信政策切换可立即终止恶性通胀)
- Cagan 的实证传统 + Lucas 的理论革命共同形成现代货币经济学

## 反面论点与数据空白

- **样本偏差**:Cagan 1956 七案例都是战争 / 战败 / 革命后的极端情形,其外推到温和通胀(年化 5-20%)的有效性存疑。
- **适应性预期假设过时**:Cagan 假设回看式预期,Lucas 革命后被理性预期取代——但 2008 后行为宏观([[Robert Shiller]] / [[George Akerlof]] [Akerlof 已在微观侧 entities 中])再次质疑理性预期的实证基础,可能恢复部分 Cagan 适应性传统。
- **货币需求函数的稳定性**:Cagan 假设半弹性 $\gamma$ 跨国稳定。但实际数据显示 $\gamma$ 受金融制度、外汇可得性、美元化程度影响巨大——使简单 Cagan 模型在政策决策中作用有限。
- **未涵盖的现代恶性通胀**:Cagan 1956 数据库未包括 1980s 拉美、津巴布韦 2008-09、委内瑞拉 2018+——后两者的"加密美元化"使货币替代成为新动力学,Cagan 框架需要重要扩展。
- **regional-bias**:Cagan 七案例集中在 20 世纪上半叶欧洲与一项中国案例;非洲、拉美、南亚的恶性通胀案例缺失。[regional-bias]

## 相关页

- 概念:[[恶性通胀]] / [[铸币税与通胀税]] / [[货币数量论]]
- 同事 / 后继者:[[Milton Friedman]](Cagan 在 Friedman 1956 论文集发表此文)/ [[Robert Lucas]] / [[Thomas Sargent]]
- 教材:[[Macroeconomics-Mankiw-9e]] Ch 5 附录
