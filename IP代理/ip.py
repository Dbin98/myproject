#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/31 14:38
# @Author  :Alive
# @Site    :
# @File    :ip.py
# @Software:PyCharm
import requests

url = 'http://ip.293.net/'
# UA伪装
headers = {
    'UserAgent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
}
response = requests.get(url=url, headers=headers, proxies={"http": "123.101.237.80:9999"})
print(response.status_code)
page_text = response.text
with open('ip.html', 'w', encoding='utf-8') as fp:
    fp.write(page_text)
