#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/22 11:05
# @Author  :Alive
# @Site    :
# @File    :网页采集器.py
# @Software:PyCharm
import requests
# UA伪装
if __name__ == '__main__':
    # UA伪装
    herders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带参数：用字典的方法
    kw = input('输入关键字：')
    params = {
        'query': kw
    }
    # 使用params参数对携带参数进行拼接,返回response对象
    response = requests.get(url=url, params=params, headers=herders)
    # 获取响应数据的字符串
    page_text = response.text
    # 持久化保存
    fileName = kw+'.html'
    with open(fileName, 'w', encoding='UTF-8') as ft:
        ft.write(page_text)
        ft.close()
    print(fileName, "爬虫结束")
