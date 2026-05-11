---
created: 2026-05-02
updated: 2026-05-02
sources: ["Microeconomics an intuitive approach with calculus (Nechyba, Thomas J) .pdf"]
tags: [概念, microeconomics, foundations, batch3, 风险与状态偏好]
confidence: medium
decay_category: medium
status: foundation
---

# u(x)凹性

> 基础效用函数 $u$ 的凹性 ($u'' \lt 0$) 是 vN-M 期望效用框架中**风险厌恶**的数学等价。Jensen 不等式:对凹 $u$,$u(\mathbb{E}[\tilde x]) \ge \mathbb{E}[u(\tilde x)]$。$u'' \lt 0$ 程度决定风险厌恶强度(Arrow-Pratt 度量)。

## 核心等价

$$\text{风险厌恶} \quad \Longleftrightarrow \quad u''(x) \lt 0 \quad \forall x$$

Jensen 不等式:对凹函数 $u$,
$$u(\mathbb{E}[\tilde x]) \ge \mathbb{E}[u(\tilde x)]$$

即"确定收入的效用 ≥ 赌局的期望效用"。

## 直觉:边际效用递减

凹 $u$ = 边际效用 $u'(x)$ 递减:
- 从 100 → 200 的效用增益 < 从 0 → 100 的效用增益。
- 损失 100 的效用损失 > 赢得 100 的效用增益。

→ 主体偏好确定 100 而非 50% 概率赢 200 + 50% 概率赢 0。

## 常见凹函数形式

| 形式 | 公式 | ARA | RRA |
|---|---|---|---|
| **CARA** | $u(x) = -e^{-\alpha x}/\alpha$ | $\alpha$ | $\alpha x$ |
| **CRRA** | $u(x) = x^{1-\gamma}/(1-\gamma)$ | $\gamma/x$ | $\gamma$ |
| **对数** | $u(x) = \ln x$ | $1/x$ | $1$ |
| **二次** | $u(x) = x - bx^2$ | $\frac{2b}{1-2bx}$ | $\frac{2bx}{1-2bx}$ |
| **混合型** | 实证估计 | 变量 | 变量 |

## 风险中性 vs 风险偏好

- **风险中性**($u'' = 0$):$u(x) = ax + b$。最大化期望效用 = 最大化期望收入。金融机构、重复博弈中的大玩家近似风险中性。
- **风险偏好**($u'' \gt 0$):$u$ 凸。赌博、彩票购买者表现出风险偏好(在特定区域)。Kahneman-Tversky 1979 prospect theory 的价值函数在损失区是凸的(loss-seeking)。

## 与确定性等价的关系

凹 $u$ 使 CE $\lt \mathbb{E}[\tilde x]$:
- 风险厌恶者愿意接受**低于期望收入**的确定收入,以消除风险。
- 差额 = 风险溢价 $RP = \mathbb{E}[\tilde x] - CE$。

详见 [[确定性等价]] / [[风险溢价]]。

## 与保险需求的关系

凹 $u$ 意味着风险厌恶者购买保险:
- 精算公平保险($\text{premium} = \text{expected loss}$):完全保险。
- 精算不公平保险($\text{premium} \gt \text{expected loss}$):部分保险,保险量随 loading 增加而减少。

详见 [[精算公平保险]] / [[完全保险]]。

## 反面论点与数据空白

- **凹 $u$ 不能捕捉损失厌恶**:Kahneman-Tversky 1979 的价值函数在收益区是凹的($\alpha \approx 0.88$),在损失区是凸的($\beta \approx 0.88$),且有 kink 在 $x = 0$(损失厌恶 $\lambda \approx 2.25$)。单一凹函数 $u$ 无法同时捕捉这三个特征。
- **Rabin 校准批评**:Rabin 2000 *Econometrica* 证明小风险下的风险厌恶行为与大风险下 vN-M 预测严重不一致 → 简单的凹 $u$ 可能不是正确的模型。
- **状态依赖性**:同一个人的 $u$ 在不同状态下(健康 / 病;就业 / 失业)形状不同。教材假设状态独立。
- **异质性**:Barsky et al. 1997 *American Economic Review* 的 HRS 估计显示 RRA 从 $-1$ 到 $+10$ 都有,群体分布非正态。
- **数据空白**:Barsky et al. 1997 / Andersen et al. 2008 / Harrison-Rutström 2009 的大量实证,教材极度压缩。

## 相关页

- 上游:[[风险厌恶]] / [[期望效用函数]] / [[vN-M期望效用]]
- 应用:[[确定性等价]] / [[风险溢价]] / [[精算公平保险]] / [[完全保险]]
- 主题:[[风险与状态偏好]]
