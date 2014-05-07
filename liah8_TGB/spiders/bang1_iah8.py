from scrapy.spider import Spider

class DmozSpider(Spider):
    name = "taioanchouhap"
    allowed_domains = ["taioanchouhap.pixnet.net",
                       'taioan-chouhap.myweb.hinet.net']
    start_urls = [
        "http://taioanchouhap.pixnet.net/blog",
        "http://taioan-chouhap.myweb.hinet.net/0_boklok.htm"
    ]

    def parse(self, response):
        filename = response.url.split("/")[-2]
        open(filename, 'wb').write(response.body)