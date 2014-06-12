# encoding:utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from liah8_TGB.items import Liah8TgbItem
u'''
scrapy crawl TGB -o ./語料/TGB/原來TGB.json -t json
gzip ./語料/TGB/原來TGB.json
'''
class TgbSpider(CrawlSpider):
	name = "TGB"
	allowed_domains = ["taioanchouhap.pixnet.net",
					   'taioan-chouhap.myweb.hinet.net']
	start_urls = [
		"http://taioanchouhap.pixnet.net/blog",
		"http://taioan-chouhap.myweb.hinet.net/0_boklok.htm",
		'http://taioanchouhap.pixnet.net/blog/post/177926499',
	]
	
	rules = [
		Rule(
			SgmlLinkExtractor(allow=[".*/blog/post/.*", ]),
			callback="parse_TGB", follow=True
		),
		Rule(
			SgmlLinkExtractor(allow=[".*0_boklok.*", ]),
			follow=True
		),
    ]
	def parse_TGB(self, response):
		sel = Selector(response)
		item = Liah8TgbItem()
		item['url'] = response.url
		item['title'] = sel.css('li.title').extract()
		item['date'] = sel.css('li.publish').extract()
		item['context'] = sel.css('div.article-content-inner').extract()
		yield item
