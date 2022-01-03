import requests
url = "http://m.ip138.com/ip.asp?ip="


def getIPAddressa(ip):
    try:
        req = requests.get(url + ip)
        req.raise_for_status()
        req.encoding = req.apparent_encoding
        print(req.url)
        return req.text[-500:]
    except Exception:
        return "异常"


if __name__ == "__main__":
    ip = input("请输入ip地址：")
    print(getIPAddressa(ip))
