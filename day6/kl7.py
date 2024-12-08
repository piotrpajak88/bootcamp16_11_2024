class Animal:
    def __init__(self, name):
        self.name = name

    def wydaj_odglos(self):
        pass

    def info(self):
        print(f"Nazwa zwierzaka: {self.name}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def wydaj_odglos(self):
        print("Miau!")

    def info(self):
        super().info()
        print(f"Kolor: {self.color}")

class Tiger(Cat):
    def __init__(self, name,color,liczba_paskow):
        super().__init__(name,color)
        self.liczba_paskow = liczba_paskow

    def wydaj_odglos(self):
        print("Rau!")

    def info(self):
        super().info()
        print(f"Liczba pasków: {self.liczba_paskow}")

animal = Animal("Bezimienny")
animal.wydaj_odglos()
animal.info()

cat1 = Cat("Mruczek", "czarny")
cat1.wydaj_odglos()
cat1.info()

# Nazwa zwierzaka: Bezimienny
# Miau!
# Nazwa zwierzaka: Mruczek
# Kolor: czarny

tiger1 = Tiger("Tiger", "pomaranczowy", 104)
tiger1.wydaj_odglos()
tiger1.info()

# Rau!
# Nazwa zwierzaka: Tiger
# Kolor: pomaranczowy
# Liczba pasków: 104

