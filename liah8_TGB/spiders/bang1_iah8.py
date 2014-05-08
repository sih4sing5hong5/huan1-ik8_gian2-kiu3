from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

class DmozSpider(Spider):
	name = "taioanchouhap"
	allowed_domains = ["taioanchouhap.pixnet.net",
					   'taioan-chouhap.myweb.hinet.net']
	start_urls = [
		"http://taioanchouhap.pixnet.net/blog",
		"http://taioan-chouhap.myweb.hinet.net/0_boklok.htm",
		'http://taioanchouhap.pixnet.net/blog/post/177926499',
	]
	
	def parse_TGB(self, response):
		print(response.url)
		
		sel = Selector(response)
		for url in sel.xpath('//a/@href').extract():
			if url.startswith('/blog/post/'):
				yield Request(url='http://taioanchouhap.pixnet.net/'+url,
							callback=self.parse_TGB)
			elif url.startswith('http://taioanchouhap.pixnet.net/blog/post/'):
				yield Request(url=url,
						callback=self.parse_TGB)
		
