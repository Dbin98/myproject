#!/user/bin/env python
# -*- coding: utf-8 -*-
# @Time    :2021/3/17 19:50
# @Author  :Alive
# @Site    :
# @File    :pac.py
# @Software:PyCharm
import os
import time

import requests
from bs4 import BeautifulSoup


def get_html(post_name, tab, pn):
    """
    获取html
    :param post_name: 贴吧名
    :param tab: 标签名
    :param pn: 页码
    :return:
    """
    try:
        url = 'https://tieba.baidu.com/f'

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                          Chrome/75.0.3770.100 Safari/537.36'
        }
        # tag:
        # 核心区：corearea; 看帖：main
        data = {
            'kw': post_name,
            'tab': tab,
            'pn': pn,
        }
        response = requests.get(url, params=data, headers=headers, timeout=30)
        # 必须修改HTML页面，把HTML结束标签改到最后，否则soup解析只到原来的HTML标签就结束了，后面的code标签里的内容被丢弃
        html = response.text.replace('</body>', '')
        html = html.replace('</html>', '')
        response = html + '</body></html>'
        # response.encoding = 'utf-8'
        # print(response.text)
        return response
    except RuntimeError:
        return 'ERROR'

def get_post_info(html, m, pn):
    """
    获取帖子的标题、链接信息，并从中筛选出有特定关键词的帖子
    :param html: 处理后的HTML页面
    :param m: month
    :param pn: 页码
    :return: 帖子信息
    """
    url = 'https://tieba.baidu.com'
    soup = BeautifulSoup(html, 'lxml')
    # 找到目标code标签，返回tag列表
    code = soup.find_all('code', attrs={'id': 'pagelet_html_frs-list/pagelet/thread_list'})
    # 提取code标签的内容（注释），返回列表
    comment = code[0].contents
    # print(type(comment[0]))
    # comment = code[0].string
    # print(type(comment))
    # 重新开始解析comment
    soup = BeautifulSoup(comment[0], 'lxml')
    # soup = BeautifulSoup(comment, 'lxml')

    # 找到目标li标签
    info = []

    # # 先找到置顶帖
    # litags_top = soup.find_all('li', attrs={'class': 'j_thread_list thread_top j_thread_list clearfix'})
    # for li in litags_top:
    #     info_top = dict()
    #     try:
    #         info_top['title'] = li.find('a', attrs={'class': 'j_th_tit'}).text.strip()
    #         info_top['link'] = ''.join([url, li.find('a', attrs={'class': 'j_th_tit'})['href']])
    #         info_top['time'] = li.find('span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
    #         info.append(info_top)
    #     except:
    #         print("错误：获取置顶帖标题失败！")

    # 再找到常规帖，提取标题、链接、发表日期、摘要信息
    litags = soup.find_all('li', attrs={'class': 'j_thread_list clearfix'})
    for li in litags:
        try:
            info_norm = dict()
            info_norm['title'] = li.find('a', attrs={'class': 'j_th_tit'}).text.strip()
            info_norm['link'] = ''.join([url, li.find('a', attrs={'class': 'j_th_tit'})['href']])
            info_norm['date'] = li.find('span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            info_norm['abstract'] = li.find('div', attrs={'class': 'threadlist_abs threadlist_abs_onlyline'}). \
                text.strip()
            info.append(info_norm)
        except AttributeError as e:
            print("错误：%s，可能是因为没有找到相应的标签" % e.args)
        except:
            print("错误：获取常规帖标题及摘要失败！")

    print('第 %s 页已经爬取成功， 开始处理...' % (pn/50+1))
    # 筛选发表日期在一个月以内，且标题和摘要里有关键词['发热'，'卡'， '掉帧'， '']的帖子
    # 获取当日日期
    today = time.strftime('%m-%d', time.localtime(time.time()))
    month = int(today.split('-')[0])
    day = int(today.split('-')[1])

    if month - m >= 1:
        last_month = month - m
    else:
        last_month = 12 + (month - m)
    # if last_month == 2 and day >= 29:
    #     one_month_before = ''.join([str(last_month), '-', '28'])
    # else:
    #     one_month_before = ''.join([str(last_month), '-', str(day)])

    # num = len(info)
    info_new = []
    for post in info:
        if ':' in post['date']:
            info_new.append(post)
        elif int(post['date'].split('-')[0]) == last_month and int(post['date'].split('-')[1]) >= day:
            info_new.append(post)
        elif int(post['date'].split('-')[0]) == month and int(post['date'].split('-')[1]) <= day:
            info_new.append(post)

    # # 关键词分开存放
    # keywords = ['发热', '卡顿', '掉帧', '卡死']
    # num = len(keywords)
    # info_has_kw = [[] for i in range(num)]
    # for post in info_new:
    #     for i in range(num):
    #         if keywords[i] in post['abstract']:
    #             info_has_kw[i].append(post)
    #             break

    print('第 %s 页已经处理完成，开始爬取下一页...' % (pn/50+1))
    # return info_has_kw
    return info_new

def save2file(info, savepath=os.path.dirname(os.path.realpath(__file__))+'\\post.txt'):
    """
    将爬取到的帖子内容写入到本地，保存到指定目录的txt文件中，保存目录默认为当前目录。
    :param info: 帖子内容
    :param savepath: 输出文件路径，默认为当前目录
    :return:
    """
    # num = len(info)
    # for i in range(num):
    #     with open(savepath, 'a+') as f:
    #         for post in info[i]:
    #             f.write('标题：{} \t 链接：{} \t'.format(post['title'], post['link']))
    with open(savepath, 'a+') as f:
        for post in info:
            f.write('标题：{} \t 链接：{} \t'.format(post['title'], post['link']))
    print("当前页面已经保存到本地！")

if __name__ == '__main__':
    post_name = '王者荣耀'
    tab = 'main'
    # 循环控制爬取的页数
    for pn in range(10):
        html = get_html(post_name, tab, pn*50)
        info = get_post_info(html, 3, pn*50)
        # print(info)
        save2file(info)
    print('-------所有帖子下载完成-------')