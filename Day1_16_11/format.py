user = "Tomek" #str
wiek = 39 #int
wersja = 3.900001 #<class 'float'>
print(type(wersja))
liczba =123456789 #int

print('Witaj %s, masz teraz %d lat' % (user,wiek))
# print('Witaj %d, masz teraz %s lat' % (user,wiek)) -> bedzie bład

print('Witaj %(user)s, masz teraz %(wiek)d lat' % {'user':user,'wiek':wiek})
print('Witaj %(user)s, masz teraz %(wiek)d lat' % {'user':user,'wiek':wiek})
print('Witaj %(user)s, masz teraz %(age)d lat' % {'user':user,'age':wiek})
#ctrl + d kopiowanie calej linii

#shift+clrt+strzalka w dol

print(f"Witaj {user}, masz teraz {wiek} lat, milo cie widziec {user}!")
print("Witaj {}, masz teraz {} lat!".format(user,wiek))


print("Używamy wersji Pythona %i" % 3)#Uzywamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3.9)#Uzywamy wersji Pythona 3.900000
print("Używamy wersji Pythona %.1f" % 3.9)#Uzywamy wersji Pythona 3.9
print("Używamy wersji Pythona %.2f" % 3.9)#Uzywamy wersji Pythona 3.90
print("Używamy wersji Pythona %.0f" % 3.9)#Uzywamy wersji Pythona 4
print("Używamy wersji Pythona %.f" % 3.9)#Uzywamy wersji Pythona 4

x = 3.99
print("Liczba %f", x)
print("Liczba ", x)

x = round(x)
print("Liczba po zaokragleniu ", x)

x = 3.14159
x = round(x,2)
print("Liczba po zaokragleniu ", x)

print(f"Uzywamy wersji Pythona {wersja}")
print(f"Uzywamy wersji Pythona {wersja:.1f}")
print(f"Uzywamy wersji Pythona {wersja:.2f}")
print(f"Uzywamy wersji Pythona {wersja:.0f}")

print(liczba)

print("Nasza duza liczba {}".format(liczba)) #Nasza duza liczba 123456789
print("Nasza duza liczba {:,}".format(liczba)) #Nasza duza liczba 123,456,789

print(f"Nasza duza liczba {liczba:,}") #Nasza duza liczba 123,456,789
print(f"Nasza duza liczba {liczba:,}".replace(',',' ')) #Nasza duza liczba 123 456 789
print(f"Nasza duza liczba {liczba:,}".replace(',','.')) #Nasza duza liczba 123.456.789

print(f"Nasza duza liczba {liczba:_}") #Nasza duza liczba 123_456_789

parametr = 150_000_000_000
print(type(parametr))   #<class 'int'>

print(f"{user}")
print(f"{user:>10}") #dopelni do prawej zeby bylo 10 znakow:      Tomek
print(f"{user:<15}") #do lewej teraz do 15 znakow: Tomek
print(f"{user:^15}") #teraz zcentruje do 15 znakow:      Tomek

tekst = "jeden dwa trzy cztery" #['jeden', 'dwa', 'trzy', 'cztery']
print(tekst.split())

tekst2 = "jeden, dwa, trzy, cztery"
print(tekst2.split(','))
#['jeden', ' dwa', ' trzy', ' cztery']
print(tekst2.split(', '))
#['jeden', 'dwa', 'trzy', 'cztery']
