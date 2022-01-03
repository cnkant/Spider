import csv

# 读取csv
with open('test.csv','r',encoding='utf-8') as f:
    f_csv=csv.reader(f)
    next(f_csv) # 跳过第一行输出
    for line in f_csv:
        print(line)
写入csv
row=[('python','3.7'),('c++','2.0'),('html','6')]
with open("06_test.csv",'a+') as f:
    data=csv.writer(f)
    data.writerows(row)
读写字典
with open('test.csv','r') as f:
    f_read=csv.DictReader(f)
    for i in f_read:
        print(i)
# 写入字典
header=['A','B','C']
rows=[{'A':'a','B':'b','C':'c'},
      {'A':'1','B':'2','C':'3'},
      {'A':'5','B':'6','C':'7'}]
with open('06_dict.csv','a+') as f:
    f_csv=csv.DictWriter(f,header)
    f_csv.writeheader() # 写入标题
    f_csv.writerows(rows)
