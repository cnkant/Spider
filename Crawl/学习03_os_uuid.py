import os
import uuid
from uuid import UUID   # 3、5需要用到这个类
path=os.path.join(os.getcwd(),'123.txt')
print(os.getcwd())
print(path)
# 1、4不需要加参数
# 基于时间戳
print(uuid.uuid1())
# 基于随机数
print(uuid.uuid4())
# 3、5需要加参数
# 基于名字的MD5散列
print(uuid.uuid3(UUID(int=9),name='lk'))
# 基于名字的SHA-1散列
print(uuid.uuid5(UUID(int=9),name='lk'))
