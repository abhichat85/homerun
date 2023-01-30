# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class FLatsSpider(CrawlSpider):
    name = "flats"
    # allowed_domains = ["www.magicbricks.com"]
    start_urls = [
        'https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&cityName=Bangalore'
    ]

	# rules = (
 #        Rule(LinkExtractor(allow=(), restrict_css=('.pageNextPrev',)),
 #             callback="parse_item",
 #             follow=True),)

    def parse(self, response):
        print('Processing..' + response.url)
