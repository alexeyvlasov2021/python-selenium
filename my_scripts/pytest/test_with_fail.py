import pytest

pytestmark = pytest.mark.math

def test_check_sum():
    assert 1+1 == 2

# pytest will continue to execute rest tests
def test_multiplication():
    assert 1*10 == 7

def test_divide():
    assert 100/10 == 10