#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/3/5 10:47
# @Author  :Alive
# @Site    :
# @File    :超话内容爬取.py
# @Software:PyCharm
import requests
import json
import re
import csv
import time,random
from w3lib.html import remove_tags
fileHeader = ['发布时间','内容']
def csv_data(fileHeader):
    with open("chaohua.csv", "a", newline="") as fp:
        write = csv.writer(fp)
        write.writerow(fileHeader)
url = 'https://m.weibo.cn/api/container/getIndex?containerid=100808abf16b190b1e62990c5d0a185cab7b57_-_sort_time&luicode=10000011&lfid=100103type=1&q=中南民族大学'

head_list=["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.1071 SLBChan/15",
   ]
ip=['175.146.208.226',
    '60.167.159.165',
    '222.141.244.206',
    '110.243.2.113']
proxy={'http':random.choice(ip)}
header={'user-agent':random.choice(head_list)}
next_url = 'https://m.weibo.cn/api/container/getIndex?containerid=100808abf16b190b1e62990c5d0a185cab7b57_-_sort_time&luicode=10000011&lfid=100808abf16b190b1e62990c5d0a185cab7b57&since_id={}'
pat='since_id=(.*)'
for page in range(1,300):
    try:
        r=requests.get(url,headers=header,proxies=proxy)
        df=json.loads(r.text)
        since_id=df.get('data').get('pageInfo').get('since_id')
        data=df.get('data').get('cards')[0].get('card_group')
        for item in data:
            send_time=item.get('mblog').get('created_at')
            content=remove_tags(item.get('mblog').get('text'))
            csv_data([send_time, content])
        url=re.sub(pat,'since_id='+str(since_id),url)
        print('第{}页写入完毕'.format(page))
        time.sleep(random.randint(3,5))
    except:
        print('未爬到数据')
