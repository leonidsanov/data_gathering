import scrapy
import csv
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy.loader import ItemLoader
from ..items import UnsplashItem
from itemloaders.processors import MapCompose


# Определяем класс паука
class UnsplashImgSpider(CrawlSpider):
    # Имя паука
    name = "unsplash_img"
    # Домен по которому будет работать паук
    allowed_domains = ["unsplash.com"]
    # Стартовый URL
    start_urls = ["https://unsplash.com/"]

    # Правила для извлечения ссылок
    rules = (
        # Правило для ссылок на категории фотографий
        Rule(LinkExtractor(restrict_xpaths=("//a[@class='p7ajO KHq0c']")), callback="parse_category", follow=True),
        # Правило для ссылок на отдельные фотографии
        Rule(LinkExtractor(allow=r"/photos/"), callback="parse_photo"),
    )

    # Функция для обработки ответов по ссылкам на категории
    def parse_category(self, response):
        # Извлекаем название категории из заголовка страницы
        category = response.xpath("//title/text()").get().split("·")[0].strip()
        # Сохраняем название категории в метаданных запроса
        response.meta["category"] = category

    # Функция для обработки ответов по ссылкам на фотографии
    def parse_photo(self, response):
        # Создаем экземпляр класса UnsplashItem
        item = UnsplashItem()
        # Заполняем поля элемента извлеченными данными
        # URL изображения
        item["image_url"] = response.url
        # Название изображения
        item["image_name"] = response.xpath("//title/text()").get().split("·")[0].strip()
        # Категория, к которой принадлежит изображение
        # item["image_category"] = response.meta.get("category", "Unknown")
        item["image_category"] = response.xpath("//a[@class='IQzj8 eziW_']/text()")
        # Возвращаем элемент
        return item

    # # Функция для сохранения данных в файл csv
    # def save_to_csv(self, item):
    #     # Открываем файл csv в режиме дозаписи
    #     with open("image_data.csv", "a", encoding="utf-8") as f:
    #         # Создаем объект для записи данных в csv формате
    #         writer = csv.writer(f)
    #         # Записываем данные из элемента в файл
    #         writer.writerow([item["image_url"], item["image_name"], item["image_category"]])



    # def parse_item(self, response):
    #     loader = ItemLoader(item=UnsplashItem(), response=response)
    #     loader.default_input_processor = MapCompose(str.strip)

    #     loader.add_xpath(image_name, '//')
    #     # item = {}
        # # #item["domain_id"] = response.xpath('//input[@id="sid"]/@value').get()
        # # #item["name"] = response.xpath('//div[@id="name"]').get()
        # # #item["description"] = response.xpath('//div[@id="description"]').get()
        # return item
        # # print(response.url)
