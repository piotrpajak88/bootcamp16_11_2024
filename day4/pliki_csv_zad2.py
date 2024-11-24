import csv

columns = []
rows = []

#filename = 'dane/records_3.csv'
filename = 'dane/records_discount.csv'

with open(filename,'r') as f:
    dialect = csv.Sniffer().sniff(f.read(1024)) # odczytalismy 1024 elementy
    print(dialect.delimiter) # ;
    f.seek(0) # wracamy do początku pliku
    #csvreader = csv.reader(f,delimiter=';') # Mozna tak by bylo gdy jest jeden plik,jak jest wiecej to jest problem
    # teraz moze byc wiele pilkow roznie delimiterowanych
    csvreader = csv.reader(f, delimiter=dialect.delimiter)
    print(csvreader) # <_csv.reader object at 0x0000025C423114E0>
    # iterator - mozna uzywac go w sekwencji
    # pobierac po kolei pojedyncze elementy next()

    columns = next(csvreader) # pierwszy wiersz

    for row in csvreader: # zacznie od drugiego
        # print(row)
        rows.append(row)

print("Columns", columns)
print("Rows", rows)

# Columns ['sku', 'exp_date', 'price']
# Rows [['1', 'today', '100.0'], ['2', 'today', '200.0'], ['3', 'tomorrow', '250'], ['4', 'today', '50'], ['5', 'today', '500.0']]
