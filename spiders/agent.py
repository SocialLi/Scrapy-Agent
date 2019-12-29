# -*- coding: utf-8 -*-
import scrapy
from agents.items import AgentsItem


class AgentSpider(scrapy.Spider):
    name = 'agent'
    allowed_domains = ['xicidaili.com']
    base_url = 'https://www.xicidaili.com/nn/'
    offset = 1
    start_urls = [base_url + str(offset)]


    def parse(self, response):
        ip_list = response.xpath('//table[@id="ip_list"]//tr')[1:]
        for ip in ip_list:
            item = AgentsItem()
            item['ip'] = ip.xpath('./td[2]/text()').extract_first()
            item['port'] = ip.xpath('./td[3]/text()').extract_first()
            yield item

        if self.offset < 10:
            self.offset += 1
            yield scrapy.Request(
                self.base_url + str(self.offset),
                callback=self.parse,
            )
