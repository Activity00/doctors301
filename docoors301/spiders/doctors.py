# -*- coding: utf-8 -*-
import scrapy

from docoors301.items import Docoors301Item


class DoctorsSpider(scrapy.Spider):
    name = "doctors"
    #allowed_domains = ["Activity"]
    start_urls = ['http://www.guahao.com/hospital/5cee04f9-4cc8-4499-a35b-6f37f2dd8a74000']

    def parse(self, response):
        content= response.xpath('//section[@class="grid-section hospital-dept grid-section-outside js-departments"]/div[@class="grid-content"]/ul//li')
        item=Docoors301Item()
        first=[]
        for i in content.xpath('//label/text()').extract():
            first.append(i.strip())
        for i in content.xpath(''):
            pass
        