import requests
from bs4 import BeautifulSoup
r=requests.get('https://vk.com/mamontok')
print(r.ok)
print('1)', r.text)
page = BeautifulSoup(r.text, 'html.parser')
print('2)', page)
