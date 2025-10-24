import pytest
from src.signer import signer
from src.validator import validator

def test_validator_valid_signature():
    m, signature = signer("m válida")
    assert validator(m, signature)

def test_validator_invalid_message():
    m, signature = signer("m original")
    assert not validator("m adulterada", signature)

def test_validator_invalid_signature():
    m, signature = signer("Teste")
    wrong_signature = hex((int(signature, 16) + 1) % 65536)
    assert not validator(m, wrong_signature)

def test_validator_wrong_type_signature():
    m = "Teste"
    signature_invalida = "abcdef"
    with pytest.raises(ValueError):
        validator(m, signature_invalida)
