import random
from itertools import zip_longest

# pętla - możliwość wykonania tego samego fragmentu kodu wielokrotnie

# for - pętla iteracyjna

for i in range(10):
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

for i in range(10):
    print(i, i, sep=":")

# 0:0
# 1:1
# 2:2
# 3:3
# 4:4
# 5:5
# 6:6
# 7:7
# 8:8
# 9:9

for i in range(10):
    print(i, end="")
# 01234567890

print()  # żeby ustawić domyślny znak końca linii (czyli \n)

for _ in range(1, 5):  # _  niema zmienna
    print("Komunikat")
    # print(_)

my_string = "Radek"

for letter in my_string:
    print(letter)

lista_kule = list(range(1, 50))  # od 1 do 49
lista_wylosowane = []

for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_wylosowane.append(wyn)
    lista_kule.remove(wyn)
print(lista_wylosowane)
print([wyn for wyn in lista_wylosowane])

# for a in lista_wyn: print(a)

lista_wylosowane.sort()
print(lista_wylosowane)

lista3 = [j for j in range(1, 10) if j % 2 == 0]

print(lista3)  # [2, 4, 6, 8]

for c in lista3:
    if c == 2:
        c += 1
        print("Tylko jesli c=2 (teraz juz 3)")
    print("Przy kazdym elemencie petli", c)

# Tylko jesli c=2 (teraz juz 3)
# Przy kazdym elemencie petli 3
# Przy kazdym elemencie petli 4
# Przy kazdym elemencie petli 6
# Przy kazdym elemencie petli 8

a = 1
print(a)  # 1
a += 1
print(a)  # 2
a -= 1
print(a)  # 1
a *= 2
print(a)  # 2
a /= 2
print(a)  # 1.0
a %= 2
print(a)  # 1.0

imiona = ['Radek', 'Tomek', 'Zenek', "Zbyszek"]
for p in imiona: print(p)

# Radek
# Tomek
# Zenek
# Zbyszek

for p in imiona:
    print(p)

# Radek
# Tomek
# Zenek
# Zbyszek

print(p)  # Zbyszek, globalne zmienne

for i in range(len(imiona)):
    print(i, imiona[i])

# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zbyszek

for p in imiona:
    print(imiona.index(p), p)

# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zbyszek


# enumerate() - zwraca element kolekcji i jego pozycje

for i in enumerate(imiona):
    print(i)

# (0, 'Radek')
# (1, 'Tomek')
# (2, 'Zenek')
# (3, 'Zbyszek')
a, b = (0, 'Radek')
print(a, b)  # 0 Radek

for pozycja, osoba in enumerate(imiona):
    print(pozycja, osoba)

# 0 Radek
# 1 Tomek
# 2 Zenek
# 3 Zbyszek

for p, o in enumerate(imiona, start=1):
    print(p, o)

# 1 Radek
# 2 Tomek
# 3 Zenek
# 4 Zbyszek

ludzie = ['Radek', 'Janek', "Tomek", "Marek"]
wiek = [45, 40, 18, 23, 33]
# wypisanie w takie formie Radek 45

for i in zip(ludzie, wiek):
    print(i)

# ('Radek', 45)
# ('Janek', 40)
# ('Tomek', 18)
# ('Marek', 23)

for l, w in zip(ludzie, wiek):
    print(l, w)

# Radek 45
# Janek 40
# Tomek 18
# Marek 23

# 0 Radek 45

for i in enumerate(zip(ludzie, wiek)):
    print(i)

# (0, ('Radek', 45))
# (1, ('Janek', 40))
# (2, ('Tomek', 18))
# (3, ('Marek', 23))

for i, (l, w) in enumerate(zip(ludzie, wiek)):
    print(i, l, w)

# 0 Radek 45
# 1 Janek 40
# 2 Tomek 18
# 3 Marek 23

zipped = zip_longest(ludzie, wiek, fillvalue='NONE')
print(type(zipped))  # <class 'itertools.zip_longest'>
zipped_tuple = tuple(zipped)
print(zipped_tuple)
# (('Radek', 45), ('Janek', 40), ('Tomek', 18), ('Marek', 23), ('NONE', 33))

# iterator pozwala na asekwencyjny dostep do danych
# po odczytaniu danych nie sa juz dostepne
# pętle po zipped juz nie zadzialaja

for i in zipped:
    print(i)

# ('Radek', 45)
# ('Janek', 40)
# ('Tomek', 18)
# ('Marek', 23)
# ('NONE', 33)

print("----------------------")

for (o, w) in zipped:
    print(o, w)

for i in zipped_tuple:
    print(i)

# ('Radek', 45)
# ('Janek', 40)
# ('Tomek', 18)
# ('Marek', 23)
# ('NONE', 33)


for name,age in zipped_tuple:
    print(name, age)

# Radek 45
# Janek 40
# Tomek 18
# Marek 23
# NONE 33

