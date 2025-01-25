# test parametryzowany - mozna uruchomic test z roznymi argumentami

import pytest

def calculate_square(num):
    return num ** 2

def test_square_1():
    assert calculate_square(3) == 9

@pytest.mark.parametrize("input,expected_output",[(2,4),(3,9),(4,16)])
def test_square_calculate_parametrized(input,expected_output):
    assert calculate_square(input) == expected_output

    # = == == == == == == == == == == == == == == test
    # session
    # starts == == == == == == == == == == == == == == =
    # collecting...collected
    # 4
    # items
    #
    # pytest_zad2.py::test_square_1
    # PASSED[25 %]
    # pytest_zad2.py::test_square_calculate_parametrized[2 - 4]
    # PASSED[50 %]
    # pytest_zad2.py::test_square_calculate_parametrized[3 - 9]
    # PASSED[75 %]
    # pytest_zad2.py::test_square_calculate_parametrized[4 - 16]
    # PASSED[100 %]
    #
    # == == == == == == == == == == == == == == == 4
    # passed in 0.03
    # s == == == == == == == == == == == == == == ==