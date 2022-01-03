import re
# ^[A-Za-z]+$表26个字母组成的字符串
# ^[A-Za-z0-9]+$表26个字母和0-9组成的字符串

# re.research()在一个字符串中搜索匹配正则表达式的第一个位置
#匹配中国邮政编码
# r''表示原生字符串，保留转义字符
match0 = re.search(r'[1-9]\d{5}', '这种不匹配的字符会被忽略100081 459789')
if match0:
    print(match0.group(0))

# re.match()从一个字符串的开始位置起匹配正则表达式
match1 = re.match(r'[1-9]\d{5}', '测试 123456')
if match1:
    print(match1.group(0))
else:
    print("match1对象为空，错误")
match1 = re.match(r'[1-9]\d{5}', '123456 测试')
if match1:
    print(match1.group(0))
else:
    print("match1对象为空错误")

# re.findall()搜索字符串，以列表类型返回全部能匹配的字串
ls1 = re.findall(r'[1-9]\d{5}', 'BAT666666 ACC888899')
if ls1:
    print(ls1)

# re.split()将一个字符串按照正则表达式匹配结果进行分割
ls2 = re.split(r'[1-9]\d{5}', 'ABC100086DEF456789')
if ls2:
    print(ls2)
ls2 = re.split(r'[1-9]\d{5}', 'ABC100086 DEF456789', maxsplit=1)
# maxsplit表示最大分割数
if ls2:
    print(ls2)

# re.finditer()搜索字符串，返回一个匹配结果的迭代类型，每个迭代元素是match对象
for m in re.finditer(r'[1-9]\d{5}', 'BAT123456TSU456789 DEF100086 111222'):
    print(m.group(0))

# re.sub()在一个字符串中替换所以匹配正则表达式的子串，返回替换后的字符串
print(re.sub(r'[1-9]\d{5}', 'zipcode', 'BITa110153 HG455555'))
print(re.sub(r'[1-9]\d{5}', 'zipcode', 'BITa110153 HG455555', count=1))
# count为最大替换次数

# 面向对象用法
regex = re.compile(r'[1-9]\d{5}')
print("生成正则表达式类型:")
print(regex)
match = regex.search('BaT123456 256555')
print(match.group(0))
