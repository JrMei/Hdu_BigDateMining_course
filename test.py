import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine_similarity

# 计算Jaccard相似度
def jaccard_similarity(A, B):
    A = set(A)
    B = set(B)
    intersection = len(A.intersection(B))
    union = len(A.union(B))
    return intersection / union

# 计算余弦相似度
def cosine_similarity(A, B):
    # 使用 sklearn 的 cosine_similarity 函数来避免除以零的问题
    return sklearn_cosine_similarity([A], [B])[0][0]

# 主程序
if __name__ == '__main__':
    text1 = "小米SU7近期受到广泛关注,人气很高"
    text2 = "华为P60去年受到广泛关注,人气颇高"
    
    # 将字符串转换为字频向量
    vectorizer = CountVectorizer(analyzer='word')
    vectors = vectorizer.fit_transform([text1, text2])
    vector_A = vectors.toarray()[0]
    vector_B = vectors.toarray()[1]
    
    # 计算余弦相似度和Jaccard相似度
    cos_sim = cosine_similarity(vector_A, vector_B)
    jac_sim = jaccard_similarity(vector_A, vector_B)
    
    print("余弦相似度:", cos_sim)
    print("Jaccard相似度:", jac_sim)