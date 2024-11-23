# instrukcje warunkowe
# fachowo sie mowi instrukcje sterowania przeplywem programu

# if sterowana warunkiem

# if warunek:
# komenda(blok) wykonywany gdy warunek spelniony

odp = False

if odp:
    print("Brawo")

print("Dalsza czesc programu")

odp = 'Radek'

odp = 'Tomek'

if odp == "Radek":
    print("radek")
else:
    print("Inny przypadek")

if True:
    pass  # nic nie rob

podatek = 0.9

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

suma_zam = 50

if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabacik wynosi {rabacik}")  # Rabacik wynosi 0

rabat = 25 if suma_zam > 150 else 0  # ternanry operator, operator warunkowy

print(f"Rabat wynosi {rabat}")  # Rabat wynosi 0

