# słownik - para klucz - wartość
# {"klucz" : 'wartość'}
# klucze nie mogą się powtarzać
# słownik jest odpowiednikiem json'a w pythonie


my_dict = {"A": "one", "B": "two", "C": 'three', 'D': 'four'}
print(my_dict)  # {'A': 'one', 'B': 'two', 'C': 'three', 'D': 'four'}
print(type(my_dict))  # <class 'dict'>

empty_dict = dict()  # tworzenie pustego słownika
print(empty_dict)  # {} pusty słownik

empty_dict2 = dict()
print(empty_dict2)  # {} pusty słownik
print(type(empty_dict2))  # <class 'dict'>

dict_with_integer = {1: 'one', 2: 'two', 3: 'three'}
print(dict_with_integer)  # {1: 'one', 2: 'two', 3: 'three'}

dict_mixed = {1: 'one', 'A': 'two', 3: 'three'}
print(dict_mixed)
# ctr + alt + l - formatuje zgodnie z PEP8

print(dict_mixed.keys())  # dict_keys([1, 'A', 3])
print(dict_mixed.values())  # dict_values(['one', 'two', 'three'])
print(dict_mixed.items())  # dict_items([(1, 'one'), ('A', 'two'), (3, 'three')])

dict_with_list = {1: 'one', 2: 'two', 'A': ['asif', 'john', 'maria']}
print(dict_with_list)  # {1: 'one', 2: 'two', 'A': ['asif', 'john', 'maria']}

dict_with_list_and_tuple = {1: 'one', 2: 'two', 'A': ['asif', 'john', 'maria'], 'B': ('Bat', 'cat', 'hat')}
print(dict_with_list_and_tuple)  # {1: 'one', 2: 'two', 'A': ['asif', 'john', 'maria'], 'B': ('Bat', 'cat', 'hat')}

dict_with_all = {1: 'one',
                 2: 'two',
                 'A': ['asif', 'john', 'maria'],
                 'B': ('Bat', 'cat', 'hat'),
                 'C': {"name", 'age', 10}}

print(
    dict_with_all)  # {1: 'one', 2: 'two', 'A': ['asif', 'john', 'maria'], 'B': ('Bat', 'cat', 'hat'), 'C': {'age', 10, 'name'}}

dict_with_dict = {1: 'one',
                  2: 'two',
                  'A': ['asif', 'john', 'maria'],
                  'B': ('Bat', 'cat', 'hat'),
                  'C': {"name", 'age', 10},
                  "D": {"Name": "Radek", "age": 99}}

print(
    dict_with_dict)  # {1: 'one', 2: 'two', 'A': ['asif', 'john', 'maria'], 'B': ('Bat', 'cat', 'hat'),
# 'C': {'name', 10, 'age'}, 'D': {'Name': 'Radek', 'age': 99}}

keys = {'a', 'b', 'c', 'd'}
my_dict2 = dict.fromkeys(keys)
print(my_dict2)  # {'d': None, 'a': None, 'c': None, 'b': None}

value = 10
my_dict3 = dict.fromkeys(keys, value)
print(my_dict3)  # {'b': 10, 'a': 10, 'd': 10, 'c': 10}

value = [10, 20, 30]
my_dict4 = dict.fromkeys(keys, value)
print(my_dict4)  # {'d': [10, 20, 30], 'b': [10, 20, 30], 'a': [10, 20, 30], 'c': [10, 20, 30]}

keys = [1, 2, 2, 3, 4, 4, 5]  # lista z duplikatami
dict_unique = dict.fromkeys(keys)
print(dict_unique)  # {1: None, 2: None, 3: None, 4: None, 5: None}
list_unique = list(dict_unique)
print(list_unique)  # [1, 2, 3, 4, 5]

print(list(dict.fromkeys(keys)))  # w jednej linijce usuwanie duplikatow bez zmiany kolejnosci

# wypisanie wartosci dla kluczy

print(my_dict["A"])  # one
print(dict_mixed[3])  # three
print(dict_with_list_and_tuple["B"])  # ('Bat', 'cat', 'hat')
print(dict_with_all["C"])  # {'name', 'age', 10}
print(dict_with_integer[2])  # two

# naciskamy ctrl i klikamy na nazwe zmiennej zeby przejsc do linijki gdzie zostala zdefiniowana

# print(my_dict['e']) # KeyError: 'e'

print(my_dict4.get("a"))  # [10, 20, 30]
print(my_dict4.get("e"))  # None
# mozemy ustawic watrosc domysla jaka bedzie zwracana gdy nie ma klucza w slowniku
print(my_dict4.get("e", "Nie ma"))  # Nie ma

my_dict5 = {'Name': 'Radek', "ID": 12345, "DOB": 1991, 'Address': "Warsaw"}
print(my_dict5)

print(my_dict5['DOB'])  # 1991
my_dict5['DOB'] = '1980'
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DOB': '1980', 'Address': 'Warsaw'}

dict1 = {"DOB": 1995}
print(type(dict1))  # <class 'dict'>

# update slownika innym slownikiem
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DOB': '1980', 'Address': 'Warsaw'}
my_dict5.update(dict1)
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DOB': 1995, 'Address': 'Warsaw'}

my_dict5['Job'] = 'Developer'
print(my_dict5)  # {'Name': 'Radek', 'ID': 12345, 'DOB': 1995, 'Address': 'Warsaw', 'Job': 'Developer'}

dict2 = {'cpi': 3.41}
print(dict2)  # {'cpi': 3.41}

# update słownika
# dodanie klucza jesli taki jeszcze nie istnieje
my_dict5.update(dict2)
print(my_dict5)
# {'Name': 'Radek', 'ID': 12345, 'DOB': 1995, 'Address': 'Warsaw', 'Job': 'Developer', 'cpi': 3.41}

my_dict5['aaa'] = 'bbb'
print(my_dict5)

# {'Name': 'Radek', 'ID': 12345, 'DOB': 1995, 'Address': 'Warsaw', 'Job': 'Developer', 'cpi': 3.41, 'aaa': 'bbb'}
