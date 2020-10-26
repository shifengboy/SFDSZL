#!/usr/bin/env python 
# encoding: utf-8 
'''
@Auther:陈士锋
@version: v1.0
@file: test_calc.py
@time: 2020/9/14 9:39 PM
'''
# 测试文件
import sys, os

import pytest
import yaml

sys.path.append(os.pardir)

from pythoncode.calc import Calculator


# 模块级别，在模块始末调用
def setup_module():
    print('模块级别setup')


def teardown_module():
    print('模块级别teardown')


# 函数级别，在函数始末调用（在类外部）
def setup_function():
    print('函数级别setup')


def teardown_function():
    print('函数级别teardown')


def test_case1():
    print('testcase1')


with open('datas/calc.yml') as f:
    datas = yaml.safe_load(f)
    myids = datas.keys()
    mydatas = datas.values()


class TestCalc:
    # setup_class,teardown_class 类级别每个类里面执行前后分别执行
    def setup_class(self):
        self.cal = Calculator()
        print('类级别setup')

    def teardown_class(self):
        print('类级别teardown')

    # 方法级别，每个方法里面的测试用例前后分别执行setup、teardown
    def setup(self):
        # self.cal = Calculator()
        print('setup')

    def teardown(self):
        print('teardown')

    # 方法级别，每个方法里面的测试用例前后分别执行setup、teardown
    def setup_method(self):
        # self.cal = Calculator()
        print('方法级别setup')

    def teardown_method(self):
        print('方法级别teardown')

    @pytest.mark.add
    @pytest.mark.parametrize('a,b,result', [
        (1, 1, 3),
        (2, 2, 4),
        (100, 100, 200),
        (0.1, 0.1, 0.2),
        (-1, -1, -2)
    ], ids=['int', 'int', 'bignum', 'float', '负数'])  # 参数化
    def test_add(self, a, b, result):
        # cal = Calculator()
        assert result == self.cal.add(a, b)

    # @pytest.mark.add
    # @pytest.mark.parametrize('a,b,result', mydatas, ids=myids)
    # def test_add1(self,a,b,result):
    #     # cal = Calculator()
    #     assert result == self.cal.add(a, b)

    @pytest.mark.div
    def test_div(self):
        # cal = Calculator()
        assert 1 == self.cal.div(1, 1)

