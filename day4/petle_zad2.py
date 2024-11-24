dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}
print(dictionary)  # {'imie': 'Radek', 'nazwisko': 'Kowalski'}
print(type(dictionary))  # <class 'dict'>

# Wypisanie kluczy
for k in dictionary:
    print(k)
# imie
# nazwisko

for k in dictionary.keys():
    print(k)
# imie
# nazwisko


# Wypisanie wartosci
for v in dictionary.values():
    print(v)
# Radek
# Kowalski


# Wypisanie krotek (klucz-wartosc)
for i in dictionary.items():
    print(i)
# ('imie', 'Radek')
# ('nazwisko', 'Kowalski')

for k,v in dictionary.items():
    print(k,v,sep=" <=> ")

# imie <=> Radek
# nazwisko <=> Kowalski

for k,v in dictionary.items():
    print(k,v)
# imie Radek
# nazwisko Kowalski

for k,v in dictionary.items():
    print(k,":",v)
# imie : Radek
# nazwisko : Kowalski

