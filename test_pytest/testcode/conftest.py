#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:conftest.py
@time:2020/09/15
"""

import pytest
import yaml
from pythoncode.calc import Calculator

# 钩子函数，解决中文用例名称显示乱码
def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture(params=['user1', 'user2', 'user3'])
# @pytest.fixture()
def login(request):
    print('登陆方法')
    print('传入的参数为：'+str(request.param))  # 获取params参数
    yield ['username', 'passwd']  # 激活fixture teardown方法
    print('teardown')

@pytest.fixture(scope='module')
def get_calc():
    print("计算开始")
    calc = Calculator()
    yield calc
    print("计算结束")