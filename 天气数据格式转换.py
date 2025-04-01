import os

def save_first_lines(input_folder, output_file):
    # 打开输出文件用于写入
    with open(output_file, 'w', encoding='utf-8') as outfile:
        # 遍历输入文件夹中的所有文件
        for filename in os.listdir(input_folder):
            # 只处理以.txt结尾的文件
            if filename.endswith('.txt'):
                file_path = os.path.join(input_folder, filename)
                # 打开每一个txt文件读取第一行
                with open(file_path, 'r', encoding='utf-8') as infile:
                    first_line = infile.readline().strip()
                    # 将第一行数据写入输出文件
                    outfile.write(first_line + '\n')

# 指定输入文件夹和输出文件的路径
input_folder = '/Volumes/HIKSEMI/茶叶采摘期/2024茶叶简报/全省天气数据'  # 替换为你的文件夹路径
output_file = '/Volumes/HIKSEMI/茶叶采摘期/2024茶叶简报/天气数据按地方分/杭州.txt'  # 替换为你的输出文件路径

# 调用函数
save_first_lines(input_folder, output_file)
