import requests
import os
url = "https://imgsa.baidu.com/exp/w=480/sign=086ffb78b98f8c54e3d3c4270a282dee/d0c8a786c9177f3ec037c19b7dcf3bc79f3d5620.jpg"
root = "D://VscodePy//pics//"  # 最后必须加//，否则图片会保存在VscodePy目录，pics成为名字开头的一部分
img_path = root + url.split('/')[-1]
print(img_path)


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()  # 如果不是200，引发HTTPError异常
        # print(r.content)
        if not os.path.exists(root):
            os.mkdir(root)  # 若不存在路径则创建
        if not os.path.exists(img_path):  # 若图片文件不存在
            with open(img_path, "wb") as f:  # 为什么不能是root？而是img_path
                # 因为它指的是文件名，可换成要保存的路径+//abc.jpg
                f.write(r.content)
                f.close()
            print("图片爬取成功！")
        else:
            print("图片已存在！")
    except:
        print("产生异常")


if __name__ == "__main__":
    getHTMLText(url)
