#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/24 14:28
# @Author  :Alive
# @Site    :
# @File    :xpath基础.py
# @Software:PyCharm
from lxml import etree

if __name__ == '__main__':
    # 实例化etree
    parser = etree.HTMLParser(encoding="utf-8")  # 自己创建html解析器，增加parser参数
    r = etree.parse('1.html', parser=parser)
    # print(r.xpath('//div[@id="top_left_menu"]//li[2]//text()'))
    # print(r.xpath('//title'))
    print(r)
