# stworzyc slownik
# zapisac slownik do pliku za popmoca pickle
# odcvzytamy slownik

import pickle

slownik = {"name": "Radek", "age": 78}
print(type(slownik))
print(slownik)

# pickle uzywa zapisu bajtowego

with open('../dict1.pkl', 'wb') as f:
    pickle.dump(slownik, f)

with open("../dict1.pkl", "rb") as file:
    data = pickle.load(file)

print(data)
print(type(data))

# {'name': 'Radek', 'age': 78}
# <class 'dict'>


print(data['name'])  # Radek
