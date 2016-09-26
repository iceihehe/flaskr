# -*- coding: utf-8 -*-


class DefaultConfig(object):

    PROJECT = 'flaskr'

    SECRET_KEY = 'secret'

    MASTER_DATABASE_URI = 'postgresql://flaskr:flaskr@192.168.2.55/flaskr'
    SLAVE_DATABASE_URI = 'postgresql://flaskr:flaskr@192.168.2.55/flaskr'
