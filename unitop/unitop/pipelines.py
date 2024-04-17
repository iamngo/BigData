# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymongo
import json
#from bson.objectid 
#import ObjectId
import csv
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class MongoDBUnitopPipeline:
    def __init__(self):
        '''
        self.client = pymongo.MongoClient('mongodb+srv://........./?retryWrites=true&w=majority&appName=.....')
        self.db = self.client['lawnet']
        '''
        #pass
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client['dbunitop']
    
    def process_item(self, item, spider):
        '''
        collection =self.db['dbunitop']
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Error inserting item: {e}")
        '''
        #pass
        collection =self.db['unitop']
        try:
            collection.insert_one(dict(item))
            return item
        except Exception as e:
            raise DropItem(f"Lỗi khi chèn item vào MongoDB: {e}")

class JsonDBUnitopPipeline:
    def process_item(self, item, spider):
        self.file = open('jsondataunitop.json','a',encoding='utf-8')
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        self.file.close
        return item

class MySQLUnitopPipline:
    # Tham khảo: https://scrapeops.io/python-scrapy-playbook/scrapy-save-data-mysql/
    pass

class CSVDBUnitopPipeline:
    def process_item(self, item, spider):
        self.file = open('csvdataunitop.csv','a',encoding='utf-8')
        csv_line = "$".join([str(item[field]) for field in item]) + '\n'
        self.file.write(csv_line)
        self.file.close()
        return item

        '''
        Viết code để xuất ra file csv, thông tin item trên dòng
        mỗi thông tin cách nhau với dấu $
        Ví dụ: coursename$lecturer$intro$describe$courseUrl
        Sau đó, cài đặt cấu hình để ưu tiên Pipline này đầu tiên
        '''