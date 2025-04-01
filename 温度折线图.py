import matplotlib.pyplot as plt

def read_data(file_path):
    high_temp = []
    low_temp = []
    avg_temp = []
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():  # 确保不是空行
                data = line.split(',')  # 根据实际分隔符调整
                if len(data) >= 6:  # 确保有足够的列数
                    high_temp.append(float(data[3]))  # 第四列
                    low_temp.append(float(data[4]))  # 第五列
                    avg_temp.append(float(data[5]))  # 第六列
                else:
                    print(f"Skipping line due to insufficient data: {line.strip()}")
    
    return high_temp, low_temp, avg_temp

def plot_temperatures(high_temp, low_temp, avg_temp):
    plt.figure(figsize=(10, 6))
    
    plt.plot(high_temp, label='High_temp', color='red')
    plt.plot(low_temp, label='Low_temp', color='blue')
    plt.plot(avg_temp, label='Aver_temp', color='green')
    
    plt.xlabel('Days')
    plt.ylabel('temperature (°C)')
    plt.title('Temperature Curve')
    plt.legend()
    plt.grid(True)
    plt.show()

# 文件路径
file_path = '/Volumes/HIKSEMI/茶叶采摘期/2024茶叶简报/天气数据按地方分/杭州.txt'  # 替换为你的数据文件路径

# 读取数据
high_temp, low_temp, avg_temp = read_data(file_path)

# 绘制图表
plot_temperatures(high_temp, low_temp, avg_temp)
