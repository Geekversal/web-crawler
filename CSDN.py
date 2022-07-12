import requests
import parsel
import urllib.request as ur
import lxml.etree as le
import re

'''
Get web code
'''
keyword = input('关键词：')
pn_start = int(input('起始页：'))
pn_end = int(input('终止页：'))

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
        }
for page in range(pn_start, pn_end+1):
    response = requests.get(url='https://so.csdn.net/so/search/s.do?p={page}&q={keyword}&t=&viparticle=&domain=&o=&s=&u=&l=&f='.format(
               page=page, keyword=keyword), headers=headers)
    #print(response.text)

    '''
    Parse Data
    '''
    selector = parsel.Selector(response.text)
    #print(selector)
    href = selector.xpath("//h3[@class='title substr']/a/@href").getall()
    print(href)

    '''
    Attract blog contents
    '''
    for link in href:
        print(link)
        respomse_1 = requests.get(url=link, headers=headers)
        selector_1 = parsel.Selector(respomse_1.text)
        title = selector_1.xpath('').get()
        content = selector_1.xpath('').get()


'''
Create Dictionary
'''



#             # 博客标题
#             try:
#                 title = le.HTML(response_blog).xpath('//h1[@class="title-article"]/text()')[0]
#             except:
#                 print('-----标题不在设置固定类的标签中')
#             # 去除博客标题中的不合法关键字
#             title = re.sub(r'[/\\:*"<>|?]','',title)
#             print(title)
            #
            # # 网页存入本地
            # filepath = 'blog/%s.html' % title
            # with open(filepath, 'wb') as f:
            #     f.write(response_blog)
            # print(title)


