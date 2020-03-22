from scrapy import cmdline
cmdline.execute('scrapy crawl wxapp_spider'.split())
#上下命令等同
# cmdline.execute(['scrapy','crawl','qsdbk'])