
tekst = 'Witaj Świecie'
print(tekst)

tekst.upper()
print(tekst.upper())
print(tekst)
name = "Radek"
print(len(name))#

print(name[0])#
print(name[1])#
print(name[2])#
print(name[3])#
print(name[4])#

print(name[2:4])
print(name[:4])


my_str = "  Hello Everyone  "
print(my_str.strip()) #Hello Everyone
print(my_str.strip()) #Hello Everyone

my_str2 = '***Hello***Everyone***'
# print(my_str2.strip('*'))
# print(my_str2.rstrip('*'))
# print(my_str2.lstrip('*'))


print(tekst.removeprefix('Witaj'))
print(tekst.removesuffix('Świecie'))

print(tekst.count('i'))
print(tekst.count('i',0,4))
print(tekst.count('j',0,4))

print(my_str2)
print(my_str2.replace('He','Ho')) # ***Hollo***Everyone***

print(my_str.replace(" ",""))#HelloEveryone
print(my_str.center(40))#             Hello Everyone

print(tekst.index("Ś")) #6
print(tekst.index("Św")) #6

print("moj ulubiony serial to\"Tytul\"") #mozna znak ucieczki - zazwyczaj znaczy nie iterpretuj
#kolejnego znaku

imie = "Radek"

formatted_text = f"Mam na imie {imie} i lubie Pythona"
print(formatted_text)

# \t - tabulator
# \n - nowa linia
# \b -backspace

starszy ="Witaj %s!"

print(starszy % imie) #Witaj Radek
print("Witaj {}!".format(imie)) #Witaj Radek!


print("""Tekst
wielolinijowy
!!!""")

"""Komentarz
wielolinijowy
!!!"""


'''Komentarz
wielolinijowy
!!!'''

encoded_s = tekst.encode('utf-8')
print(encoded_s) #b'Witaj \xc5\x9awiecie'
print(type(encoded_s)) #<class 'bytes'>
print(encoded_s.decode('utf-8')) #Witaj Świecie
print(encoded_s.replace(b"j",b"Z")) #b'WitaZ \xc5\x9awiecie'

