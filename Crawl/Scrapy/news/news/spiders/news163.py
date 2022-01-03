# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from  news.items import NewsItem
# https://news.163.com/21/0110/12/FVVRJTI0000189FH.html
# https://news.163.com/21/0110/10/FVVMSFN5000189FH.html
# https://news.163.com/21//d+/\d+/.*?html
# https://www.163.com/dy/article/FVVGTKF60514R9OJ.html
# https://www.163.com/dy/article/FVVI0OFA055040N3.html
# https://www.163.com/dy/article/FVVR477H0541A1UA.html
# https://www.163.com/dy/article/.*?html
class News163Spider(CrawlSpider):
    name = 'news163'
    allowed_domains = ['news.163.com']
    start_urls = ['http://news.163.com/']
    rules = (
        Rule(LinkExtractor(allow=r'https://news.163.com/21/\d+/\d+/.*?html'), callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        item = NewsItem()
        item['news_thread']=response.url.split('/')[-1][:-5]
        self.get_title(response,item)
        self.get_time(response,item)
        self.get_source(response,item)
        self.get_source_url(response,item)
        self.get_text(response,item)
        item['news_url']=response.url
        return item
    def get_title(self,response,item):
        title=response.css('title::text').extract()
        if title:
            # 如果标题存在
            # print('title:{}'.format(title[0]))
            item['news_title']=title[0]
    def get_time(self,response,item):
        time=response.css('div .post_info::text').extract()
        if time:
            # print('time:{}'.format(time[0].strip().replace('来源:','').replace('\u3000','')))
            item['news_time']=time[0].strip().replace('来源:','').replace('\u3000','')
    def get_source(self,response,item):
        source=response.css('.post_info a::text').extract_first()
        if item:
            # print('source:{}'.format(source))
            item['news_source']=source
    def get_source_url(self,response,item):
        source_url=response.css('.post_info a::attr(href)').extract_first()
        if source_url:
            # print("source_url:{}".format(source_url))
            item['source_url']=source_url
    def get_text(self,response,item):
        text=response.css('.post_body p::text').extract()
        if text:
            # print('text:{}'.format(text))
            item['news_text']=text