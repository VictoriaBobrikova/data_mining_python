{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from bs4 import BeautifulSoup\n",
    "from fake_useragent import UserAgent\n",
    "import requests\n",
    "import time\n",
    "import csv\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "from prettytable import PrettyTable"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "def user_parser (j, id):\n",
    "    url = \"https://api.vk.com/method/users.get.xml?user_ids=\"+id[1:]+\"&fields=home_town\"\n",
    "    r = requests.get(url)\n",
    "    page = BeautifulSoup(r.text, 'html.parser')\n",
    "    try:\n",
    "        answer = [{'number': str(j),'url': id, 'id': page.uid.get_text(), 'home town': page.home_town.get_text()}]\n",
    "    except AttributeError:\n",
    "        answer = [{'number': str(j),'url': id, 'id': page.uid.get_text(), 'home town': 'Error'}]\n",
    "    try:\n",
    "        writer.writerows(answer)\n",
    "    except UnicodeEncodeError:\n",
    "        answer = [{'number': str(j), 'url': id, 'id': page.uid.get_text(), 'home town': 'Mudak'}]\n",
    "        writer.writerows(answer)\n",
    "    time.sleep(0.33)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1664.3 Safari/537.36\n",
      "{'User-Agent': 'Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36'}\n"
     ]
    }
   ],
   "source": [
    "ua = UserAgent()\n",
    "print(ua.chrome)\n",
    "header = {'User-Agent':str(ua.chrome)}\n",
    "print(header)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "path = \"Home_Town.csv\"\n",
    "j=0\n",
    "bdate=17\n",
    "\n",
    "answer = [{'number': 'dict','url': 'dict', 'id': 'dict', 'home town': 'dict'}]\n",
    "with open(path, 'w', newline='') as file:\n",
    "    writer = csv.DictWriter(file, fieldnames=answer[0])\n",
    "    writer.writeheader()\n",
    "    while bdate<=25:\n",
    "        sex=1\n",
    "        while sex<=2:\n",
    "            i=1\n",
    "            while i<=48:\n",
    "                if i==0:\n",
    "                    url = \"https://vk.com/search?c%5Bage_from%5D=\"+str(bdate)+\"&c%5Bage_to%5D=\"+str(bdate)+\"&c%5Bcity%5D=2&c%5Bcountry%5D=1&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Bsex%5D=\"+str(sex)+\"&c%5Buniversity%5D=56&offset=0\"\n",
    "                else:\n",
    "                    url = \"https://vk.com/search?c%5Bage_from%5D=\"+str(bdate)+\"&c%5Bage_to%5D=\"+str(bdate)+\"&c%5Bcity%5D=2&c%5Bcountry%5D=1&c%5Bname%5D=1&c%5Bper_page%5D=40&c%5Bphoto%5D=1&c%5Bsection%5D=people&c%5Bsex%5D=\"+str(sex)+\"&c%5Buniversity%5D=56&offset=\"+str(20+i*20)\n",
    "                r=requests.get(url, headers=header)\n",
    "                print(r.ok)\n",
    "                page = BeautifulSoup(r.text, 'html.parser')\n",
    "                #print(page.prettify())\n",
    "                tags=page.findAll(\"div\", {\"class\":\"labeled name\"})\n",
    "                #print (tags)\n",
    "                print('Page', i+1)\n",
    "                for tag in tags:\n",
    "                    some=tag.findAll(\"a\", {\"class\": None})\n",
    "                    for link in some:\n",
    "                        j=j+1\n",
    "                        print (j,')' ,link.get('href'))\n",
    "                        user_parser(j, link.get('href'))\n",
    "                i=i+1\n",
    "                time.sleep(0.33)\n",
    "            sex=sex+1\n",
    "        bdate=bdate+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[1251, 'Санкт-Петербург'], [21, 'Норильск'], [21, 'Мурманск'], [19, 'Уфа'], [18, 'Екатеринбург'], [17, 'Челябинск'], [16, 'Тольятти'], [16, 'Сургут'], [16, 'Северодвинск'], [15, 'Череповец'], [15, 'Архангельск'], [14, 'Петрозаводск'], [13, 'Краснодар'], [13, 'Владивосток'], [11, 'Хабаровск'], [11, 'Набережные Челны'], [11, 'Москва'], [11, 'Колпино'], [11, 'Брянск'], [11, 'Барнаул'], [10, 'Якутск'], [10, 'Уральск'], [10, 'Сыктывкар'], [10, 'Самара'], [10, 'Омск'], [10, 'Магнитогорск'], [10, 'Костанай'], [10, 'Кемерово'], [9, 'Ставрополь'], [9, 'Сочи'], [9, 'Смоленск'], [9, 'Оренбург'], [9, 'Мирный'], [9, 'Калининград'], [9, 'Гатчина'], [9, 'Выборг'], [9, 'Великий Новгород'], [9, 'Saint-P'], [9, 'Cанкт-Петербург'], [8, 'Торжок'], [8, 'Тихвин'], [8, 'СПБ'], [8, 'Петропавловск-Камчатский'], [8, 'Нижневартовск'], [8, 'Донецк'], [8, 'Великие Луки'], [8, 'Алматы'], [7, 'Ярославль'], [7, 'Ухта'], [7, 'Псков'], [7, 'Пермь'], [7, 'Орск'], [7, 'Новосибирск'], [7, 'Новокузнецк'], [7, 'Красноярск'], [7, 'Иркутск'], [6, 'Южно-Сахалинск'], [6, 'Усть-Каменогорск'], [6, 'Тверь'], [6, 'Сосновый Бор'], [6, 'Пятигорск'], [6, 'Ноябрьск'], [6, 'Находка'], [6, 'Ленинград'], [6, 'Киров'], [6, 'Казань'], [6, 'Воронеж'], [6, 'Вологда'], [6, 'Ангарск'], [6, 'St. Petersburg'], [5, 'спб'], [5, 'питер'], [5, 'Тосно'], [5, 'Североморск'], [5, 'Рыбинск'], [5, 'Рудный'], [5, 'Пенза'], [5, 'Нижнекамск'], [5, 'Магадан'], [5, 'Кировск'], [5, 'Елизово'], [5, 'Волгоград'], [5, 'Белорецк'], [5, 'Актобе'], [5, 'SPB'], [4, 'Чайковский'], [4, 'Туапсе'], [4, 'Томск'], [4, 'Ташкент'], [4, 'Рязань'], [4, 'Россия'], [4, 'Пушкин'], [4, 'Приозерск'], [4, 'Полярные Зори'], [4, 'Новороссийск'], [4, 'Новодвинск'], [4, 'Нальчик'], [4, 'Кострома'], [4, 'Коряжма'], [4, 'Комсомольск-на-Амуре'], [4, 'Иваново'], [4, 'Зея'], [4, 'Ессентуки'], [4, 'Астана'], [4, 'Актау'], [4, 'Saint Petersburg'], [3, 'Шымкент'], [3, 'Чита'], [3, 'Чебоксары'], [3, 'Ульяновск'], [3, 'Улан-Удэ'], [3, 'Тюмень'], [3, 'Спб'], [3, 'Севастополь'], [3, 'Санкт-Петербург.'], [3, 'Салехард'], [3, 'САНКТ-ПЕТЕРБУРГ'], [3, 'Нижний Тагил'], [3, 'Нефтеюганск'], [3, 'Надым'], [3, 'Липецк'], [3, 'Котлас'], [3, 'Кирово-Чепецк'], [3, 'Караганда'], [3, 'Кандалакша'], [3, 'Кадуй'], [3, 'Йошкар-Ола'], [3, 'Ижевск'], [3, 'Златоуст'], [3, 'Железногорск'], [3, 'Гомель'], [3, 'Глазов'], [3, 'Вышний Волочек'], [3, 'Братск'], [3, 'Благовещенск'], [3, 'Бишкек'], [3, 'Баку'], [3, 'Астрахань'], [3, 'Армавир'], [3, 'St.Petersburg'], [2, 'санкт петербург'], [2, 'россия'], [2, 'омск'], [2, 'ленинград'], [2, 'колпино'], [2, 'город над вольной Невой'], [2, 'Ялта'], [2, 'Энгельс'], [2, 'Шарья'], [2, 'Черняховск'], [2, 'Харовск'], [2, 'Феодосия'], [2, 'Удомля'], [2, 'Тула'], [2, 'Тихорецк'], [2, 'Таганрог'], [2, 'Стерлитамак'], [2, 'Сочи, Санкт-Петербург'], [2, 'Сосновый бор'], [2, 'Сортавала'], [2, 'Соликамск'], [2, 'Сибай'], [2, 'Сегежа'], [2, 'Северная Пальмира'], [2, 'Саяногорск'], [2, 'Сахалин'], [2, 'Саров'], [2, 'Саратов'], [2, 'Саранск'], [2, 'Санкт_Петербург'], [2, 'Санкт-Петербург, Колпино'], [2, 'Санкт-Петербуг'], [2, 'Санкт петербург'], [2, 'С-Пб'], [2, 'Рига'], [2, 'Прокопьевск'], [2, 'Пошехонье'], [2, 'Павловск'], [2, 'Орёл'], [2, 'Орел'], [2, 'Одесса'], [2, 'Новый Уренгой'], [2, 'Новочеркасск'], [2, 'Новочебоксарск'], [2, 'Николаев'], [2, 'Нижний Новгород'], [2, 'Нефтекумск'], [2, 'Нефтекамск'], [2, 'Муром'], [2, 'Мончегорск'], [2, 'Могилев'], [2, 'Минск'], [2, 'Междуреченск'], [2, 'Мегион'], [2, 'Лянтор'], [2, 'Луга'], [2, 'Лесной'], [2, 'Кумертау'], [2, 'Краснотурьинск'], [2, 'Котово'], [2, 'Кондопога'], [2, 'Комсомольск-на-амуре'], [2, 'Когалым'], [2, 'Клайпеда'], [2, 'Кингисепп'], [2, 'Киев'], [2, 'Кемь'], [2, 'Канск'], [2, 'Каменск-Уральский'], [2, 'Ишимбай'], [2, 'Исфара'], [2, 'Зеленогорск'], [2, 'Ереван'], [2, 'Душанбе'], [2, 'Гусев'], [2, 'Гродно'], [2, 'Город на Неве'], [2, 'Галич'], [2, 'Всеволожск'], [2, 'Воркута'], [2, 'Волхов'], [2, 'Вилючинск'], [2, 'Биробиджан'], [2, 'Бельцы'], [2, 'Белореченск'], [2, 'Белгород'], [2, 'Балаково'], [2, 'Атырау'], [2, 'Арсеньев'], [2, 'Апатиты'], [2, 'Андреаполь'], [2, 'Анапа'], [2, 'Альметьевск'], [2, 'Абинск'], [2, 'Ulyanovsk'], [2, 'St.-Petersburg'], [2, 'Saint-P.'], [2, 'Saint Petesburg'], [2, 'Saint P.'], [2, 'Piter'], [2, 'Daugavpils'], [2, 'Cанкт-петербург']]\n"
     ]
    }
   ],
   "source": [
    "path = \"Home_Town.csv\"\n",
    "users = []\n",
    "cities = []\n",
    "with open(path, \"r\", newline=\"\") as file:\n",
    "    reader = csv.reader(file)\n",
    "    i=0\n",
    "    for row in reader:\n",
    "        if row[3] == \"Error\" or row[3] == '' or row[3] == \"Mudak\":\n",
    "            i=i\n",
    "        elif i==0:\n",
    "            users.append(row)\n",
    "            #print(row)\n",
    "            i = i + 1\n",
    "        else:\n",
    "            row[0]=i\n",
    "            users.append(row)\n",
    "            #print(row)\n",
    "            i=i+1\n",
    "Num_people=len(users)\n",
    "for j in range(len(users)):\n",
    "    if          users[j][3] == 'Санкт - Петербург' or \\\n",
    "                users[j][3] == 'Санкт Петербург' or\\\n",
    "                users[j][3] == 'СПб' or\\\n",
    "                users[j][3] == 'Питер' or\\\n",
    "                users[j][3] == 'Saint-Petersburg' or \\\n",
    "                users[j][3] == 'Петербург' or \\\n",
    "                users[j][3] == 'Санкт-петербург' or \\\n",
    "                users[j][3] == 'Санкт- Петербург' or \\\n",
    "                users[j][3] == 'Санкт-Петербург ' or\\\n",
    "                users[j][3] == 'санкт-петербург':\n",
    "        cities.append('Санкт-Петербург')\n",
    "    else:\n",
    "        cities.append(users[j][3])\n",
    "c=list(set(cities))\n",
    "\n",
    "for i in range(len(c)):  #считаем города, которые встречаются один раз, мусором и статистически не важными. Удаляем мусор\n",
    "    if cities.count(c[i])==1:\n",
    "        cities.remove(c[i])\n",
    "c=list(set(cities))\n",
    "\n",
    "c1=[]\n",
    "calc=[]\n",
    "for i in range(len(c)):\n",
    "    c1.append(cities.count(c[i]))\n",
    "for i in range(len(c)):\n",
    "    calc.append([c1[i],c[i]])\n",
    "calc.sort(reverse=True)\n",
    "print(calc)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Число анализируемых пользователей = 3076\n",
      "+----+------------------+----------------------+-----------------------------+\n",
      "| N  |      Город       | Число студентов, чел | В процентном соотношении, % |\n",
      "+----+------------------+----------------------+-----------------------------+\n",
      "| 1  | Санкт-Петербург  |         1251         |            40.67            |\n",
      "| 2  |     Норильск     |          21          |             0.68            |\n",
      "| 3  |     Мурманск     |          21          |             0.68            |\n",
      "| 4  |       Уфа        |          19          |             0.62            |\n",
      "| 5  |   Екатеринбург   |          18          |             0.59            |\n",
      "| 6  |    Челябинск     |          17          |             0.55            |\n",
      "| 7  |     Тольятти     |          16          |             0.52            |\n",
      "| 8  |      Сургут      |          16          |             0.52            |\n",
      "| 9  |   Северодвинск   |          16          |             0.52            |\n",
      "| 10 |    Череповец     |          15          |             0.49            |\n",
      "| 11 |   Архангельск    |          15          |             0.49            |\n",
      "| 12 |   Петрозаводск   |          14          |             0.46            |\n",
      "| 13 |    Краснодар     |          13          |             0.42            |\n",
      "| 14 |   Владивосток    |          13          |             0.42            |\n",
      "| 15 |    Хабаровск     |          11          |             0.36            |\n",
      "| 16 | Набережные Челны |          11          |             0.36            |\n",
      "| 17 |      Москва      |          11          |             0.36            |\n",
      "| 18 |     Колпино      |          11          |             0.36            |\n",
      "| 19 |      Брянск      |          11          |             0.36            |\n",
      "| 20 |     Барнаул      |          11          |             0.36            |\n",
      "| 21 |      Якутск      |          10          |             0.33            |\n",
      "| 22 |     Уральск      |          10          |             0.33            |\n",
      "| 23 |    Сыктывкар     |          10          |             0.33            |\n",
      "| 24 |      Самара      |          10          |             0.33            |\n",
      "| 25 |       Омск       |          10          |             0.33            |\n",
      "+----+------------------+----------------------+-----------------------------+\n"
     ]
    }
   ],
   "source": [
    "city=['Город']\n",
    "city_num=['Число студентов, чел']\n",
    "city_percent=['В процентном соотношении, %']\n",
    "for i in range(len(calc)):\n",
    "    city_num.append(calc[i][0])\n",
    "    city_percent.append(calc[i][0]*100/Num_people)\n",
    "    city.append(calc[i][1])\n",
    "print('Число анализируемых пользователей =', Num_people)\n",
    "th=['N' ,city[0], city_num[0], city_percent[0]]\n",
    "table = PrettyTable(th)\n",
    "for i in range(25):\n",
    "    i=i+1\n",
    "    table.add_row([i ,city[i], city_num[i], round(city_percent[i],2)])\n",
    "print(table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAbIAAAEICAYAAAA6InEPAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMS4wLCBo\ndHRwOi8vbWF0cGxvdGxpYi5vcmcvpW3flQAAIABJREFUeJzt3XmcHFW99/HPNxGYhAgIiSgQjBII\nCGKUgOIDOFFEfUQBjSzC1YAawAVBA5crXI0LFx+dK4t4hYgYDIZFvCigsgh02EQIEpawyGIkiLIK\nOCQBSX7PH3VGiqY73TOZ6e6TfN+v17yoOnXq1Ld7wvz6VFV3KyIwMzPL1bB2BzAzM1sZLmRmZpY1\nFzIzM8uaC5mZmWXNhczMzLLmQmZmZllzITMzs6y5kFlbSVooaYmkXkmPSPqxpFHtzmW2MiS9W9Kf\nJP1V0j6l9vUk/UHSK9uZb1XjQmad4IMRMQp4K7A9cGyb85itrBOBDwLvA34gaXhqPx74VkT8o23J\nVkEuZNYxIuIvwG+AbQAkHSjpLkn/kPSApIPL/SXtIWm+pGck3S/pfam9ImlpmuX1phnfwtJ+CyX9\nh6Q7Jf09zQK7Stt3T+M+Jel6SdtWHfcsSc+Xxn6otG0tST2SHkwzzFMljShtHycpStmWSfpU2jZM\n0tHpsTwh6TxJ61ft94qqHDPScndVjr1T/0+V2g5Kz+ffJV0q6XX1fheSdkqP/SlJiyRNlbRPVe7y\nc/waSYslbVAaYztJj0laI62Pr/fY0/a3l455q6Tu0rZKVd9d+36nkk4pjRmSnk3Lv0nbN5J0oaQn\nJd0n6dOlcWZI+mfq/5SkC+rNlvrTF1g7Iu6IiFuB54ENJO0AvD4izqv3vNvAuJBZx5A0Fvi/wC2p\n6VFgd2Ad4EDgBElvTX13AH4CHAmsB+wCLCwN97mIGJVmeh+scbj9gfcCmwFbkGaBafwzgIOBDYDT\ngAslrVWOChyXxn5/1bj/L403ERgPbAx8pbS97/+5ddP+15S2HQbsCbwT2Aj4O/D9GtlXKBWObwB/\nLbXtCXwZ+DAwJh337Dr7b0rxguJ7qe9EYH5EnFt6Tq+h9BxHxN+ACrB3aagDgHMi4p/lx141Rt8x\nNwZ+BXwTWB+YDvxc0phGjzciyr9rgDen9b7fzdnAQxTP6RTgvyS9uzTEuWnfTYHXA59YweGa7fuo\n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\npXxiTJ4AAAAASUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x390b407d30>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig = plt.figure()\n",
    "axes = fig.add_subplot (1, 1, 1)\n",
    "plt.barh(city[2:11], city_percent[2:11], align='center', color='orange')\n",
    "axes.set_xscale ('linear')\n",
    "plt.title('Распределение студентов в %')\n",
    "plt.grid(True)   # линии вспомогательной сетки\n",
    "plt.show()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
