from sqlalchemy import create_engine
from sqlalchemy import Column,String,Integer
from sqlalchemy.orm import sessionmaker # 创建连接
from sqlalchemy.ext.declarative import declarative_base # 创建表的基类

# 创建引擎
engine=create_engine(
    # //用户名:密码@IP地址:端口/数据库
    "mysql+pymysql://root:root@127.0.0.1:3306/pytest",
    pool_size=10,  # 连接池大小
    # 超过连接池大小外最多可以创建的连接，也就是一共可以创建15个连接
    max_overflow=5,
    echo=True,  # 调试信息展示
)

Base=declarative_base()
# 每张表都是一个类
# 创建host表
class Host(Base):
    __tablename__='hosts'   # 表名
    id=Column(Integer,primary_key=True,autoincrement=True)
    hostname=Column(String(64),unique=True,nullable=False)
    ip_addr=Column(String(126),unique=True,nullable=False)
    port=Column(Integer,default=8080)

if __name__ == '__main__':
    Base.metadata.create_all(engine)    # 创建表
    Session=sessionmaker(bind=engine)
    sess=Session()  # 创建连接
    # 添加数据
    h=Host(hostname='test1',ip_addr='127.0.0.1')
    h2=Host(hostname='test2',ip_addr='192.168.1.1',port=8080)
    h3=Host(hostname='test3',ip_addr='192.168.1.2',port=8081)

    # 添加数据
    sess.add(h) # 添加一条数据
    sess.add_all([h2,h3])   # 添加多条数据

    # 删除数据
    sess.query(Host).filter(Host.id>1).delete()

    # 更新数据
    sess.query(Host).filter(Host.id==1).update({'port':3309})

    # 查询数据
    # res=sess.query(Host).filter(Host.id==1).all()
    # 查询数据的第二种写法
    res=sess.query(Host).filter_by(id=1).all()
    for r in res:
        print(r.hostname,r.port)

    sess.commit()   # 提交
