@echo off
cd /d D:\llm-wiki-wanghai

echo [%date% %time%] 夜间维护开始...

REM Step 0: Sync wiki corpus to ARS passport
echo [%date% %time%] 同步 Wiki → Passport...
python scripts\adapters\wiki.py --output-dir passports 2>&1

echo [%date% %time%] 开始 Claude Code 维护...
cd wiki

REM 使用 Claude Code 非交互模式执行维护指令
call claude -p "请按顺序执行以下夜间维护任务（v2 增强版），完成后输出'NIGHTLY MAINTENANCE DONE'：
1. 【写入-门控检查】扫描 `raw/inbox/`，若存在文件则按 write-gating Skill 执行门控判定后摄入。
2. 【Lint + 衰减审计】执行完整 Lint 检查，并额外审计：
   - 所有 `decay_category: fast` 且 `updated` 超过 6 个月的页面，标记 `[MAYBE_STALE]`
   - 所有 `status: draft` 且超过 90 天未被引用的页面，标记 `[INACTIVE]`
   - 检查是否有 `[REFUTED]` 页面被新来源重新支持，若有则建议复活
   - 自动修复可修复项。
3. 【状态综合更新】根据最近所有的摄取、门控判定和衰减审计结果，更新 state.md（核心共识、活跃争论、知识缺口、最近重要更新）。
4. 【图谱密度审计】（如果页面数 ≥ 200）使用 Obsidian MCP 统计每个页面的链接数，生成密度分布报告，识别出链接密度低于 2 的页面作为潜在孤立问题。
5. 在 wiki/log.md 末尾追加汇总日志。
" > D:\llm-wiki-wanghai\nightly-log.txt 2>&1

echo [%date% %time%] 维护结束，日志已保存至 D:\llm-wiki-wanghai\nightly-log.txt
exit
