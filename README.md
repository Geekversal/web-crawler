# web-crawler
## How to use
``` bash
$ cd csdnSpider
$ scrapy crawl search_spider -a keyword=<KEYWORD> -a pages=<NUM_OF_PAGE> -a startPage=<START_PAGE>
```
## Output
+ output file: KEYWORD_data.csv (csv format) in current directory
+ Format: nickname, title, description, url, content
## Note
+ Code sections are currently excluded from the result.
## Requirements
* [Scrapy 2.6.1](https://scrapy.org/)
## E.g.
``` bash
$ crapy crawl search_spider -a keyword=AI -a pages=20 -a startPage=1
```
