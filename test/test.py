import pytest

from src.main import *
from unittest.mock import patch


@pytest.mark.asyncio
def test_root():
    result = root()
    yield result
    assert result == {"message": "Hello World!"}

@pytest.mark.asyncio
def test_funcaoteste():
    with patch('random.randint', return_value=333653):
        result = funcaoteste()
        yield result

    assert result == {"teste": True, "num_aleatorio": 333653}

@pytest.mark.asyncio
def test_create_filme():
    filme_teste = Filme(id=1, name="Homem-Aranha 3", genre="Ação/Aventura", year=2007, rating=6.3)
    result = create_filme(filme_teste)
    yield result
    assert filme_teste == result

@pytest.mark.asyncio
def test_update_filme_negativo():
    result = update_filme(-5)
    yield result
    assert not result

@pytest.mark.asyncio
def test_update_filme_positivo():
    result = update_filme(10)
    yield result
    assert result

@pytest.mark.asyncio
def test_delete_filme_negativo():
    result = delete_filme(-5)
    yield result
    assert not result

@pytest.mark.asyncio
def test_delete_filme_positivo():
    result = delete_filme(10)
    yield result
    assert result

