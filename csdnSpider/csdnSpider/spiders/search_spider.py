import json

import scrapy
from csdnSpider.items import CsdnspiderItem
import re
import urllib.parse
import w3lib.html

class SearchSpider(scrapy.Spider):
    name = 'search_spider'
    rec=re.compile(r'<em>|</em>')
    url = 'https://so.csdn.net/api/v3/search?q={}&t=blog&p={}&s=0&tm=0&lv=-1&ft=0&l=&u=&platform=pc'

    def __init__(self, keyword='AI', pages = '20', startPage = '1', saveDir = "./", **kwargs):
        self.keyword = keyword
        self.pages = int(pages)
        self.startPage = int(startPage)
        self.saveDir = saveDir

    #Scrape the multiple pages
    def start_requests(self):
        for i in range(self.startPage, self.startPage + self.pages,1):
            url=self.url.format(urllib.parse.quote(self.keyword) ,i)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )

    # Get meta data and save it to item
    def parse(self, response):
        res=json.loads(response.text)
        result_vos=res.get('result_vos')
        for i in result_vos:
            item=CsdnspiderItem()
            item['nickname']=re.sub(self.rec,'',i['nickname'] if 'nickname' in i and i['nickname']!=None else '')
            item['title']=re.sub(self.rec,'',i['title']  if 'title' in i and  i['title']!=None else '')
            item['description']=re.sub(self.rec,'',i['description']  if 'description' in i and  i['description']!=None else '')
            item['url']=re.sub(self.rec,'',i['url_location']  if 'url_location' in i and  i['url_location']!=None else '')
            # Follow the url to get the detail page
            yield scrapy.Request(
                url=item['url'],
                callback=self.parse_detail,
                meta={'csdnspideritem':item}
            )

    # Get detail page content and save it to item
    def parse_detail(self, response):
        item=response.meta['csdnspideritem']
        content=response.xpath('//*[@id="article_content"]').extract_first()
        # Exclude code sections
        codeSections = response.xpath('//*[@id="content_views"]/pre')
        for codeSec in codeSections:
            content=content.replace(codeSec.extract(),'')

        # Clean up the content
        content = content.strip().replace('\n','').replace('\r','').replace('\t','')
        content = re.sub(r'\s+',' ',content)
        # Remove all the tags and keep the text
        item['content']=w3lib.html.remove_tags(content)
        yield item