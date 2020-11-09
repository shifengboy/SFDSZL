#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test.py
@time:2020/11/08
"""
import yaml

with open('./main_page.yml',encoding='UTF-8') as f:
    datas = yaml.safe_load(f)
    steps = datas['goto_market']
    for step in steps:
         print(step)