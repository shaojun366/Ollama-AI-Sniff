import os
import re

def split_articles(input_file, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    print(f"Attempting to open input file: {input_file}")
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: The input file does not exist.")
        return

    # 使用正则表达式匹配分隔符（假设分隔符为50个以上的下划线）
    articles = re.split(r'_{50,}', content)

    articles = [article.strip() for article in articles if article.strip()]

    for idx, article in enumerate(articles, start=1):
        output_file = os.path.join(output_dir, f'{idx}.txt')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(article)
        print(f'Saved {output_file}')

if __name__ == '__main__':
    input_file = r'D:\AIRD\AINATURE\AI_nature_701-800.txt'  # 请修改为实际的文件路径
    output_dir = r'D:\AIRD\papers2'          # 请修改为实际的输出目录
    split_articles(input_file, output_dir)
