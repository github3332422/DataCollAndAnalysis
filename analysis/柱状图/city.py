import pandas as pd

'''
在BOSS直聘上爬取的数据有问题，不具有可操作性
'''
df = pd.DataFrame(pd.read_csv("../../data/data.csv",encoding='gbk'))

count_by_city = df.groupby(['place'])['place'].count()
print(count_by_city)