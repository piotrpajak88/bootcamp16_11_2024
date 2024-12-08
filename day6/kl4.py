# napisac klase Dom
# pola prywatne kolor, liczba okien, metraz
# dodac metyody do oczytu tych pol

class Dom:
    """
    Klasa opisujaca Dom
    """

    def __init__(self, kolor : str, liczba_okien : int ,metraz : float):
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien
        self.__metraz = metraz


    def podaj_kolor_domu(self):
        print(f"Kolor domu to {self.__kolor}")

    def podaj_liczbe_okien(self):
        print(f"Dom ma {self.__liczba_okien} okna")

    def podaj_metraz(self):
        print(f"Dom ma {self.__metraz} metrow kwadratowych")

    def zmien_okna(self):
        try:
            odp = int(input("Podaj liczne okien: "))
        except:
            pass
        self.__liczba_okien = odp
        self.podaj_liczbe_okien()

    def zmien_metraz(self):
        try:
            odp = float(input("Podaj metraz: "))
        except:
            pass
        self.__metraz = odp
        self.podaj_metraz()

    def zmien_kolor(self):
        odp = input("Podaj kolor farby: ")
        self.__kolor = odp
        self.podaj_kolor_domu()
        self.__farba()

    def __farba(self):
        print("Zabraklo farby")

dom1 = Dom("niebieski", 20, 250.5)
dom1.podaj_kolor_domu()
dom1.podaj_liczbe_okien()
dom1.podaj_metraz()

dom1.zmien_kolor()
