# od python 3.10 mamy match case

# lista = []
# lang = input("Podaj znany Ci język programowania ")
#
# match lang.lower().replace(" ",""):
#     case "python":
#         print("Znasz Pythona")
#         lista.append(lang)
#     case "java":
#         print("Java to kawa")
#         lista.append(lang)
#     case _: #odpowiednik else
#         print("Nie znam takiego jezyka")
#
# print(f"lista z odpowiedziami {lista}")


dane = [1, 2, 3]
# dane ={'nazwa':"Radek",'wiek':36}

match dane:
    case [a, b, c]:
        print(f"Lista z trzema elementami: {a}, {b}, {c}")
    case {'nazwa': n, "wiek": w}:
        print(f"Słownik reprezentujacy osobe {n}, wiek {w}")
    case _:
        print("Błędny typ danych")

if dane == [a,b,c]:
    print(f"{dane} ma elementy {a}, {b}, {c}")


