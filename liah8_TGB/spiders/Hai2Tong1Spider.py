# encoding:utf-8
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from liah8_TGB.items import Liah8TgbItem
u'''
scrapy crawl Hai2Tong1 -o ./語料/TGB/原來Hai2Tong1.json -t json
gzip ./語料/TGB/原來Hai2Tong1.json
'''
class Hai2Tong1Spider(CrawlSpider):
	name = "Hai2Tong1"
	allowed_domains = ["web.htps.tn.edu.tw",
					]
	start_urls = [
  		'http://web.htps.tn.edu.tw/90ct/Default.htm',
		'http://web.htps.tn.edu.tw/90ct/main.htm',
		'http://web.htps.tn.edu.tw/90ct/songs/songs.htm',
		'http://web.htps.tn.edu.tw/90ct/songs/song_l.htm',
		'http://web.htps.tn.edu.tw/90ct/songs/song_m/song_m03_1.htm',
		'http://web.htps.tn.edu.tw/90ct/history/history4.htm',
		'http://web.htps.tn.edu.tw/90ct/double_voice/double_voice1.htm',
		'http://web.htps.tn.edu.tw/90ct/tlpa/index.htm',
		'http://web.htps.tn.edu.tw/90ct/strange_words/strange_words.htm',
		'http://web.htps.tn.edu.tw/90ct/guess_what/guess1.htm',
		'http://web.htps.tn.edu.tw/90ct/guess_what/guess1.htm',
	]
	
	rules = [
		Rule(
			SgmlLinkExtractor(
				allow=['web.htps.tn.edu.tw/90ct/', ],
				deny=['web.htps.tn.edu.tw/90ct/default_1.htm'],
# 				tags=('a', 'area', 'frame'), attrs=('href','src'),
				),
			callback="parse_bang7_iah8", follow=True
		),
# 		Rule(
# 			SgmlLinkExtractor(allow=[".*0_boklok.*", ]),
# 			follow=True
# 		),
    ]
	def parse_bang7_iah8(self, response):
		sel = Selector(response)
		item = Liah8TgbItem()
		item['url'] = response.url
		item['title'] = ''
		item['date'] = ''
		item['context'] = bytearray(response.body[:]).decode('big5',errors='replace')
# 		print(item['context'])
		yield item
