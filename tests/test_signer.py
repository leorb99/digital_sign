import pytest
import tempfile
from src.signer import signer
from src.rsa import N

def test_signer_with_text():
    m, signature = signer("Teste simples")
    assert isinstance(m, str)
    assert isinstance(signature, str)
    assert signature.startswith("0x")
    valor_signature = int(signature, 16)
    assert 0 <= valor_signature < N, "signature fora do intervalo RSA"

def test_signer_with_file():
    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as f:
        f.write("Conteúdo do arquivo")
        path = f.name
    m, signature = signer(path)
    assert m == "Conteúdo do arquivo"
    assert signature.startswith("0x")
    assert isinstance(signature, str)

def test_signer_determinism():
    _, a1 = signer("m fixa")
    _, a2 = signer("m fixa")
    assert a1 == a2
