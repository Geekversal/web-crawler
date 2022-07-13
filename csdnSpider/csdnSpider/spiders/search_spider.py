import json

import scrapy
from csdnSpider.items import CsdnspiderItem
import re


class SearchSpider(scrapy.Spider):
    name = 'search_spider'
    # allowed_domains = ['csdn.net']
    # start_urls = ['http://csdn.net/']
    rec=re.compile(r'<em>|</em>')

    url='https://so.csdn.net/api/v2/search?q=人工智能&t=all&p={}&s=0&tm=0&lv=-1&ft=0&l=&u=&platform=pc'

    def start_requests(self):
        #开启多个线程 爬取多页
        for i in range(1,5,1):
            url=self.url.format(i)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )
    def parse(self, response):
        # 取接口返回数据，存入item
        res=json.loads(response.text)
        result_vos=res.get('result_vos')
        for i in result_vos:
            item=CsdnspiderItem()
            item['nickname']=re.sub(self.rec,'',i['nickname'] if 'nickname' in i and i['nickname']!=None else '')
            item['title']=re.sub(self.rec,'',i['title']  if 'title' in i and  i['title']!=None else '')
            item['description']=re.sub(self.rec,'',i['description']  if 'description' in i and  i['description']!=None else '')
            item['url']=re.sub(self.rec,'',i['url']  if 'url' in i and  i['url']!=None else '')

            yield item
