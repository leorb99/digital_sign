import pytest
from src.utils import mod_inv
from src.utils import mod_pow

def test_mod_inv():
    assert mod_inv(3, 11) == (4, 1)
    assert mod_inv(7, 26) == (15, 1)
    assert mod_inv(7, 160) == (23, 1)
    assert mod_inv(17, 3120) == (2753, 1)
    assert mod_inv(2, 4) == (None, None)

def test_mod_pow():
    assert mod_pow(2, 5, 13) == 6
    assert mod_pow(3, 13, 17) == 12
    assert mod_pow(7, 23, 187) == 46
    assert mod_pow(4, 0, 9) == 1
    assert mod_pow(10, 1, 6) == 4