from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import time
import csv
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
import sys
import argparse


def putUni():
    put = argparse.ArgumentParser(
        prog='Project_Jup',
        description='''This program is used to learn the students geography of Saint-Petersburg Unis from open vk.com data. List of Unis: 1 - СПбГУ; 56 - Петра; 53 - Итмо; 38 - НГУ им.Лесгафта (бывш. СПбГУФК); 48 - ГАСУ, 34 - РГПУ им.А.И.Герцена. Choose reqiured number of Uni, then write Project_Jup.py -n <number>'''
    ) #создали экземпляр класса ArgumentParser
    put.add_argument('-n', choices=[1, 56, 53, 38, 48, 34], default=56, type=int) #добавили ожидаемый параметр в командной строке с помощью метода add_argument
    return put


if __name__ == '__main__':
    put = putUni()
    namespace = put.parse_args() #для разбора командной строки, это наш параметр введённый


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
#print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
#print(header)


path = "Home_Town.csv"
j=0
bdate=17
k = namespace.n

answer = [{'number': 'dict','url': 'dict', 'id': 'dict', 'home town': 'dict'}]
with open(path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=answer[0])
    writer.writeheader()
    while bdate<=25:
        sex=1
        while sex<=2:
            i=0
            while i<=48:
                if i==0:
                    url = "https://vk.com/search?c%5Bage_from%5D="+str(bdate)+"&c%5Bage_to%5D="+str(bdate)+"&c%5Bcity%5D=2&c%5Bcountry%5D=1&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Bsex%5D="+str(sex)+"&c%5Buniversity%5D="+str(k)+"&offset=0"
                else:
                    url = "https://vk.com/search?c%5Bage_from%5D="+str(bdate)+"&c%5Bage_to%5D="+str(bdate)+"&c%5Bcity%5D=2&c%5Bcountry%5D=1&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Bsex%5D="+str(sex)+"&c%5Buniversity%5D="+str(k)+"&offset="+str(20+i*20)
                r=requests.get(url, headers=header)
                print(r.ok)
                page = BeautifulSoup(r.text, 'html.parser')
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


path = "Home_Town.csv"
users = []
cities = []
with open(path, "r", newline="") as file:
    reader = csv.reader(file)
    i=0
    for row in reader:
        if row[3] == "Error" or row[3] == '' or row[3] == "Mudak":
            i=i
        elif i==0:
            users.append(row)
            #print(row)
            i = i + 1
        else:
            row[0]=i
            users.append(row)
            #print(row)
            i=i+1

Num_people=len(users)

for j in range(len(users)):
    if          users[j][3] == 'Санкт - Петербург' or \
                users[j][3] == 'Санкт Петербург' or\
                users[j][3] == 'СПб' or\
                users[j][3] == 'Питер' or\
                users[j][3] == 'Saint-Petersburg' or \
                users[j][3] == 'Петербург' or \
                users[j][3] == 'Санкт-петербург' or \
                users[j][3] == 'Санкт- Петербург' or \
                users[j][3] == 'Санкт-Петербург ' or\
                users[j][3] == 'санкт-петербург':
        cities.append('Санкт-Петербург')
    else:
        cities.append(users[j][3])
c=list(set(cities))

for i in range(len(c)):  #считаем города, которые встречаются один раз, мусором и статистически не важными. Удаляем мусор
    if cities.count(c[i])==1:
        cities.remove(c[i])
c=list(set(cities))

c1=[]
calc=[]
for i in range(len(c)):
    c1.append(cities.count(c[i]))
for i in range(len(c)):
    calc.append([c1[i],c[i]])
calc.sort(reverse=True)
print(calc)


city=['Город']
city_num=['Число студентов, чел']
city_percent=['В процентном соотношении, %']
for i in range(len(calc)):
    city_num.append(calc[i][0])
    city_percent.append(calc[i][0]*100/Num_people)
    city.append(calc[i][1])
print('Число анализируемых пользователей =', Num_people)
th=['N' ,city[0], city_num[0], city_percent[0]]
table = PrettyTable(th)
for i in range(25):
    i=i+1
    table.add_row([i ,city[i], city_num[i], round(city_percent[i], 2)])
print(table)


fig = plt.figure()
axes = fig.add_subplot (1, 1, 1)
plt.barh(city[2:11], city_percent[2:11], align='center', color='orange')
axes.set_xscale ('linear')
plt.title('Распределение студентов в %')
plt.grid(True)   # линии вспомогательной сетки
plt.show()

