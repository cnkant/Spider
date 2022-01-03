#json string:
import json
s = json.loads(
    '{"name":"test", "type":{"name":"seq", "parameter":["1", "2"],"test":[{"test1":"1_1"},{"test2":"2_2"}]}}'
)
print(s)
print(s.keys())
print(s["name"])
print(s["type"]["name"])
print(s["type"]["parameter"][1])
print(s["type"]["test"][0]['test1'])
print(s["type"]["test"][1]['test2'])
