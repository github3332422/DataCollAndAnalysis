import pandas as pd
import numpy as np

'''
读入数据文件
'''
df = pd.DataFrame(pd.read_csv("../../data/data.csv",encoding='gbk'))

'''
去掉异常值
'''
df = df[df['expersion'] != '4天/周']
df = df[df['expersion'] != '5天/周']
df = df[df['education'] != '3个月']
df = df[df['education'] != '4个月']
df = df[df['education'] != '6个月']
df = df[df['education'] != '中专/中技']
df = df[df['lowSalary'] != '200/天']
df = df[df['lowSalary'] != '300/天']
df = df[df['lowSalary'] != '160/天']
# 实证统计,将学历不限的职位要求认定为最低学历:大专
df['education'] = df['education'].replace('学历不限','本科')
df['expersion'] = df['expersion'].replace('经验不限','1-3年')

df['education'] = df['education'].replace('大专',1)
df['education'] = df['education'].replace('本科',2)
df['education'] = df['education'].replace('硕士',3)
df['education'] = df['education'].replace('博士',4)

'''
'''
pattern = '\d+'
df['expersion'] = df['expersion'].str.findall(pattern)

avg_work_year = []
for i in df['expersion']:
    # 如果工作经验为'不限'或'应届毕业生',那么匹配值为空,工作年限为0
    if len(i) == 0:
        avg_work_year.append(0)
    # 如果匹配值为一个数值,那么返回该数值
    elif len(i) == 1:
        avg_work_year.append(int(''.join(i)))
    # 如果匹配值为一个区间,那么取平均值
    else:
        num_list = [int(j) for j in i]
        avg_year = sum(num_list)/2
        avg_work_year.append(avg_year)
df['exp'] = avg_work_year

'''
通过对数据的处理，获取到每个职位的平均薪水，并将数据插入
'''
salary = []
for x,y in zip(df['highSalary'],df['lowSalary']):
    salary.append((x + int(y[0:y.index('K')]))/2)
df['salary'] = salary

df.to_csv("data_deal.csv",encoding='utf-8')
