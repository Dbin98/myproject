#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/2/1 18:31
# @Author  :Alive
# @Site    :
# @File    :数据爬取.py
# @Software:PyCharm
import csv
import random
import time

import requests
from lxml import etree

url = "https://tieba.baidu.com/f?kw=中南民族大学&ie=utf-8&tab=main"
next = "https://tieba.baidu.com/f?kw=中南民族大学&ie=utf-8&pn={}"

fileHeader = ["姓名", "标题"]


def csv_data(fileHeader):
    with open("tieba.csv", "a", newline="", encoding='utf-8') as fp:
        write = csv.writer(fp)
        write.writerow(fileHeader)


def get_data(url):
    header = {
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'BIDUPSID=0CC35252D9B3C442C0F8D25ADF726880; PSTM=1602983543; BAIDUID=0CC35252D9B3C4421F4041BE2DBCFA1C:FG=1; ab_jid=4aa36af9a64bf235ddd1872de6407d83988e; ab_jid_BFESS=4aa36af9a64bf235ddd1872de6407d83988e; __yjs_duid=1_eae23490dfd738cdedc57a375b28389b1615005579852; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BDSFRCVID_BFESS=cmLOJeC62lgpwm6eEgAQT6zMBeK2qw5TH6aopufZ4m0hQVliXd9dEG0PHU8g0Kub5MgwogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tRk8oIL2fIvDqTrP-trf5DCShUFs--JiB2Q-XPoO3KO4MKnPbJbzMM-pbN7laloxLCPf3MbgylRp8P3y0bb2DUA1y4vpK-5u02TxoUJ2BM5IJhQMqtnW0PkebPRiJPb9Qg-qahQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hC8Ce5LMD63M5pJfejLO-I52sJOOaCvNMlTOy4oTj6Djbp3f265-3Cvt_f-KMq6Ieqk4KJth3MvB-fnj-45zJIDjBUjCanTieKTgQft20MkAeMtjBbQaJmjMLb7jWhvdep72yhodQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCHJ5KOtRPH_Iv5b-0_MDnxMt-_-P4DeUbLWURZ5mAqoJRj-P3VMR5HbUQG35KhXt5-B5jDbbTnaIQqa-JhexFmhj3s0qKjMJ7bq4343bRTaUKy5KJvfJ_GXtJbhP-UyPvMWh37QmJlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMopCafJOKHICRej_aDMK; BAIDUID_BFESS=0CC35252D9B3C4421F4041BE2DBCFA1C:FG=1; BDUSS=zR2cmV2blA4UHk5RGM4M2o5TnJYcWFJUmhVaVpyVEJiZjJYRVV2LVlMOGlpSGxnRVFBQUFBJCQAAAAAAAAAAAEAAAApg4BnAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACL7UWAi-1FgY; BDUSS_BFESS=zR2cmV2blA4UHk5RGM4M2o5TnJYcWFJUmhVaVpyVEJiZjJYRVV2LVlMOGlpSGxnRVFBQUFBJCQAAAAAAAAAAAEAAAApg4BnAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACL7UWAi-1FgY; ab_sr=1.0.0_M2M3ZTFiYTQ2YmYwYjFjZTJjYTBlNTkwMDQ5MDQ4M2FiOTFlZjExZTY5YjY3MmI5ZDQ4YzY0NzcwMjIwNDU4ZmRmNjllN2Q5OTY2ZGMzMGRiODIyNWI5YWVjZTNlZDU4',
        'Referer': 'https://tieba.baidu.com/f?ie=utf-8&kw=%E4%B8%AD%E5%8D%97%E6%B0%91%E6%97%8F%E5%A4%A7%E5%AD%A6',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 SLBrowser/7.0.0.2261 SLBChan/15'
    }
    response = requests.get(url=url, headers=header)
    response.encoding = "utf-8"
    page_text = response.text
    tree = etree.HTML(page_text)
    a_list = tree.xpath('//div[@id="content_leftList"]/ul/li/div/div[2]')
    for i in a_list:
        title = i.xpath('./div[1]/div[1]/a/text()')
        auther = i.xpath('./div[1]/div[2]//text()')[1]
        print([auther, title])


if __name__ == "__main__":
    # csv_data(fileHeader)
    get_data(url)
