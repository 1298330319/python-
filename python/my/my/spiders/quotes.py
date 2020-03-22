# -*- coding: utf-8 -*-
import scrapy
from my.items import MyItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    '''
    #这是xpath语法提取数据
    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            text = quote.xpath(".//span[@class='text']//text()").get()
            author = quote.xpath(".//span/small/text()").get()
            tag = quote.xpath("./div[@class='tags']/a//text()").getall()
            print('author:%s,tag:%s,text:%s' % (author,tag,text))
    '''

    #这是css选择器
    def parse(self, response):
          quotes = response.css(".quote")
          for quote in quotes:
              text = quote.css(".text::text").extract()
              author = quote.css(".author::text").extract()
              tag = quote.css(".tag::text").extract()
              item = MyItem(text=text,author=author,tag=tag)
              yield item

          next = response.css(".pager .next a::attr(href)").extract()
          print(next)



