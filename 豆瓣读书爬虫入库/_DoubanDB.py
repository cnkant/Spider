from sqlalchemy import create_engine
from sqlalchemy import Integer,String,Column,Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
engine=create_engine(
    "mysql+pymysql://root:root@127.0.0.1:3306/pytest",
    echo=True
    # 只需要一个线程，不需要连接池等额外信息
)

class Douban(Base):
    __tablename__='douban'
    id=Column(Integer,primary_key=True,autoincrement=True)
    # String()类型在数据库中均为VARCHAR()类型
    title=Column(String(100))
    about=Column(Text())
    star=Column(String(100))
    comments=Column(String(100))
    abstract=Column(Text())

Base.metadata.create_all(engine)    # 创建表

Session=sessionmaker(engine)
session=Session()