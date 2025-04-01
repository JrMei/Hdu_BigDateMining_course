import numpy as np

# 欧式距离
def oushi_dist(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# 余弦相似度
def yuxian_simi(a, b):
    dot_product = np.dot(a, b)
    norm_a = np.linalg.norm(a)
    norm_b = np.linalg.norm(b)
    return dot_product / (norm_a * norm_b)

# 编辑距离
def edit_dist(a, b):
    m, n = len(a), len(b)
    dp = np.zeros((m + 1, n + 1))
    for i in range(m + 1):
        dp[i, 0] = i
    for j in range(n + 1):
        dp[0, j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i, j] = min(dp[i - 1, j] + 1,      # 删除
                           dp[i, j - 1] + 1,      # 插入
                           dp[i - 1, j - 1] + abs(a[i - 1] - b[j - 1]))  # 替换
    return dp[m, n]

# Jaccard相似性
def jaccard_simi(a, b):
    intersection = np.logical_and(a, b).sum()
    union = np.logical_or(a, b).sum()
    return intersection / union

# 测试向量
x = np.array([0, 1, 0, 1])
y = np.array([1, 0, 1, 0])

testA = oushi_dist(x,y)
testB = yuxian_simi(x,y)
testC = edit_dist(x,y)
testD = jaccard_simi(x,y)
# 计算相似性
print("欧式距离:", oushi_dist(x, y))
print("余弦相似度:", yuxian_simi(x, y))
print("编辑距离:", edit_dist(x, y))
print("Jaccard相似性:", jaccard_simi(x, y))