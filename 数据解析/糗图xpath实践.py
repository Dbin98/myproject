#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/25 13:25
# @Author  :Alive
# @Site    :
# @File    :糗图xpath实践.py
# @Software:PyCharm
import requests
from lxml import etree
import os

if __name__ == '__main__':
    # 创建图片文件夹，保存图片
    if not os.path.exists('./糗图'):
        os.mkdir('./糗图')
    # 指定URL
    url = 'https://www.qiushibaike.com/imgrank/'
    # UA伪装
    headers = {
        'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    # 解析网页
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    a_list = tree.xpath('//div[@class="col1 old-style-col1"]//div[@class="thumb"]')
    print(a_list)
    # 解析图片url
    for i in a_list:
        detail_url = 'https:'+i.xpath('./a/img/@src')[0]
        # 发起请求
        img = requests.get(url=detail_url, headers=headers).content
        img_name = i.xpath('./a/img/@alt')[0] + '.jpg'
        # 图片储存路径
        imgPath = './糗图/' + img_name
        with open(imgPath, 'wb') as fp:
            fp.write(img)
        print(img_name, '下载成功')
    print('爬取完成')

