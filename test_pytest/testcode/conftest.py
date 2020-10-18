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