from fastapi import APIRouter

from src.schemas.genero import GeneroCadastro, GeneroEditar
from src.repositories import genero_repository

router = APIRouter()

@router.get("/generos")
def listar_generos():
    return genero_repository.consultar_todos()

@router.post("/generos")
def cadastrar_categoria(categoria: GeneroCadastro):
    categoria_criada = genero_repository.cadastrar(categoria)
    return categoria_criada

@router.delete("/generos/{id}")
def apagar(id: int):
    genero_repository.apagar(id)

@router.put("/generos/{id}")
def editar(id: int, categoria: GeneroEditar):
    categoria_editada = genero_repository.editar(id, categoria)
    return categoria_editada