#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/2/25 11:24
# @Author  :Alive
# @Site    :
# @File    :微博评论数据采集.py
# @Software:PyCharm
import csv
import re
import time

import requests
import json

fileHeader = ["id", "评论时间", "用户id", "昵称", "评论内容"]
url = 'https://m.weibo.cn/comments/hotflow?id=4608230024020646&mid=4608230024020646&max_id_type=0'
next_url = 'https://m.weibo.cn/comments/hotflow?id=4608230024020646&mid=4608230024020646&max_id={}&max_id_type={}'
count = 0
continue_url = url

def csv_data(fileHeader):
    with open("weibo.csv", "a", newline="") as fp:
        write = csv.writer(fp)
        write.writerow(fileHeader)

url_list = []
def get_data(i):
    # UA伪装
    headers = {
        'Cookie':'XSRF-TOKEN=422f3a; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=oid%3D4608230024020646%26luicode%3D10000011%26lfid%3D231522type%253D1%2526t%253D10%2526q%253D%2523%25E4%25B8%258A%25E6%25B5%25B7%25E5%25A4%25A7%25E5%25AD%25A6%25E8%2580%2583%25E7%25A0%2594%25E6%2588%2590%25E7%25BB%25A9%2523%26uicode%3D20000061%26fid%3D4608230024020646; SUB=_2A25NM1WpDeRhGeNJ41EV8SzPyT6IHXVu3HvhrDV6PUJbkdAfLVPkkW1NS4hD33ytzMfLUH7oOXcB5W0MlzynLfdw; _T_WM=88470475858',
        'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0',
        'Referer': 'https://m.weibo.cn/detail/4608230024020646'
    }
    for i in url_list:
        response = requests.get(url=url_list[i], headers=headers).json()
        max_id = response.get('data')['max_id']
        max_id_type = response.get('data')['max_id_type']
        content_list = response.get('data').get('data')
        for item in content_list:
            global count
            count += 1
            created_at = item['created_at']
        user_id = item.get('user')['id']
        user_name = item.get('user')['screen_name']
        text = ''.join(re.findall('[\u4e00-\u9fa5]',item['text']))
        print([count, created_at, user_id, user_name, text])
        csv_data([count, created_at, user_id, user_name, text])
    global next_url
    continue_url = next_url.format(max_id,max_id_type)
    print(continue_url)
    time.sleep(2)
    get_data(continue_url)  # 调用函数本身

if __name__ == "__main__":
    csv_data(fileHeader)
    get_data(url)
