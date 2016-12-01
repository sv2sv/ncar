# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ncar.items import NcarItem,OItem


class GetsomeSpider(CrawlSpider):
    list = list()
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
            list.append(item)

    def parse_item(self, response):
        for l in list:
            if(l["url"]==response.url):
                for sel in response.xpath("//td[@class='t_f']/div[3]/a"):
                    item = OItem()
                    item['nname']=sel.xpath("text()").extract()
                    item['urls']=sel.xpath("@href").extract()
                    l['links'].append(item)


