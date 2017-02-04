# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Docoors301Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    firstdpt=scrapy.Field()
    seconddpt=scrapy.Field()
    name=scrapy.Field()
    zc_one=scrapy.Field()
    zc_two=scrapy.Field()
    description=scrapy.Field()
    good=scrapy.Field()
    