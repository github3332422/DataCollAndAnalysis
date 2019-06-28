import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.DataFrame(pd.read_csv("../../data/data.csv",encoding='gbk'))

'''
去掉异常值数据
'''
df = df[df['education'] != '3个月']
df = df[df['education'] != '4个月']
df = df[df['education'] != '6个月']
df = df[df['education'] != '中专/中技']
df = df[df['lowSalary'] != '200/天']
df = df[df['lowSalary'] != '300/天']
df = df[df['lowSalary'] != '160/天']

'''
通过对数据的处理，获取到每个职位的平均薪水，同时将这一列插入进去
'''
salary = []
for x,y in zip(df['highSalary'],df['lowSalary']):
    salary.append((x + int(y[0:y.index('K')]))/2)
df['salary'] = salary

count_by_degree = df.groupby(['education'])['salary'].count()
value_by_degree = pd.DataFrame([count_by_degree.index, count_by_degree.values], index = ['degree', 'counts']).T
sort_by_degree = value_by_degree.copy()
degree_mappings = {'学历不限':1, '大专':2, '本科':3, '硕士':4,'博士':5}
sort_by_degree['sortby'] = sort_by_degree['degree'].map(degree_mappings)
sort_by_degree.sort_values(by='sortby', inplace=True)
# sort_by_degree
print(value_by_degree)
group_by_degree = df.groupby(['education'])['salary']
df_degree = []
for group in sort_by_degree['degree']:
    v = group_by_degree.get_group(group).values
    df_degree.append(v)


mpl.rcParams["font.sans-serif"]=["FangSong"]
mpl.rcParams["axes.unicode_minus"]=False
ax9 = plt.figure(figsize=(10, 5)).add_subplot(111)
sns.boxplot(data=df_degree)
ax9.set_xticklabels(sort_by_degree['degree'], fontsize=18)
ax9.set_title('不同学历的薪酬分布', fontsize=22)
ax9.set_ylabel('薪酬K/月', fontsize=20)
plt.savefig("../../tmp/箱尾图/educationBox.png")
plt.show()

