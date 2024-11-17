# krotka (tupla) - kolekcja niemutowalna

# lepsze wykorzystanie pamiecia

# jednoelementowa krotka, zmienna, niezmienna - stała

tupla1 = "Radek" # <class 'str'>
print(type(tupla1))


tupla2 = ("Radek") # <class 'str'>
print(type(tupla2))

tupla3 = "Radek", # ('Radek',)
print(tupla3)
print(type(tupla3)) # <class 'tuple'>

tupla4 = ("radek",)
print(tupla4)

temp = 36,6
print(type(temp)) # <class 'tuple'>
print(temp) # (36, 6)

tupla_liczby = 43, 55, 22.34, 11, 200
print(type(tupla_liczby))
print(tupla_liczby) # (43, 55, 22.34, 11, 200)

# del usuniecie z pamieci
#del temp[0] #TypeError: 'tuple' object doesn't support item deletion

# mozna usunac cala tuple
del temp
#print(temp) #NameError: name 'temp' is not defined

print(tupla_liczby)
print(tupla_liczby[1:3])
print(tupla_liczby[-3:-1])
print(tupla_liczby[1:6:2])

print(tupla_liczby[-1])
print(tupla_liczby[-1::-1])

print(200 in tupla_liczby)        # True

tupla_names = "Radek", "Tomek", "Mateusz", "Tomek"

print(tupla_names.count('Tomek')) #  2 elementy "Tomek"

print(tupla_names.index('Radek')) # 0

print(sorted(tupla_names)) # ['Mateusz', 'Radek', 'Tomek', 'Tomek']

# funkcja sorted() zwraca nowa liste

print(tupla_names)  #   ('Radek', 'Tomek', 'Mateusz', 'Tomek')

a,b = 1,2 #przypisze wartosci  wedlug kolejnosci
print(f"{a = }, {b = }")

# a, b =1,2,3 #ValueError: too many values to unpack (expected 2)

a, *b = 1, 2, 3
print(f"{a = }, {b = }") #a = 1, b = [2, 3]

tupla_names = ('Radek','Tomek', 'Zenek', 'Bartek')
*name1, name2, name3 = tupla_names
print(f"{name1 = } {name2 = } {name3 = }") # name1 = ['Radek', 'Tomek'] name2 = 'Zenek' name3 = 'Bartek'

name1, *name2, name3 = tupla_names
print(f"{name1 = } {name2 = } {name3 = }") # name1 = 'Radek' name2 = ['Tomek', 'Zenek'] name3 = 'Bartek'

name1, name2, *name3 = tupla_names
print(f"{name1 = } {name2 = } {name3 = }") # name1 = 'Radek' name2 = 'Tomek' name3 = ['Zenek', 'Bartek']



tupla_zadanie = "OLA", 'Ania', "Ada", "Gabi", "Kasia", "Paulina"
*i1, i2, i3, i4 = tupla_zadanie
print(i1, i2, i3, i4) # ['OLA', 'Ania', 'Ada'] Gabi Kasia Paulina

print("Jeden", "Dwa", "Trzy", sep="") # JedenDwaTrzy
print("Jeden", "Dwa", "Trzy", sep=":") # Jeden:Dwa:Trzy
print("Jeden", "Dwa", "Trzy", sep=":",end="") #
print("Dalszy tekst") #Jeden:Dwa:TrzyDalszy tekst
print("Radek") # juz teraz wypisalo w nowej

# sep - znak oddzielajacy elementy (domyslnie " ")
# end - znak na koncu linii (domyslnie "\n")

lista = list(tupla_names)
print(lista) # ['Radek', 'Tomek', 'Zenek', 'Bartek']
print(type(lista)) # <class 'list'>
print(len(lista)) # 4


