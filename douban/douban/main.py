from scrapy import  cmdline
cmdline.execute('scrapy crawl douban_spider'.split())
#cmdline.execute('scrapy crawl douban_spider -o douban.json'.split())