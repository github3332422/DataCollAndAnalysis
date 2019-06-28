#薪水和学历的关系图
import pandas as pd
import numpy as np

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
通过对数据的处理，获取到每个职位的平均薪水
'''
salary = []
for x,y in zip(df['highSalary'],df['lowSalary']):
    salary.append((x + int(y[0:y.index('K')]))/2)
#插入一列数据
df['salary'] = salary
print(pd.pivot_table(df,values=['salary'],columns=['education'],aggfunc=[np.mean]).unstack())