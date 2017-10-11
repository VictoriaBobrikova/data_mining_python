import requests
from bs4 import BeautifulSoup


r=requests.get('https://vk.com/mamontok')
print(r.ok) #проверка, загрузилась страница или нет (page.status_code)=200
#print(r.text)
page = BeautifulSoup(r.text, 'html.parser') #для обработки веб-страницы
#print(page)
print(page.find_all('a')) #поиск по тегу
print(page.find_all('div')[2].get_text()) #извлекаем текст второго элемента данного тега
#page.html[a class="wide_link al_pinfo" href="/mamontok?act=info"] - как-то отсюда
for link in page('a'):
    print(link['href']) #так получим все ссылки и возможно, полную инфу тоже по ссылке можно получить
