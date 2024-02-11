# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


# class UnsplashPipeline:
#     def process_item(self, item, spider):
#         return item

# Определяем класс Pipeline
class UnsplashPipeline(object):
    # Метод для инициализации пайплайна
    def __init__(self):
        # Создаем объект для записи данных в csv формате
        self.writer = csv.writer(open("image_data.csv", "a", encoding="utf-8"))

    # Метод для обработки элементов
    def process_item(self, item, spider):
        # Вызываем функцию для сохранения данных в файл csv
        self.save_to_csv(item)
        # Возвращаем элемент
        return item

    # Функция для сохранения данных в файл csv
    def save_to_csv(self, item):
        # Записываем данные из полей элемента в файл
        self.writer.writerow([item["image_url"], item["image_name"], item["image_category"]])
