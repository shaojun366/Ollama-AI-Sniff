import os
import requests
import json
from tqdm import tqdm

# Llama API 的地址
LLAMA_API_URL = 'http://localhost:11434/api/generate'

def is_ai_mentioned(text):
    """
    调用 Llama API，判断文本中是否提到了 AI 对研究的帮助
    """
    prompt = f"""
以下是一篇论文的内容：

{text}

问：这篇论文是否提到了人工智能（AI）对其研究的帮助？请仅回答“是”或“否”。
答：
    """

    # 构建请求数据
    data = {
        "model": "llama3.2",
        "prompt": prompt,
        "options": {
            "max_tokens": 10,  # 限制回复长度
            "temperature": 0.0  # 使回复尽可能确定
        },
        "stream": False
    }

    try:
        response = requests.post(LLAMA_API_URL, json=data)
        response.raise_for_status()
        result = response.json()
        answer = result.get('response', '').strip()

        if '是' in answer:
            return True
        else:
            return False

    except Exception as e:
        print(f"调用 Llama API 时出错：{e}")
        return False

def read_txt_file(txt_path):
    """
    读取 TXT 文件内容
    """
    try:
        with open(txt_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return text
    except Exception as e:
        print(f"无法读取文件 {txt_path}：{e}")
        return ""

def main():
    folder_path = input("请输入论文文件夹的路径：")
    output_file = 'analysis_results2.txt'

    results = []

    # 获取文件列表，只包含 TXT 文件
    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith('.txt')]

    # 使用 tqdm 显示进度条
    with tqdm(total=len(file_list), desc="处理进度") as pbar:
        for filename in file_list:
            file_path = os.path.join(folder_path, filename)
            print(f"\n正在处理文件：{filename}")
            text = read_txt_file(file_path)
            if text:
                # 判断是否提到了 AI
                if is_ai_mentioned(text):
                    result = f"{filename} +"
                else:
                    result = f"{filename} -"
            else:
                result = f"{filename} - 无法读取内容"

            # 将结果添加到列表
            results.append(result)

            # 实时输出结果
            print(result)

            # 更新进度条
            pbar.update(1)

    # 将结果写入到文本文件
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in results:
            f.write(line + '\n')

    print(f"\n分析完成，结果已保存到 {output_file}")

if __name__ == "__main__":
    main()
