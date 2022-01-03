from sqlalchemy import create_engine
from sqlalchemy import String,Integer,Column,select,ForeignKey
from sqlalchemy.orm import sessionmaker,relationship
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()
engine=create_engine(
    "mysql+pymysql://root:root@127.0.0.1:3306/pytest",
    pool_size=10,
    max_overflow=5,
    echo=True
)

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
        cascade='all,delete'
    )

class Language(Base):
    __tablename__='language'
    id=Column(Integer(),primary_key=True,autoincrement=True)
    name=Column(String(125),nullable=True)
    advantage=Column(String(125),nullable=True)
    disadvantage=Column(String(125),nullable=True)
    user_id=Column(Integer(),ForeignKey('user.id'))

Base.metadata.create_all(engine)    # 创建表
if __name__ == '__main__':
    Session=sessionmaker(engine)
    session=Session()   # 实例化

    # 添加用户
    # u1=User(name='张三',gender='男',town='北京')
    # u2 = User(name='李四', gender='男', town='上海')
    # u3 = User(name='小刘', gender='女', town='郑州')
    # session.add_all([u1,u2,u3])
    # session.commit()
    # # 添加语言
    # l1=Language(name='Python',advantage='开发快',disadvantage='运行慢')
    # # 关联用户u1，把u1的id赋值给ll的user_id
    # l1.user=u1
    # l2=l1=Language(name='Python3',advantage='开发快',disadvantage='运行慢')
    # l2.user=u2
    # session.add_all([l1,l2])
    # session.commit()
    #
    # # 另一种写法
    # u4 = User(name='王五', gender='男', town='河北')
    # u4.language = [Language(name='H5', advantage='简单', disadvantage='运行慢'),
    #                Language(name='C++', advantage='运行快', disadvantage='上手难')]
    # session.add(u4)
    # session.commit()

    # 查询
    # res=session.query(User).filter_by(id=4).first()
    # print("用户名：",res.name)
    # lan=session.query(Language).filter_by(user_id=res.id)
    # # 因为id=4的用户喜欢两门语言，所以循环输出
    # for i in lan:
    #     print(i.name,i.advantage)

    # 删除
    # u=session.query(User).filter_by(id=4).first()
    # session.delete(u)
    # session.commit()

    # 更改数据
    # 更改用户名
    u=session.query(User).filter(User.id==1).first()
    u.name='大王'
    session.commit()
    # 更改关联表的语言名
    lan=u.language[0].name='JS'
    session.commit()
