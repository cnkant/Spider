import requests
r1=requests.get("http://httpbin.org")
r2=requests.get("http://httpbin.org/post")
payload={'key1':'value1','key2':'value2'}
r3=requests.post("http://httpbin.org",data=payload)
r4=requests.post("http://httpbin.org/post",data=payload)
r1.encoding='utf-8'
r2.encoding='utf-8'
r3.encoding='utf-8'
r4.encoding='utf-8'
print(r1.text)
print(r2.text)
print(r3.text)
print(r4.text)