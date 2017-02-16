# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Docoors301Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name=scrapy.Field()
    image_urls=scrapy.Field()#头像链接
    images=scrapy.Field()
    zc=scrapy.Field()#职称
    ks=scrapy.Field()#科室
    js=scrapy.Field()#介绍
    goodat=scrapy.Field()#擅长
    
    