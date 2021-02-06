#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:server.py
@time:2021/01/24
"""
import json

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from jenkinsapi.jenkins import Jenkins

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

username = 'shifeng_test'
password = '123456'
host = '127.0.0.1'
port = 3306
dbname = 'flask'
option = 'charset=utf8mb4'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{host}:{port}/{dbname}?{option}'

jenkins = Jenkins('http://127.0.0.1:8080/', username='admin', password='117335232301e58eac7b14c43b75d3f5b8')


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    testcases = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.name

    def as_dic(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'testcases': json.loads(self.testcases)
        }


# 一个测试任务/测试计划，代表了测试用的集合与编排顺序
class TaskServer(Resource):
    def get(self):
        task_id = request.args.get('id', None)
        if task_id:
            task = Task.query.filter_by(id=task_id).first()
            # return testcase.username
            return jsonify(errorcode=0, body=task.as_dic())
        else:
            return {'errcode': 1, 'body': [task.as_dic() for task in Task.query.all()]}

    def post(self):
        data = request.json.copy()
        data['testcases'] = json.dumps(data['testcases'])
        task = Task(**data)
        print(task)
        db.session.add(task)
        db.session.commit()
        return {'msg': 'ok', 'errcode': 0}

    def put(self):
        pass

    def delete(self):
        pass


class ExecutionService(Resource):
    def get(self):
        pass

    def post(self):
        # task = Task(**request.json)
        using_headless = request.json.get('using_headless')
        jenkins['iSelenium_Python'].invoke(build_params={'using_headless': using_headless})
        return {'errcode': 0, 'status_code': 200, 'msg': 'ok'}


class ResultService(Resource):
    """
    测试结果的保存
    """
    pass


class ReportService(Resource):
    def get(self):
        """
        查询测试结果，生成测试报告
        """
        pass

    def post(self):
        pass


api.add_resource(TaskServer, '/task')
api.add_resource(ExecutionService, '/execution')
if __name__ == '__main__':
    app.run(debug=True)
