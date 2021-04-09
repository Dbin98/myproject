import requests
import json
import re
import os,csv
import time,random
os.chdir('C:/Users/zuk/Desktop')
import pandas as pd
from w3lib.html import remove_tags
base_url='''
https://m.weibo.cn/api/container/getIndex?containerid=100808abf16b190b1e62990c5d0a185cab7b57_-_sort_time&luicode=10000011&lfid=100103type=1&q=中南民族大学&since_id=4570020618700830
'''
commend_url = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id_type=0'
next_url = 'https://m.weibo.cn/comments/hotflow?id={}&mid={}&max_id={}&max_id_type={}'
head_list=["Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16",
    "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
    "Mozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14",
    "Opera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02",
   ]
ip=['114.101.42.16:65309',
    '220.179.255.7:8118',
    '103.44.145.182:8080',
    '115.223.7.110:80']
proxy={'http':random.choice(ip)}
header={'user-agent':random.choice(head_list)}
pat='since_id=(.*)'
inf=[]
commend = []
continue_url = commend_url
def getdata(base_url):
    for page in range(1,2):
        try:
            r = requests.get(base_url, headers=header, proxies=proxy)
            df = json.loads(r.text)
            since_id = df.get('data').get('pageInfo').get('since_id')
            data = df.get('data').get('cards')[0].get('card_group')
            for item in data:
                userid = item.get('mblog').get('user').get('id')
                username = item.get('mblog').get('user').get('screen_name')
                send_time = item.get('mblog').get('created_at')
                content = remove_tags(item.get('mblog').get('text'))
                reposts_count = item.get('mblog').get('reposts_count')
                comments_count = item.get('mblog').get('comments_count')
                attitudes_count = item.get('mblog').get('attitudes_count')
                send_url = 'https://m.weibo.cn/detail/'+ item.get('mblog').get('id')
                if comments_count > 0:
                    id = item.get('mblog').get('id')
                    mid = item.get('mblog').get('mid')
                    commendurl = commend_url.format(id, mid)
                    commend = []
                    try:
                        response = requests.get(url=commendurl, headers=header, proxies=proxy).json()
                        content_list = response.get('data').get('data')
                        for item in content_list:
                            created_at = item['created_at']
                            user_id = item.get('user')['id']
                            user_name = item.get('user')['screen_name']
                            text = item['text']
                            commend.append([created_at, user_id, user_name, text])
                    except:
                        print('未爬取数据')
                else:
                    commend = []
                inf.append([userid, username, send_time,send_url, content, reposts_count, comments_count, attitudes_count, commend,since_id])
            base_url = re.sub(pat, 'since_id=' + str(since_id), base_url)
            print('第{}页写入完毕'.format(page))
            time.sleep(random.randint(2, 4))
        except:
            print('未爬到数据')
    inf1 = pd.DataFrame(inf, columns=['用户id', '昵称', '发布时间','发布url','内容', '转发数', '评论数', '点赞数', '评论','sin_id'])
    inf1.to_csv('具有网址的网络舆情数据2.csv', index=False, encoding='gb18030')
    print('爬虫结束')

if __name__ == '__main__':
    getdata(base_url)
