import redis

r = redis.Redis()

r.set("name", "Radek")

wartosc = r.get('name')
print(wartosc) # b'Radek'
print(wartosc.decode('utf8')) # Radek

print(5 * '-')

r.delete('name')

czy_istnieje = r.exists('name')
print(czy_istnieje) # 0

print(5 * '-')
