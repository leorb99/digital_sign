import pytest
from src.signer import signer
from src.validator import validator


def test_validator_valid_signature():
    """Verifica se a assinatura válida é aceita."""
    mensagem, assinatura = signer("Mensagem válida")
    assert validator(mensagem, assinatura), "Assinatura válida foi rejeitada"


def test_validator_invalid_message():
    """Mensagem adulterada deve ser rejeitada."""
    mensagem, assinatura = signer("Mensagem original")
    assert not validator("Mensagem adulterada", assinatura), "Mensagem adulterada foi aceita!"


def test_validator_invalid_signature():
    """Assinatura modificada deve ser rejeitada."""
    mensagem, assinatura = signer("Teste")
    assinatura_errada = hex((int(assinatura, 16) + 1) % 65536)
    assert not validator(mensagem, assinatura_errada), "Assinatura adulterada foi aceita!"


def test_validator_wrong_type_signature():
    """Deve lidar com assinatura em formato inválido."""
    mensagem = "Teste"
    assinatura_invalida = "abcdef"  # sem prefixo 0x
    with pytest.raises(ValueError):
        validator(mensagem, assinatura_invalida)
