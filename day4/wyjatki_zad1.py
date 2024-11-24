# wyjątki błędy wykonania programu

# print(5/0) # ZeroDivisionError: division by zero

# przechwytywanie i obsługa wyjątków

try:
    # print(5 / 0)
    # print("a" / 2)
    # print(int("A"))
    # raise KeyError("błąd klucza") # rzucenie wyjątku
    wynik = 90 / 3
except ZeroDivisionError:
    print("Nie wolno dzielić przez zero!")
except TypeError:
    print("Błąd typu.")
except ValueError:
    print("Błąd wartości.")
except Exception as e:
    print("Błąd", e)
else:
    print("Wynik: ", wynik)
finally:
    print("Obliczenia wykonane.")
print("Program nadal działa.")

# Nie wolno dzielić przez zero!
# Program nadal działa.

# Błąd typu.
# Program nadal działa.

# #Błąd wartości.
# Program nadal działa.

# Błąd 'błąd klucza'
# Program nadal działa.

# Wynik:  30.0
# Obliczenia wykonane.
# Program nadal działa.
