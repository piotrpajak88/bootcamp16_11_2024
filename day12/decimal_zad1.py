from decimal import Decimal, ROUND_HALF_UP

decimal_1 = Decimal('0.1')
decimal_2 = Decimal(0.1)
decimal_3 = Decimal(1)

print(decimal_1)
print(decimal_2)
print(decimal_3)

# 0.1
# 0.1000000000000000055511151231257827021181583404541015625
# 1

# porownanie
print(f"Decimal('0.1') == Decimal(0.1)? {decimal_1 == decimal_2}")
# Decimal('0.1') == Decimal(0.1)? False
print(f"Decimal('0.1') == Decimal('0.1')? {decimal_1 == Decimal('0.1')}")
# Decimal('0.1') == Decimal('0.1')? True
print(f"Decimal(1) == Decimal('1')? {decimal_3 == Decimal('1')}")
# Decimal(1) == Decimal('1')? True

a = Decimal('10.345')
b = Decimal('3.2')

add = a + b
substract = a - b
multiply = a * b
divide = a / b

print(f"a + b = {add}")
print(f"a - b = {substract}")
print(f"a * b = {multiply}")
print(f"a / b = {divide}")

# a + b = 13.545
# a - b = 7.145
# a * b = 33.1040
# a / b = 3.2328125

add = add.quantize(Decimal("0.01"))
substract = substract.quantize(Decimal("0.01"))
multiply = multiply.quantize(Decimal("0.01"))
divide = divide.quantize(Decimal("0.01"))

print(5 * '-')
print(f"a + b = {add}")
print(f"a - b = {substract}")
print(f"a * b = {multiply}")
print(f"a / b = {divide}")

# -----
# a + b = 13.54
# a - b = 7.14
# a * b = 33.10
# a / b = 3.23

divide = a / b
print("Dzielenie z ustawieniem zaokraglania", divide.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
# Dzielenie z ustawieniem zaokraglania 3.23

value = Decimal("5.456")
rounding_nearest_005 = (value/Decimal("0.05")).quantize(Decimal("1"), rounding=ROUND_HALF_UP) * Decimal("0.05")
print(rounding_nearest_005) # 5.45


