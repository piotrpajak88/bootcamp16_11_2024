class MyNumber:
    def __init__(self, value):
        self.value = value


num1 = MyNumber(5)
num2 = MyNumber(15)

print(5 < 15)
# print(num1 < num2) #TypeError: '<' not supported between instances of 'MyNumber' and 'MyNumber'
print(num1.value < num2.value)

class MyNumber2:
    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        return self.value < other.value

    def __eq__(self, other):
        return self.value == other.value

    def __le__(self, other):
        return self.value <= other.value

num3 = MyNumber2(5)
num4 = MyNumber2(15)
num5 = MyNumber2(15)
print("-----------")
print(num3 < num4)
print(num3 > num4)
print(num4 > num3)
print(num5 == num4)
print(num3 <= num4)
print(num5 <= num4)