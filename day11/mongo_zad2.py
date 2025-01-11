from pymongo import MongoClient

client  = MongoClient("mongodb://localhost:27017")

db = client["przykladowa_baza"]

kolekcja = db["uzytkownicy"]

# kolekcja.insert_one(
#     {'imie':'Jan', 'nazwisko': 'Kowalski',"wiek":30}
# )

kolekcja.insert_many(
    [
        {'imie':'Anna', 'nazwisko': 'Nowak',"wiek":30},
        {'imie':'Pawel', 'nazwisko': 'Wisniewski',"wiek":25},
        {'imie':'Adam', 'nazwisko': 'Szymonski',"wiek":35}
    ]
)

for uzytkownik in kolekcja.find():
    print(uzytkownik)

print(5 * '-')
print(kolekcja.find_one({"imie":"Jan"}))

client.close()

# {'_id': ObjectId('67827dce6727ce66f0773c18'), 'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 30}
# {'_id': ObjectId('67827e68682b82f8ee6f4831'), 'imie': 'Anna', 'nazwisko': 'Nowak', 'wiek': 30}
# {'_id': ObjectId('67827e68682b82f8ee6f4832'), 'imie': 'Pawel', 'nazwisko': 'Wisniewski', 'wiek': 25}
# {'_id': ObjectId('67827e68682b82f8ee6f4833'), 'imie': 'Adam', 'nazwisko': 'Szymonski', 'wiek': 35}
#
# -----
# {'_id': ObjectId('67827dce6727ce66f0773c18'), 'imie': 'Jan', 'nazwisko': 'Kowalski', 'wiek': 30}

