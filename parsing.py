import requests
from bs4 import BeautifulSoup
<<<<<<< HEAD
<<<<<<< HEAD


r=requests.get('https://vk.com/mamontok')
print(r.ok) #проверка, загрузилась страница или нет (page.status_code)=200
#print(r.text)
page = BeautifulSoup(r.text, features='xml') #для обработки веб-страницы
#print(page)
print(page.find_all('a')) #поиск по тегу
print(page.find_all('a')[2].get_text()) #извлекаем текст второго элемента данного тега
#page.html[a class="wide_link al_pinfo" href="/mamontok?act=info"] - как-то отсюда
for link in page('a'):
    print(link['href']) #так получим все ссылки и возможно, полную инфу тоже по ссылке можно получить
=======
=======

>>>>>>> 490adc44bd9a41df5564528f5d88c82e0f625983
r=requests.get('https://api.vk.com/method/users.get.xml?user_ids=mamontok&fields=home_town')
print(r.ok) 
print('1)', r.text)
page = BeautifulSoup(r.text, 'html.parser')
<<<<<<< HEAD
print('2)', page)
>>>>>>> branch_daniil
=======
print('2)', page.home_town)
>>>>>>> 490adc44bd9a41df5564528f5d88c82e0f625983
