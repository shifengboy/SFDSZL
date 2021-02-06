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
        db.create_all()

    def test_task(self):
        r = requests.post(
            'http://127.0.0.1:5000/task',
            json={
                'name': f'shifeng{timestamp}',
                'email': '123456@qq.com',
                'testcases': [1, 2, 3]}
        )
        assert r.status_code == 200

        r = requests.get(
            'http://127.0.0.1:5000/task'
        )
        assert r.status_code == 200
        assert len(r.json()['body']) > 0

    def test_jenkins(self):
        # jenkins = Jenkins('http://shifeng.online:8080/',username='shifeng',password='117e264a214fafba4c27b2580bfbc486a4')
        jenkins = Jenkins('http://127.0.0.1:8080/', username='admin', password='117335232301e58eac7b14c43b75d3f5b8')
        print(jenkins.version)
        print(jenkins.keys())
        r = jenkins['iSelenium_Python'].invoke(build_params={'using_headless': True})
        print(r)

    def test_execution(self):
        r = requests.post(
            'http://127.0.0.1:5000/execution',
            json={'using_headless': True}
        )
        assert r.status_code == 200


if __name__ == '__main__':
    print(time)
