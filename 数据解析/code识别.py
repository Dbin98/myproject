#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/27 11:25
# @Author  :Alive
# @Site    :
# @File    :code识别.py
# @Software:PyCharm

import requests
from lxml import etree
if __name__ == '__main__':
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    # 指定url
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/guwen/default.aspx'
    # 发起请求
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    url2 = 'https://so.gushiwen.cn' +tree.xpath('//*[@id="imgCode"]/@src')[0]
    img = requests.get(url=url2, headers=headers).content
    with open('./code.jpg','wb') as fp:
        fp.write(img)
    print('请人工识别')