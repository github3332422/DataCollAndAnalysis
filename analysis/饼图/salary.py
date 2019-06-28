import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

df = pd.DataFrame(pd.read_csv("../../data/data.csv",encoding='gbk'))

'''
去掉异常值
'''
df = df[df['lowSalary'] != '200/天']
df = df[df['lowSalary'] != '300/天']
df = df[df['lowSalary'] != '160/天']
'''
ps：爬虫的时候数据弄反了，所有这里弄的时候需要注意一下。
'''
# print(df['highSalary'])
# print(df['lowSalary'])
# count_by_salary = df.groupby(['lowSalary'])['lowSalary'].count()
# print(count_by_salary)
'''
通过对数据的处理，获取到每个职位的平均薪水
'''
salary = []
for x,y in zip(df['highSalary'],df['lowSalary']):
    #按照范围来计算
    # salary.append(str(x) + '-' + y[0:y.index('K')])
    #按照平均值来计算
    salary.append((x + int(y[0:y.index('K')]))/2)
    # df['salary'] = (x + int(y[0:y.index('K')]))/2
    # print(y,y[0:y.index('K')])

#插入一列数据
df['salary'] = salary

#按照平均值进行排序，不可取，数据范围量太广
# count_by_salary = df.groupby(['salary'])['salary'].count()
# print(count_by_salary)

number = []
message = []

d1 = [x for x in df['salary'] if x <= 10]
number.append(len(d1))
message.append("0-10k")
d2 = [x for x in df['salary'] if 10 < x <= 20]
number.append(len(d2))
message.append("10-20k")
d3 = [x for x in df['salary'] if 20 < x <= 30]
number.append(len(d3))
message.append("20-30k")
d4 = [x for x in df['salary'] if 30 < x <= 40]
number.append(len(d4))
message.append("30-40k")
d5 = [x for x in df['salary'] if 40 < x <= 50]
number.append(len(d5))
message.append("40-50k")
d6 = [x for x in df['salary'] if 50 < x <= 60]
number.append(len(d6))
message.append("50-60k")
d7 = [x for x in df['salary'] if 60 < x <= 80]
number.append(len(d7))
message.append("60-80k")

print(number,message)


mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False
plt.pie(number,
        labels=message,
        autopct="%3.1f%%",
        startangle=60
)
plt.title("大数据市场的薪水分布")
plt.savefig("../../tmp/饼图/salaryPie.png")

plt.show()
