dzialania = ['*', '/', '+', '-']
opcje_do_wyboru = f"""
Proszę wybrac działanie do wyboru z listy {dzialania}.
Jeżeli chcesz zakończyć działanie programu wpisz cokolwiek innego.
"""



wybor = ""
a = 0
b = 0
while True:
    wybor = input (opcje_do_wyboru)
    if wybor not in dzialania:
        break
    else:
        while True:
            try:
                a = int(input("Podaj pierwsza liczbe calkowita"))
                b = int(input("Podaj druga liczbe calkowita"))
            except:
                print("Podaj liczby całkowite")
                continue
            else:
                break
        if wybor == "+":
            wynik = a + b
            print(f'a + b = {wynik}')
        elif wybor == "-":
            wynik = a - b
            print(f'a - b = {wynik}')
        elif wybor == "*":
            wynik = a * b
            print(f'a * b = {wynik}')
        elif wybor == "/":
            try:
                wynik = a/b
            except ZeroDivisionError:
                print("Nie dziel przez zero")
            else:
                print(f'a / b = {wynik}')
        else:
            print("Coś nie tak jest w tym programie") # nie powinno dojsc do tego kroku



