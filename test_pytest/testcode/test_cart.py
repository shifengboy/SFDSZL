#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_cart.py
@time:2020/09/16
"""
import pytest


#
# def test_cart1(login):
#     print('购物车用例1')
#
#
# def test_cart2(login):
#     print('购物车用例2')

# 参数化结合fixture使用
# 情况一：传入值和数据
# 情况二：传入一个fixture方法,将数据传入到fixture方法中，fixture使用request参数来接受这组数据，在方法体中使用request.param来接受这个数据
@pytest.mark.parametrize('login', [
    ('username1', 'passwd1'),
    ('username2', 'passwd2')
], indirect=True)
def test_cart3(login):
    print('购物车用例3')
