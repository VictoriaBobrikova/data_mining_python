from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import time
import csv
import sys
import argparse


def putUni():
    put = argparse.ArgumentParser(
        prog='Student_list_parse',
        description='''This program is used to learn the students geography of Saint-Petersburg Unis from open vk.com data. List of Unis: 1 - СПбГУ; 56 - Петра; 53 - Итмо; 38 - НГУ им.Лесгафта (бывш. СПбГУФК); 48 - ГАСУ, 34 - РГПУ им.А.И.Герцена. Choose reqiured number of Uni, then write Student_list_parse.py -n <number>'''
    ) #создали экземпляр класса ArgumentParser
    put.add_argument('-n', choices=[1, 56, 53, 38, 48, 34], default=1, type=int) #добавили ожидаемый параметр в командной строке с помощью метода add_argument

    return put


if __name__ == '__main__':
    put = putUni()
    namespace = put.parse_args() #для разбора командной строки, это наш параметр введённый

    #print (namespace.n)
    #print ("Привет, {}!".format (namespace.n) )

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

k = namespace.n
path = open('{}_home_town.csv'.format(k), 'w') #здесь как-то надо создать соответствующее номеру универа название файла, он создаёт, но дальше не понимает его

j=0

bdate=17

answer = [{'number': 'dict','url': 'dict', 'id': 'dict', 'home town': 'dict'}]
with open(path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=answer[0])
    writer.writeheader()
    while bdate<=25:
        sex=1
        while sex<=2:
            i=1
            while i<=48:
                if i==0:
                    url = "https://vk.com/search?c%5Bage_from%5D="+str(bdate)+"&c%5Bage_to%5D="+str(bdate)+"&c%5Bcity%5D=2&c%5Bcountry%5D=1&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Bsex%5D="+str(sex)+"&c%5Buniversity%5D="+str(k)+"&offset=0"
                else:
                    url = "https://vk.com/search?c%5Bage_from%5D="+str(bdate)+"&c%5Bage_to%5D="+str(bdate)+"&c%5Bcity%5D=2&c%5Bcountry%5D=1&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Bsex%5D="+str(sex)+"&c%5Buniversity%5D="+str(k)+"&offset="+str(20+i*20)
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
                time.sleep(0.33)
            sex=sex+1
        bdate=bdate+1