import csv


j = 0

path = "Home_Town.csv"
users = []
cities = []
with open(path, "r", newline="") as file:
    reader = csv.reader(file)
    i=0
    for row in reader:
        row[0]=i
        users.append(row)
        print(row)
        i=i+1
