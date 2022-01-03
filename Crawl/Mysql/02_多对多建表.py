from sqlalchemy import create_engine
from sqlalchemy import String,Integer,Column,select,ForeignKey,Table
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import or_,and_ # 查询使用

Base=declarative_base()
engine=create_engine(
    "mysql+pymysql://root:root@127.0.0.1:3306/pytest",
    pool_size=10,
    max_overflow=5,
    echo=True
)

# 借助第三张表进行多对多建表
# 表名user_2_language
User2Lan=Table('user_2_language',Base.metadata,
               Column("user_id",ForeignKey('user.id'),primary_key=True),
               Column("language_id",ForeignKey('language.id'),primary_key=True))

class User(Base):
    __tablename__='user'
    id=Column(Integer(),primary_key=True,autoincrement=True)
    name=Column(String(125),nullable=True)
    gender=Column(String(10),nullable=True,default='保密')
    town=Column(String(125))
    language=relationship(
        'Language',
         backref='user',   # 反向引用声明
         # 这样删除user用户时，Language中对应的内容才会被删除
         cascade='all,delete',
         secondary=User2Lan
    )

class Language(Base):
    __tablename__='language'
    id=Column(Integer(),primary_key=True,autoincrement=True)
    name=Column(String(125),nullable=True)
    advantage=Column(String(125),nullable=True)
    disadvantage=Column(String(125),nullable=True)

# Base.metadata.create_all(engine)    # 创建表
if __name__ == '__main__':
    Session=sessionmaker(engine)
    session=Session()

    '''
    # 添加数据
    # 添加用户
    u1 = User(name='张三', gender='男', town='北京')
    u2 = User(name='李四', gender='男', town='上海')
    session.add_all([u1,u2])
    session.commit()
    # 添加语言
    l1=Language(name='python',advantage='开发快',disadvantage='运行慢')
    l1.user.append(u1)
    session.add(l1)
    session.commit()
    # 同时添加
    u3 = User(name='小刘', gender='女', town='郑州')
    u3.language=[Language(name='C++', advantage='运行快', disadvantage='上手难'),
                 Language(name='python', advantage='开发快', disadvantage='运行慢')]
    session.add(u3)
    session.commit()
    '''
    # 删除、更新操作和一对多建表相同

    # 查询
    number1=session.query(User).filter(User.id>0).count()    # id大于0的用户个数
    print(number1)
    # 以user的id降序排列，升序排列将‘-’去掉即可
    number2=session.query(User).order_by(-User.id).all()
    for item in number2:
        print(item.id)

    # 正则表达式查询
    # %：表示零个或多个字符
    # _：表示任意单个字符
    # []：表示括号内所列字符中的一个
    # [^]：表示不在括号所列之内的单个字符
    man=session.query(User).filter(User.name.like("_三")).all()[0]
    print(man.name)

    # or_、and_查询
    Obj1=session.query(User).filter(or_(User.id==1,User.id==2)).all()
    for item in Obj1:
        print(item.name)
    Obj2=session.query(User).filter(and_(User.name.like('%三'),User.id==1)).all()
    for item in Obj2:
        print(item.name)
