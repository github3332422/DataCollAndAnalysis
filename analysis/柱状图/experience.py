import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.DataFrame(pd.read_csv("../../data/data.csv",encoding='gbk'))

# print(df['expersion'])
'''
去掉特殊值
'''
df = df[df['expersion'] != '4天/周']
df = df[df['expersion'] != '5天/周']

'''
统计每段经验所需要的人数
'''
count_by_expersion = df.groupby(['expersion'])['expersion'].count()

'''
查看不同经验所需求的人数
'''
value_by_expersion = pd.DataFrame([count_by_expersion.index, count_by_expersion.values], index = ['expersion', 'counts']).T
# print(value_by_expersion.index,value_by_expersion.values)
print(value_by_expersion)
mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False
plt.bar(count_by_expersion.index, count_by_expersion.values, hatch='/',alpha=0.8)
plt.xticks(count_by_expersion.index,count_by_expersion.index, rotation=0)
plt.xlabel('经验')
plt.ylabel('职位数(个)')
plt.title("经验要求分布")
plt.savefig("../../tmp/柱状图/expersionBar.png")
plt.show()

