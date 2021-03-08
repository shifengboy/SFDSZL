#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_server.py
@time:2021/01/25
"""
import time

import requests
from jenkinsapi.jenkins import Jenkins

from flask_test.server import db

timestamp = time.strftime("%y%m%d%H%M%S")


class TestTask:
    def test_db_init(self):
        # 初始化数据库
        db.create_all()

    def test_task_post(self):
        r = requests.post(
            'http://127.0.0.1:5000/task',
            json={
                "name": "chenshifeng1",
                "description": "测试描述demo",
                "testcases": {"1": "输入正确的用户名",
                              "2": "输入正确的密码",
                              "3": "登录成功"}
            }
        )
        print(r.json())
        assert r.status_code == 200

    def test_task_get(self):
        r = requests.get(
            'http://127.0.0.1:5000/task'
        )
        print(r.request.url)
        print(r.json())
        assert r.status_code == 200
        assert len(r.json()['body']) > 0

    def test_task_get_by_id(self, task_id=1):
        r = requests.get(
            'http://127.0.0.1:5000/task', params={'task_id': task_id}
        )
        print(r.json())
        assert r.status_code == 200
        assert len(r.json()['body']) > 0

    def test_jenkins(self):
        jenkins = Jenkins('http://shifeng.online:8080/', username='shifeng',
                          password='117e264a214fafba4c27b2580bfbc486a4')
        # jenkins = Jenkins('http://localhost:8080/', username='admin', password='117335232301e58eac7b14c43b75d3f5b8')
        print(jenkins.version)
        print(jenkins.keys())
        r = jenkins['iSelenium_Python'].invoke(build_params={'using_headless': True})
        print(r)

    def test_execution(self):
        r = requests.post(
            'http://127.0.0.1:5000/execution',
            json={
                'using_headless': True,
                "task_id": 2
            }
        )
        assert r.status_code == 200


class TestReport:
    def test_report_post(self):
        r = requests.post(
            'http://127.0.0.1:5000/report',
            json={
                'testcase_id': 1,
                'status': 'pass',
                'output': '',
            }
        )
        assert r.status_code == 200

    def test_report_get(self):
        r = requests.get(
            'http://127.0.0.1:5000/report'
        )
        assert r.status_code == 200
        assert len(r.json()['body']) > 0


if __name__ == '__main__':
    print(time)
