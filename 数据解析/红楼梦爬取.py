#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/24 14:12
# @Author  :Alive
# @Site    :
# @File    :红楼梦爬取.py
# @Software:PyCharm
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    url = 'http://www.purepen.com/hlm/index.htm'
    response = requests.get(url=url)
    response.encoding = 'GBK'
    page_text = response.text
    soup = BeautifulSoup(page_text, 'lxml')
    print(soup.find('tbody'))