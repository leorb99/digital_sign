import pytest
from src.utils import mdc

def test_mdc_com_valores_basicos():
    assert mdc(10, 5) == 5
    assert mdc(12, 8) == 4
    assert mdc(100, 25) == 25
    assert mdc(81, 27) == 27

def test_mdc_com_numeros_primos():
    assert mdc(13, 7) == 1
    assert mdc(17, 29) == 1

def test_mdc_com_zero():
    assert mdc(0, 5) == 5
    assert mdc(5, 0) == 5
    assert mdc(0, 0) == 0

def test_mdc_com_numeros_iguais():
    assert mdc(9, 9) == 9
    assert mdc(100, 100) == 100

def test_mdc_ordem_dos_parametros():
    assert mdc(8, 12) == 4
    assert mdc(12, 8) == 4