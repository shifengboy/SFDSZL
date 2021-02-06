#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:flask_restful_demo.py
@time:2021/01/22
"""
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['db'] = []

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


class TestCase(Resource):
    def get(self):
        testcase_id = request.args.get('id', None)
        if testcase_id:
            testcase = User.query.filter_by(id=testcase_id).first()
            # return testcase.username
            return jsonify(errorcode=0, bddy=testcase.username)
        else:
            return [user.username for user in User.query.all()]

    def post(self):
        # todo:用例的新增
        # app.config['db'].append(request.json)
        print(request.json)
        user = User(**request.json)
        print(user)
        db.session.add(user)
        db.session.commit()

        return {"msg": request.json, "errorcode": 0}

    def put(self):
        # todo:用例的更新
        pass

    def delete(self):
        # todo:用例的删除
        pass


api.add_resource(TestCase, '/testcase')

if __name__ == '__main__':
    app.run(debug=True)
