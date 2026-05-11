---
created: 2026-05-02
updated: 2026-05-02
sources: ["黄仁勋最新演讲：驱动未来增长的底层商业逻辑——“Token工厂经济学”.md"]
tags: [企业, 半导体, AI推理, 被收购]
status: draft
---

# Groq

## 简介

确定性数据流处理器（Deterministic Dataflow Processor）厂商，专注于 AI 推理领域。**已被 [[NVIDIA]] 收购并获得技术授权**（[[黄仁勋]] GTC 2026 演讲披露）。

## 技术特征

- 静态编译 + 编译器调度。
- 大量片上 SRAM（500 MB），不依赖外置 HBM。
- 极低延迟、极高 Token 生成速度，专为单一推理工作负载优化。

## 与 [[Vera Rubin]] 的非对称分离推理

[[NVIDIA]] 通过 [[Dynamo]] 软件将推理管线解耦：

| 阶段 | 承担硬件 | 原因 |
| --- | --- | --- |
| 预填充（Prefill） + 注意力解码 | Vera Rubin（288 GB 内存） | 需要大量算力与 KV Cache 存储 |
| 前馈网络解码（Token 生成） | Groq（500 MB SRAM） | 需要极高带宽与低延迟 |

来源给出的配置建议：

- 高吞吐工作负载 → 100% Vera Rubin。
- 大量高价值 Token 生成（如代码生成）→ 25% Groq + 75% Vera Rubin。

## 产品

- **Groq LP30**：由三星代工，已进入量产，预计 2026 年 Q3 出货。
- **LP40**：将集成到 Feynman 时代，由 NVIDIA 与 Groq 团队联合打造。

## 局限

- 内存容量小（500 MB SRAM），难以独立承载大模型参数与 KV Cache。
- 在多样化推理负载下需配合 NVIDIA 系统才能规模化部署。

## 相关页面

- [[NVIDIA]]、[[Vera Rubin]]（NVIDIA 系统）、[[Token工厂经济学]]、[[极致协同设计]]
