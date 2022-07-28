from scrapy.crawler import CrawlerProcess
from csdnSpider.spiders.search_spider import SearchSpider
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from scrapy.utils.log import configure_logging

# Enable logging for CrawlerRunner
keywords = ["计算机架构", "算法与数据结构", "编程语言与编译器", "数学知识", "操作系统", "计算机网络", "数据库", "人工智能", "软件工程"]

configure_logging()
runner = CrawlerRunner(settings=get_project_settings())
for keyword in keywords:
    runner.crawl(SearchSpider, keyword = keyword, pages=20, startPage=1, saveDir="C:/Users/pwz26/OneDrive/Desktop/web-crawler/csdnSpider/")
deferred = runner.join()
deferred.addBoth(lambda _: reactor.stop())

reactor.run()  # the script will block here until all crawling jobs are finished
