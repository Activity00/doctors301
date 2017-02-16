# -*- coding: utf-8 -*-
import re

import scrapy

from docoors301.items import Docoors301Item


class DoctorsSpider(scrapy.Spider):
    name = "doctors"
    #allowed_domains = ["Activity"]
    start_urls = ['http://www.301hospital.com.cn/web/expert/myhc/yyzj.html']
    
    def parse(self, response):
        content= response.xpath('//ul[@class="clearfix"]/li/a/@href').extract()
        for item in content:
            yield scrapy.Request(response.urljoin(item),callback=self.parsedoctorlsit)
    
    def parsedoctorlsit(self,response):
        content=response.xpath('//a[@class="zjmore"]/@href').extract()
        for item in content:
            yield scrapy.Request(response.urljoin(item),callback=self.detail)
        
    def detail(self,response):
        item=Docoors301Item()
        item['name']=response.xpath('//li[@class="zj_xm"]/strong/text()').extract_first()[3:]
        item['image_urls']=response.urljoin(response.xpath('//div[contains(@class,"zj_ys_img")]//@src').extract_first()[3:])
        
        zc=response.xpath('//li[@class="zj_xm"]/text()').extract_first()
        item['zc']=re.findall(r'职称：(.*)科室',zc.encode('utf-8'))[0]
        ks=response.xpath('//li[@class="zj_xm"]/text()').extract_first()
        item['ks']=re.findall(r'科室：(.*)',ks.encode('utf-8'))[0]
        
        item['js']=response.xpath('//li[@class="zj_jj"]/p/text()').extract_first("暂无")
        item['goodat']=response.xpath('//div[@class="zj_ys_b"]/p[@style="text-indent:40px;"]/text()').extract_first("暂无")
        yield item
                
        