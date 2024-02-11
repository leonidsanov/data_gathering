import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.loader import ItemLoader
from ..items import ZebrsItem
from itemloaders.processors import MapCompose

class ZebrsImgSpider(CrawlSpider):
    name = "zebrs_img"
    allowed_domains = ["www.zebrs.com"]
    start_urls = ["https://www.zebrs.com/categories/smartphones"]

    rules = (Rule(LinkExtractor(restrict_xpaths='div//[@class="position-relative teaser-item-div"]'), callback="parse_item", follow=True),)

    def parse_item(self, response):
        loader = ItemLoader(item=ZebrsItem(), response=response)
        loader.default_input_processor = MapCompose(str.strip)
