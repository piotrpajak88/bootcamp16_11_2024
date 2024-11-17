import sys

wiek = 47
rok = 2024



# print(rok // wiek) #czesc calkowita z dzielenia
# print(5 // 2) # 2
# print(rok % wiek) # modulo
# print(wiek ** rok) # do potegi
# print(f"{wiek ** rok:,}")# do potegi
wynik = wiek ** rok
# print(len(str(wynik)))
# #print(len(str(wynik ** 2)))
# #ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit
#
# print(0.2 + 0.8) # float 1.0
# print(0.2 + 0.7) # float 0.8999999999999999
# print(0.1 + 0.2) # float 0.30000000000000004
#
# # var = sys.float_info
# # print(var.max)
#
# #dzielenie liczb calkowitych daje floata
#
# print(type(4 / 2)) #<class 'float'>
# print(4 / 2) #2.0
#
# czy_znasz_pythona = True
# print(type(czy_znasz_pythona)) #<class 'bool'>
# print(bool(5)) #True
# print(bool(0)) #False
# print(bool(100)) #True
# print(bool("radek")) #True
# print(bool("")) #False
# print(bool(None)) #False
#
# a = 14
# b = 3
#
# print(f"Wynik porownania {a} > {b} to {a > b}") #Wynik porownania 14 > 3 to True
# print(f"Wynik porownania {a > b = }") #Wynik porownania a > b = True
# print("Wynik porownania", a, " < ", b, " = ", a < b) # Wynik porownania 14  <  3  =  False
#
# # operacje logiczne
# # and
# print(True and True)
# print(True and False)
# print(False and False)
#
# # or
# print(True or True)
# print(True or False)
# print(False or False)

# nie ma xor w pythonie

my_str = '1234567'

print(my_str.isnumeric())
print(my_str.isdigit())
print(my_str.isalnum())
print(my_str.isalpha())
print(my_str.isdecimal())

def check_string(my_string : str):
    print(f"{my_string} isnumeric: ",my_string.isnumeric())
    print(f"{my_string} isdigit: ",my_string.isdigit())
    print(f"{my_string} isalnum: ",my_string.isalnum())
    print(f"{my_string} isalpha: ",my_string.isalpha())
    print(f"{my_string} isdecimal: ",my_string.isdecimal())
    print(f"{my_string} istitle: ",my_string.istitle())
    print("\n")

check_string('1234567')
check_string('aaaaa')
check_string('aaa123')
check_string('  Tralalala  ')