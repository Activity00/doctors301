# -*- coding: utf-8 -*-
import scrapy

from docoors301.items import Docoors301Item


class DoctorsSpider(scrapy.Spider):
    name = "doctors"
    #allowed_domains = ["Activity"]
    start_urls = ['http://www.guahao.com/hospital/5cee04f9-4cc8-4499-a35b-6f37f2dd8a74000']

    def parse(self, response):
        content= response.xpath('//section[@class="grid-section hospital-dept grid-section-outside js-departments"]/div[@class="grid-content"]/ul//li//span/a/@href').extract()
        for item in content:
            yield scrapy.Request(item,callback=self.parse_dept)
    
    def parse_dept(self,response):
        content=response.xpath('//div[@class="g-clear g-doc-info"]/a/@href').extract()
        for item in content:
            yield scrapy.Request(item,callback=self.detail)
        
    def detail(self,response):
        content=response.xpath('//div[@class="detail word-break"]')
        name=content.xpath('.//h1/strong/text()').extract_first()
        dpt=content.xpath('.//div/p/a[@monitor-div-id="98f685a3-9eac-49f2-92c0-fdaef46e8fa1000"]/text()').extract_first()
        sc=content.xpath('.//div[@class="goodat"]/span/text()').extract_first()
        jj=content.xpath('.//div[@class="about"]/a/@data-description').extract_first()
        yield {'name':name,'dpt':dpt,'sc':sc,'jj':jj}
                
        