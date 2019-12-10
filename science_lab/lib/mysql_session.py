
"""
确保 session 在使用完成后用 session.close, session.commit 或者 session.rollback 把连接还回 pool
"""


from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from tornado.options import options
from settings import mysql_master
import pymysql
pymysql.install_as_MySQLdb()


engine = create_engine(
        'mysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'.format(**mysql_master),
        echo=options.debug,  # 为 True 时候会把sql语句打印出来，打出sql会降低性能
        max_overflow=0,  # 超过连接池大小外最多创建的连接
        pool_size=100,  # 连接池大小
        pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
        pool_recycle=3600,  # 多久之后对线程池中的线程进行一次连接的回收（重置）
        pool_pre_ping=True  # 如果值为True，那么每次从连接池中拿连接的时候，都会向数据库发送一个类似 select 1 的测试查询语句来判断服务器是否正常运行。当该连接出现 disconnect 的情况时，该连接连同pool中的其它连接都会被回收。
    )
SessionFactory = sessionmaker(bind=engine)
session = scoped_session(SessionFactory)
