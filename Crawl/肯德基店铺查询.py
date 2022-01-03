import requests
import json

headers = {
    'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
form_data = {'cname': None, 'pageIndex': '1', 'pageSize': '10'}

# 获取返回结果
def getPages(url):
    try:
        req = requests.post(url, headers=headers, data=form_data)
        req.raise_for_status()
        return req.text
    except:
        print("异常！")
        return ''


if __name__ == "__main__":
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    cname = input("请输入要查询的地点(省or市or县)：")
    form_data['cname'] = cname
    text = getPages(url)
    # print(text)
    json_data = json.loads(getPages(url))
    # print(json_data)
    amount = json_data['Table'][0]['rowcount']
    print("{}共有{}家肯德基店！".format(cname, amount))
    count = input("请输出您想要显示的店铺数量：")
    form_data['pageSize'] = count
    json_data = json.loads(getPages(url))
    print("信息如下：")
    form = '序号：{:<5}店名：{:<15}'
    for i in range(eval(count)):
        name = json_data['Table1'][i]['storeName']
        address = json_data['Table1'][i]['addressDetail']
        print(form.format(i + 1, name))
        print("Address: {}".format(address))
