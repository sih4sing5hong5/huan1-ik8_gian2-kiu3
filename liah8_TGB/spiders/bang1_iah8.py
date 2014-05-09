from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from liah8_TGB.items import Liah8TgbItem

class TgbSpider(CrawlSpider):
	name = "taioanchouhap"
	allowed_domains = ["taioanchouhap.pixnet.net",
					   'taioan-chouhap.myweb.hinet.net']
	start_urls = [
		"http://taioanchouhap.pixnet.net/blog",
		"http://taioan-chouhap.myweb.hinet.net/0_boklok.htm",
		'http://taioanchouhap.pixnet.net/blog/post/177926499',
	]
	
	rules = [
		Rule(
			SgmlLinkExtractor(allow=[".*/blog/post/177926499.*", ]),
			callback="parse_TGB", follow=True
		),
    ]
	kinn2 = '/blog/post/177926'
	def parse_TGB(self, response):
		print(response.url)
		
		sel = Selector(response)
# 		for url in sel.xpath('//a/@href').extract():
# 			if url.startswith(self.kinn2):
# 				yield Request(url='http://taioanchouhap.pixnet.net/' + url,
# 							callback=self.parse_TGB)
# 			elif url.startswith('http://taioanchouhap.pixnet.net' + self.kinn2):
# 				yield Request(url=url,
# 						callback=self.parse_TGB)
		if self.kinn2 in response.url:
			item = Liah8TgbItem()
			item['title'] = sel.css('li.publish').extract()
			item['date'] = sel.css('li.publish').extract()
			item['context'] = sel.css('div.article-content-inner').extract()
			yield item
