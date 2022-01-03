from sqlalchemy import create_engine    # 创建引擎
from sqlalchemy import MetaData # 创建属性
from sqlalchemy import Table    # 创建表
from sqlalchemy import Column,String,Integer    # 创建表字段
from sqlalchemy import select   # 用于第二种方法查询数据
from sqlalchemy.orm import sessionmaker # 用于第三种方法创建session
from sqlalchemy.ext.declarative import declarative_base # 用于方法三创建表的基类

# 创建引擎
engine=create_engine(
    # //用户名:密码@IP地址:端口/数据库
    "mysql+pymysql://root:root@127.0.0.1:3306/pytest",
    pool_size=10,  # 连接池大小
    # 超过连接池大小外最多可以创建的连接，也就是一共可以创建15个连接
    max_overflow=5,
    echo=True,  # 调试信息展示
)
# 取得元数据，介绍数据库
metadata=MetaData()
# 创建用户表
user=Table('user',metadata, # 表名为user，参数
           # 列名，类型，是否为主键，自增长
            Column('id',Integer,primary_key=True,autoincrement=True),
            Column('name',String(20))
)
# metadata.create_all(engine) # 创建数据表


#方法一：原生语句增删改查
# 插入，必须用双引号
engine.execute("insert into user (name) values ('KantLee')")
# 更新数据
engine.execute("update user set id=5,name='python' where id=1")
# 查询数据
result=engine.execute("select * from user") # 迭代器
print(result)
for i in result:
    print(i)    # 元组
# 删除数据
engine.execute("delete from user where id=5")


'''
# 方法二：表结构的增删改查
connect=engine.connect()    #获取连接
# 增加数据
# connect.execute(user.insert(),{'name':'python'})
# 修改数据,c必须要加
connect.execute(user.update().where(user.c.id==6).values(name='C++'))
# 查询数据
res=connect.execute((select([user.c.name,user.c.id])))    # 迭代器
print(res.fetchall())  # 列表
# 删除数据
connect.execute(user.delete().where(user.c.id==6))
connect.close()
'''


# 方法三：集成ORM类操纵数据库-Flask使用-重要-必须掌握
# 另开文件




