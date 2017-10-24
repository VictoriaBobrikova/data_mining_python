import requests
import csv
from bs4 import BeautifulSoup


r=requests.get('https://api.vk.com/method/users.get.xml?user_ids=zhukoo&fields=home_town')
print(r.ok) #проверка, загрузилась страница или нет (page.status_code)=200
print(r.text)
page = BeautifulSoup(r.text, 'html.parser') #для обработки веб-страницы
#print(page.home_town)
#data = csv.writer(open('data.csv', 'w'))
answer = [{'id': page.uid.get_text(), 'home town': page.home_town.get_text()}]
print (answer)
with open('data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=answer[0])
    writer.writeheader()
    writer.writerows(answer)