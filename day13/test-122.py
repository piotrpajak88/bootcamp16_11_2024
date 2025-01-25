# unittesty - testy jednostkowe

from unittest import TestCase

class TryTesting(TestCase):
    def test_always_passed(self):
        self.assertTrue(True)

    def test_uppercase(self):
        assert 'python'.upper() == 'PYTHON' #sprawdzenie wyniku dzialania funkcji upper()

    def test_reversed(self):
        assert list(reversed([1,2,3])) == [3,2,1]
    def test_always_fail(self):
        self.assertTrue(False)

