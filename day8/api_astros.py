# REST API - sposob komunikowania sie i wymiany danych pomiedzy koientem i serwerem
# klient np. przegladarka
# serwer - tzw backend, serwer, ktory na wystawione metody potrafiace obsluzyc zadania klienta
# GET, POST, PUT/PATCH, DELETE - metody http
# GET - pobiera dane
# POST - do tworzenia obiektu, wysyla dane na serwer, w body mozna przeslac jsona
# PUT/PATCH - aktualizuje obiekt
# DELETE - usuniecie obiektu

import requests
import pandas as pd
from pydantic import BaseModel
from typing import List

url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
print(response)  # <Response [200]>

# statusy http
# 2xx - OK
# 3xx - warningi,przekierowania
# 4xx - 404 - brak zasobu, 400 Bad Request, bledy po stronie klienta
# 5xx - bledy servera , 500 internal Server Error

# czysty json
# print(response.text)

response_data = response.json()
# print(type(response_data))  # <class 'dict'>

for k in response_data:
    print(k)

# people
# number
# message

for k, v in response_data.items():
    print(k, "=>", v)

# people = > [{'craft': 'ISS', 'name': 'Oleg Kononenko'}, {'craft': 'ISS', 'name': 'Nikolai Chub'},
#             {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}, {'craft': 'ISS', 'name': 'Matthew Dominick'},
#             {'craft': 'ISS', 'name': 'Michael Barratt'}, {'craft': 'ISS', 'name': 'Jeanette Epps'},
#             {'craft': 'ISS', 'name': 'Alexander Grebenkin'}, {'craft': 'ISS', 'name': 'Butch Wilmore'},
#             {'craft': 'ISS', 'name': 'Sunita Williams'}, {'craft': 'Tiangong', 'name': 'Li Guangsu'},
#             {'craft': 'Tiangong', 'name': 'Li Cong'}, {'craft': 'Tiangong', 'name': 'Ye Guangfu'}]
# number = > 12
# message = > success

people_list = response_data['people']

matthew = response_data['people'][3]['name']
print(matthew)  # Matthew Dominick


# df = pd.DataFrame(response_data['people'])
# print(df)

class Astronaut(BaseModel):
    craft: str
    name: str


class AstroData(BaseModel):
    message: str
    number: int
    people: List[Astronaut]


data = AstroData(**response_data)
print(data)

# message = 'success'
# number = 12
# people = [Astronaut(craft='ISS', name='Oleg Kononenko'), Astronaut(craft='ISS', name='Nikolai Chub'),
#           Astronaut(craft='ISS', name='Tracy Caldwell Dyson'), Astronaut(craft='ISS', name='Matthew Dominick'),
#           Astronaut(craft='ISS', name='Michael Barratt'), Astronaut(craft='ISS', name='Jeanette Epps'),
#           Astronaut(craft='ISS', name='Alexander Grebenkin'), Astronaut(craft='ISS', name='Butch Wilmore'),
#           Astronaut(craft='ISS', name='Sunita Williams'), Astronaut(craft='Tiangong', name='Li Guangsu'),
#           Astronaut(craft='Tiangong', name='Li Cong'), Astronaut(craft='Tiangong', name='Ye Guangfu')]

# print(data.message)
# print(data.number)

# for people in data.people:
#     print(people)
#     print(people.name)

# craft='ISS' name='Oleg Kononenko'
# Oleg Kononenko
# craft='ISS' name='Nikolai Chub'
# Nikolai Chub
# craft='ISS' name='Tracy Caldwell Dyson'
# Tracy Caldwell Dyson
# craft='ISS' name='Matthew Dominick'
# Matthew Dominick
# craft='ISS' name='Michael Barratt'
# Michael Barratt
# craft='ISS' name='Jeanette Epps'
# Jeanette Epps
# craft='ISS' name='Alexander Grebenkin'
# Alexander Grebenkin
# craft='ISS' name='Butch Wilmore'
# Butch Wilmore
# craft='ISS' name='Sunita Williams'
# Sunita Williams
# craft='Tiangong' name='Li Guangsu'
# Li Guangsu
# craft='Tiangong' name='Li Cong'
# Li Cong
# craft='Tiangong' name='Ye Guangfu'
# Ye Guangfu

for p in data.people:
    print(p.__class__.__name__)

# Astronaut
# Astronaut
# Astronaut
# Astronaut
# Astronaut
# Astronaut
# Astronaut
# Astronaut
# Astronaut
# Astronaut
# Astronaut
# Astronaut