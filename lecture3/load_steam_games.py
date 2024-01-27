import json
from pymongo import MongoClient

# Подключение к серверу MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Выбор базы данных и коллекции
db = client['steam']
collection = db['games']

# Чтение файла JSON
with open('steam_games.json', 'r', encoding="utf-8") as file:
    data = json.load(file)

# data = data['features']

# Функция разделения данных на более мелкие фрагменты
def chunk_data(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

# Разделение данных на фрагменты по 5000 записей в каждом
chunk_size = 5000
data_chunks = list(chunk_data(data, chunk_size))

# Вставка фрагментов в коллекцию MongoDB
for chunk in data_chunks:
    collection.insert_many(chunk)

print("Данные успешно вставлены.")
