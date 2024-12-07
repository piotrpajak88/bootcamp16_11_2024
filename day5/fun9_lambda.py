# funkcja lambda
# skrocony zapis funkcji
# lambda zwraca wynik - return
# funkcja anonimowa - deklaracja w miejscu wykonania

odejmij = lambda a, b: a - b

print(odejmij(6, 8))  # -2
print(odejmij(a=7, b=10))  # -3

res = lambda *args: sum(args)
print(res(10, 20))  # 30

res = lambda **kwargs: sum(kwargs.values())
print(res(a=10, b=25, c=80))  # 115

product = lambda a, b: a * b
print(product(4, 54))  # 216


def product1(nums):
    total = 1
    for i in nums:
        total *= i
    return total


res1 = lambda **kwargs: product1(kwargs.values())
print(res1)  # <function <lambda> at 0x000001FC337F8C20>
print(res1(a=10, b=90))  # 900


def my_func(n):
    return lambda a: a + n


add10 = my_func(10)
add20 = my_func(20)
add30 = my_func(30)

print(add10(5))
print(add20(5))
print(add30(5))

# 15
# 25
# 35

oblicz_vat = lambda cena, vat=8: cena * (100 + vat) / 100
print(oblicz_vat(1000))
print(oblicz_vat(1000, 23))
print(oblicz_vat(vat=15, cena=1000))

# 1080.0
# 1230.0
# 1150.0


wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
# nie ma mozliwosci w powyzszym przypadku, zeby by elif
print(wiek(5))
print(wiek(14))
print(wiek(30))

# dziecko
# nastolatek
# dorosły

lista = [1, 2, 3, 45, 67, 78, 100, 200, 300]
print([i * 2 for i in lista])
# [2, 4, 6, 90, 134, 156, 200, 400, 600]
print(lista * 2)
# [1, 2, 3, 45, 67, 78, 100, 200, 300, 1, 2, 3, 45, 67, 78, 100, 200, 300]
import numpy as np

lista1 = np.array(lista)
print(lista1 * 2)
# [  2   4   6  90 134 156 200 400 600]
print(list(map(lambda x: x * 2, lista)))
# [2, 4, 6, 90, 134, 156, 200, 400, 600]

print(list(map(lambda x: x * 1.1, lista)))
# [1.1, 2.2, 3.3000000000000003, 49.50000000000001, 73.7,
# 85.80000000000001, 110.00000000000001, 220.00000000000003, 330.0]

# filtrowanie

print([liczba for liczba in lista if liczba % 2 == 0])
# [2, 78, 100, 200, 300]
print(list(filter(lambda x: x % 2 == 0, lista)))
# [2, 78, 100, 200, 300]

print(list(filter(lambda x: x % 2 == 0 and x < 200, lista)))  # [2, 78, 100]
print(list(filter(lambda x: x % 2 == 0 and 5 < x < 200, lista)))  # [78, 100]

list2 = ['one','TWO','three','FOUR']
print(list(filter(lambda x: x.isupper(), list2)))
print(list(filter(lambda x: x.islower(), list2)))
# ['TWO', 'FOUR']
# ['one', 'three']

list3 = ['one','TWO2','three3','88','99','102','1.23']
numeric = list(filter(lambda x :x.isnumeric(),list3))
print(numeric)  # ['88', '99', '102']


alpha = list(filter(lambda x :x.isalpha(),list3))
print(alpha)  # ['one']

mix= list(filter(lambda x :x.isnumeric() and not x.isalpha(),list3))
print(f"Mix: {mix}")  # Mix: ['88', '99', '102']

alphanum = list(filter(lambda x :x.isalnum(),list3))
print(alphanum)  # ['one', 'TWO2', 'three3', '88', '99', '102']

