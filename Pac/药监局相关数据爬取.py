#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/1/23 15:33
# @Author  :Alive
# @Site    :
# @File    :药监局相关数据爬取.py
# @Software:PyCharm
import requests
import json

if __name__ == '__main__':
    # 指定url
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    # UA伪装
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
    }
    all_list = []  # 所有数据
    id_list = []  # 所有ID列表
    # post参数处理
    for page in range(1, 6):
        data = {
            'on': 'true',
            'page': str(page),
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': '',
        }
        data_list = requests.post(url=url, data=data, headers=header).json()
        for list in data_list['list']:
            id_list.append(list['ID'])
    # 获取详细数据
    # 指定URL
    url2 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id': id
        }
        # 发起请求,返回对象
        results_json = requests.post(url=url2, data=data, headers=header).json()
        all_list.append(results_json)
    # 持久化存储
    fileName = '药监局.json'
    with open(fileName, 'w', encoding='UTF-8') as fp:
        json.dump(all_list, fp=fp, ensure_ascii=False)
        fp.close()
    print("爬取成功")
