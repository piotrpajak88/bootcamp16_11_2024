# 1. Stwórz Listę
# Stwórz listę zawierającą pięć różnych owoców.

fruits = ['apple', 'orange','strawberry','banana','raspberry']

# 2. Znajdź Drugi Element Listy
# Mając listę, znajdź drugi element listy.

print(fruits[1])

# 3. Zmień Element w Liście
# Zmień trzeci element listy na "malina".

fruits[2] = 'malina'

# 4. Stwórz Krotkę
# Stwórz krotkę zawierającą trzy różne kolory.

colors = ('blue','black','white')

# 5. Wybierz Ostatni Element Krotki
# Mając krotkę, wybierz jej ostatni element.

print(colors[-1])

# 8. Stwórz String Zawierający Twoje Imię i Nazwisko
# Stwórz string "Jan Kowalski".

my_full_name = "Piotr Pająk"

jk = "Jan Kowalski"

# 9. Podziel String na Imię i Nazwisko
# Podziel powyższy string na dwa osobne stringi: imię i nazwisko.

temp_list = jk.split()

imie = temp_list[0]
nazwisko = temp_list[1]

# 10. Użyj F-stringa do Połączenia Tekstu
# Stwórz string "Mam na imię Jan i mam 25 lat" używając f-stringa.

age = 25

my_f_string = f'Mam na imię {imie} i mam {age} lat'

# 11. Zadanie: Znajdź Długość Listy
# Mając listę [1, 2, 3, 4, 5], znajdź jej długość.

print(len([1, 2, 3, 4, 5]))

# 12. Zadanie: Połącz Dwie Listy
# Mając dwie listy, na przykład [1, 2, 3] i [4, 5, 6], połącz je w jedną.

print([1, 2, 3] + [4, 5, 6])

temp_list = [1, 2, 3]
temp_list.extend([4, 5, 6])
print(temp_list)

# 13. Zadanie: Dodaj Element na Końcu Listy
# Dodaj nowy element na końcu listy [1, 2, 3], na przykład 4.

temp_list = [1, 2, 3]
temp_list.append(4)
print(temp_list)

# 14. Zadanie: Wybierz Element z Krotki
# Mając krotkę (1, 2, 3, 4, 5), wybierz trzeci element.

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[2])

# 15. Zadanie: Odwróć Listę
# Odwróć kolejność elementów w liście [1, 2, 3, 4, 5].

temp_list =  [1, 2, 3, 4, 5]
temp_list.reverse()
print(temp_list)

# 16. Zadanie: Znajdź Maksymalny Element w Liście
# Znajdź największy element w liście [1, 2, 3, 4, 5].

temp_list =  [1, 2, 3, 4, 5]
print(max(temp_list))

# 17. Zadanie: Formatowanie Stringa
# Stwórz string "Python", a następnie dodaj do niego string " jest super!", tworząc pełne zdanie.

my_str = "Python"
my_str += " jest super!"
print(my_str)

# 18. Zadanie: Zastąp Słowo w Stringu
# Mając string "Lubię Pythona", zastąp słowo "Pythona" słowem "programowanie".

my_str = "Lubię Pythona"
my_str = my_str.replace('Pythona', 'programowanie')
print(my_str)

# 19. Zadanie: Wyodrębnij Podstring
# Wyodrębnij słowo "Python" ze stringa "Lubię Pythona".

my_str = "Lubię Pythona"
print(my_str[my_str.index('P'):-1])

# 20. Zadanie: Stwórz Listę Liczb Nieparzystych
# Stwórz listę zawierającą pierwsze pięć liczb nieparzystych.

odd = list(range(1,10,2))
print(odd)

a = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9]
odd = a[::2]
print(odd)