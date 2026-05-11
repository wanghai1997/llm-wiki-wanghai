# LLM Wiki — 个人知识库

结构化个人知识库，由 LLM 辅助维护，遵循"不内容发明、可追溯至源文件"原则。

## 仓库结构

```
├── purpose.md              # Wiki 目标定义与覆盖领域
├── CLAUDE.md               # LLM 维护者核心指令
├── README.md               # 本文件
├── .gitignore              # 排除 raw/ PDF 大文件
├── nightly-task.cmd         # 夜间自动维护脚本
│
├── references/             # 操作流程参考文档
│   ├── ingest-workflow.md   # 两段式摄入流程
│   ├── lint-checklist.md    # Lint 健康检查清单
│   ├── log-format.md        # 日志格式规范
│   └── ...
│
├── scripts/                # 自动化脚本
│
├── wiki/                   # Wiki 主体（Obsidian Vault）
│   ├── index.md            # 全局索引
│   ├── state.md            # 领域状态综合快照
│   ├── log.md              # 操作日志（只追加）
│   ├── entities/           # 人物 / 机构实体页
│   ├── concepts/           # 概念页（顶层跨领域概念）
│   ├── topics/             # 主题导览页
│   ├── literature/         # 文献笔记
│   ├── _templates/         # 页面模板
│   ├── raw/                # 源文件（PDF/DOCX 不入库，外部存储）
│   │   ├── inbox/          # 待处理入口
│   │   └── archive/        # 已处理归档
│   └── foundations/        # 各学科基础理论层
│       ├── microeconomics/         # 微观经济学（Nechyba）
│       ├── macroeconomics/         # 宏观经济学（Mankiw）
│       ├── econometrics/           # 计量经济学（MM + Wooldridge）
│       ├── china-monetary-policy/  # 中国货币政策（孙国峰）
│       ├── management/             # 管理学（Robbins & Coulter）
│       ├── green-economics/        # 绿色经济学（Nordhaus）
│       ├── ecological-products/    # 生态产品价值实现（中国论文）
│       ├── digital-economy/        # 数字经济（江小涓）
│       ├── financial-economics/    # 金融经济学（徐高）
│       ├── design-thinking/        # 设计思维（Tim Brown）
│       └── producer-services/      # 生产性服务业（中国论文）
│
└── .claude/                # Claude Code 配置
    ├── skills/             # 技能文件
    └── settings.local.json
```

## 覆盖领域

- 经济学（微观 / 宏观 / 计量 / 金融）
- 管理学
- 生态产品价值
- 产品设计与用户体验
- 创新创业
- 投资

## 维护方式

本仓库由 LLM 按 `CLAUDE.md` 指令维护。三大核心操作：

| 操作 | 触发 | 流程 |
|------|------|------|
| Ingest | "处理 inbox" | 两段式：分析→确认→生成 |
| Query | 提问 | 读取索引定位，综合回答 |
| Lint | "检查" | 健康检查 → 报告 → 修复 |

源文件入口为 `wiki/raw/inbox/`，摄入后移入 `wiki/raw/archive/`。所有操作记录在 `wiki/log.md`。
