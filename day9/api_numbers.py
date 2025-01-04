import requests

from main import print_hi

url = 'http://numbersapi.com/random/year?json'

response = requests.get(url)
data = response.json()
print(data)
print(type(data))
print("Podaj odpowiedz na pytanie:\n", data['text'].replace(str(data['number']),""))
odp = input()
if odp == str(data['number']):
    print("Prawidlowa odpowiedz")
else:
    print("Bledna odpowiedz")