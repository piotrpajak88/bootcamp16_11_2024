# Zbior (set) - przechowuje unikalnie wartosci, brak duplikatow

# Set nie posiada indeksu, elementy nie sa numerowane

#nie zachowuje kolejnosci przy dodawaniu elementow

lista = [44,55,66,77,33,22,11,33,11]
zbior = set(lista)
print(zbior) # {33, 66, 11, 44, 77, 22, 55}
lista2 = list(zbior)
print(lista2) # [33, 66, 11, 44, 77, 22, 55]
lista2.remove(33)
print(lista2) #[66, 11, 44, 77, 22, 55]

# utworzenie pustego seta
#nie tworzy sie klamerkami
# pusty set tylko i wylacznie za pomoca slowka set()
zb2 = set()
print(zb2)
print(type(zb2)) # <class 'set'>

print(type({})) # <class 'dict'>

# Dodawanie elementow do zbioru (seta)
#add - dodawnie do seta

zb2.add(2)
zb2.add(3)
zb2.add(5)
zb2.add(5)
zb2.add(5)
zb2.add(7)
zb2.add(10)

print(zb2) # {2, 3, 5, 7, 10}

print(zbior) # {33, 66, 11, 44, 77, 22, 55}
zbior.add(33)
zbior.add(18)
zbior.add(18)

print(zbior) # {33, 66, 11, 44, 77, 18, 22, 55}

#pop() - usuniecie pierwszego elementu ze zbiory

print(zbior.pop()) # 33
print(zbior) # {66, 11, 44, 77, 18, 22, 55}, nie zmienil kolejnosci

zbior.pop()
zbior.pop()
print(zbior) # {44, 77, 18, 22, 55}

print(sorted(zbior)) # [18, 22, 44, 55, 77] ->posortowana lista

zbior.remove(55)
zbior.remove(18)
print(f"Zbiora po usunieciu: {zbior = }") # Zbiora po usunieciu: zbior = {44, 77, 22}
print(f"Zbiora po usunieciu: {zbior}") # Zbiora po usunieciu: {44, 77, 22}

# tworzenie zbioru z konkretnymi elementami

zbior2 = {667, 11, 44, 18, 52, 22, 667, 62, 999}
print(zbior2) # {999, 11, 44, 18, 52, 22, 667, 62}

zbior3 = {667, 11, 44, 18, 667, 62, 999, 123, 234}

#suma zbiorow
#tworzy nowy zbior
print(zbior2 | zbior3) # {999, 234, 11, 44, 123, 18, 52, 22, 667, 62}
print(zbior2.union(zbior3)) # {999, 234, 11, 44, 123, 18, 52, 22, 667, 62}
#zbiory bazowe nie zmienily sie
print(zbior2) # {999, 11, 44, 18, 52, 22, 667, 62}
print(zbior3) # {999, 234, 11, 44, 18, 123, 667, 62}

zbior4 = {8,9,10}
print(zbior2.union(zbior3,zbior4))
# {999, 8, 9, 234, 11, 44, 123, 10, 18, 52, 22, 667, 62}
# suma trzech zbiorow
print(zbior2 | zbior3 | zbior4)
# {999, 8, 9, 234, 11, 44, 123, 10, 18, 52, 22, 667, 62}

#czesc wspolna
print(zbior2 & zbior3) # {999, 11, 44, 18, 667, 62}
print(zbior2.intersection(zbior3)) # {999, 11, 44, 18, 667, 62}
print(zbior2 & zbior3 & zbior4) # set()

#roznica zbiorow
print(zbior2 - zbior3) # {52, 22}
print(zbior2.difference(zbior3)) #{52, 22}
print(zbior3.difference(zbior2)) # {234, 123}

zbior_copy = zbior.copy()
print(zbior_copy) # {44, 77, 22}
zbior.clear()
print(zbior) # set()
print(zbior_copy) # {44, 77, 22}

#suma zbiorow
#zmienia zbior bazowy
# wynik laczenia w zbiorze a
a = {1,2}
b = {2,3}
a.update(b)
print(a) # {1, 2, 3}

a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
# czesc wspolna, ale zmieni sie wartosc zbioru a
print(a) # {2, 3}


#frozenset() - zbior niemutowalny
frozen = frozenset([1,2,3])
print(frozen) # frozenset({1, 2, 3})

lista_temp = [[2,3],[4,5]]
print(lista_temp) # [[2, 3], [4, 5]]

#nie da sie robic zagniezdzonych zbiorow
# nested_set = {1,{2, 3}} TypeError: unhashable type: 'set'

#trzeba tu frozen seta uzyc

nested_set = {1,frozenset({2, 3})}
print(nested_set) # {1, frozenset({2, 3})}

zb3 = {1,2,3,4,5,6,7,8,9}
print(sum(zb3)) # 45 suma elementow zbioru
print(max(zb3)) # 9 wartosc maksymalna
print(min(zb3)) # 1 wartosc minimalna
print(len(zb3)) # 9 dlugosc zbioru
print(sorted(zb3)) # zwroci liste [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = {1,2,3}
b = {1,2}
print(b.issubset(a)) # True - b jest podzbiorem a

