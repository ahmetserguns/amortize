
from amortize.calc import is_int,is_float,is_number

def test_int():
    assert is_int("3.4") is False

def test_float():
    assert is_float("4") is False

def test_number():
    assert  is_number("1.3") is True




