from scrapy.spider import Spider
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

class DmozSpider(CrawlSpider):
    name = "taioanchouhap"
    allowed_domains = ["taioanchouhap.pixnet.net",
                       'taioan-chouhap.myweb.hinet.net']
    start_urls = [
        "http://taioanchouhap.pixnet.net/blog",
        "http://taioan-chouhap.myweb.hinet.net/0_boklok.htm",
        'http://taioanchouhap.pixnet.net/blog/post/177926499',
    ]
    rules = (
        # Extract links matching 'category.php' (but not matching 'subsection.php')
        # and follow links from them (since no callback means follow=True by default).
        Rule(SgmlLinkExtractor(allow=(
    '/taioanchouhap.pixnet.net/blog/.+',)), callback='parse'),
    )

    def parse(self, response):
        filename = response.url.replace("/", '_')
        open(filename, 'wb').write(response.body)
