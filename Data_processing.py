import csv
import matplotlib.pyplot as plt
import numpy as np

j = 0

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

print(len(cities))
print(set(cities))
c=list(set(cities))

for i in range(len(c)):  #считаем города, которые встречаются один раз, мусором и статистически не важными. Удаляем мусор
    if cities.count(c[i])==1:
        cities.remove(c[i])
print(cities)
print("3)", set(cities))
print(len(set(cities)))

c=list(set(cities))
c1=[]
calc=[]

for i in range(len(c)):
    c1.append(cities.count(c[i]))
for i in range(len(c)):
    calc.append([c1[i],c[i]])
calc.sort(reverse=True)
print(calc)
city=[]
city_num=[]
for i in range(10):
    city_num.append(calc[i][0])
    city.append(calc[i][1])
print(city)
print(city_num)

fig = plt.figure()
plt.bar(city, city_num)
plt.title('Simple bar chart')
plt.grid(True)   # линии вспомогательной сетки
plt.show()