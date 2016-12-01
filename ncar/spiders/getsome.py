# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ncar.items import NcarItem


class GetsomeSpider(CrawlSpider):
    global li
    li = list()
    name = 'getsome'
    allowed_domains = ['ncar.cc']
    start_urls = ['http://bbs.ncar.cc/forum.php?mod=forumdisplay&fid=129']

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='xbs xbs_4 block move-span']//li/a"), callback='parse_item', follow=True),
    )

    def parse_start_url(self,response):
        for sel in response.xpath("//div[@class='xbs xbs_4 block move-span']//li/a"):
            item = NcarItem()
            item['name'] = sel.xpath("text()").extract()
            item['url'] = sel.xpath("@href").extract()
            item['links'] = dict() 
            li.append(item)
#        print li

    def parse_item(self, response):
        for l in li:
            print response.url.find(l['url'][0]),l['url'][0],response.url,type(l['url']),type(response.url.find(l['url'][0]))
            #if(l['url']==response.url):
            if(response.url.find(l['url'][0])!=-1):
                for sel in response.xpath("//td[@class='t_f']/div[3]/a"):
                    l['links'][sel.xpath("text()").extract()[0]]=sel.xpath("@href").extract()[0]
                    yield l


