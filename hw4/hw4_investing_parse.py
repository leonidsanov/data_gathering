# Импорт необходимых библиотек
import requests
from lxml import html
from pymongo import MongoClient

# Определение целевого URL
url = "https://ru.investing.com/etfs/russia-etfs?&issuer_filter=0"

