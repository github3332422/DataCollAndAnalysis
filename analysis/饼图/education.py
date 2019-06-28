import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.DataFrame(pd.read_csv("../../data/data.csv",encoding='gbk'))
'''
对特殊值进行处理
'''
df = df[df['education'] != '4个月']
df = df[df['education'] != '6个月']
'''
统计每个学历段的人数
'''
count_by_education = df.groupby(['education'])['education'].count()
# print(count_by_education)
'''
得到一个学历和要求人数的二维矩阵
'''
value_by_degree = pd.DataFrame([count_by_education.index, count_by_education.values], index = ['degree', 'counts']).T
# print(value_by_degree)
sort_by_degree = value_by_degree.copy()
print(sort_by_degree)
mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False
plt.pie(count_by_education.values,
        labels=count_by_education.index,
        autopct="%3.1f%%",
        startangle=60
)
plt.title("大数据市场对不同学历人数的需求")
plt.savefig("../../tmp/饼图/educationPie.png")
plt.show()


