import chardet

with open("test.log", "r") as file:
    lines = file.read()

print(lines)

# Powitanie
# Kolejne
# Jeszcze jedno
# Dodane
# Dodane
# Dodane
# DoĹ›dane

with open("test.log", "r", encoding='utf-8') as file:
    lines = file.read()

print(lines)

# Powitanie
# Kolejne
# Jeszcze jedno
# Dodane
# Dodane
# Dodane
# Dośdane

file_path = "test.log"
with open(file_path, "rb") as file:  # rb - odczyt bajtowy
    raw_data = file.read()

print(raw_data)

# b'Powitanie\r\nKolejne\r\nJeszcze jedno\r\nDodane\r\nDodane\r\nDodane\r\nDo\xc5\x9bdane\r\n'

result = chardet.detect(raw_data) # sprawdza typ kodowania
print(result)

# {'encoding': 'MacRoman', 'confidence': 0.6375949367088607, 'language': ''}

# po zwiekszeniu probki czyli wiecej znakow w tekscie, wynik poprawny:
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}

encoding = result['encoding']
confidence = result['confidence']

print("Kodowanie znaków: ", encoding)
print("Trafność: ", confidence)

print(raw_data.decode(encoding=encoding))

# Kodowanie znaków:  utf-8
# Trafność:  0.938125
# Powitanie
# Kolejne
# Jeszcze jedno
# Dodane
# Dąęoane
# Dońane
# Dośdane


