from fastapi import APIRouter

from src.schemas.categoria import CategoriaCadastro, CategoriaEditar
from src.repositories import categoria_repository

router = APIRouter()

@router.get("/categorias")
def listar_categorias():
    return categoria_repository.consultar_todos()

@router.post("/categorias")
def cadastrar_categoria(categoria: CategoriaCadastro):
    categoria_criada = categoria_repository.cadastrar(categoria)
    return categoria_criada

@router.delete("/categorias/{id}")
def apagar(id: int):
    categoria_repository.apagar(id)

@router.put("/categorias/{id}")
def editar(id: int, categoria: CategoriaEditar):
    categoria_editada = categoria_repository.editar(id, categoria)
    return categoria_editada