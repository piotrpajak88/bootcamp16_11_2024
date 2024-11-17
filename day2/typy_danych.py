import sys

wiek = 47
rok = 2024



# print(rok // wiek) #czesc calkowita z dzielenia
# print(5 // 2) # 2
# print(rok % wiek) # modulo
# print(wiek ** rok) # do potegi
# print(f"{wiek ** rok:,}")# do potegi
wynik = wiek ** rok
print(len(str(wynik)))
#print(len(str(wynik ** 2)))
#ValueError: Exceeds the limit (4300 digits) for integer string conversion; use sys.set_int_max_str_digits() to increase the limit

print(0.2 + 0.8) # float 1.0
print(0.2 + 0.7) # float 0.8999999999999999
print(0.1 + 0.2) # float 0.30000000000000004

# var = sys.float_info
# print(var.max)

#dzielenie liczb calkowitych daje floata

print(type(4 / 2)) #<class 'float'>
print(4 / 2) #2.0