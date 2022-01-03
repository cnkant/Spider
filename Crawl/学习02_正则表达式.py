import re
'''
re.match(pattern,string,flag)  
    只能匹配一个，但是必须从头匹配（正则表达式，字符串，额外参数）
    flag一般用的有两个：re.I---使匹配对大小写不敏感，re.S---匹配包括换行在内的所有字符
re.search(pattern,string,flag)
    只能匹配一个， 可以全局匹配
Match和Search得到的是正则表达式匹配对象，提取结果需要使用特定的函数

group()匹配的正则字符串
groups()返回包含字符串的元组，需提取把内容括起来

re.complie(pattern[flags])
    编译正则表达式，可以供match和search使用
re.findall()
    匹配所有合规字符串，配合re.complie，返回列表
re.sub(pattern,replace,text,flag)
    替换文本

'''

text='href="www.baidu.com">pathon>href="www.netease.com"'
# group()、groups()
result1=re.search('href=".*?"',text,re.I|re.S)
print(result1.group())
result2=re.search('href="(.*?)"',text,re.I|re.S)
print(result2.groups())
# re.complie
result3=re.compile('href="(.*?)"',re.I|re.S)
print(result3.search(text).group())
# findall
print(result3.findall(text))
# 避免因为同时爬取成千上万条数据量消耗系统资源，使用迭代器
for i in result3.finditer(text):
    print(i)    # 返回迭代器对象，提取用group()
    print(i.group())
# re.sub
res=re.sub("href","url",text,re.I|re.S)
print(res)



