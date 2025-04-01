from difflib import SequenceMatcher, Differ

# 定义两个需要比较的文本字符串
with open('/Users/meijiarui/Desktop/大数据分析与挖掘/text1.txt','r',encoding='utf-8') as file1: 
   text1 = file1.read()

with open('/Users/meijiarui/Desktop/大数据分析与挖掘/text2.txt','r',encoding='utf-8') as file2:
   text2 = file2.read()

# 初始化 SequenceMatcher 对象
matcher = SequenceMatcher(None, text1, text2)

# 计算相似度比例
similarity = matcher.ratio()
print(f"相似度比例: {similarity:.2f}")

# 如果需要生成详细的差异报告，可以使用 Differ 类
d = Differ()
diff = list(d.compare(text1.splitlines(keepends=True), text2.splitlines(keepends=True)))

# 打印差异报告
print("差异报告:")
for line in diff:
    print(line)