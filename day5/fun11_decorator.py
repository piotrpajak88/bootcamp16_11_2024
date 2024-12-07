# dekorator - funkcja opakowaujaca inna funkcje w dodatkowa funkcjonalnosc
#przyjmuje jako argument funkcje
# wykorzystuje zasady funkcji zagniezdzonej

def dekor(fun):
    def wew():
        print("Dekoruj")
        return fun()

    return wew

@dekor
def hej():
    print("Hej!!")


hej()  # Hej!!
#po dodaniu dekoratora:
# Dekoruj
# Hej!!

