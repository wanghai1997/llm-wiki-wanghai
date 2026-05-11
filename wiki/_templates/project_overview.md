---
project: 
status: planning  # planning | researching | writing | under-review | revising | finalized
created: 
tags:
  - ars-project
---

# {{项目名称}}

## 课题目标（1-3 句）

- ...

---

## 会话上下文（每次 ARS 会话结束后更新）

> 将此块内容粘贴到 ARS 会话开头，即可恢复上下文。

```
课题：[项目名称]
最新 passport：passports/xxx-xxxx.passport.yaml
ARS_PASSPORT_RESET=ON
当前阶段：Stage N
上次结论：[PASS / 待修] — [一句话总结]
resume_from_passport=<hash>（如有）
本次意图：[下一阶段的目标]
```

| 属性 | 值 |
|------|-----|
| ARS 阶段 | Stage N |
| 阶段结论 | PASS / 待修 / ... |
| 最后 passport | `passports/obsidian-corpus-*.passport.yaml` |
| 最后 resume hash | `resume_from_passport=<hash>` |
| ARS_PASSPORT_RESET | ON / OFF |
| 最后更新 | YYYY-MM-DD HH:MM |

### 当前待办

- [ ] ...
- [ ] ...

---

## 阶段日志

### Stage 1 — RESEARCH（日期）

- **结论**：
- **关键决策**：
- **待办**：

<!-- 回写文献笔记时，复制以下格式到对应文献页的末尾： -->
<!--
## 研究定位
- ARS Stage 1 评估：[核心支撑 / 背景参考 / 方法论借鉴 / 待验证]
- 在本项目 Literature Matrix 中的位置：Theme X（xxx）
- 关键引用点：[论文的哪个论点可以引用该文献的哪个发现]
-->

---

### Stage 2 — WRITE（日期）

- **结论**：
- **大纲要点**：
- **关键决策**：
- **待办**：

---

### Stage 2.5 — INTEGRITY（日期）

- **结论**：
- **发现的问题**：
- **需修正的文献**（citekey + 错误类型）：

<!-- 如发现某文献引用信息有误，直接修正 Obsidian 中对应笔记的 frontmatter，然后重新运行 sync。 -->
<!-- 修正完成后在此记录： -->
<!--
- [ ] [citekey] year: 2023 → 2024（已在 Obsidian 中修正并重新 sync）
- [ ] [citekey] authors 补充 missing given name
-->

---

### Stage 3 — REVIEW（日期）

- **结论**：
- **审稿意见要点**：
- **待办**：

<!-- 审稿意见回写文献笔记时，复制以下格式到对应文献页： -->
<!--
## 评审反馈
- Reviewer N（角色）：[具体问题 / 评价]
- 严重程度：[CRITICAL / MAJOR / MINOR]
- 我的回应：[接受 / 部分接受 / 反驳] — [理由 + 修改方案]
- 关联修订项：R[N]
-->

---

### Stage 4 — REVISE（日期）

- **结论**：
- **修订要点**：
- **待办**：

<!-- 每次修订决策记录格式： -->
<!--
### 修订决策 R[N]（日期）
- 来源：[Reviewer N / DA / EIC / 自查]
- 原文问题：[具体描述]
- 修订方案：[具体描述]
- 影响范围：[哪些章节 / 段落]
- 状态：[已完成 / 待验证]
-->

---

### Stage 3' — RE-REVIEW（日期）

- **结论**：
- **残留问题**：
- **待办**：

---

### Stage 4' — RE-REVISE（日期）

- **结论**：
- **修订要点**：
- **待办**：

---

### Stage 4.5 — FINAL INTEGRITY（日期）

- **结论**：
- **发现的问题**：
- **待办**：

---

### Stage 5 — FINALIZE（日期）

- **输出格式**：
- **最终文件路径**：

---

### Stage 6 — PROCESS SUMMARY（日期）

- **协作质量评估**：
- **AI 自省报告要点**：
- **项目归档路径**：

---

## 关键风险与未解决问题

- [ ] ...
- [ ] ...

## 相关笔记

```dataview
LIST FROM [[{{项目名称}}]] AND #literature-note
```
