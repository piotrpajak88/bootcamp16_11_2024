from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2024-11-24
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2024-11-24 10:33:51.467306
print(type(time))  # <class 'datetime.datetime'>

print("Godzina", time.hour)
print("Dzień", today.day)

# Godzina 10
# Dzień 24

formatted_date = datetime.now().strftime("%d/%m/%Y")
print("Dzisiejsza data ", formatted_date)  # Dzisiejsza data  24/11/2024

formatted_time = datetime.now().strftime("%H:%M")
print("Aktualna godzina  ", formatted_time)  # Aktualna godzina   10:47
print("Aktualna godzina  ", formatted_time.removeprefix("0"))  # Aktualna godzina   (dla 09:47 -> 9:47)

tomorrow = today + timedelta(days=1)  # 2024-11-25
print(tomorrow)

####################################

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.00},
    {'sku': 2, 'exp_date': today, 'price': 200.00},
    {'sku': 3, 'exp_date': tomorrow, 'price': 250},
    {'sku': 4, 'exp_date': today, 'price': 50},
    {'sku': 5, 'exp_date': today, 'price': 500.00},
]

#print(products)

print("-------------------------")

for product in products:
    print(product)
    print(product['exp_date'])

    if product['exp_date'] != today:
        continue
    product['price']  *= 0.7
    print(f"""
Price for sku {product['sku']}
is now {product['price']}
""")

# -------------------------
# {'sku': 1, 'exp_date': datetime.date(2024, 11, 24), 'price': 100.0}
# 2024-11-24
#
# Price for sku 1
# is now 70.0
#
# {'sku': 2, 'exp_date': datetime.date(2024, 11, 24), 'price': 200.0}
# 2024-11-24
#
# Price for sku 2
# is now 140.0
#
# {'sku': 3, 'exp_date': datetime.date(2024, 11, 25), 'price': 250}
# 2024-11-25
# {'sku': 4, 'exp_date': datetime.date(2024, 11, 24), 'price': 50}
# 2024-11-24
#
# Price for sku 4
# is now 35.0
#
# {'sku': 5, 'exp_date': datetime.date(2024, 11, 24), 'price': 500.0}
# 2024-11-24
#
# Price for sku 5
# is now 350.0
#

