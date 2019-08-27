import requests
from pprint import pprint
city = input('City : ')
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid=fd544b1b7275898c4aff9c0c79eba983'
res = requests.get(url)
data = res.json()

pprint(data)
