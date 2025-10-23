import pytest
from src.utils import mod_inv, mod_pow, rotate_left
from src.utils import mod_pow

def test_mod_inv():
    assert mod_inv(3, 11) == 4
    assert mod_inv(7, 26) == 15
    assert mod_inv(7, 160) == 23
    assert mod_inv(17, 3120) == 2753
    with pytest.raises(ValueError):
        mod_inv(2, 4)

def test_mod_pow():
    assert mod_pow(2, 5, 13) == 6
    assert mod_pow(3, 13, 17) == 12
    assert mod_pow(7, 23, 187) == 46
    assert mod_pow(4, 0, 9) == 1
    assert mod_pow(10, 1, 6) == 4

def test_basic_rotation():
    n = 0b00000000000000000000000000001111  # 15
    result = rotate_left(n, 4)
    expected = 0b00000000000000000000000011110000  # 240
    assert result == expected

def test_zero_rotation():
    n = 0xDEADBEEF
    assert rotate_left(n, 0) == n

def test_full_rotation():
    n = 0x12345678
    assert rotate_left(n, 32) == n

def test_rotation_overflow():
    n = 0x12345678
    rotated = rotate_left(n, 36)  # equivalente a rotate_left(n, 4)
    expected = rotate_left(n, 4)
    assert rotated == expected

def test_wrap_around():
    n = 0x80000000 
    result = rotate_left(n, 1)
    expected = 0x00000001
    assert result == expected

def test_all_ones():
    n = 0xFFFFFFFF
    for i in range(33):
        assert rotate_left(n, i) == 0xFFFFFFFF

def test_all_zeros():
    n = 0x00000000
    for i in range(33):
        assert rotate_left(n, i) == 0x00000000

def test_rotation_16bits():
    n = 0xA5A5A5A5
    result = rotate_left(n, 16)
    expected = 0xA5A5A5A5
    assert result == expected