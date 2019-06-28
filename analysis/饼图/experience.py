import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.DataFrame(pd.read_csv("../../data/data.csv",encoding='gbk'))
# print(df['expersion'])
'''
对特殊值进行处理
'''
df = df[df['expersion'] != '4天/周']
df = df[df['expersion'] != '5天/周']
'''
统计每个学历段的人数
'''
count_by_expersion = df.groupby(['expersion'])['expersion'].count()
# print(count_by_education)
'''
得到一个学历和要求人数的二维矩阵
'''
value_by_expersion = pd.DataFrame([count_by_expersion.index, count_by_expersion.values], index = ['degree', 'counts']).T
# print(value_by_expersion)
sort_by_degree = value_by_expersion.copy()
print(sort_by_degree)

mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False
plt.pie(count_by_expersion.values,
        labels=count_by_expersion.index,
        autopct="%3.1f%%",
        startangle=60
)
plt.title("大数据市场对不同经验人数的需求")
plt.savefig("../../tmp/饼图/expersionPie.png")
plt.show()

