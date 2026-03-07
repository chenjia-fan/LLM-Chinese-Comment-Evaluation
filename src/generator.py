import json
import os
import time
from openai import OpenAI
from dotenv import load_dotenv


current_script_path = os.path.abspath(__file__)
# 获取 src 目录

src_dir = os.path.dirname(current_script_path)
# 获取项目根目录
BASE_DIR = os.path.dirname(src_dir)

# 统一定义基于根目录的绝对路径
INPUT_FILE = os.path.join(BASE_DIR, "data", "HumanEval-textprompts.jsonl")
OUTPUT_DIR = os.path.join(BASE_DIR, "test_results")
LOG_DIR = os.path.join(BASE_DIR, "raw_logs")
ENV_FILE = os.path.join(BASE_DIR, ".env")

# 打印路径自检（如果路径不对，第一眼就能看到）
print(f"📂 项目根目录认定为: {BASE_DIR}")
print(f"📖 读取数据文件: {INPUT_FILE}")
print(f"📁 代码将保存至: {OUTPUT_DIR}")
# kpi调用
load_dotenv(ENV_FILE)
MY_KEY = os.getenv("API_KEY")

if not MY_KEY:
    raise ValueError(f"❌ 错误：在 {ENV_FILE} 中找不到 API_KEY！")

client = OpenAI(
    api_key=MY_KEY,
    base_url="https://api.deepseek.com"
)

# 确保文件夹存在（基于绝对路径创建）
for d in [OUTPUT_DIR, LOG_DIR]:
    os.makedirs(d, exist_ok=True)


def clean_code_professional(text):
    if "```python" in text:
        text = text.split("```python")[1].split("```")[0]
    elif "```" in text:
        text = text.split("```")[1].split("```")[0]
    return text.strip()


def generate_all():
    print(f"\n🚀 实验启动：正在请求...\n")

    if not os.path.exists(INPUT_FILE):
        print(f"❌ 找不到输入文件，请确认文件是否在: {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        tasks = [json.loads(line) for line in f]

    for i, data in enumerate(tasks, 1):
        task_id = data["task_id"].replace("/", "_")
        file_path = os.path.join(OUTPUT_DIR, f"{task_id}.py")

        if os.path.exists(file_path):
            print(f"⏩ 跳过: {task_id}")
            continue

        # ==========================================
        # 在控制台打印当前处理的进度
        print(f"[{i}/{len(tasks)}] 正在处理: {task_id}...")

        try:
            response = client.chat.completions.create(
                model="deepseek-reasoner",
                messages=[
                    {"role": "system",
                     "content": "你是一个资深 Python 程序员。请根据描述直接输出函数实现，不要解释，不要 Markdown 之外的文本。"},
                    {"role": "user", "content": data["prompt"]}
                ],
                temperature=0.01
            )

            # 存日志
            with open(os.path.join(LOG_DIR, f"{task_id}.json"), "w", encoding="utf-8") as log_f:
                log_f.write(response.model_dump_json())

            # 存代码
            raw_content = response.choices[0].message.content
            clean_ai_code = clean_code_professional(raw_content)

            with open(file_path, "w", encoding="utf-8") as out_f:
                out_f.write(clean_ai_code)

            time.sleep(0.5)

        except Exception as e:
            print(f"❌ {task_id} 出错: {e}")

    print(f"\n✅ 数据采集结束！")


if __name__ == "__main__":
    generate_all()