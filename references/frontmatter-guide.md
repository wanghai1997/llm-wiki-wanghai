# YAML Front Matter 指南

每个 Wiki 页面顶部必须包含：

---

created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [来源文件名1.md, 来源文件名2.md]
tags: [标签1, 标签2]
status: draft 或 consolidated 或 foundation
-------------------------------------------

`status` 含义：

- draft：初步提取，尚待更多来源交叉验证。
- consolidated：多个来源一致支持的论点。
- foundation：不可变底层事实，位于 `foundations/` 目录的页面专属。

## 置信度标注（v2 增强）

`confidence` 评分（0.0-1.0）由以下因子乘积计算：

- 来源可靠性（教材/年鉴=0.95, 顶刊论文=0.85, 工作论文=0.60, 网络文章=0.40）
- 支撑证据数（≥3个独立来源=1.0, 2个=0.85, 1个=0.70）
- 时效性因子（3年内=1.0, 3-5年=0.90, 5-10年=0.75, 10年+=0.60）

`decay_category` 按学科特性分级衰减：

- `persistent`：基础理论（如供求定律），永不主动衰减
  → 所属目录 `foundations/`, 典型 `status: foundation`
- `slow`：应用理论（如产业组织理论），衰减半衰期=10年
  → 所属目录 `concepts/`, 典型 `status: consolidated`
- `normal`：实证发现（如某项政策的效应评估），衰减半衰期=3年
  → 所属目录 `concepts/` 和 `topics/`, 典型 `status: consolidated/draft`
- `fast`：统计数据、市场动态，衰减半衰期=1年
  → 所属目录 `entities/` 和 `topics/state.md`, 典型 `status: draft`

示例：
------

confidence: 0.95
decay_category: persistent
--------------------------
