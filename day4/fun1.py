# zmienne globalne
a = 6
b = 8


def dodaj():  # funckja bezargumentowa
    print(a + b)
    c = 7  # to jest zmienna lokalna tylko dla tej funcji


## argumenty pozycyjne, po  kolei trafaia do kolejnych argumentow w funkcji
def dodaj2(a, b):  # zaciemnilismy widocznosc globalnych,  musimy obowiazkowo podac a i b
    print(a + b)


# c = 0 argument o wartosci domyslnej
def odejmij(a, b, c=0):
    print(a - b - c)


print(dodaj)  # <function dodaj at 0x000001369A1FCAE0>
print(type(dodaj))  # <class 'function'>
dodaj()  # 14
# print(c) # NameError: name 'c' is not defined

# dodaj2() # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'

dodaj2(6, 8)  # 14

odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4

odejmij(c=8, a=9, b=88)  # -87
odejmij(1, b=87)  # -86

# Nie mozna przekazywac argumentow pozyzyjnych po nazwanych
# odejmij(c=90, 3, 4) # SyntaxError: positional argument follows keyword argument

print(dodaj())  # None

# print(dodaj() + dodaj()) # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
# jezeli funkcja nie zwraca wyniku, to nie mozemy dalej tego wyniku uzyc
