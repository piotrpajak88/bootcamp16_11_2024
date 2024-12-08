# funkcje zwracajace wynik
# musza byc zakonczone return

def odejmij(a, b):
    return a - b


def odejmij2(a=0, b=0, c=-0):
    return a - b - c


print(odejmij(6, 9))
wynik = odejmij(6, 9)
print("Wynik", wynik)

print(odejmij2())
print(odejmij2(10, 5))
print(odejmij2(1, c=8, b=5))

print(odejmij(6, 9) + odejmij2(100, 23, 4))

a = 10
b = 10


def dodaj():
    a = 6  # zmienne lokalne
    b = 8  # nie zmienaja wartości globalnych
    print(a + b)


def dodaj2():
    print(a + b)


print(f"Zmienna a,b z gory (globalne): {a},{b}")
# Zmienna a,b z gory (globalne): 10,10
dodaj()  # 14
print(f"Zmienna a,b z gory (globalne): {a},{b}")
# Zmienna a,b z gory (globalne): 10,10
dodaj2() # 20

def dodaj3():
    global a # uzyjh zmiennej globalnej
    a=5
    b=8
    print(a+b)

dodaj3()  # 13
print(f"Zmienna a,b z gory (globalne): {a},{b}")
# Zmienna a,b z gory (globalne): 5,10
dodaj2() # 15

