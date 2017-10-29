import csv


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
            print(row)
            i = i + 1
        else:
            row[0]=i
            users.append(row)
            print(row)
            i=i+1
