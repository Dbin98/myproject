#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/24 10:16
# @Author  :Alive
# @Site    :
# @File    :bs4基础.py
# @Software:PyCharm
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # 导入本地页面文件
    fp = open('1.html', 'r', encoding='UTF-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup)
    # print(soup.title)  # 返回的是第一次出现的tagName
    # print(soup.find('title')) # 返回的是第一次出现的tagName
    # print(soup.find('div', class_='wiki-common-headTabBar'))
    # print(soup.find_all('div'))  # 返回所有符合的标签
    # print(soup.select('.baike'))  # select可以返回标签，class，id选择器
    # print(soup.select('.special')[0].get_text())  # >表示一个层级，‘ ’表示多个层级
    print(soup.select('.special  a')[0])