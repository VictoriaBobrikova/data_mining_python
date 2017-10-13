import requests
from bs4 import BeautifulSoup

r=requests.get('https://api.vk.com/method/users.get.xml?user_ids=mamontok&fields=home_town')
print(r.ok) 
print('1)', r.text)
page = BeautifulSoup(r.text, 'html.parser')
print('2)', page.home_town)