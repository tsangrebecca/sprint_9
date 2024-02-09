import pytest
import bloomdata as bd


def test_increment_int():  # must start with test_ for pytest to recognize it
    assert bd.increment(3) == 4 # will pass
    assert bd.increment(-2) == -1

def test_increment_float():
    assert bd.increment(1.5) == 2.5

def test_increment_int_return_type():
    assert isinstance(bd.increment(3), int)
    # what this will return will be an instance of an integer
    # for boolean value