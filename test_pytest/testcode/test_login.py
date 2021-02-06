#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_login.py
@time:2020/09/15
"""


import pytest

# 测试用例之前，先执行login方法
def test_case1(login):
    print(f'case1 login={login}')

@pytest.mark.usefixtures('login')
def test_case2():
    print('case2')
    # print(f'case1 login={login}')  #该方法无法获取返回值


def test_case3(login):
    print('case3')
