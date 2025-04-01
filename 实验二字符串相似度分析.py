import numpy as np 
from sklearn.feature_extraction.text import CountVectorizer 
from scipy.spatial.distance import pdist
    
# 计算Jaccard相似度
def Jaccard_simi(A , B):
    set_a , set_b = set(A),set(B)
    intersectioin = len(set_a & set_b)
    union = len(set_a | set_b)
    return intersectioin / union

# 计算余弦相速度
def cosin_simi(A , B):
    dot_product = np.dot(A,B)
    a_norm = np.linalg.norm(A)
    b_norm = np.linalg.norm(B)
    return dot_product / (a_norm * b_norm)

# 主程序
if __name__ == '__main__':
   text1 = "小米SU7近期受到广泛关注,人气很高"
   text2 = "华为P60去年受到广泛关注,人气颇高"
    
   #将字符串转换字频向量
   vectorizer = CountVectorizer(analyzer='word',tokenizer=None)
   vectors = vectorizer.fit_transform([text1, text2])
   vector_A = vectors.toarray()[0,]
   vector_B = vectors.toarray()[1,]
   
   cos_sim = cosin_simi(vector_A,vector_B)
   jac_sim = Jaccard_simi(vector_A, vector_B) 
   
   print("余弦相似度:",cosin_simi(vector_A, vector_B))
   print("Jaccard相似度:",Jaccard_simi(vector_A, vector_B))
