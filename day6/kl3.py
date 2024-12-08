class Car:
    """
    A simple representation of a car.
    """
    def __init__(self, model, year):
        self.model = model
        self.year = year
        # hermetyzacja - ustawienie pola jako prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 12

    def licznik(self):
        print(f"Prędkość samochodu: {self.__predkosc} km/h")

    def hamuj(self ):
        if self.__predkosc > 10:
            self.__predkosc -= 10
        else:
            self.__predkosc = 0

car = Car("Opel",2024)
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
car.gaz()
# Po oznaczeniu pola jako prywatne nie mozna odczytac tego pola
# print(car.__predkosc)
# AttributeError: 'Car' object has no attribute '__predkosc'. Did you mean: '_Car__predkosc'?
car.licznik() # Prędkość samochodu: 50 km/h
car.__predkosc = 0
car.licznik() # Prędkość samochodu: 50 km/h
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.hamuj()
car.licznik()
car.hamuj()
car.licznik()
car.hamuj()
car.licznik() # Prędkość samochodu: 0 km/h
# enkapsulacja - hermetyzujemy pola i dajemy metody do ich manipulacji


# C:\Users\88iro\PycharmProjects\bootcamp16_11_2024\pythonProject2\.venv\Scripts\python.exe C:\Users\88iro\PycharmProjects\bootcamp16_11_2024\pythonProject2\day6\kl3.py
# Prędkość samochodu: 72 km/h
# Prędkość samochodu: 72 km/h
# Prędkość samochodu: 12 km/h
# Prędkość samochodu: 2 km/h
# Prędkość samochodu: 0 km/h

