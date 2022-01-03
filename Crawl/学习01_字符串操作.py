'''
Str.replace()---字符串替换
Str.translate()---ord映射替换
Str.split()---分割字符串，返回列表
Str.startswith()---判断字符串开头
Str.endswith()---判断字符串结尾
Str.join()---合并字符串
Str.strip()---去除首尾字符
%s %d----format----f    字符串填充
'''
# str.translate()
intab="aeiou"
outtab="12345"
trantab=str.maketrans(intab,outtab)
str2="this is string example....wowppp!!!"
print(str2.translate(trantab))

# str.join()
urls=['python','3.7','hello','world']
s='='.join(urls)    # 以什么符合拼接就在引号中写什么
print(s)

# str.strip()
str="ohello"
print(str.strip('o'))

# %s %d----format----f
keyword="word"
url1="http://www.baidu.com/s?wd=%s"%keyword # 若替换数字则用%d
url2="http://www.baidu.com/s?wd={}".format(keyword)
url3=f"http://www.baidu.com/s?wd={keyword}"
print(url1,url2,url3)   # 效果一致

