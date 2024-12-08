# klasa abstrakcyjna
# klasa z ktorej nie mozna zrobic obiektu
# metoda abstrakcyjna
from abc import ABC, abstractmethod

class Ptak(ABC):
    """
    Klasa opisujaca ptaka w pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością ", self.szybkosc)

    @abstractmethod #metoda abstrakcyjna
    def wydaj_odglos(self):
        pass

class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam.")

    def wydaj_odglos(self):
        print("Ko ko ko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")

class Orzel(Ptak):
    """
    Klasa Orzel
    """
    def wydaj_odglos(self):
        print("Kir kir kir")

    def polowanie(self):
        print("Tu", self.gatunek, "Rozpoczynam polowanie")

# TypeError: Can't instantiate abstract class Ptak without an implementation for abstract method 'wydaj_odglos'
#or1 = Ptak("Orzeł", 45)
#or1.latam()
# Tu Orzeł . Lecę z szybkością  45

kur1 = Kura("Kura domowa")
kur1.latam()  # Tu Kura domowa Ja nie latam.

or2 = Orzel("Orzel bielik", 50)
or2.latam()
# Tu Orzel bielik Lecę z szybkością  50
kur1.dziobanie()
or2.polowanie()
# Tu Kura domowa Idę sobie podziobać
# Tu Orzel bielik Rozpoczynam polowanie
