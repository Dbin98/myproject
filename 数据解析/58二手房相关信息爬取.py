#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/24 17:36
# @Author  :Alive
# @Site    :
# @File    :58二手房相关信息爬取.py
# @Software:PyCharm
import requests
from lxml import etree

if __name__ == '__main__':
    # UA伪装
    headers = {
        'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    # 获取页面数据
    parser = etree.HTMLParser(encoding='UTF-8')
    html = etree.parse('2.html', parser=parser)
    data_list = html.xpath('//div[@class="property"]')
    # 持久化保存
    fp = open('./武汉二手房.txt', 'w', encoding='UTF-8')
    for li in data_list:
        title = li.xpath('.//div[@class="property-content-title"]/h3/text()')[0]
        detail = li.xpath('.//p[@class="property-price-total"]//text()')[0]
        fp.write(title+':'+'价格'+':'+detail+'万'+'\n')
        print(title+'  爬取成功')
    fp.close()



