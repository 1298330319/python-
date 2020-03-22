# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from wxapp.items import WxappItem
class WxappSpiderSpider(CrawlSpider):
    name = 'wxapp_spider'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), callback='parse_item', follow=True),#follow代表是否穿跟进

        Rule(LinkExtractor(allow=r".+article-.+\.html"),
  callback="parse_detail",follow=False)
            )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()
        author_p = response.xpath("//p[@class='authors']")
        author = author_p.xpath("./a/text()").get()
        pub_time = author_p.xpath(".//span[@class='time']/text()").get()
        article = author_p.xpath("//td[@id='article_content']//text()").getall()
        #print('authoe:%s,time:%s' % (author,pub_time))
        article = ''.join(article).strip()
        item = WxappItem(title=title,author=author,pub_time=pub_time,article=article)

        yield item