# pliki csv - dane oddzielone znakiempodzialu
# imie,opis,ocena
# Andrzej,fajny,4

import csv
from dataclasses import fields

row = ['Radek', 'Coe', '3', '0']
fields = ['name', 'branch', 'year', 'cgpa']

zipped_dict = dict(zip(fields,row))
print(zipped_dict)
# {'name': 'Radek', 'branch': 'Coe', 'year': '3', 'cgpa': '0'}

# z defaultowym newline bedzie pusta linia pomiedzy wierszami, a tego nie chcemy
# bo pozniej przy wczytywaniu tez bedziemy mieli pusta linie
with open("dane/records.csv", 'w', newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(row)

# zapis kilku wierszy
with open("dane/records_2.csv", 'w', newline="") as csv_f:
    csvwriter = csv.writer(csv_f)
    csvwriter.writerow(fields)
    csvwriter.writerow(row)

#to samo tylko w inny sposób:
with open("dane/records_3.csv", 'w', newline="") as csv_f:
    csv_dict_writer = csv.DictWriter(csv_f, fieldnames = fields)
    csv_dict_writer.writeheader() # zapisz nazwy kolumn
    csv_dict_writer.writerow(zipped_dict) # zapis jednego slownika jako wiersz

products = [
    {'sku': 1, 'exp_date': 'today', 'price': 100.00},
    {'sku': 2, 'exp_date': 'today', 'price': 200.00},
    {'sku': 3, 'exp_date': 'tomorrow', 'price': 250},
    {'sku': 4, 'exp_date': 'today', 'price': 50},
    {'sku': 5, 'exp_date': 'today', 'price': 500.00},
]

fields_products = [k for k in products[0]]

with open("dane/records_discount.csv", 'w', newline="") as csv_f:
    csv_dict_writer = csv.DictWriter(csv_f, fieldnames = fields_products,delimiter=";")
    csv_dict_writer.writeheader() # zapisz nazwy kolumn
    csv_dict_writer.writerows(products) # zapis listy slownikow jako kolejne wiersze (writerows zamiast writerow)
