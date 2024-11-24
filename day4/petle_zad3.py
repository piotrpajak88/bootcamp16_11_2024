# while - petla sterowana warunkiem

# petla nieskonczona
# while True:
#     print("Komunikat")

licznik = 0
while True:
    print("Komunikat 1 !!!")
    licznik += 1
    if licznik > 15:
        break  # przerwanie petli

print(licznik)  # 16

licznik = 0
while licznik < 15:
    licznik += 1
    print("Komunikat 2 !!!")

# password = input("Podaj hasło: ")
#
# while password != "secret":
#     password = input("Błędne hasło! Podaj hasło ponownie: ")
# print("Hasło poprawne!")

# Podaj hasło: aaa
# Błędne hasło! Podaj hasło ponownie: ooo
# Błędne hasło! Podaj hasło ponownie: lll
# Błędne hasło! Podaj hasło ponownie: sekret
# Błędne hasło! Podaj hasło ponownie: secret
# Hasło poprawne!


# lista=[]
# lista_int=[]
#
# while True:
#     wej = input("Podaj liczbę: ")
#     if not wej.isnumeric():
#         break
#     lista.append(wej)
#     lista_int.append(int(wej))
#
# print(lista)
# print(lista_int)

# ['12', '13', '14', '15']
# [12, 13, 14, 15]

# A string is numeric if all characters are numeric
# dla floata nie zadziala bo jest kropka
# Dla isdigit jest podobnie
# stackoverflow proponuje, zeby we float najpierw poprzez replace zamienic "." na ""

# Podaj liczbę: 4.123
# []
# []

my_list = [1, 2, 3, 5, 4, 6, 5, 5]
element_to_remove = 5
while element_to_remove in my_list:
    my_list.remove(element_to_remove)

print(my_list)  # [1, 2, 3, 4, 6]

