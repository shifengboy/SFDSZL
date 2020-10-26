#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_attach.py
@time:2020/10/11
"""
import allure

def test_attach_text():
    allure.attach('这是个纯文本',attachment_type=allure.attachment_type.TEXT)

def test_attach_html():
    allure.attach('<body>这是一个HTMLbody块</body>','html测试块',attachment_type=allure.attachment_type.HTML)

def test_attach_photo():
    allure.attach.file('/Users/chenshifeng/MyCode/PythonCode/SFDSZL/test_pytest/testcode/photo.png',name='这是一个图片',attachment_type=allure.attachment_type.PNG)

def test_attach_video():
    allure.attach.file('/Users/chenshifeng/Documents/视频demo.mp4',name='这是一个视频',attachment_type=allure.attachment_type.MP4)