import pytest
import tempfile
from src.signer import signer
from src.rsa import N


def test_signer_with_text():
    """Verifica se a assinatura é gerada corretamente a partir de texto direto."""
    mensagem, assinatura = signer("Teste simples")
    assert isinstance(mensagem, str)
    assert isinstance(assinatura, str)
    assert assinatura.startswith("0x"), "Assinatura deve estar em formato hexadecimal"
    valor_assinatura = int(assinatura, 16)
    assert 0 <= valor_assinatura < N, "Assinatura fora do intervalo RSA"


def test_signer_with_file():
    """Verifica se a assinatura é gerada corretamente lendo de arquivo."""
    with tempfile.NamedTemporaryFile("w+", delete=False, encoding="utf-8") as f:
        f.write("Conteúdo do arquivo")
        caminho = f.name

    mensagem, assinatura = signer(caminho)
    assert mensagem == "Conteúdo do arquivo"
    assert assinatura.startswith("0x")
    assert isinstance(assinatura, str)


def test_signer_determinism():
    """Mesma mensagem deve gerar mesma assinatura."""
    _, a1 = signer("mensagem fixa")
    _, a2 = signer("mensagem fixa")
    assert a1 == a2, "Assinatura variou para mesma entrada"
