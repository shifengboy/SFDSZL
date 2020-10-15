#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_calc2.py
@time:2020/09/16
"""
#计算器测试用例
import pytest
from pythoncode.calc import Calculator


class TestCalculator:

    def setup_class(self):
        print("测试开始")
        self.calc = Calculator()

    def teardown_class(self):
        print("测试结束")

    def setup(self):
        print('【开始计算】')

    def teardown(self):
        print('【计算结束】')


    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 2], [100, 1, 200], [0.1, 0.1, 0.2], [-1, -1, -2],
        [1, 0.5, 1.5]
    ], ids=['int_case_pass', 'int_case_fail', 'float_case_pass', 'minus_case_pass', 'zero_case_pass'])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 0], [100, 1, 200], [0.8, 0.1, 0.7], [-2, -1, -1],
        [1, 0.5, 0.5]
    ], ids=['int_case_pass', 'int_case_fail', 'float_case_pass', 'minus_case_pass', 'zero_case_pass'])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [100, 1, 200], [0.1, 0.1, 0.01], [-1, -1, 1],
        [1, 0.5, 0.5]
    ], ids=['int_case_pass', 'int_case_fail', 'float_case_pass', 'minus_case_pass', 'zero_case_pass'])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [
        [1, 1, 1], [100, 1, 200], [0.1, 0.1, 1], [-1, -1, 1],
        [1, 0.5, 2]
    ], ids=['int_case_pass', 'int_case_fail', 'float_case_pass', 'minus_case_pass', 'zero_case_pass'])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect
