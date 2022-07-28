# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
from os.path import exists

class CsdnspiderPipeline:
    def open_spider(self, spider):
        file = spider.saveDir + spider.keyword + '_data.csv'
        exist = exists(file)
        self.f = open(file, 'a+',newline="", encoding='utf-8')
        # Write headers of the csv file if it doesn't exist
        self.fieldnames = ["nickname", "title", "description", "url", "content"]
        self.writer = csv.DictWriter(self.f, fieldnames=self.fieldnames)
        if not exist:
            self.writer.writeheader()

    def process_item(self, item, spider):
        self.writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.f.close()
