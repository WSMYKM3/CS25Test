import csv

name = input("Name: ")
number = input("Number: ")

# 1
# "a" means append mode
# with open("csvWrite.csv","a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, number])
    
# 2 DictWriter
with open("csvWrite.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "number"])
    # here name and number is created with fieldnames, so they can not be changed
    writer.writerow({"name": name, "number": number})

# file.close() is not a must if use with open instead