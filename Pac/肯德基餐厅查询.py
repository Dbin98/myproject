#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/22 16:31
# @Author  :Alive
# @Site    :
# @File    :肯德基餐厅查询.py
# @Software:PyCharm
import requests

if __name__ == '__main__':
    # 指定url
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    # UA伪装
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    # 处理post参数
    keyword = input("请输入查询地址:")
    data = {
        'cname': '',
        'pid': '',
        'keyword': keyword,
        'pageIndex': '1',
        'pageSize': '100'

    }
    # 发起请求、返回对象
    response = requests.post(url=url, data=data, headers=header)
    # 获取数据
    add_list = response.text
    print(add_list)
    # 持久化存储
    fileName = keyword + '地区餐厅地址'
    with open(fileName, 'w', encoding='UTF-8') as fp:
        fp.write(add_list)
        fp.close()
    print(fileName, "查询完毕")
