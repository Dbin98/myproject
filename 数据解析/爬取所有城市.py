#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/25 15:09
# @Author  :Alive
# @Site    :
# @File    :爬取所有城市.py
# @Software:PyCharm
# 需求，爬取全国城市名称
import requests
from lxml import etree

if __name__ == '__main__':
    # UA 伪装
    headers = {
        'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    # 指定url
    url = 'https://www.aqistudy.cn/historydata/'
    # 获取相关页面数据
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    # 存储所有数据
    all_city = []
    # a_list = tree.xpath('//div[@class="bottom"]//a/text()')
    a_list = tree.xpath('//div[@class="bottom"]/ul/li/a/text() | //div[@class="bottom"]/ul/div/li/a/text()')
    for a in a_list:
        all_city.append(a)
    print(all_city, len(all_city))
