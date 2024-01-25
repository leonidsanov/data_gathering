'''Использовать библиотеку requests в Python для отправки запросов GET, POST, PUT и DELETE на конечную точку
REST API https://jsonplaceholder.typicode.com/posts/1.
- использовать методы requests.get(), requests.post(), requests.put() и requests.delete() для отправки
соответствующих HTTP-запросов.
- проверить код состояния ответа и вывести текст ответа, если запрос был успешным.

Инструкции:
можно использовать предоставленный код в качестве отправной точки для своего решения.
'''

import requests

url = 'https://jsonplaceholder.typicode.com/posts/1'
get_response = requests.get(url)

if get_response.status_code == 200:
    print('Запрос успешен 200')
    print(get_response.text)

request = {"title": "geekbrains", "body": "строительная компания итальяно", "userId": 1}
get_reasponse = requests.post("https://jsonplaceholder.typicode.com/posts", json=request)
if get_reasponse.status_code == 201:
    print('запрос успешен 201')
    print(get_reasponse.text)
else:
    print(get_reasponse.status_code)

put_request = {"каталог": 1, "Раздел": "математика"}
url = "https://jsonplaceholder.typicode.com/posts/1"
get_reasponse = requests.put(url, put_request)
if get_reasponse.status_code == 200:
    print('запрос успешен 200')
    print(get_reasponse.text)


get_reasponse = requests.delete(url)
if get_reasponse.status_code == 200:
    print('запрос успешен 200')
    print(get_reasponse.text)