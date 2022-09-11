import csv
with open("Data.csv",'r') as file:
    data=csv.reader(file)
    for d in data:
    	print(d)
