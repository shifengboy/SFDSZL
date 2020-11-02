#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_delete_member.py
@time:2020/11/02
"""
from app.page.app import APP


class TestDeleteMember:
    def setup(self):
        self.app = APP()
        self.main = self.app.start().goto_main_page()

    def test_delete_member(self):
        name = '老邓007'
        result = self.main.go_address_list().click_member_manager().click_delete_member(
            name).delete_member().close_member_manager().search_member(name)
        assert '无搜索结果' == result

