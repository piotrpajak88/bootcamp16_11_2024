def restauracja(zamowienie):
    def zamow_pizze(skladniki='pieczarki'):
        print(f"Zamowiono pizze, skladniki: {skladniki}")

    def zamow_napoj(nazwa='herbata'):
        print("Zamowiono napoj", nazwa)

    if zamowienie.casefold().strip() == 'pizza':
        return zamow_pizze  # zwraca adres funkcji
    elif zamowienie.casefold().strip() == 'napoj':
        return zamow_napoj
    else:
        print("Podajemy tylko pizze lub napoje")
        return


zamowienie_pizza = restauracja("pizza")
zamowienie_napoj = restauracja("napoj")

zamowienie_pizza()
zamowienie_pizza('pieczarki,szynka')
zamowienie_napoj()
zamowienie_napoj('kawa')
restauracja("hamburger")
restauracja("pizza")()
restauracja("pizza")('peperoni, salami')
