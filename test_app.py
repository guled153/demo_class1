import pytest

from app import add
def test_add():
    assert add(2,3) == 5

def test_add2():
    assert add(3,3) == 6
