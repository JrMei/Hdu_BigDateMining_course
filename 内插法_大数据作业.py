import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial import distance_matrix
from datetime import datetime, timedelta

# 示例输入数据，包含经纬度、实际温度和预报温度
data = {
    'latitude': [30.5, 30.6, 30.7, 30.8, 30.9],
    'longitude': [114.2, 114.3, 114.4, 114.5, 114.6],
    'actual_temperature': [12, 15, 18, 20, 22],
    'forecast_temperature': [13, 16, 17, 21, 23],
    'date': [
        '2024-03-01', '2024-03-01', '2024-03-01', '2024-03-01', '2024-03-01'
    ]
}

df = pd.DataFrame(data)

# 筛选大于10℃的温度
df = df[(df['actual_temperature'] > 10) & (df['forecast_temperature'] > 10)]

# 定义网格范围和分辨率
min_lat, max_lat = df['latitude'].min(), df['latitude'].max()
min_lon, max_lon = df['longitude'].min(), df['longitude'].max()
lat_grid, lon_grid = np.mgrid[min_lat:max_lat:100j, min_lon:max_lon:100j]

# IDW插值函数
def idw_interpolation(x, y, z, xi, yi, power=2):
    dist = distance_matrix(np.c_[xi.flatten(), yi.flatten()], np.c_[x, y])
    dist[dist == 0] = 1e-10  # 避免除以零
    weights = 1.0 / dist**power
    weights /= weights.sum(axis=1)[:, None]
    zi = np.dot(weights, z)
    return zi.reshape(xi.shape)

# 假设开始日期和结束日期
start_date = datetime.strptime("2024-03-01", "%Y-%m-%d")
end_date = datetime.strptime("2024-05-31", "%Y-%m-%d")

# 生成每日的假数据，确保每一天都有数据
daily_data = []
current_date = start_date
while current_date <= end_date:
    for index, row in df.iterrows():
        daily_data.append({
            'latitude': row['latitude'],
            'longitude': row['longitude'],
            'actual_temperature': row['actual_temperature'] + np.random.uniform(-2, 2),  # 添加一些波动
            'forecast_temperature': row['forecast_temperature'] + np.random.uniform(-2, 2),
            'date': current_date.strftime("%Y-%m-%d")
        })
    current_date += timedelta(days=1)

daily_df = pd.DataFrame(daily_data)

# 简单预测模型：假设温度达到20℃时开始开采，达到25℃时结束采摘
harvest_start_threshold = 20
harvest_end_threshold = 25

harvest_start_date = None
harvest_end_date = None

# 遍历每一天的数据进行预测
current_date = start_date
while current_date <= end_date:
    daily_temp_df = daily_df[daily_df['date'] == current_date.strftime("%Y-%m-%d")]
    if not daily_temp_df.empty:
        current_temp = idw_interpolation(daily_temp_df['longitude'].values, daily_temp_df['latitude'].values, daily_temp_df['actual_temperature'].values, lon_grid, lat_grid).mean()
        if not np.isnan(current_temp):
            if current_temp >= harvest_start_threshold and harvest_start_date is None:
                harvest_start_date = current_date
            if current_temp >= harvest_end_threshold and harvest_end_date is None:
                harvest_end_date = current_date
    current_date += timedelta(days=1)

if harvest_start_date:
    print(f"预计开采期开始日期: {harvest_start_date.strftime('%Y-%m-%d')}")
else:
    print("未能确定开采期开始日期")

if harvest_end_date:
    print(f"预计采摘结束日期: {harvest_end_date.strftime('%Y-%m-%d')}")
else:
    print("未能确定采摘结束日期")

# 重新计算实际温度和预报温度的插值
actual_temp_grid = idw_interpolation(df['longitude'].values, df['latitude'].values, df['actual_temperature'].values, lon_grid, lat_grid)
forecast_temp_grid = idw_interpolation(df['longitude'].values, df['latitude'].values, df['forecast_temperature'].values, lon_grid, lat_grid)

# 温度订正模型（假设为实际温度与预报温度的平均）
corrected_temp_grid = (actual_temp_grid + forecast_temp_grid) / 2

# 绘制插值结果
plt.figure(figsize=(10, 8))
plt.contourf(lon_grid, lat_grid, corrected_temp_grid, levels=100, cmap='viridis')
plt.scatter(df['longitude'], df['latitude'], c=df['actual_temperature'], edgecolor='k', cmap='viridis')
plt.colorbar(label='Corrected Temperature (℃)')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Corrected Temperature Interpolation')
plt.show()
