import pytest

from src.main import *

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

@pytest.mark.asyncio
async def test_validar_filme():
    filme_teste = Filme(id=3, name="Matrix", genre="Ação/Ficção científica", year=1999, rating=8.7)
    result = await validar_filme(filme_teste)

    assert result
