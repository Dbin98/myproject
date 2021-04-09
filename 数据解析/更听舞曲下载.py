#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/25 17:32
# @Author  :Alive
# @Site    :
# @File    :更听舞曲下载.py
# @Software:PyCharm
import requests
from lxml import etree
import os

if __name__ == '__main__':
    # 创建音乐文件夹
    if not os.path.exists('./音乐'):
        os.mkdir('./音乐')
    # 指定url
    url = 'http://www.333ttt.com/up/top16.html'
    # UA 伪装
    headers = {
        'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//div[@class="songlist"]/ul/li')
    for li in li_list:
        title = li.xpath('.//span[@class="l_bt_da"]/a//text()')[0] + '.mp3'
        last_url = li.xpath('.//span[@class="l_xz"]//text()')[0].split('\\')[5].split('\'')[1]
        music_data = requests.get(url=last_url, headers=headers).content
        filePath = './音乐/' + title
        with open(filePath, 'wb') as fp:
            fp.write(music_data)
            print(title + "下载完成")
    fp.close()
    print("下载完成")
