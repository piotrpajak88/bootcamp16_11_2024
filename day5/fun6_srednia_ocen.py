# funkcja ktora oblicza srednia ocen

def moja_srednia(*cyfry):
    try:
        return sum(cyfry)/len(cyfry)
    except Exception as e:
        print("Błąd, ", e)
        return

def srednia(name=None,*cyfry):
    print(cyfry)
    count=len(cyfry)
    suma = 0
    try:
        for c in cyfry:
            suma +=c

        avg = suma/count
    except Exception as e:
        print("Błąd, ", e)
    else:
        print(f"Srednia dla ucznia {name} wynosi {avg}")
    finally:
        print("Nastepne obliczenia")

moja_srednia()
print(moja_srednia(1))
print(moja_srednia(1, 2, 3, 4))
print(moja_srednia(1, 2, 3, 4, 5, 6))
print(moja_srednia("aaa", 1, 2, 3, 4))



srednia("aaa", 1, 2, 3, 4)
srednia("Maciej", 1, 2, 3, 4)
srednia("Maciej")