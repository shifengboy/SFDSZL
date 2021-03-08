#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@author:chenshifeng
@file:test_generate.py
@time:2020/11/29
"""
import json
from mitmproxy import http

# 修改规则模型
rule = [0, 1, 3, 5, 7,-10]

# 统计url
url_index = dict()

def response(flow: http.HTTPFlow):
    # 拿到请求 url
    url = flow.request.url.split('.json')[0]

    # 如果 url 不在 url_index 字典的key中
    if url not in url_index.keys():
        # 把对应的key值赋值为0
        url_index[url] = 0
    else:
        url_index[url] += 1

    seed = url_index[url] % len(rule)


    # 加上过滤条件
    if "quote.json" in flow.request.pretty_url and "x=" in flow.request.pretty_url:
        # 把响应数据转化成python对象，保存到data中
        data = json.loads(flow.response.text)
        # print('data:',data)
        # print(flow.response.content)

        # 对数据进行批量修改
        # data_new = json_travel(data, num=9)
        data_new = json_travel(data, array=rule[seed])
        print("array:",rule[seed])

        # data['data']['items'][0]['quote']['name'] = "hhshife0001"
        # data['data']['items'][1]['quote']['name'] = "shife00002"
        # data['data']['items'][1]['quote']['current'] = 0.1
        # print('data_new:',data_new)
        # 把修改后的内容赋值给 response 原始数据格式
        # flow.response.text = json.dumps(data)
        flow.response.text = json.dumps(data_new)
        # print(flow.response.text)



# dict、list、string、num（int、float）
def json_travel(data, array=None, text=1, num=1):
    """
    完成json数据的倍数操作
    :param data: 要修改的内容
    :param array: 列表的修改规则，为None默认不修改
    :param text: 字符串的修改规则，为1默认不修改
    :param num: 整数或者浮点数的修改规则，为1默认不修改
    :return: data_new
    """
    # 定义返回的数据
    data_new = None

    # 判断传入data的类型
    if isinstance(data, dict):
        # 把修改后的数据定义为一个空字典
        data_new = dict()

        # 对传入的响应数据进行遍历
        for k, v in data.items():
            # 每一个key所对应的value，也就是v传入的json_travel继续处理
            data_new[k] = json_travel(v, array, text, num)


    # 如果是列表，对列表的每一项进行遍历
    elif isinstance(data, list):
        data_new = list()

        # 遍历列表中的所有元素
        for item in data:
            item_new = json_travel(item, array, text, num)
            # print(item_new)

            # 如果传入的array为空，对列表的元素不做处理
            if array is None:
                data_new.append(item_new)
            else:
                # 判断传入的array修改规则，是否可以正常修改
                if isinstance(array, int) and array >= 0:
                    # 对每一个元素进行加倍修改
                    for i in range(array):
                        data_new.append(item_new)
                else:
                    data_new = data

    # 如果是字符串
    elif isinstance(data, str):
        # 如果 text 为正整数
        if isinstance(text, int) and text >= 0:
            # 对于字符串做加倍操作
            data_new = data * text
        else:
            data_new = data

    # 如果是int或者float这样的数字
    elif isinstance(data, int) or isinstance(data, float):
        # 对数字做乘积运算
        if data is not True:
            data_new = data * num

    # 其他数据类型保持原样
    else:
        data_new = data

    return data_new

if __name__ == '__main__':
    data =  {
              "name": "chenshifeng",
              "age": 18,
              "age2":19,
              "interest": ["song","eat","TV","movie"],
              "work": {
                "company1": "software testing",
                "company2": " software development"
              }
            }
    print(json_travel(data, num=2))