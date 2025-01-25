import pytest

def add(a, b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Dzielenie przez zero!")
    return a / b


def test_addition():
    result = add(2.5, 3.5)
    assert result == 6.0
    assert result == 6

def test_division_1():
    result = divide(10, 2)
    assert result == 5.0
    assert result == 5

def test_division_2():
    try:
        divide(10, 0)
    except ZeroDivisionError as e:
        assert str(e) == "Dzielenie przez zero!"

def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

def test_division_type():
    assert divide(6,"2")

def test_division_type_error():
    with pytest.raises(TypeError):
        divide(6, "2")


