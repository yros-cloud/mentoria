from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="DevOps Mentoria API", version="1.0.0")

class Item(BaseModel):
    name: str
    description: str = None
    price: float

fake_db: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Aplicação FastAPI para Mentoria de DevOps"}

@app.get("/items")
def list_items():
    return fake_db

@app.post("/items")
def create_item(item: Item):
    fake_db.append(item)
    return {"message": "Item adicionado com sucesso", "item": item}
