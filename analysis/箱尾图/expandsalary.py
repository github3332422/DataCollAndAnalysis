import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df = pd.DataFrame(pd.read_csv("../../data/data.csv",encoding='gbk'))
'''
去掉异常值
'''
df = df[df['expersion'] != '4天/周']
df = df[df['expersion'] != '5天/周']
df = df[df['lowSalary'] != '200/天']
df = df[df['lowSalary'] != '300/天']
df = df[df['lowSalary'] != '160/天']

'''
通过对数据的处理，获取到每个职位的平均薪水,并且把数据插入
'''
salary = []
for x,y in zip(df['highSalary'],df['lowSalary']):
    salary.append((x + int(y[0:y.index('K')]))/2)
df['salary'] = salary

count_by_experience = df.groupby(['expersion'])['salary'].count()
value_by_experience = pd.DataFrame([count_by_experience.index, count_by_experience.values], index = ['expersion', 'counts']).T
sort_by_experience = value_by_experience.copy()
mappings = {'不限':1, '1年以下':2, '1-3年':3, '3-5年':4, '5-10年':5, '10年以上':6}
sort_by_experience['sortby'] = sort_by_experience['expersion'].map(mappings)
sort_by_experience.sort_values(by='sortby', inplace=True)


group_by_experience = df.groupby(['expersion'])['salary']
df = []
for group in sort_by_experience['expersion']:
    v = group_by_experience.get_group(group).values
    df.append(v)


mpl.rcParams["font.sans-serif"]=["FangSong"]
mpl.rcParams["axes.unicode_minus"]=False
ax7 = plt.figure(figsize=(10, 6)).add_subplot(111)
sns.boxplot(data=df)
ax7.set_xticklabels(sort_by_experience['expersion'], fontsize=18)
ax7.set_title('不同工作经验的薪酬分布', fontsize=22)
ax7.set_ylabel('薪酬K/月', fontsize=20)
plt.savefig("../../tmp/箱尾图/expersionBox.png")
plt.show()



