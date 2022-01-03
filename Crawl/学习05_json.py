import json

# json中使用双引号
data={
    'aa':11,
    'bb':22,
    'cc':'33'
}
# 字典转化json
print(json.dumps(data))  # 转化为json格式
# 字典写入json文件
with open('05_data.json','w') as f:
    json.dump(data,f)
# json格式转字典格式
json_data='{"ee":"11","rr":"pp","oo":22}'
print(json.loads(json_data))
# 读出json文件，读出为字典格式
with open("05_data.json",'r') as f:
    print(json.load(f))
