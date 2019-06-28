import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.DataFrame(pd.read_csv("../../data/data.csv",encoding='gbk'))
'''
对特殊值进行处理
'''
df = df[df['education'] != '3个月']
df = df[df['education'] != '4个月']
df = df[df['education'] != '6个月']
df = df[df['education'] != '中专/中技']
'''
统计每个学历段的人数
'''
count_by_education = df.groupby(['education'])['education'].count()
# print(count_by_education)
'''
得到一个学历和要求人数的二维矩阵
'''
value_by_degree = pd.DataFrame([count_by_education.index, count_by_education.values], index = ['degree', 'counts']).T
print(value_by_degree)
sort_by_degree = value_by_degree.copy()
print(sort_by_degree)

print(count_by_education.index)
print(count_by_education.values)
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
# tick_label: 刻度标签
plt.bar(count_by_education.index, count_by_education.values, hatch='/',alpha=0.8)
plt.xticks(count_by_education.index,count_by_education.index, rotation=0)
# plt.xticks(total, rotation=45, fontsize=10)
plt.xlabel('学历')
plt.ylabel('职位数(个)')
plt.title("学历要求分布")
plt.savefig("../../tmp/柱状图/educationBar.png")
plt.show()


