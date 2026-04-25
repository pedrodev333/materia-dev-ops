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

@app.get("/helloworld")
async def root():
    return {"message": "Hello World!"}

@app.get("/funcaoteste")
async def funcaoteste():
    return {"teste": True, "num_aleatorio": random.randint(0,57000)}

@app.post("/filmes/cadastro")
async def create_filme(filme: Filme):
    return filme

@app.put("/filmes/update/{id_filme}")
async def update_filme(id_filme: int):
    return id_filme > 0

@app.delete("/filmes/delete/{id_filme}")
async def delete_filme(id_filme: int):
    return id_filme > 0