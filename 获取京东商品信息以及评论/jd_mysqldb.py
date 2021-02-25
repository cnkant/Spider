from sqlalchemy import String,Integer,Text,Column
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine(
    "mysql+pymysql://root:root@127.0.0.1:3306/jdcrawl?charset=utf8",
    pool_size=200,
    max_overflow=300,
    echo=False
)

BASE=declarative_base() # 实例化

class Goods(BASE):
    __tablename__='goods'
    id=Column(Integer(),primary_key=True,autoincrement=True)
    sku_id = Column(String(200), primary_key=True, autoincrement=False)
    name=Column(String(200))
    price=Column(String(200))
    comments_num=Column(Integer)
    shop=Column(String(200))
    link=Column(String(200))

class Comments(BASE):
    __tablename__='comments'
    id=Column(Integer(),primary_key=True,autoincrement=True,nullable=False)
    sku_id=Column(String(200),primary_key=True,autoincrement=False)
    comments=Column(Text())

BASE.metadata.create_all(engine)
Session=sessionmaker(engine)
sess_db=scoped_session(Session)
