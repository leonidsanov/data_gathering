# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# Определяем класс UnsplashItem, который наследует от scrapy.Item
class UnsplashItem(scrapy.Item):
    # Определяем поля для элемента URL изображения
    image_url = scrapy.Field()
    # Название изображения
    image_name = scrapy.Field()
    # Категория, к которой принадлежит изображение
    image_category = scrapy.Field()
