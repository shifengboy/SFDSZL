#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test.py
@time:2020/11/02
"""
import yaml

with open('appconfig.yml') as f:
    datas = yaml.safe_load(f)
    print(datas['ip'])