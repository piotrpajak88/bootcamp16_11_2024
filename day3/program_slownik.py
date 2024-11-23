dict_pol_eng = {"słownik": "dictionary", "pies": "dog", "kot": 'cat', "mysz": "mouse"}

word = input(f"Podaj slowo z listy {list(dict_pol_eng.keys())}: ").strip().casefold().replace(" ","")

# The casefold() method in Python is used to convert all characters of a string into lowercase letters. It is similar to
# the lower() method but is more aggressive in its conversion, meaning it can convert more characters to lowercase
# and handle more cases where characters have different representations in different language
# niemieckie ẞ jest zamieniane na ss


print(f"Jego tłumaczenie na język angielski to: {dict_pol_eng.get(word,"Nie ma takiego słowa")}")

# tekst1 = 'Groẞ'
# tekst2 = 'GROSS'
#
# print(tekst1.lower() == tekst2.lower())  # False
# print(tekst1.casefold() == tekst2.casefold())  # True


