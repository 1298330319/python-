# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem

class QsdbkSpider(scrapy.Spider):
    name = 'qsdbk'
    allowed_domains = ['qiushidabaike.com']
    start_urls = ['http://www.qiushidabaike.com/']

    '''
    response 是一个 scrapy.http.response.html.HtmlResponse 对象，可以执行xpath和css语法来提取
    提取出来的对象是一个‘selector’或者是一个‘selectorlist’对象，想要获取其中的字符串，应该执行
    getall()或者get()方法
    '''
    def parse(self, response):
        dls = response.xpath("//div[@id='j-main-list']/dl[@class='main-list']")
        for dl in dls:
            text = dl.xpath("./dd[@class='content']/p/text()").getall()
            text = ''.join(text)
            item = QsbkItem(text=text)
            yield item


    '''如果数据解析出来要传给pipline处理，可以使用yield生成器执行
    def parse(self, response):
        dls = response.xpath("//div[@id='j-main-list']/dl[@class='main-list']")
        for dl in dls:
            text = dl.xpath("./dd[@class='content']/p/text()").getall()
            text = ''.join(text)
            item = QsbkItem(text=text)
            yield itemitesms = []

也可以使用一下方法
            items = append(item)
        return items
    '''