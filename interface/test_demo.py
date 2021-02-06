#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_demo.py
@time:2020/11/24
"""
import requests
from jsonpath import jsonpath
from hamcrest import *
from requests.auth import HTTPBasicAuth


class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "name": "chenshifeng",
            "level": 1
        }
        r = requests.get('http://httpbin.testing-studio.com/get', params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post_form(self):
        payload = {
            "name": "chenshifeng",
            "level": 1
        }
        r = requests.post('http://httpbin.testing-studio.com/post', data=payload)
        print(r.text)  # r.text = r.encoding + r.content
        print(r.json())  # r.json() = r.encoding + r.content + Content-Type json
        assert r.status_code == 200

    def test_post_json(self):
        payload = {
            "name": "chenshifeng",
            "level": 1
        }
        r = requests.post('http://httpbin.testing-studio.com/post', json=payload)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_header(self):
        payload = {
            "name": "chenshifeng",
            "level": "1"
        }
        r = requests.get('http://httpbin.testing-studio.com/get', headers=payload)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()["headers"]["Name"] == "chenshifeng"

    def test_jsonpath(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        # print(r.json())
        print(jsonpath(r.json(), '$..name'))
        assert r.status_code == 200
        assert r.json()["category_list"]["categories"][0]["name"] == "开源项目"
        assert jsonpath(r.json(), '$..name')[0] == "开源项目"

    def test_hamcrest(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.text)
        assert_that(r.json()["category_list"]["categories"][0]["name"], equal_to("开源项目"))

    def test_cookie(self):
        header = {
            # 'Cookie': 'username=chenshifeng',
            'User-Agent': 'shifeng/2.25.0'
        }
        cookie_data = {"name": "chenshifeng", "love": "meinv"}
        # r = requests.get('http://httpbin.org/cookies',headers = header)
        r = requests.get('http://httpbin.org/cookies', headers=header, cookies=cookie_data)
        print(r.request.headers)

    def test_auth(self):
        r = requests.get('http://httpbin.org/basic-auth/shifeng/123456',auth = HTTPBasicAuth('shifeng','123456'))
        print(r)
        print(r.text)
