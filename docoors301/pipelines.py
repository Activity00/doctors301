# -*- coding: utf-8 -*-
import MySQLdb

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
    
class MySqlPipeline(object):
    
    def __init__(self, db_uri,db_name,username,password):
        self.db_uri = db_uri
        self.db_name = db_name
        self.username=username
        self.password=password
        
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            db_uri=crawler.settings.get('DB_URI'),
            db_name=crawler.settings.get('DB_NAME', 'doctors'),
            username=crawler.settings.get('DB_USERNAME'),
            password=crawler.settings.get('DB_PASSWORD') 
        )
    def open_spider(self, spider):
        self.db = MySQLdb.connect(self.db_uri,self.username,self.password,self.db_name,charset="utf8")
        
    def close_spider(self, spider):
        self.db.close()
    
    def process_item(self, item, spider):
        cursor = self.db.cursor()
        try:
            cursor.execute('insert into base_info(name,zc,ks,js,goodat,image_url,path) values(%s,%s,%s,%s,%s,%s,%s)',(
            item['name'],item['zc'],item['ks'],item['js'],item['goodat'],item['images'][0]['url'],item['images'][0]['path']))
            self.db.commit()
        except:
            print '数据回滚'
            self.db.rollback()
        return item
    
    