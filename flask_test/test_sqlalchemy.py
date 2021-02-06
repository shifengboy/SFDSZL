#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_sqlalchemy.py
@time:2021/01/23
"""
from flask_test.flask_sqlalchemy_demo import db, User


def test_db():
    db.create_all()
    all=User.query.all()
    print(all)
    user=User(id='1',username='shifeng',email='123456@qq.com')
    db.session.add(user)
    db.session.commit()