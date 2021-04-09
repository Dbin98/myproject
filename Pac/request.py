#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/22 10:23
# @Author  :Alive
# @Site    :
# @File    :request.py
# @Software:PyCharm
import requests

if __name__ == '__main__':
    # 指定url
    url = 'https://www.sogou.com/'
    # 发起请求,返回响应对象
    response = requests.get(url=url)
    # 获取响应对象数据，返回字符串
    page_text = response.text
    print(page_text)
    # 持久化存储
    with open('./sougou.html', 'w', encoding='UTF-8') as ft:
        ft.write(page_text)
    print("爬取数据结束")
