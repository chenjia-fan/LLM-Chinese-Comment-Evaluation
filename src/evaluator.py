import multiprocessing
import json
import os
import time
import re


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
# 假设你的目录结构是：
# LLM-Evaluation-Project/
# ├── data/ (存放 jsonl)
# ├── src/ (存放此脚本)
# ├── test_results/
# └── results/
BASE_DIR = os.path.dirname(CURRENT_DIR)

# 自动定位数据文件
OFFICIAL_CHINESE_FILE = os.path.join(BASE_DIR, "data", "HumanEval-textprompts.jsonl")
ENGLISH_ORIGINAL_FILE = os.path.join(BASE_DIR, "data", "human-eval-v2-20210705.jsonl")

# 待评测代码目录
GENERATED_CODE_DIR = os.path.join(BASE_DIR, "test_results")

# 结果输出到专门的 results 文件夹
OUTPUT_PATH = os.path.join(BASE_DIR, "results")
os.makedirs(OUTPUT_PATH, exist_ok=True)
RESULT_REPORT_FILE = os.path.join(OUTPUT_PATH, "research_deepseek_final_report.json")

TIMEOUT_SECONDS = 3
# =============================================================

def run_code_isolated(code, test_suite, queue):
    try:
        # 隔离全局变量，防止模型代码污染评测脚本
        clean_globals = {"__builtins__": __builtins__}
        test_script = test_suite["test"]
        entry_point = test_suite["entry_point"]

        full_script = f"{code}\n\n{test_script}"
        if f"check({entry_point})" not in test_script:
            full_script += f"\ncheck({entry_point})"

        exec(full_script, clean_globals)
        queue.put({"status": "PASS", "message": "All tests passed"})

    except AssertionError as e:
        queue.put({"status": "FAIL_LOGIC", "message": f"Assertion error"})
    except Exception as e:
        queue.put({"status": "FAIL_RUNTIME", "message": f"{type(e).__name__}"})

def main_evaluator():
    print(f"🚀 启动科研级评测系统...")
    print(f"📂 当前工作目录认定为: {BASE_DIR}")

    # 1. 加载英文标准库
    english_standards = {}
    if not os.path.exists(ENGLISH_ORIGINAL_FILE):
        print(f"❌ 错误：找不到英文标准文件 {ENGLISH_ORIGINAL_FILE}")
        return

    with open(ENGLISH_ORIGINAL_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            tid = data["task_id"].replace("/", "_")
            english_standards[tid] = {"test": data["test"], "entry_point": data["entry_point"]}

    # 2. 扫描已生成的代码文件
    if not os.path.exists(GENERATED_CODE_DIR):
        print(f"❌ 错误：找不到代码目录 {GENERATED_CODE_DIR}")
        return

    def extract_number(f):
        s = re.findall(r'\d+', f)
        return int(s[0]) if s else 0

    code_files = [f for f in os.listdir(GENERATED_CODE_DIR) if f.endswith(".py")]
    code_files.sort(key=extract_number)

    # 3. 评测循环
    all_results = []
    summary_stats = {"PASS": 0, "FAIL_LOGIC": 0, "FAIL_SYNTAX": 0, "FAIL_RUNTIME": 0, "TIMEOUT": 0}

    print(f"📊 共有 {len(code_files)} 个样本待评测...\n")

    for file_name in code_files:
        task_id = file_name.replace(".py", "")
        if task_id not in english_standards:
            continue

        with open(os.path.join(GENERATED_CODE_DIR, file_name), 'r', encoding='utf-8') as f:
            generated_code = f.read()

        result_queue = multiprocessing.Queue()
        process = multiprocessing.Process(
            target=run_code_isolated,
            args=(generated_code, english_standards[task_id], result_queue)
        )

        process.start()
        process.join(TIMEOUT_SECONDS)

        if process.is_alive():
            process.terminate()
            process.join()
            current_res = {"status": "TIMEOUT", "message": "Maximum execution time exceeded"}
        else:
            current_res = result_queue.get() if not result_queue.empty() else {"status": "FAIL_RUNTIME", "message": "Crash"}

        summary_stats[current_res["status"]] += 1
        all_results.append({"task_id": task_id, "status": current_res["status"]})
        print(f"[{task_id}] {current_res['status']}")

    # 4. 保存报表
    final_output = {
        "metadata": {"timestamp": time.ctime(), "pass_rate": f"{(summary_stats['PASS'] / len(all_results) * 100):.2f}%"},
        "summary": summary_stats,
        "details": all_results
    }

    with open(RESULT_REPORT_FILE, 'w', encoding='utf-8') as f:
        json.dump(final_output, f, indent=4, ensure_ascii=False)

    print(f"\n✅ 评测完成！结果已存入: {RESULT_REPORT_FILE}")
    print(f"📈 最终 Pass@1: {final_output['metadata']['pass_rate']}")

if __name__ == "__main__":
    main_evaluator()