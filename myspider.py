# -*- coding: utf-8 -*-
import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['http://www.booksky.cc/novel/279873/read_1.html']

    def parse(self, response):
        for title in response.css('.title>h1>a'):
            yield {'title': title.css(' ::text').extract_first()}
        for cont in response.css('.content'):
            yield {'cont': cont.css(' ::text').extract()}
        for n in response.xpath('//a[@class="btn btn-primary"]/i[@class="pticon pticon-chevron-right"]/..'):
            yield {'n': n.css(' ::text').extract()}

        for next_page in response.xpath('//a[@class="btn btn-primary"]/i[@class="pticon pticon-chevron-right"]/..'):
            yield response.follow(next_page, self.parse)
