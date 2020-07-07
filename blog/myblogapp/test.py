import requests
from pprint import pprint
import os

from django.conf import settings
# city = input("Enter city : ")
# url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=fd544b1b7275898c4aff9c0c79eba983'

# r = requests.get(url.format(city)).json()

# pprint(r)

# xx = os.environ.get('DEFAULT_CITY')
# print(xx)

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG_VALUE = os.environ.get('DEBUG_VALUE')
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')

EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')

DEFAULT_CITY = os.environ.get('DEFAULT_CITY')
OWM_API = os.environ.get('OWM_API')

print(SECRET_KEY)
print(DEBUG_VALUE)
print(AWS_ACCESS_KEY_ID)
print(AWS_SECRET_ACCESS_KEY)
print(AWS_STORAGE_BUCKET_NAME)
print(EMAIL_HOST)
print(EMAIL_HOST_USER)
print(EMAIL_HOST_PASSWORD)
print(DEFAULT_CITY)
print(OWM_API)


serial_list = [1, 2, 3, 4, 5]
even_list = [n * 2 for n in serial_list]
print(serial_list, [n * 2 for n in serial_list])
