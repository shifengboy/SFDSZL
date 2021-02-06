#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:jenkins_api.py
@time:2021/01/16
"""
import requests
'''
import json    
   dic = {"name":"niuniu","age":18}
   print(json.dumps(dic))#把字典转成json串
   fj = open('a.json','w')
   print(json.dump(dic,fj))#把字典转换成的json串写到一个文件里面
   s_json = '{"name":"niuniu","age":20,"status":true}'
   print(json.loads(s_json))#把json串转换成字典
   fr = open('b.json','r')
   print(json.load(fr))#从文件中读取json数据，然后转成字典
'''

url = 'shifeng:chenshifeng@http://shifeng.online:8080/job/iInterface_python/build'

result = requests.post(url)
