#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/25 15:27
# @Author  :Alive
# @Site    :
# @File    :站长素材简历模板下载.py
# @Software:PyCharm
# 需求:爬取站长素材中免费简历模板
import requests
from lxml import etree
import os
if __name__ == '__main__':
    # 创建文件夹保存简历
    if not os.path.exists('./简历'):
        os.mkdir('./简历')
    # UA伪装
    headers = {
        'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    # 指定url
    url = 'https://sc.chinaz.com/jianli/free.html'
    response = requests.get(url=url, headers=headers)
    response.encoding = 'UTF-8'
    page_text = response.text
    tree = etree.HTML(page_text)
    # 解析下一页url
    url_list = tree.xpath('//div[@id="main"]/div/div/a/@href')
    for i in url_list:
        next_url = 'https:' + i
        # 发起请求
        next_page = requests.get(url=next_url, headers=headers).text
        html = etree.HTML(next_page)
        # 解析最终url
        last_url = html.xpath('//ul[@class="clearfix"]/li[1]/a/@href')[0]
        # 发起请求
        doc_data = requests.get(url=last_url, headers=headers).content
        # 定义简历名称
        fileName = last_url.split('/')[-1]
        # 设置保存路径
        filePath = './简历/' + fileName
        # 持久化保存
        with open(filePath,'wb') as fp:
            fp.write(doc_data)
        print(fileName+'下载完成')
    print("爬取完成")
