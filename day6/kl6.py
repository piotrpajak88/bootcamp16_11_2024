class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Nazywam się {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Manager(Pracownik):
    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 5000)
pracownik.przedstaw_sie()
wyn_prac = pracownik.oblicz_pensje()
print(f"Pensja pracownika: {wyn_prac}")
# Nazywam się Jan Kowalski
# Pensja pracownika: 5000

manager = Manager("Anna", "Nowak", 7000, 10000)
manager.przedstaw_sie()
wyn_man = manager.oblicz_pensje()
print(f"Pensja managera: {wyn_man}")
# Nazywam się Anna Nowak
# Pensja managera: 17000

print(isinstance(manager, Pracownik))  # True
print(isinstance(manager, Manager))  # True
print(issubclass(Manager, Pracownik))  # True
print(issubclass(Pracownik, Manager))  # False
