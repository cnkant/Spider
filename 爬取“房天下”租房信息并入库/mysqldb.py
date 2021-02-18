from sqlalchemy import create_engine
from sqlalchemy import String, Integer, Column, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session  # 多线程爬虫时避免出现线程安全问题
from sqlalchemy.ext.declarative import declarative_base

BASE = declarative_base()  # 实例化
engine = create_engine(
    "mysql+pymysql://root:root@127.0.0.1:3306/pytest?charset=utf8",
    max_overflow=300,  # 超出连接池大小最多可以创建的连接
    pool_size=100,  # 连接池大小
    echo=False,  # 不显示调试信息
)


class House(BASE):
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title=Column(String(200))
    price=Column(String(200))
    block=Column(String(200))
    building=Column(String(200))
    address=Column(String(200))
    detail=Column(Text())
    name=Column(String(20))
    phone=Column(String(20))


BASE.metadata.create_all(engine)
Session = sessionmaker(engine)
sess = scoped_session(Session)
