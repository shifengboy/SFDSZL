#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test.py
@time:2020/09/17
"""
import pytest


@pytest.fixture(scope='function')   #默认为scope='function'
def login():
    print('登陆方法')
    yield ['username','passwd']  #激活fixture teardown方法
    print('teardown')

# 测试用例之前，先执行login方法
def test_case1(login):
    print(f'case1 login={login}')

def test_case2(login):
    print(f'case2 login={login}')

def test_case3(login):
    print('case3')
