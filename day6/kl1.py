# klasa - szablon, wzór, przepis
# obiekt - zbudowany wg przepisu, instancja
# enkapsulacja, hermetyzacja, abstrakcja, dziedziczenie, polimorfizm
# pola, funckje

class Human:
    """
    Klasa Human  opisujaca czlowieka w pythonie
    """
    imie = "John"
    plec = "M"
    wiek = 30

    def powitanie(self):
        """
        Funkcja powitujaca czlowieka
        """
        print(f"Witam, ja jestem {self.imie}")

    def wypisz_wiek(self):
        """
        Funkcja wypisujaca wiek czlowieka
        """
        print(f"Mam {self.wiek} lat")

    def wypisz_plec(self):
        if self.plec == "M":
            print("Jestem mężyczyzna")
        elif self.plec == "K":
            print("Jestem kobietą")
        else:
            print(" ")

print(Human, __doc__)
print(print, __doc__)

cz2 = Human()
cz2.imie = "Janek"
cz2.plec = "M"
cz2.wiek = 35

print(cz2.imie)
print(cz2.plec)
print(cz2.wiek)

# Janek
# M
# 35
cz2.powitanie()
# Witam, ja jestem Janek
cz2.wypisz_wiek()
# Mam 35 lat

