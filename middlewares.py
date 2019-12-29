# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random


class RandomUserAgentMiddleware:
    def process_request(self, request, spider):
        user_agent = random.choice(spider.settings.get('USER_AGENTS'))
        request.headers['User-Agent'] = user_agent


# class ProxyMiddleware:
#     def process_request(self, request, spider):
#         request.meta['proxy'] = 'http://119.102.189.0:9999'
