#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/22 15:05
# @Author  :Alive
# @Site    :
# @File    :百度翻译破解.py
# @Software:PyCharm
import requests
import json

if __name__ == '__main__':
    # UA伪装
    herders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    # 指定url
    post_url = 'https://fanyi.baidu.com/sug'
    # post请求参数处理
    while(True):
        kw = input("输入要翻译的英语单词：")
        data = {
            'kw': kw
        }
        # 进行请求，返回对象
        response = requests.post(url=post_url, data=data, headers=herders)
        # 获取json数据
        dict_obj = response.json()
        print(kw + '的意思是：' + dict_obj.get('data')[0]['v'])
