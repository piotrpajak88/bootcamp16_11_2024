class Human:
    """
    Klasa reprezentująca osobę.
    """

    def __init__(self, imie, wiek, wzrost, plec = 'k'):
        """
        Metoda inicjalizująca
        :param imie:
        :param wiek:
        :param wzrost:
        :param plec:
        """
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

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
        if self.plec.upper() == "M":
            print("Jestem mężyczyzna")
        elif self.plec.upper() == "K":
            print("Jestem kobietą")
        else:
            print(" ")

    def wypisz_wzrost(self):
        print(f"Mam {self.wzrost} cm wzrostu")


# cz1 = Human() # TypeError: Human.__init__() missing 3 required positional arguments: 'imie', 'wiek', and 'wzrost'
cz1 = Human("Ania", 34, 165)

print(cz1.imie)  # Ania
print(cz1.wiek)  # 34
print(cz1.wzrost)  # 165
print(cz1.plec)  # k

cz2 = Human("Radek",45,193,'m')

print(cz2.imie)  # Radek
print(cz2.wiek)  # 45
print(cz2.wzrost)  # 193
print(cz2.plec)  # m

print(cz1.__doc__) #    Klasa reprezentująca osobę.

cz1.powitanie()
cz1.wypisz_wiek()
cz1.wypisz_plec()
cz1.wypisz_wzrost()

cz2.powitanie()
cz2.wypisz_wiek()
cz2.wypisz_plec()
cz2.wypisz_wzrost()

# Witam, ja jestem Ania
# Mam 34 lat
# Jestem kobietą
# Mam 165 cm wzrostu
#
# Witam, ja jestem Radek
# Mam 45 lat
# Jestem mężyczyzna
# Mam 193 cm wzrostu
