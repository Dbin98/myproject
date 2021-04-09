import scrapy


class FirstSpider(scrapy.Spider):
    name = 'first'
    # 做限定的
    # allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/','https://www.sogou.com']

    def parse(self, response):
        print(response)
