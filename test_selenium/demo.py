#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:demo.py
@time:2021/01/10
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--dump-dom')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument("--mute-audio")

driver = webdriver.Chrome(options=chrome_options, executable_path="/root/tool/chromedriver/chromedriver")
driver.get('http://www.baidu.com/')
print(driver.page_source)
driver.quit()
