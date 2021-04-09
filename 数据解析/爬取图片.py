#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/23 18:00
# @Author  :Alive
# @Site    :
# @File    :爬取图片.py
# @Software:PyCharm
# 需求，爬取糗事百科相关图片
import requests

if __name__ == '__main__':
    # UA伪装
    herders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    url = 'https://pic.qiushibaike.com/system/pictures/12400/124006643/medium/56L2IYBOD6NX3C5I.jpg'
    # content返回二进制，text返回字符串、json()返回对象
    img_data = requests.get(url=url).content
    # 持久化存储
    with open('./choutu.jpg', 'wb') as fp:
        fp.write(img_data)
    print("爬取成功")
