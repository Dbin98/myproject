#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/22 15:57
# @Author  :Alive
# @Site    :
# @File    :豆瓣评分排行榜.py
# @Software:PyCharm
import requests
import json

if __name__ == '__main__':
    # 指定url
    url = 'https://movie.douban.com/j/chart/top_list'
    # UA伪装
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    # get参数处理
    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '0',
        'limit': '20',
    }
    # 发起请求,返回数据对象
    response = requests.get(url=url, params=param, headers=header)
    # 获取数据
    data_list = response.json()
    print(data_list)
    # 持久化保存
    with open('./dou.json', 'w', encoding='UTF-8') as fp:
        json.dump(data_list, fp=fp, ensure_ascii=False)
        fp.close()
    print("爬取成功")
