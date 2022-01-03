import os
lis = []
path = "C:\\Users\\KangLi\\Desktop\\计实验17-1班截图\\"
with open('D:\\VscodePy\\pytest\\jsy.txt', 'r',encoding='utf-8') as fp:
    line = fp.readline().strip()
    while line:
        linestr = line
        lis.append(linestr)
        line = fp.readline().strip()
i = 0
for filename in os.listdir(path):
    src = path + filename
    dst = path + lis[i] + '.jpg'
    i += 1
    os.rename(src, dst)
