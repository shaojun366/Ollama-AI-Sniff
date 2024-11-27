import os

def rename_files(directory):
    # 遍历指定目录下的所有文件
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(directory, filename)
            # 读取第一行并立即关闭文件
            with open(file_path, 'r', encoding='utf-8') as f:
                first_line = f.readline().strip()
            # 提取前6个单词
            words = first_line.split()
            first_six_words = words[:6]
            # 用下划线连接单词
            new_filename = '_'.join(first_six_words) + '.txt'
            # 替换非法文件名字符（Windows系统）
            invalid_chars = '<>:"/\\|?*'
            for char in invalid_chars:
                new_filename = new_filename.replace(char, '')
            # 生成新的文件路径
            new_file_path = os.path.join(directory, new_filename)
            # 如果新文件名已存在，避免覆盖
            counter = 1
            original_new_filename = new_filename
            while os.path.exists(new_file_path):
                new_filename = f"{os.path.splitext(original_new_filename)[0]}_{counter}.txt"
                new_file_path = os.path.join(directory, new_filename)
                counter += 1
            # 重命名文件
            try:
                os.rename(file_path, new_file_path)
                print(f"已将文件 {filename} 重命名为 {new_filename}")
            except PermissionError as e:
                print(f"无法重命名文件 {filename}：{e}")

if __name__ == '__main__':
    directory = r'D:\AIRD\papers2'  # 替换为您的文件夹路径
    rename_files(directory)
