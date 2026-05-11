# ARS 产出 → Wiki 回写流程

> 本文档定义 ARS 流水线产出如何结构化地写回 Wiki，确保知识库随每次 ARS 会话持续"增厚"。

## 回写场景与操作

### 场景 1：Research Brief → 文献笔记

**触发时机**：ARS Stage 1 结束，生成 Research Brief 后。

**操作**：
1. 识别 Research Brief 中评估的关键文献
2. 在 Wiki 中定位对应文献的笔记页（`wiki/raw/archive/` 或 `wiki/foundations/*/concepts/`）
3. 在笔记末尾追加 `## 研究定位` 节：

```markdown
## 研究定位
- ARS Stage 1 评估：该文属于「核心支撑文献」，证据等级 III
- 在你的 Literature Matrix 中的位置：Theme A（xxx）+ Theme C（yyy）
- ARS 评估日期：YYYY-MM-DD
```

**Wiki 页面类型**：source（`raw/archive/`）、concept（`foundations/*/concepts/`）

---

### 场景 2：审稿意见 → 文献/概念笔记

**触发时机**：ARS Stage 3（评审）结束后。

**操作**：
1. 提取每条评审意见中涉及的文献引用或概念
2. 在 Wiki 中定位对应页面
3. 追加 `## 评审反馈` 节：

```markdown
## 评审反馈
- Reviewer N（方法论）指出：<具体问题>
- Reviewer N（文献）建议：<补充/替换建议>
- EIC 建议：<整体方向>
- ARS 评审日期：YYYY-MM-DD
```

**Wiki 页面类型**：concept、source

---

### 场景 3：修订决策 → 项目总览

**触发时机**：ARS Stage 4 每次修订决策后。

**操作**：
1. 在项目总览笔记（`wiki/state.md` 或专用项目笔记）的「修订决策日志」节追加：

```markdown
### 修订决策 R<N> (YYYY-MM-DD)
- **原文问题**：<问题描述>
- **修订方案**：<具体修改>
- **影响范围**：<涉及的章节/段落>
- **触发来源**：Reviewer N / Self-check / Stage 2.5 完整性检查
```

**Wiki 页面类型**：state.md（项目总览）

---

### 场景 4：完整性检查发现 → 文献笔记修正

**触发时机**：ARS Stage 2.5 或 4.5 完整性检查后。

**操作**：
1. 如果发现某篇文献的元数据有误（年份、DOI、作者拼写）
2. 直接修正 Wiki 中对应页面的 frontmatter
3. 重新运行 `scripts/sync-wiki-corpus.sh` 更新 passport

**修正示例**：
```yaml
# 修正前
authors: Zhang, W.

# 修正后
authors: Zhang, Wei; Lin, Qiang
year: 2024
doi: 10.1016/j.compedu.2024.105001
```

---

### 场景 5：新洞察 → 新建 Wiki 页面

**触发时机**：ARS 会话中产生了值得长期保留的新概念/发现。

**操作**：
1. 新建 Wiki 概念页，遵循 `references/frontmatter-spec.md` 规范
2. 在 `sources` 字段中标注 `ARS Session YYYY-MM-DD` 作为来源
3. 在 `wiki/log.md` 追加操作记录
4. 重新运行同步生成新 passport

---

## 回写检查清单

每次 ARS 会话结束后确认：

- [ ] 项目总览中的 checkpoint 已更新（阶段号、结论、passport hash）
- [ ] Research Brief 中的关键文献评估已写回对应笔记
- [ ] 审稿意见已关联到相关文献/概念笔记
- [ ] 修订决策已记录在项目总览
- [ ] 如有元数据修正，已重新同步 passport
- [ ] 如有新概念产出，已新建 Wiki 页面并更新 index.md

## 核心原则

**ARS 是执行引擎，Wiki 是记忆体。每次 ARS 会话的结论必须写回 Wiki——否则记忆断裂。**
