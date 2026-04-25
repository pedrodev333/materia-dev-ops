import pytest

from src.main import *
from unittest.mock import patch


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World!"}

@pytest.mark.asyncio
async def test_funcaoteste():
    with patch('random.randint', return_value=333653):
        result = await funcaoteste()

    assert result == {"teste": True, "num_aleatorio": 333653}

@pytest.mark.asyncio
async def test_create_filme():
    filme_teste = Filme(id=1, name="Homem-Aranha 3", genre="Ação/Aventura", year=2007, rating=6.3)
    result = await create_filme(filme_teste)
    assert filme_teste == result

@pytest.mark.asyncio
async def test_update_filme_negativo():
    result = await update_filme(-5)
    assert not result

@pytest.mark.asyncio
async def test_update_filme_positivo():
    result = await update_filme(10)
    assert result

@pytest.mark.asyncio
async def test_delete_filme_negativo():
    result = await delete_filme(-5)
    assert not result

@pytest.mark.asyncio
async def test_delete_filme_positivo():
    result = await delete_filme(10)
    assert result

