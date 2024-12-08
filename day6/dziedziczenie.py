class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):
    """
    Klasa samochódu dziedzicząca po klasie Pojazd.
    """
    def __init__(self, kolor, marka="Fiat"):
        super().__init__(kolor)  # wywołanie konstruktora klasy nadrzędnej (obowiązkowo trzeba ją wywołać)
        self.marka = marka

    def info(self):
        super().info()  # wywołanie metody nadrzędnej (nie musimy tutaj)
        print(f"Marka: {self.marka}")

class Rower(Pojazd):
    """
    Klasa roweru dziedzicząca po klasie Pojazd.
    """

poj = Pojazd("czerwony")
poj.info()  # Kolor: czerwony

sam = Samochod("zielony")
sam.info()
# Kolor: zielony
# Marka: Fiat

rower = Rower("żółty")
rower.info()

lista = [poj, sam, rower]
print(lista)
# [<__main__.Pojazd object at 0x0000027CC32D65D0>, <__main__.Samochod object at 0x0000027CC32D6780>, <__main__.Rower object at 0x0000027CC32D67B0>]

# polimorfizm - obiekty różnych klas traktowane jak jednej.
for i in lista:
    print(i.__class__.__name__)
    i.info()

# Pojazd
# Kolor: czerwony
# Samochod
# Kolor: zielony
# Marka: Fiat
# Rower
# Kolor: żółty

