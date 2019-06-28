import csv

def read_csv_one():
    for i in range(0,8):
        s = '../../data/data'+ str(i) + '.csv'
        print(s)
        with open(s, 'r',encoding='utf-8')as fp:
            reader = csv.DictReader(fp)
            for i in reader:
                list = []
                list.append(i['name'])
                list.append(i['place'])
                list.append(i['education'])
                list.append(i['expersion'])
                list.append(i['highSalary'])
                list.append(i['lowSalary'])
                list.append(i['fuli'])
                list.append(i['yaoqiu'])
                write_to_csv(list)
                # t = i['education']
                # print(t)

def write_csv_one():
		headers = {'name','education','expersion','place','fuli','highSalary','lowSalary','yaoqiu'}
		with open('../../data/demo.csv', 'a+',encoding='UTF-8',newline='')as fp:
			writer = csv.DictWriter(fp,headers)
			writer.writeheader()
			writer.writerows(list)

def write_to_csv(list):
    with open('../../data/data.csv', 'a+', newline='',encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(list)
read_csv_one()
# write_csv_one()