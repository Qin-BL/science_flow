
from sqlalchemy import Column, Integer, String, DateTime, Boolean, TIMESTAMP, func, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from lib.mysql_session import engine


class BaseModel(object):

    # 告诉sqlalchemy是基类
    __abstract__ = True
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8'
    }


Base = declarative_base(cls=BaseModel)


class Test(Base):

    __tablename__ = 'test'

    id = Column(Integer, primary_key=True)
    content = Column(VARCHAR(128), nullable=True, default='hello world')
    update_time = Column(DateTime, server_default=func.now(), onupdate=func.now(), comment="update time")


class User(Base):

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(128), nullable=True, default='小明')
    headimg = Column(VARCHAR(128), nullable=True, default='http://cdn.layui.com/avatar/168.jpg')
    mail = Column(VARCHAR(128), nullable=False)
    phone = Column(VARCHAR(128), nullable=True, default='')
    password = Column(VARCHAR(128), nullable=False)


# 创建表
Base.metadata.create_all(engine)
