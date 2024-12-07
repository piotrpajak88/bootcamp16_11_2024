from functools import reduce


def add(a, b):
    return a + b


sum_all = reduce(add, [1, 2, 3])
print(f"Reduce [sum_all]: {sum_all}")
# Reduce [sum_all]: 6
# (1+2)+3

sum_all = reduce(lambda a, b: a + b, [1, 2, 3, 4])
print(sum_all)  # 10

product = reduce(lambda a, b: a * b, [1, 2, 3, 4])
print(product)  # 24

lista = [1, 2, 3, 45, 67, 78, 100, 200, 300]
sum_all = reduce(lambda a, b: a + b, list(map(lambda n: n * 2, list(filter(lambda n: n % 2 == 0, lista)))))
print(sum_all) # 1360