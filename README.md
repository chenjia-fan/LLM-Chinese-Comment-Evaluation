# 🚀 LC2E: LLM-Chinese-Code-Evaluation
> **基于 Inspur Yuan2.0-M32 (HumanEval-CN) 基准的大模型中文编程力评测**

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![LLM](https://img.shields.io/badge/Model-DeepSeek--R1%20%7C%20Qwen--Max-orange.svg)
![Status](https://img.shields.io/badge/Pass@1-96.34%25-brightgreen.svg)

## 📌 项目简介 (Project Overview)
本项目建立了一个自动化的代码评测流水线，专门用于评估大语言模型（LLM）在中文指令下的编程正确性。

### 📚 数据集说明 (Dataset Attribution)
本项目采用的测试集为 `HumanEval-textprompts.jsonl`，该数据由 **浪潮 (Inspur) Yuan2.0-M32** 项目团队维护。
- **来源**：基于原始 [OpenAI HumanEval](https://github.com/openai/human-eval) 数据集。
- **构造方式**：利用 GPT-4 进行高质量语义翻译，保留了原始任务的严谨性，同时消除了中英语义转换的歧义。
- **定位**：主要用于衡量模型在中文编程任务（Chinese Coding Tasks）上的语义理解与逻辑实现能力。

---

## 📊 实验结果 (Experimental Results)
评测日期：2026-03-08 | 指标：Pass@1 (Greedy Decoding)

| 模型 (Model) | 提示词来源 (Dataset) | Pass@1 (Acc) | 备注 |
| :--- | :--- | :--- | :--- |
| **DeepSeek-Reasoner (R1)** | **Yuan2.0-M32 (CN)** | **96.34%** | Reasoning-Chain |
| Qwen-Max | Yuan2.0-M32 (CN) | 待更新 | Aliyun Flagship |
| Llama-3-70B | HumanEval (EN) | 82.0% (Ref) | Original English |

---

## 🏗️ 实验工作流 (Evaluation Workflow)



1. **指令工程 (Instruction Engineering)**：
   - 提取自浪潮数据集的 `prompt` 字段。
   - 采用系统级提示词约束模型仅输出 Python 函数体。

2. **代码生成 (Generation)**：
   - 调用模型 API，设置 `temperature=0.01` 降低随机性。
   - 原始响应内容（含 Token 消耗、时间戳、Request ID）持久化存储于 `raw_logs/`。

3. **沙箱评测 (Sanitised Execution)**：
   - 利用 `multiprocessing` 模块构建隔离执行环境。
   - 注入 `clean_globals` 命名空间，严格防止题目间的变量污染。

---

## 📁 目录结构 (Project Structure)
```text
.
├── data/               # 存放源数据 (包含浪潮 Yuan2.0-M32 翻译版)
├── src/                # 核心脚本 (Generator 生成器 & Evaluator 评测器)
├── test_results/       # 模型生成的原始代码 (.py)
├── raw_logs/           # API 原始 JSON 响应 (科研诚信证据链)
└── results/            # 最终生成的自动化评测报告 (.json)
