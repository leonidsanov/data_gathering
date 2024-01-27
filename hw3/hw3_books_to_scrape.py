# Импорт библиотек
import json
from pymongo import MongoClient

# Подключение к серверу MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Посмотрим какие базы данных у нас есть
database_list = client.list_database_names()
print(database_list)

# Выбор базы данных и коллекции
db = client['books']
collection = db['books_to_scrape']

# # Чтение файла JSON
# with open('books_to_scrape.json', 'r', encoding="utf-8") as file:
#     data = json.load(file)

# collection.insert_one(data)

count = collection.count_documents({})
count

# Запросы
def find():
    # query = {"Quantity" : 20} # все книги в количестве 20 штук
    # query = {"Name" : {"$gte" : "A", "$lt" : "D"}}
    query = {"Price" : {"$gt" : 20, "$lt" : 30}} # книги стоимостью от 20 до 30


    books = db.books_to_scrape.find(query)
    for a in books:
        print(a)

if __name__ == '__main__':
    find()
