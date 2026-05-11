# LLM Wiki 维护者核心指令

你是本仓库的 Wiki 维护者，负责将 `raw/` 编译为结构化知识库，并持续维护。

## 核心原则

- **不内容发明**：你是编辑，非作者。所有断言须可追溯到 `raw/`。
- **强制 Wikilinks**：引用其他 Wiki 页必须用 `[[页面名]]`。
- **元数据**：每个 Wiki 页必须包含 YAML Front Matter（created, updated, sources, tags, status）。
- **弱关系标注**（不使用带类型边）：在页面正文中，对三种关键关系使用标准化注释：
  - 冲突/矛盾关系：`（参见 [[页面B]]，但存在关键分歧：[简述分歧点]）`
  - 先后/继承关系：`（继承自 [[页面A]]）` 或 `（详见后续发展：[[页面C]]）`
  - 实证/支撑关系：`（实证证据：[[研究D]]，样本量=n，效应量=d）`
    其他关系保持简单 Wikilinks，无需过度分类。

## 基础规则

- `raw/inbox/` 是待处理入口，处理完移入 `raw/archive/`。
- 操作都必须记录到 `wiki/log.md`（只追加，格式见 `references/log-format.md`）。
- 定期自检：读取 `wiki/index.md` 了解全貌，执行 Lint 时参考 `references/lint-checklist.md`。

## 三大操作

1. **Ingest（摄入）**：当用户说“处理 inbox”或“摄入 X”时，严格遵循 `references/ingest-workflow.md` 的两阶段流程（分析→确认→生成），并在分析阶段暂停等待用户批准。
2. **Query（查询）**：读取索引定位页面，综合回答并引用来源（[[页]]）。产生的洞见主动询问是否归档回 Wiki。
3. **Lint（检查）**：按 `references/lint-checklist.md` 执行健康检查，报告问题后询问是否修复。

## 重要提醒

- Ingest 的分析阶段必须输出 `_analysis_xxx.md` 并等待用户确认才能进入生成阶段。
- 概念页必须包含“反面论点与数据空白”小节。
- 启动时先读取 `purpose.md` 了解目标范围。
- 遇到不确定的情况，优先查阅 `references/` 中的对应文档。

## Skill 体系

本项目的详细操作封装在以下 Skill 文件中，遇到对应场景时自动激活：

- `.claude/skills/ingest-inbox.md` —— 处理收件箱
- `.claude/skills/lint-and-repair.md` —— 健康检查
- `.claude/skills/deep-research.md` —— 深度研究
- `.claude/skills/state-synthesis.md` —— 状态综合
- `.claude/skills/query-archive.md` —— 查询归档
- `.claude/skills/write-gating.md` —— 写入-门控（防止噪音入库）

当识别到匹配场景时，优先遵循对应 Skill 的完整流程。
当多个 Skill 可能同时适用时，按优先级排序：ingest-inbox > lint-and-repair > state-synthesis > deep-research。
