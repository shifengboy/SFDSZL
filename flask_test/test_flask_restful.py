#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_flask_restful.py
@time:2021/01/23
"""
import requests

from flask_test.flask_restful_demo import db, User


def test_db():
    db.create_all()
    all=User.query.all()
    print(all)
    user=User(id='1',username='shifeng',email='123456@qq.com')
    db.session.add(user)
    db.session.commit()
    all=User.query.all()
    print(all)

def test_testcase_post():
    r = requests.post(
        'http://127.0.0.1:5000/testcase',
        json={'username':'shifeng3',
              'email': '123456@qq.com'
              }
    )
    print(r.text)
    assert r.status_code == 200

