import requests
import parsel
import json

'''
Get web code
'''
url = 'https://blog.csdn.net/weixin_40651515/article/details/105925123?ops_request_misc=&request_id=&biz_id=102&utm_term=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&utm_medium=distribute.pc_search_result.none-task-blog-2~all~sobaiduweb~default-1-105925123.nonecase&spm=1018.2226.3001.4187'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
        }
response = requests.get(url=url, headers=headers)

#print(response.text)

'''
Parse Data
'''
selector = parsel.Selector(response.text)
content = selector.css('.htmledit_views').get()
print(type(content))
print(content)



# '''
# Attract blog contents
# '''
# for link in href:
#     print(link)
#     respomse_1 = requests.get(url=link, headers=headers)
#     selector_1 = parsel.Selector(respomse_1.text)
#     title = selector_1.xpath('').get()
#     content = selector_1.xpath('').get()