from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import time
import csv

def user_parser (j, id):
    url = "https://api.vk.com/method/users.get.xml?user_ids="+id[1:]+"&fields=home_town"
    r = requests.get(url)
    page = BeautifulSoup(r.text, 'html.parser')
    try:
        answer = [{'number': str(j),'url': id, 'id': page.uid.get_text(), 'home town': page.home_town.get_text()}]
    except AttributeError:
        answer = [{'number': str(j),'url': id, 'id': page.uid.get_text(), 'home town': 'Error'}]
    try:
        writer.writerows(answer)
    except UnicodeEncodeError:
        answer = [{'number': str(j), 'url': id, 'id': page.uid.get_text(), 'home town': 'Mudak'}]
        writer.writerows(answer)
    time.sleep(0.33)

ua = UserAgent()
print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
print(header)

path = "Home_Town.csv"
i=0
j=0
answer = [{'number': 'dict','url': 'dict', 'id': 'dict', 'home town': 'dict'}]
with open(path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=answer[0])
    writer.writeheader()
    while i<=48:
        if i==0:
            url = "https://vk.com/search?c%5Bcity%5D=2&c%5Bcountry%5D=1&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Buniversity%5D=56&offset=0"
        else:
            url = "https://vk.com/search?c%5Bcity%5D=2&c%5Bcountry%5D=1&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Buniversity%5D=56&offset="+str(20+i*20)
        r=requests.get(url, headers=header)
        print(r.ok)
        page = BeautifulSoup(r.text, 'html.parser')
        #print(page.prettify())
        tags=page.findAll("div", {"class":"labeled name"})
        #print (tags)
        print('Page', i+1)
        for tag in tags:
            some=tag.findAll("a", {"class": None})
            for link in some:
                j=j+1
                print (j,')' ,link.get('href'))
                user_parser(j, link.get('href'))
        i=i+1
        time.sleep(1)
