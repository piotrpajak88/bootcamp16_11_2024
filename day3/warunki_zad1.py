# instrukcje warunkowe
# fachowo sie mowi instrukcje sterowania przeplywem programu

# if sterowana warunkiem

# if warunek:
# komenda(blok) wykonywany gdy warunek spelniony

# odp = False
#
# if odp:
#     print("Brawo")
#
# print("Dalsza czesc programu")
#
# odp = 'Radek'
#
# odp = 'Tomek'
#
# if odp == "Radek":
#     print("radek")
# else:
#     print("Inny przypadek")
#
# if True:
#     pass  # nic nie rob
#
# podatek = 0.9

# zarobki = int(input("podaj dochod: "))
#
# if zarobki < 10000:
#     podatek = 0.0
# elif podatek < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9
# print(f"Płacisz {zarobki * podatek}")

# suma_zam = 50
#
# if suma_zam > 150:
#     rabacik = 25
# else:
#     rabacik = 0
#
# print(f"Rabacik wynosi {rabacik}")  # Rabacik wynosi 0
#
# rabat = 25 if suma_zam > 150 else 0  # ternanry operator, operator warunkowy
#
# print(f"Rabat wynosi {rabat}")  # Rabat wynosi 0

###############

alert_system = "email"
error = "error"
lista_b = []

if alert_system == "console":
    print("Stało się coś strasznego")
elif alert_system == "email":
    print("System email")
    if error == "error":
        lista_b.append("Krytyczny")
    elif error == "medium":
        lista_b.append("Ostrzeżenie")
    else:
        lista_b.append("inny bład")
else:
    print("Inny")

print("Lista błędów", lista_b)
# System email
# Lista błędów ['Ostrzeżenie']

alert_dict = {'console': "Coś poszło nie tak",
              'email': {'error': 'Krytyczny', 'medium': "Ostrzeżenie"}}

if alert_system == 'console':
    # print(alert_dict[alert_system])
    print(alert_dict.get(alert_system, "Nie ma takiego systemu"))
elif alert_system == "email":
    # errors = alert_dict[alert_system]
    errors = alert_dict.get(alert_system, {})
    # print(errors[error])
    print(errors.get(error, "Nie ma takiego błędu dla systemu email"))
else:
    print("inny")

if alert_system in alert_dict:
    if alert_system == 'console':
        print(alert_dict.get(alert_system))
    elif alert_system == "email":
        print("System email")
        print(alert_dict[alert_system])  # {'error': 'Krytyczny', 'medium': 'Ostrzeżenie'}
        if error in alert_dict[alert_system]:
            errors = alert_dict[alert_system]
            print(errors[error])
else:
    print("Inny")

punkty = 0
odp = input("Podaj date Chrztu Polski: ")

if odp == "966":
    punkty +=1
    print("Odp prawidłowa")
else:
    print("Błąd")

odp = input("Podaj stolice Polski: ")

if odp.casefold() == "warszawa":
    punkty +=1
    print("Odp prawidłowa")
else:
    print("Błąd")

print(f"Zdobyłeś {punkty} punktów")