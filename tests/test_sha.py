from src.sha import sha

def test_sha_deterministic():
    h1 = sha("mensagem de teste")
    h2 = sha("mensagem de teste")
    assert h1 == h2

def test_sha_avalanche_effect():
    h1 = sha("abc")
    h2 = sha("abd")
    assert h1 != h2

def test_sha_empty_string():
    h = sha("")
    assert isinstance(int(h, 16), int), "Hash deve ser um inteiro"
    assert 0 <= int(h, 16) < 2**16, "Hash fora do intervalo de 16 bits"

def test_sha_output_type_and_range():
    h = sha("qualquer coisa")
    assert isinstance(int(h, 16), int), "SHA deve retornar um número inteiro"
    assert 0 <= int(h, 16) < 2**16, "SHA deve estar limitado a 16 bits"

def test_sha_similar_length_hashes():
    h1 = sha("abc")
    h2 = sha("123")
    assert len(h1) == len(h2)

def test_sha_non_ascii_characters():
    h = sha("Olá mundo 🌎")
    assert isinstance(int(h, 16), int)
    assert 0 <= int(h, 16) < 2**16

def test_sha_long_message():
    texto_longo = (
        "A" * 80 
    )
    h1 = sha(texto_longo)
    h2 = sha(texto_longo)
    
    assert h1 == h2, "Hash não determinístico para mensagens longas"
    assert isinstance(int(h1, 16), int), "Hash deve retornar um inteiro"
    assert 0 <= int(h1, 16) < 2**16, "Hash fora do intervalo de 16 bits para mensagens longas"

def test_sha_increasing_length():
    base = "X" * 10
    results = []
    for i in range(10, 100, 10):
        h = sha(base * (i // 10))
        results.append(int(h, 16))
    assert len(set(results)) > 1, "SHA não muda para mensagens de tamanhos diferentes"
