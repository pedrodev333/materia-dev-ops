from src.main import *
from unittest.mock import patch

def test_root():
    assert root() == {"message": "Hello World!"}


def funcaoteste():
    with patch('random.randint', return_value=333653):
        result = funcaoteste()

    assert result == {"teste": True, "num_aleatorio": 333653}

def test_create_filme():
    filme_teste = Filme(id=1, name="Homem-Aranha 3", genre="Ação/Aventura", year=2007, rating=6.3)
    assert filme_teste == create_filme(filme_teste)

def test_update_filme_negativo():
    assert not update_filme(-5)

def test_update_filme_positivo():
    assert update_filme(10)

def test_delete_filme_negativo():
    assert update_filme(-5)

def test_delete_filme_positivo():
    assert update_filme(10)

