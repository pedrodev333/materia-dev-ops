import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Filme(BaseModel):
    id: int
    name: str
    genre: str
    year: int
    rating: float

@app.post("/filmes/cadastro")
async def create_filme(filme: Filme):
    return filme

@app.put("/filmes/update/{id_filme}")
async def update_filme(id_filme: int):
    return id_filme > 0

@app.delete("/filmes/delete/{id_filme}")
async def delete_filme(id_filme: int):
    return id_filme > 0

@app.post("/filmes/validar")
async def validar_filme(filme: Filme):
    return filme.year > 1888 and 0 <= filme.rating <= 10 and len(filme.name.strip()) > 0

