#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:handle_black2.py
@time:2020/11/10
"""
import allure


def handle_black2(func):
    def wrapper(*args,**kwargs):
        from frame.base_page import BasePage
        instance:BasePage = args[0]
        try:
            result = func(*args,**kwargs)
            return result
        except Exception as e:
            instance.driver.save_screenshot('temp2.png')
            allure.attach.file('./temp2.png',attachment_type=allure.attachment_type.PNG)
            if instance.err_num > instance.max_num:
                raise e
            for black in instance.black_list:
                ele = instance.driver.find_elements(*black)
                if len(ele)>0:
                    ele[0].click()
            instance.err_num +=1
            return wrapper(*args,**kwargs)
    return wrapper

