# Импортируем библиотеки requests и json
import requests
import json

# Задаем параметры для api foursquare
client_id = "AL1BT0PC3YSNLLGUQK0BW15ND01FUIIAVF4VLPY4EHHLKM2R" # Вставьте свой client id
client_secret = "KDMHFPDONIZ04QJHZKRNWJUTA2MJVV5HOT5SAXCKTV00UFIA" # Вставьте свой client secret
version = "20240116" # Версия api
limit = 10 # Количество заведений, которые мы хотим получить
near = "Paris, France" # Город, в котором мы ищем заведения

# Спрашиваем у пользователя, какую категорию он хочет искать
category = input("Введите интересующую вас категорию, например, кофейни, музеи или парки: ")

# Формируем url для запроса к api foursquare
url = f"https://api.foursquare.com/v2/venues/search?client_id={client_id}&client_secret={client_secret}&v={version}&limit={limit}&near={near}&query={category}"

# Делаем запрос и получаем ответ в формате json
response = requests.get(url).json()

# Извлекаем список заведений из ответа
venues = response["response"]["venues"]

# Проходим по списку заведений и выводим их название, адрес и рейтинг
for venue in venues:
    # Получаем название заведения
    name = venue["name"]
    # Получаем адрес заведения, если он есть
    address = venue["location"].get("address", "Адрес не указан")
    # Получаем рейтинг заведения, если он есть
    rating = venue.get("rating", "Рейтинг не указан")
    # Выводим информацию о заведении в консоль
    print(f"Название: {name}")
    print(f"Адрес: {address}")
    print(f"Рейтинг: {rating}")
    print()
