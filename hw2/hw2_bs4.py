# import requests
# from bs4 import BeautifulSoup

# url = "http://books.toscrape.com/"
# response = requests.get(url)

# # Парсинг HTML-содержимого веб-страницы с помощью Beautiful Soup
# soup = BeautifulSoup(response.content, 'html.parser')



# импортировать модули
import requests
from bs4 import BeautifulSoup
import json

# определить базовый URL и список категорий
base_url = "http://books.toscrape.com/"
categories = [
    "travel",
    "mystery",
    "historical-fiction",
    "sequential-art",
    "classics",
    "philosophy",
    "romance",
    "womens-fiction",
    "fiction",
    "childrens",
    "religion",
    "nonfiction",
    "music",
    "default",
    "science-fiction",
    "sports-and-games",
    "add-a-comment",
    "fantasy",
    "new-adult",
    "young-adult",
    "science",
    "poetry",
    "paranormal",
    "art",
    "psychology",
    "autobiography",
    "parenting",
    "adult-fiction",
    "humor",
    "horror",
    "history",
    "food-and-drink",
    "christian-fiction",
    "business",
    "biography",
    "thriller",
    "contemporary",
    "spirituality",
    "academic",
    "self-help",
    "historical",
    "christian",
    "suspense",
    "short-stories",
    "novels",
    "health",
    "politics",
    "cultural",
    "erotica",
    "crime",
]

# создать пустой список для хранения информации о книгах
books = []

# написать цикл, который перебирает все категории и формирует полный URL для каждой категории
for category in categories:
    category_url = base_url + "catalogue/category/books/" + category + "_1/index.html"
    # отправить запрос на получение HTML-кода страницы категории и создать объект BeautifulSoup для его анализа
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, "html.parser")
    # найти все элементы, содержащие информацию о книгах, с помощью метода find_all() и селектора CSS '.product_pod'
    products = soup.find_all("div", class_="product_pod")
    # написать вложенный цикл, который перебирает все найденные элементы и извлекает из них название, цену, количество товара в наличии и описание книги
    for product in products:
        # найти элемент с названием книги и извлечь его текст
        title = product.find("h3").find("a")["title"]
        # найти элемент с ценой книги и извлечь его текст, убрав лишние символы
        price = product.find("p", class_="price_color").text.strip("Â£")
        # найти элемент с количеством товара в наличии и извлечь его текст, убрав лишние символы и преобразовав в целое число
        stock = int(
            product.find("p", class_="instock availability")
            .text.strip()
            .strip("In stock (")
            .strip(" available)")
        )
        # сформировать URL для страницы с описанием книги, используя атрибут href элемента с названием книги
        description_url = base_url + "catalogue/" + product.find("h3").find("a")["href"]
        # отправить запрос на получение HTML-кода страницы с описанием книги и создать объект BeautifulSoup для его анализа
        description_response = requests.get(description_url)
        description_soup = BeautifulSoup(description_response.text, "html.parser")
        # найти элемент с описанием книги и извлечь его текст, убрав лишние символы
        description = (
            description_soup.find("div", id="product_description")
            .find_next_sibling("p")
            .text.strip()
        )
        # добавить извлеченную информацию в список в виде словаря с ключами 'title', 'price', 'stock', 'description'
        books.append(
            {"title": title, "price": price, "stock": stock, "description": description}
        )
    # повторить шаги 5-8 для всех страниц в категории, используя метод find() и селектор CSS '.next' для определения наличия следующей страницы
    while soup.find("li", class_="next"):
        # сформировать URL для следующей страницы, используя атрибут href элемента с классом 'next'
        next_page_url = (
            base_url
            + "catalogue/category/books/"
            + category
            + "_1/"
            + soup.find("li", class_="next").find("a")["href"]
        )
        # отправить запрос на получение HTML-кода следующей страницы и создать объект BeautifulSoup для его анализа
        response = requests.get(next_page_url)
        soup = BeautifulSoup(response.text, "html.parser")
        # найти все элементы, содержащие информацию о книгах, с помощью метода find_all() и селектора CSS '.product_pod'
        products = soup.find_all("div", class_="product_pod")
        # написать вложенный цикл, который перебирает все найденные элементы и извлекает из них название, цену, количество товара в наличии и описание книги
        for product in products:
            # найти элемент с названием книги и извлечь его текст
            title = product.find("h3").find("a")["title"]
            # найти элемент с ценой книги и извлечь его текст, убрав лишние символы
            price = product.find("p", class_="price_color").text.strip("Â£")
            # найти элемент с количеством товара в наличии и извлечь его текст, убрав лишние символы и преобразовав в целое число
            stock = int(
                product.find("p", class_="instock availability")
                .text.strip()
                .strip("In stock (")
                .strip(" available)")
            )
            # сформировать URL для страницы с описанием книги, используя атрибут href элемента с названием книги
            description_url = (
                base_url + "catalogue/" + product.find("h3").find("a")["href"]
            )
            # отправить запрос на получение HTML-кода страницы с описанием книги и создать объект BeautifulSoup для его анализа
            description_response = requests.get(description_url)
            description_soup = BeautifulSoup(description_response.text, "html.parser")
            # найти элемент с описанием книги и извлечь его текст, убрав лишние символы
            description
