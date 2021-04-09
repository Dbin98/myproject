#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/24 11:32
# @Author  :Alive
# @Site    :
# @File    :bs4案例.py
# @Software:PyCharm
# 需求：爬取三国演义小说所有的章节内容
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    # UA伪装
    herders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    # 通用爬虫
    url = 'https://www.shicimingju.com/book/hongloumeng.html'
    response = requests.get(url=url)
    response.encoding = 'UTF-8'
    page_text = response.text
    soup = BeautifulSoup(page_text, 'lxml')
    li_list = soup.select('.book-mulu li')
    fp = open('./红楼梦.txt', 'w', encoding='UTF-8')
    for li in li_list:
        title = li.a.string
        # 拼接详情页面url
        detail_url = 'https://www.shicimingju.com' + li.a['href']
        detail_response = requests.get(url=detail_url)
        detail_response.encoding = 'UTF-8'
        detail_page_text = detail_response.text
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        tagName = detail_soup.find('div', class_='chapter_content')
        chapter = tagName.text
        fp.write(title + ':' + chapter +'\n')
        print(title + '   爬取成功')
    fp.close()
