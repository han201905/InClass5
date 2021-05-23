import pytest
import leapyear


def test_leapyear():
    assert leapyear.is_leap(2000) == True

def test_leapyear2():
    assert leapyear.is_leap(2021) == False

def test_leapyear3():
    assert leapyear.is_leap(2100) == False
