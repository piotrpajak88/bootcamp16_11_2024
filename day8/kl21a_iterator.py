# iterator - pozwala w sposob sekwencyjny dostep do danych
# oszczedza zuzycie pamieci
# zapamietuje gdzie skonczylismy

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lista)
# for i in lista:
#     print(i)

iterator = iter(lista)
print(iterator)
print(type(iterator))

# <list_iterator object at 0x000002B3F02BFB50>
# <class 'list_iterator'>
# for i in iterator:
#     print(i)
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# print(next(iterator))
# print("Zrob cos")
# print("Dalej")
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# 1
# Zrob cos
# Dalej
# 2
# 3
# 4


class Count:
    def __init__(self, low, high):
        """

        :param low: start licznika
        :param high: koniec licznika
        """
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

print("-----------")

counter = Count(1,20)
print(next(counter))

