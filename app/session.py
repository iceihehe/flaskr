# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DefaultConfig

master = create_engine(DefaultConfig.MASTER_DATABASE_URI, echo=True)
slave = create_engine(DefaultConfig.SLAVE_DATABASE_URI, echo=True)

Session = sessionmaker(bind=master)


def with_slave(func):
    """使用从库的装饰器"""

    def wrapper(*args, **kwargs):

        s = Session()
        oldbind = s.bind
        s.bind = slave

        try:
            return func(*args, **kwargs)
        finally:
            s.bind = oldbind

    return wrapper
