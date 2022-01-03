import json
import requests
import re
# data_url后面的值为歌曲链接
kv = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
}

# 获取html页面
def getHTML(url):
    try:
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return " "

# 获取歌曲的shareid
def getShareId(html):
    match = re.search(r'\"shareid\"\:\".*?\"', html)  # 若不加"?","后面的内容也会被匹配到，因此要用最小匹配
    # print(match.group(0))
    shareid = eval(match.group(0).split(':')[-1])  # eval可以去掉引号

    return shareid


if __name__ == "__main__":
    share_url = input("请输入歌曲的分享链接：")
    html = getHTML(share_url)
    shareid = getShareId(html)
    down_url = "https://node.kg.qq.com/cgi/fcgi-bin/fcg_get_play_url?shareid=" + shareid
    print("歌曲的下载链接为{}".format(down_url))