import execjs
# print(execjs.get().name) # 输出所用环境名称
with open("pytest\翻译接口\\fun_e(r).js", "r", encoding='utf-8') as f:
    ctx = execjs.compile(f.read())
print(ctx.call("e", "我是大帅哥"))
