import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class UnsplashImgSpider(CrawlSpider):
    name = "unsplash_img"
    allowed_domains = ["unsplash.com"]
    start_urls = ["https://unsplash.com/"]

    rules = (Rule(LinkExtractor(restrict_xpaths=("//a[@class='p7ajO KHq0c']")), callback="parse_item", follow=True),)

    def parse_item(self, response):
        # item = {}
        # #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # #item["name"] = response.xpath('//div[@id="name"]').get()
        # #item["description"] = response.xpath('//div[@id="description"]').get()
        # return item
        print(response.url)
