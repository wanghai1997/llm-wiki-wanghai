# 两段式摄入完整流程

## 第一阶段：分析

1. 读取 `purpose.md` 和 `wiki/index.md`。
2. 通读 `raw/inbox/` 中目标文档。
3. 创建 `wiki/_analysis_[文档名].md`，包含：
   - 核心实体（建议页面名）
   - 核心概念（建议页面名）
   - 与现有 Wiki 页面的链接点（列出将更新的页面）
   - 矛盾发现（新内容 vs 已有断言）
   - 知识缺口（新概念无对应页面）
   - 发散性检查初稿（反面论点）
4. **暂停，等待用户确认**（用户可回复“继续”、“跳过”、“修改”）。

## 第二阶段：生成

1. 基于确认的分析创建/更新 `entities/`、`concepts/`、`topics/` 页面。
2. 更新 `wiki/index.md`。
3. 若影响综合认知，更新 `wiki/state.md`。
4. 概念页必须包含“反面论点与数据空白”小节。
5. 按 `references/log-format.md` 追加日志。
6. 将源文件从 `raw/inbox/` 移动到 `raw/archive/`。
7. 删除或标记 `_analysis_[文档名].md`。
