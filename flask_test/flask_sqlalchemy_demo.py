#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:flask_test-sqlalchemy_demo.py
@time:2021/01/23
"""

from flask_sqlalchemy import SQLAlchemy

from flask_test.flask_restful_demo import app

username = 'shifeng_test'
password = '123456'
host = '127.0.0.1'
port = 3306
dbname = 'flask'
option = 'charset=utf8mb4'

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}?{option}'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    steps = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.username
