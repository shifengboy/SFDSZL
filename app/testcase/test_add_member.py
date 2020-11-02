#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_add_member.py
@time:2020/11/01
"""
from app.page.app import APP


class TestAddMember:
    def setup(self):
        self.app = APP()
        self.main = self.app.start().goto_main_page()

    def test_add_member(self):

        name = '老邓007'
        gender = '男'
        phonenu = '13100000007'
        result = self.main.go_address_list().click_addmember().click_manual_menu().add_member(name, gender,
                                                                                              phonenu).get_toast()
        assert '添加成功' == result
