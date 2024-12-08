# list comprehension
# [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5]

# create a new list with squares of numbers

squared = [num ** 2 for num in numbers]

print(f"Suared: {squared}")

even_numbers = [num for num in numbers if num % 2 == 0]
print(f"Even :{even_numbers}")

# Suared: [1, 4, 9, 16, 25]
# Even :[2, 4]

modified_numbers = [num * 2 if num % 2 == 0 else num for num in numbers]
print(f"Modified: {modified_numbers}")
# Modified: [1, 4, 3, 8, 5]

numbers2 = [-2, -3, 3, 4, -7]
absolute = [abs(x) for x in numbers2]
print(f"Absolute: {absolute}")
# Absolute: [2, 3, 3, 4, 7]

word = "Python"
print(list(word))
# ['P', 'y', 't', 'h', 'o', 'n']

letters = [letter for letter in word]
print(letters)
# ['P', 'y', 't', 'h', 'o', 'n']

print([i for i in range(10)])
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print([i for i in range(200) if i % 3 == 0 if i % 9 == 0 if i % 12 == 0])
# [0, 36, 72, 108, 144, 180]

