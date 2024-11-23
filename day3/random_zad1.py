import random
from random import randint

# import - sluży do dołączenia do naszego pliku innego pliku biblioteki, frameworks itd...

# random- dzialania na liczbach psuedolosowych

print(random.randint(1, 100))  # losowy integer z przedialu od 1 do 100
print(random.randint(1, 100))
print(random.randint(1, 100))
print(random.randint(1, 100))

print(random.randrange(1, 100))  # losowy integer z przedialu od 1 do 99
print(random.randrange(100))  # losowy integer z przedialu od 0 do 99

print(random.random())  # losowy float z (0.1)


# print(random.randint())
# TypeError: Random.randint() missing 2 required positional arguments: 'a' and 'b'

def check_range(number, func):
    low_limit = 0
    up_limit = 0
    for _ in range(number):
        if func(1, 100) == 100:
            up_limit += 1
        elif func(1, 100) == 1:
            low_limit += 1
        else:
            pass

    print(f"Ilosc wyników równa low limit to {low_limit}")
    print(f"Ilosc wyników równa up limit to {up_limit}")


check_range(10000, random.randint)
# Ilosc wyników równa low limit to 113
# Ilosc wyników równa up limit to 117
# czyli przediał dla randinta jest zamkniety

check_range(10000, random.randrange)
# Ilosc wyników równa low limit to 118
# Ilosc wyników równa up limit to 0
# czyli przedział otwarty z gory


lista = [5, 7, 45, 34, 56]
index = random.randrange(len(lista))  # len(lista) =5, wiec randrange od 0 do 4
print(index, lista[index])  # 2 45
print(random.choice(lista))  # wylosowany element to 5


def check_range2(number):
    low_limit = 0
    up_limit = 0
    for _ in range(number):
        if random.random() == 1:
            up_limit += 1
        elif random.random() == 0:
            low_limit += 1
        else:
            pass

    print(f"Ilosc wyników równa low limit to {low_limit}")
    print(f"Ilosc wyników równa up limit to {up_limit}")


check_range2(1000000)

# Ilosc wyników równa low limit to 0
# Ilosc wyników równa up limit to 0

###################################


lista_kule = list(range(1, 50))  # od 1 do 49
for _ in range(6):
    wyn = random.choice(lista_kule)
    lista_kule.remove(wyn)
    print(wyn, end=' ')
print()

lista_kule = list(range(1, 50))
print(random.choices(lista_kule, k=6))  # Powtarzaja sie : [10, 39, 36, 36, 40, 35]
print(random.sample(lista_kule, k=6))  # BEZ POWTÓRZEŃ [47, 2, 41, 4, 44, 38]
print(random.sample(lista_kule, 6))  # [19, 24, 8, 11, 45, 20]

print(random.sample(range(1,50),6)) # [48, 46, 36, 34, 10, 47]


