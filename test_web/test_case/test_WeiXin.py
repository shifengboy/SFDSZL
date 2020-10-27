#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_WeiXin.py
@time:2020/10/25
"""


# from web.podemo1.page.main_page import MainPage
# from test_web.webpage.main_page import MainPage
#
#
# class TestWX:
#     def setup(self):
#         self.main = MainPage()
#
#     def test_addmember(self):
#         username = "aaaaaad"
#         account = "aaaaaad_hogwarts"
#         phonenum = "13400000003"
#
#         addmember = self.main.goto_addmember()
#         addmember.add_member(username, account, phonenum)
#         assert username in addmember.get_member(username)


from test_web.webpage.main_page import MainPage


class TestWeiXin:
    def setup(self):
        self.page = MainPage()
    def test_addmember(self):
        username = "sfusernametest003"
        account = "sfaccounttest003"
        phonenum = "13400000004"
        # self.page.goto_addmember().add_member(username, account, phonenum)

        # assert (username in self.page.goto_addmember().get_member(username))
        addmember = self.page.goto_addmember()
        addmember.add_member(username, account, phonenum)
        assert  addmember.get_member(username)
