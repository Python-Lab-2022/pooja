import csv
with open("names.csv",mode="r")as file:
    reader1=csv.reader(file)
    for row in reader1:
        print(row)
