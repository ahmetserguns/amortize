
from amortize.calc import Mortgage,is_int,is_float,is_number
a=Mortgage(150000,6,12,0)

def test_payment():
    assert a.showpayment()== 12909.964456062355

def test_summary():
    assert a.showsummary()==None

def test_schedule():
    assert a.showschedule() == None

def test_int():
    assert is_int("3.4")==False

def test_float():
    assert is_float("4")==False

def test_number():
    assert  is_number("1.3")==True

def test_cashflow():
    assert a.cashflow()== [-150000, 12909.964456062355, 12909.964456062355, 12909.964456062355, 12909.964456062355,
                           12909.964456062355, 12909.964456062355, 12909.964456062355, 12909.964456062355,
                           12909.964456062355, 12909.964456062355, 12909.964456062355, 12909.964456062355]



