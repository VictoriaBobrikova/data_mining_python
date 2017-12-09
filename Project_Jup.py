from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import time
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
import sys
import argparse
import sqlite3


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

con = sqlite3.connect('my.db')  # создали соединение с БД
cur = con.cursor()  # курсор, по строкам будет ходить


def create_table_student():
    cur.execute(
        'CREATE TABLE IF NOT EXISTS student (vk_id INT NOT NULL, name VARCHAR(45) NOT NULL, home_town VARCHAR(45) NOT NULL, PRIMARY KEY (vk_id), CONSTRAINT fk_student_student_sex  FOREIGN KEY (name) REFERENCES student_sex (student_name) ON DELETE NO ACTION ON UPDATE NO ACTION)')


def create_table_student_sex():
    cur.execute(
        'CREATE TABLE IF NOT EXISTS student_sex (student_name VARCHAR(45) NOT NULL, student_sex VARCHAR(45) NULL, PRIMARY KEY (student_name))')


def data_entry(value):
    cur.execute('INSERT INTO student (vk_id, name, home_town) VALUES(?, ?, ?)', value)
    con.commit()


def data_entry_sex(value):
    cur.execute('INSERT or IGNORE INTO student_sex (student_name, student_sex) VALUES(?, ?)', value)
    con.commit()


create_table_student()
create_table_student_sex()


def user_parser(j, id, sex):
    if sex == 1:
        sex1 = 'female'
    else:
        sex1 = 'male'
    url = "https://api.vk.com/method/users.get.xml?user_ids=" + id[1:] + "&fields=home_town"
    r = requests.get(url)
    page = BeautifulSoup(r.text, 'html.parser')
    try:  # (number, url, id, home_town, name, sex)
        answer = (str(j), id, page.uid.get_text(), page.home_town.get_text(), page.first_name.get_text(), sex1)
    except Exception:
        answer = (str(j), id, page.uid.get_text(), 'Error', 'Error', sex1)
    try:
        if answer[3] != 'Error':
            if answer[3] != '':
                data_entry((answer[2], answer[4], answer[3]))
                data_entry_sex((answer[4], answer[5]))
    except Exception:
        answer = (str(j), id, page.uid.get_text(), 'Error', 'Error', sex1)
        if answer[3] != 'Error':
            if answer[3] != '':
                data_entry((answer[2], answer[4], answer[3]))
                data_entry_sex((answer[4], answer[5]))
    time.sleep(0.33)

ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}


j=0
bdate=17
k = namespace.n

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
            tags=page.findAll("div", {"class":"labeled name"})
            print('Page', i+1)
            for tag in tags:
                some=tag.findAll("a", {"class": None})
                for link in some:
                    j=j+1
                    print (j,')' ,link.get('href'))
                    user_parser(j, link.get('href'), sex)
            i=i+1
            time.sleep(0.33)
        sex=sex+1
    bdate=bdate+1

cur.execute(
    'UPDATE student SET home_town = "Санкт-Петербург" WHERE home_town = "Санкт - Петербург" OR home_town = "Санкт Петербург" OR home_town = "СПб" OR home_town = "Питер" OR home_town = "Saint-Petersburg" OR home_town = "Петербург" OR home_town = "Санкт-петербург" OR home_town = "Санкт- Петербург" OR home_town = "Санкт-Петербург " OR home_town = "санкт-петербург"  OR home_town = "спб" OR home_town = "СПБ"')
con.commit()


cur.execute('SELECT COUNT(1) FROM student')
str_vsego = cur.fetchall()
vsego = str_vsego.pop(0)[0]
print('Число анализируемых пользователей =', vsego)

###получили списки для осей
cur.execute('SELECT home_town, COUNT(home_town) FROM student GROUP BY home_town ORDER BY COUNT(home_town) DESC')
data_town = cur.fetchall()
cur.execute('SELECT home_town, COUNT(home_town) FROM student GROUP BY home_town ORDER BY COUNT(home_town) DESC')
data_value = cur.fetchall()
cur.execute('SELECT home_town, COUNT(home_town) FROM student GROUP BY home_town ORDER BY COUNT(home_town) DESC')
data_num = cur.fetchall()

towns = []
values = []
num_people = []
values_percent = []
b = 0
while b < len(data_town):
    towns.append(data_town.pop(b)[0])
    num_people.append(data_num.pop(b)[1])
    values.append(data_value.pop(b)[1])
    values_percent.append(round(values.pop(b) * 100 / vsego, 2))

th = ['N', 'Город', 'Число студентов, чел', 'В процентном соотношении, %']
table = PrettyTable(th)
for i in range(25):
    i = i + 1
    table.add_row([i, towns[i - 1], num_people[i - 1], values_percent[i - 1]])
print(table)

fig = plt.figure()
axes = fig.add_subplot(1, 1, 1)
plt.barh(towns[0:4], values_percent[0:4], align='center', color='orange')
axes.set_xscale('linear')
plt.title('Распределение студентов в %')
plt.grid(True)  # линии вспомогательной сетки
plt.show()

