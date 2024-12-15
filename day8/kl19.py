# wyjatki
# mozemy dziedziczyc po klasie exceptcion i tworzyc wlasne wyjatki
from pandas.core.computation.ops import isnumeric


class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


# print(2 / 0) #ZeroDivisionError: division by zero
# raise ZeroDivisionError("Nie dziel przez zero") #ZeroDivisionError: Nie dziel przez zero

try:
    x = int(input("Podaj liczbe calkowita dodatnia "))
    if x < 0:
        print("Liczba ma byc wieksza od zera")
        raise MyException("Liczba musi byc dodatnia")
except MyException:
    print("Wystapil wyjatek MyException")
except ValueError:
    print("wystapil blad wartosci")
except Exception as e:
    print("Inny blad ", e)
else:
    print("Wprowadziles poprawna wartosc", x)
finally:
    print("Wprowadz kolejne dane")

# Podaj liczbe calkowita dodatnia -2
# Liczba ma byc wieksza od zera
# Wystapil wyjatek MyExcpetion

