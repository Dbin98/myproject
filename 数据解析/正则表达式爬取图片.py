#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/23 18:01
# @Author  :Alive
# @Site    :
# @File    :正则表达式爬取图片.py
# @Software:PyCharm

import requests
import re
import os

if __name__ == '__main__':
    # 创建图片文件夹，保存图片
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    # UA伪装
    herders = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    # 设置通用的url模板
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    for pageNum in range(1, 3):
        # 对应页码的url
        new_url = format(url%pageNum)
        # 使用通用爬虫对整张页面进行爬取
        page_text = requests.get(url=new_url).text
        # 使用聚焦爬虫将页面中所有的糗图进行解析
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, page_text, re.S)  # re.S 单行匹配；re.M多行匹配
        for src in img_src_list:
            # 拼接出完整的url
            src = 'https:' + src
            # 请求到图片url
            img_data = requests.get(url=src).content
            # 持久化储存
            # 生成图片名称
            img_name = src.split('/')[-1]
            # 图片储存路径
            imgPath = './qiutuLibs/' + img_name
            with open(imgPath, 'wb') as fp:
                fp.write(img_data)
                print(img_name, '下载成功')
    print("爬取完成")