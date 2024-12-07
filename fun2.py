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

print(odejmij(6,9) + odejmij2(100,23,4))

