import pytest
from src.rsa import crip, decrip, N

def test_crip():
    assert crip(97) == 746

def test_decrip():
    assert decrip(746) == 97
    
def test_encrypt_decrypt_identity():
    for m in [0, 1, 42, 123, 898]:
        c = crip(m)
        assert decrip(c) == m

def test_decrypt_encrypt_identity():
    for c in [0, 1, 42, 123, 898]:
        m = decrip(c)
        assert crip(m) == c

def test_different_messages_produce_different_ciphertexts():
    m1 = 123
    m2 = 456
    c1 = crip(m1)
    c2 = crip(m2)
    assert c1 != c2

def test_different_ciphers_produce_different_plaintexts():
    c1 = 123
    c2 = 456
    m1 = decrip(c1)
    m2 = decrip(c2)
    assert m1 != m2

def test_encrypt_is_deterministic():
    m = 77
    c1 = crip(m)
    c2 = crip(m)
    assert c1 == c2

def test_decrypt_is_deterministic():
    c = 77
    m1 = crip(c)
    m2 = crip(c)
    assert m1 == m2

def test_message_too_large():
    m = N
    with pytest.raises(ValueError):
        crip(m)

def test_cipher_too_large():
    c = N
    with pytest.raises(ValueError):
        decrip(c)