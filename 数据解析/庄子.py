#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/27 11:30
# @Author  :Alive
# @Site    :
# @File    :庄子.py
# @Software:PyCharm
import requests
from lxml import etree
import os

if __name__ == '__main__':
    # 创建庄子目录
    if not os.path.exists('./庄子'):
        os.mkdir('./庄子')
    # 指定url
    url = 'https://so.gushiwen.org/search.aspx?value=庄子'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    page_text = requests.get(url=url, headers=headers).text
    # 加载
    tree = etree.HTML(page_text)
    div_list = tree.xpath('//div[@class="sons"]')
    for i in div_list:
        detail_url = 'https://so.gushiwen.org' + i.xpath('./div/p/a/@href')[0]
        title = i.xpath('./div/p/a//text()')[0] + i.xpath('./div/p/a//text()')[1]
        # 发起请求
        detail_page = requests.get(detail_url, headers=headers).text
        html = etree.HTML(detail_page)
        data = html.xpath('//div[@class="contson"]//text()')[1]
        path = './庄子/' + title + '.txt'
        with open(path, 'w', encoding='utf-8') as fp:
            fp.write(data)
        print(title + '下载成功')
    print('下载完成')
