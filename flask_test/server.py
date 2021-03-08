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

jenkins = Jenkins('http://shifeng.online:8080/', username='shifeng', password='117e264a214fafba4c27b2580bfbc486a4')
jenkins_job = jenkins['jenkinsapi_test']


class TestCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    testcases = db.Column(db.String(1024), nullable=True)

    def __repr__(self):
        return '<User %r>' % self.id

    def as_dic(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'testcases': json.loads(self.testcases)
        }


# 一个测试任务/测试计划，代表了测试用的集合与编排顺序
class TaskServer(Resource):
    def get(self):
        task_id = request.args.get('task_id', None)
        if task_id:
            task = TestCase.query.filter_by(id=task_id).first()
            # return testcase.username
            return jsonify(errorcode=0, body=task.as_dic())
        else:
            result = {'errcode': 0, 'body': [task.as_dic() for task in TestCase.query.all()]}
            # result_json =  json.dumps(result, indent=2, ensure_ascii=False)
            return result

    def post(self):
        data = request.json.copy()
        data_new = data.copy()
        data_new["testcases"] = json.dumps(data["testcases"], ensure_ascii=False)
        task = TestCase(**data_new)
        db.session.add(task)
        db.session.commit()
        result = {"success": True, "msg": "提交成功", "data": data, "errcode": 0}
        # result_json = json.dumps(result, indent=2, ensure_ascii=False)
        return result

    def put(self):
        pass

    def delete(self):
        pass


class ExecutionService(Resource):
    def get(self):
        pass

    def post(self):
        # task = Task(**request.json)
        # using_headless = request.json.get('using_headless')
        # jenkins['iSelenium_Python'].invoke(build_params={'using_headless': using_headless})
        task_id = request.json.get('task_id')
        task = TestCase.query.filter_by(id=task_id).first()
        jenkins_job.invoke(build_params={'task': json.dumps(task.as_dic())})
        return {'errcode': 0, 'status_code': 200, 'msg': 'ok'}


class ResultService(Resource):
    """
    测试结果的保存
    """
    pass


'''
TestCase

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), unique=False, nullable=False)
    testcases = db.Column(db.String(1024), nullable=True)
'''


class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(120), unique=False, nullable=True)
    output = db.Column(db.String(1024), nullable=True)
    testcase_id = db.Column(db.Integer, db.ForeignKey('test_case.id'),  # 外键
                            nullable=False)
    testcase = db.relationship('TestCase',
                               backref=db.backref('reports', lazy=True))

    def as_dic(self):
        return {
            'id': self.id,
            'status': self.status,
            'testcase_id': self.testcase_id,
            'output': self.output
        }


class ReportService(Resource):
    def get(self):
        """
        查询测试结果，生成测试报告
        """
        # todo:
        report_id = request.args.get('report_id', None)
        if report_id:
            report = TestCase.query.filter_by(id=report_id).first()
            # return testcase.username
            return jsonify(errorcode=0, body=report.as_dic())
        else:
            result = {'errcode': 0, 'body': [report.as_dic() for report in Report.query.all()]}
            # result_json =  json.dumps(result, indent=2, ensure_ascii=False)
            return result

    def post(self):
        # todo:需要一层从name到id的转换
        report = Report(**request.json)
        db.session.add(report)
        db.session.commit()
        return {'errcode': 0, 'status_code': 200, 'msg': 'ok'}


api.add_resource(TaskServer, '/task')
api.add_resource(ExecutionService, '/execution')
api.add_resource(ReportService, '/report')
if __name__ == '__main__':
    app.run(debug=True)
