#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_taobao.py
@time:2020/12/16
"""
from time import sleep

from selenium import webdriver
class TestTaobao:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://s.taobao.com/search?q=lv')
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()
        pass

    def test_taobao(self):
        sleep(10)
        price_list = []
        title_list = []
        price_elements_list = self.driver.find_elements_by_xpath('//*[@class="price g_price g_price-highlight"]')
        title_elements_list = self.driver.find_elements_by_xpath('//*[@class="row row-2 title"]')

        # print(price_elements_list)
        for i in price_elements_list:
            price = i.text
            price_list.append(price)
        for i in title_elements_list:
            title = i.text
            title_list.append(title)

        data = []
        for i in range(len(price_list)):
            data.append([i,price_list[i],title_list[i]])

        print(data)




        import xlwt
        title = [
            '序号','价格','标题'
        ]
        #新建一个excel对象
        wbk = xlwt.Workbook()
        #添加一个名为 课程表的sheet页
        sheet = wbk.add_sheet('淘宝LV数据')
        for i in  range(len(title)):#写入表头
            sheet.write(0,i,title[i])#写入每行,第一个值是行，第二个值是列，第三个是写入的值
        for i in range(len(price_list)):
            if i !=0:#如果不是表头的话
                for j in range(3):
                    sheet.write(i,j,data[i][j])#循环写入每行数据
        #保存数据到‘test.xls’文件中
        wbk.save('szz.xls')#保存excel必须使用后缀名是.xls的，不是能是.xlsx的

