import re
match=re.search(r's[hz]\d{6}',"http://quote.eastmoney.com/sh201000.html")
print(match.group(0))