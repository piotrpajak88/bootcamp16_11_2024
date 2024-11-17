#Kolekcje
from locale import locale_alias

lista = []
# print(type(lista)) # <class 'list'>
# print(bool(lista)) # False

pusta_lista = list()
print(type(pusta_lista)) # <class 'list'>
print(bool(pusta_lista)) # False

lista_2 = [10,20,30]
print(bool(lista_2)) # True
print(lista_2)


lista_3 = [10.77,20,30.66,'abc',('aaa','bbb')]
print(bool(lista_3)) # True
print(lista_3)
print(len(lista_3)) # 5
print(lista_3[0])
print(lista_3[1])
print(lista_3[2])

#dodoawanie elementów do listy

lista.append("Radek")
lista.append("Maciek")
lista.append("Piotr")
lista.append("Andrzej")
print(lista)

print(lista[-1])
print(lista[len(lista)-1])
print(lista[-1], lista[3])
print(lista[-2], lista[2])
print(lista[-3], lista[1])
print(lista[-4], lista[0])


# wypisywanie wielu elementow z listy (slicowanie)

print(lista[0:3])
print(lista)
print(lista[-2:])
print(type(lista[-1]))
print(lista[-1:]) # ['Andrzej']
print(lista[-1]) # Andrzej

print(type(lista[-1:])) # <class 'list'>
print(type(lista[-1])) # <class 'str'>

print(lista[-2:0]) # []
print(lista[-2:0]) # []
print(lista[2:2]) # []
print(lista[1:6]) # ['Maciek', 'Piotr', 'Andrzej']
print(lista[7:10]) # []

lista[2] = 'Mikołaj'
print(lista) # ['Radek', 'Maciek', 'Mikołaj', 'Andrzej']

print(len(lista)) # 4
lista.insert(1,"Karolina") # został dodany element do listy
print(lista) #['Radek', 'Karolina', 'Maciek', 'Mikołaj', 'Andrzej']
print(len(lista)) # 5

# usuniecie elementu z listy

# 1. usuniecie po indeksie -> pop()
# 2. usuniecie po elemencie -> remove()

# 1

print(lista.pop(0)) # Radek
print(lista) # ['Karolina', 'Maciek', 'Mikołaj', 'Andrzej']
print(lista.pop()) # Andrzej
print(lista) # ['Karolina', 'Maciek', 'Mikołaj']

ind = lista.index("Mikołaj")
print("Numer indeksu dla Mikołaj: ", ind) # Numer indeksu dla Mikołaj:  2
print(lista.pop(ind)) #Mikołaj
print(lista) #['Karolina', 'Maciek']

# 2.

lista.append("Karolina")
print(lista) # ['Karolina', 'Maciek', 'Karolina']
lista.remove("Karolina") # usuwa pietrwszy napotkany element "Karolina"
print(lista) #['Maciek', 'Karolina']

# print(lista.remove("Zenek")) #ValueError: list.remove(x): x not in list

print("Karolina" in lista) # True
print("Zenek" in lista) # False

print(lista.remove("Karolina")) # None
print(lista) #['Maciek']

lista.append("Marta")
lista.append("Marta")
lista.append("Marcin")

print(lista) # ['Maciek', 'Marta', 'Marta', 'Marcin']
print(lista.index("Marta"))  # 1 -> pierwszy napotkany element o nazwie "Marta"

a = 1
b = 3
a = b

print(f"{a = }") # a = 3
print(f"{b = }") # b = 3

b = 7

print(f"{a = }") # a = 3
print(f"{b = }") # b = 7

lista_4 = lista

print(f"{lista = }") # lista = ['Maciek', 'Marta', 'Marta', 'Marcin']
print(f"{lista_4 = }") # lista_4 = ['Maciek', 'Marta', 'Marta', 'Marcin']

lista.clear()

print(f"{lista = }") # lista = []
print(f"{lista_4 = }") # lista_4 = []

print(id(lista)) # 2690726478016
print(id(lista_4)) # 2690726478016
print(id(a)) # 140706297211384
print(id(b)) # 140706297211512

a = b

print(id(a)) # 140706297211512
print(id(b)) # 140706297211512

lista_copy = lista.copy()
print(id(lista)) # 1681411981504 -> zmienia sie w kazdej innej symulacji
print(id(lista_4)) # 1681411981504 -> zmienia sie w kazdej innej symulacji
print(id(lista_copy)) # 1681416299584 -> zmienia sie w kazdej innej symulacji
print(id(a)) # 140706297211512 -> NIE zmienia sie w innej symulacji, bo liczby nie sa mutowalne
print(id(b)) # 140706297211512 -> NIE zmienia sie w innej symulacji

# id dla powyzszych liczb sa niezmienne dla kazdej symulacji
# id dla powyzszych list zmieniaja w kazdej symulacji

liczby = [45, 999, 34, 22, 12, 34]
liczby.sort() # sortuje
print(liczby) # [12, 22, 34, 34, 45, 999]

liczby_a = [45, 999, 34, 22, 12, 34, "A"]
print(liczby_a) # [45, 999, 34, 22, 12, 34, 'A']
print(type(liczby_a))

# liczby_a.sort() # TypeError: '<' not supported between instances of 'str' and 'int'

lista_osoby = ['radek', 'ala', 'agata', 'lena', 'justyna']
lista_osoby.sort()
print(lista_osoby)  # ['agata', 'ala', 'justyna', 'lena', 'radek']

lista_alfabet_pol = ['a','z','f','ą','ń']
lista_alfabet_pol.sort()
print(lista_alfabet_pol) # ['a', 'f', 'z', 'ą', 'ń']
print(ord("z")) # 122
print(ord("a")) # 97
print(ord("b")) # 98
print(ord("ą")) # 261

lista_osoby.sort(reverse = True) # sortowanie od tylu
print(lista_osoby) # ['radek', 'lena', 'justyna', 'ala', 'agata']

lista_osoby.reverse()
print(lista_osoby) # ['agata', 'ala', 'justyna', 'lena', 'radek']

liczby_3 = [3, 8, 5, 12, 1]
liczby_3.reverse()
print(liczby_3)

print(liczby)

liczby[3] = 123
print(liczby[5])
print(liczby[-1])
print(liczby[1:4])
print(liczby[-3:-1])
print(liczby.pop(3))
print(liczby)
liczby.remove(34)
print(liczby)

liczby.sort(reverse=True)
print(liczby)

print(liczby[::-1]) # wypisuje od tylu
print(liczby[0:4:2]) # start : stop : krok [999, 22]

# łaczenie list, dostajemy nową kolekcję
print(liczby + liczby_3)
liczby_4 = liczby + liczby_3
print(liczby_4)

liczby_5 = [1,2,3,4,5]
liczby_6 = [6,7,8,9]

liczby_5.extend(liczby_6)
print(liczby_5) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

tekst = 'Pth on.'
lista_str = list(tekst)
print(lista_str) # ['P', 't', 'h', ' ', 'o', 'n', '.']

lista_str_pusta = []
lista_str_pusta.append(tekst)
print(lista_str_pusta) # ['Pth on.']

#rozpakowanie sekwencji
lista_str_pusta = []
lista_str_pusta.extend(tekst)
print(lista_str_pusta) # ['P', 't', 'h', ' ', 'o', 'n', '.']

krotka = tuple(liczby)
print(liczby)
print(krotka)
