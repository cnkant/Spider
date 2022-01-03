import requests
'''
w，写入内容覆盖原文件，不存在则创建新文件
a，追加文件，不存在则创建
r，读取文件
b，操作二进制流
+，rw的集合
'''
with open('待完善项目.txt','r',encoding='utf8') as f:
    # print(f.read()) # 全部读出
    content=f.readlines()   # 逐行读取，返回列表
    for i in content:
        print(i.strip())    # 默认会读进换行符，导致两个空白行
url='https://img-operation.csdnimg.cn/csdn/silkroad/img/1605098462936.png'
re=requests.get(url,stream=True)    # 以流形式写入
with open('04_git.png','wb') as f:
    chunks=re.iter_content(chunk_size=128)  #每次下载128字节
    for chunk in chunks:
        f.write(chunk)
