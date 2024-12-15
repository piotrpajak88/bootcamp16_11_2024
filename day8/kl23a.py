# lt,le,gt,ge
# eq,ne
from functools import total_ordering

# @total_ordering pozwala na automatyczbe wygenerowanie pozostalych porownan
# tzerba wybrac dwie z roznych grup i nadpisac np.: __lt_ i __eq__
# pozostale zostana automatycznie wywnioskowane
@total_ordering
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __eq__(self, other):
        return self.grade == other.grade

    def __lt__(self, other):
        return self.grade < other.grade


alice = Student("Alice", 90)
bob = Student("Bob", 85)

print(alice < bob)
print(alice >= bob)
# False
# True
