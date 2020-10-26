#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_demo.py
@time:2020/10/22
"""
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class TestTestdemo():
    def setup_method(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self, method):
        self.driver.quit()

    def test_testdemo(self):
        self.driver.get("http://www.baidu.com")
        sleep(3)

    def test_cookie(self):
        # get_cookies() 可以获取当前打开的页面的cookies 信息
        # add_cookie() 可以把cookie 添加到当前的页面中去
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        # cookies = self.driver.get_cookies()
        cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850882282754'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850882282754'}, {'domain': '.qq.com', 'expiry': 1603462272, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1872331554.1603375850'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'LByZgHuduBrwXVen3sfhf-yhwD6PJTyrH1c-BMxaB720YdfIrJhwxefj0EAyqIn7'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5083071'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603375848'}, {'domain': '.qq.com', 'expiry': 1609339394, 'httpOnly': False, 'name': 'ied_qq', 'path': '/', 'secure': False, 'value': 'o1162704960'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '1158598003647831'}, {'domain': 'work.weixin.qq.com', 'expiry': 1603407383, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '7f2fseq'}, {'domain': '.work.weixin.qq.com', 'expiry': 1605967886, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1666447872, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1306355502.1603284081'}, {'domain': '.qq.com', 'expiry': 1834156752, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '9387b03e6aa8d66d'}, {'domain': '.work.weixin.qq.com', 'expiry': 1634820079, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1605371131, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1162704960'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1914334385, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'eee2052bc1c9659f234b207682e7ad0d970699f1e2ef15a03d68400c402983fa'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '1162704960'}, {'domain': '.qq.com', 'expiry': 1850612037, 'httpOnly': False, 'name': 'mobileUV', 'path': '/', 'secure': False, 'value': '1_1657426fdb0_29ae0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'LaDeEevhSf72mBGv-bHNzKh0MwD-11QdmFQz0dg6Ju5ELyEVTGaPeiWeAY6u8v66EKuNts1Btnj-ptv2Q4TbAcOr_LEQ_Kx5IkOBRSK4AVrVWf4MoILBN2M7tHFg4Tgi8By2FXE13xyPqqAlJ91sbSUY5ReVeBoOTn8ATjP5fCxUitDVvB-lQy1sqpWAsKOMJQ9DZMWJoeM8cr_JK_rgETL-LjyVohmUh2i_lME9mELmbU0o9Rq7rdna9RVTui2SsCZ21loaOgqtJwTvoFU6dg'}, {'domain': '.qq.com', 'expiry': 1834156744, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_1162704960'}, {'domain': '.work.weixin.qq.com', 'expiry': 1634911848, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603284080,1603284112,1603375848'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325033002201'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '6922481664'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8707570602'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'p8RVgZKAUd'}]
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(4)

    def test_shelve(self):
        # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 可以通过 key，value 来把数据保存到shelve中
        # 读取cookie
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850882282754'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850882282754'}, {'domain': '.qq.com', 'expiry': 1603462272, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1872331554.1603375850'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'LByZgHuduBrwXVen3sfhf-yhwD6PJTyrH1c-BMxaB720YdfIrJhwxefj0EAyqIn7'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a5083071'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603375848'}, {'domain': '.qq.com', 'expiry': 1609339394, 'httpOnly': False, 'name': 'ied_qq', 'path': '/', 'secure': False, 'value': 'o1162704960'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '1158598003647831'}, {'domain': 'work.weixin.qq.com', 'expiry': 1603407383, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '7f2fseq'}, {'domain': '.work.weixin.qq.com', 'expiry': 1605967886, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.qq.com', 'expiry': 1666447872, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1306355502.1603284081'}, {'domain': '.qq.com', 'expiry': 1834156752, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': '9387b03e6aa8d66d'}, {'domain': '.work.weixin.qq.com', 'expiry': 1634820079, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1605371131, 'httpOnly': False, 'name': 'ptui_loginuin', 'path': '/', 'secure': False, 'value': '1162704960'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.qq.com', 'expiry': 1914334385, 'httpOnly': False, 'name': 'iip', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'eee2052bc1c9659f234b207682e7ad0d970699f1e2ef15a03d68400c402983fa'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'o_cookie', 'path': '/', 'secure': False, 'value': '1162704960'}, {'domain': '.qq.com', 'expiry': 1850612037, 'httpOnly': False, 'name': 'mobileUV', 'path': '/', 'secure': False, 'value': '1_1657426fdb0_29ae0'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'LaDeEevhSf72mBGv-bHNzKh0MwD-11QdmFQz0dg6Ju5ELyEVTGaPeiWeAY6u8v66EKuNts1Btnj-ptv2Q4TbAcOr_LEQ_Kx5IkOBRSK4AVrVWf4MoILBN2M7tHFg4Tgi8By2FXE13xyPqqAlJ91sbSUY5ReVeBoOTn8ATjP5fCxUitDVvB-lQy1sqpWAsKOMJQ9DZMWJoeM8cr_JK_rgETL-LjyVohmUh2i_lME9mELmbU0o9Rq7rdna9RVTui2SsCZ21loaOgqtJwTvoFU6dg'}, {'domain': '.qq.com', 'expiry': 1834156744, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '1_1162704960'}, {'domain': '.work.weixin.qq.com', 'expiry': 1634911848, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1603284080,1603284112,1603375848'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325033002201'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvi', 'path': '/', 'secure': False, 'value': '6922481664'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '8707570602'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'p8RVgZKAUd'}]

        db = shelve.open("cookies")
        # db['cookie'] = cookies
        cookies = db['cookie']
        db.close()
        # 利用读取的cookie 完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        sleep(2)