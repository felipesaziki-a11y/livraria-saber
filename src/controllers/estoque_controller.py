from fastapi import APIRouter

from src.schemas.estoque import EstoqueCadastro, EstoqueEditar
from src.repositories import estoque_repository

router = APIRouter()


@router.get("/estoque")
def listar_estoque():
    return estoque_repository.consultar_todos()


@router.get("/estoque/{id}")
def consultar_estoque(id: int):
    return estoque_repository.consultar_por_id(id)


@router.post("/estoque")
def cadastrar_estoque(estoque: EstoqueCadastro):
    estoque_criado = estoque_repository.cadastrar(estoque)
    return estoque_criado


@router.delete("/estoque/{id}")
def apagar(id: int):
    estoque_repository.apagar(id)


@router.put("/estoque/{id}")
def editar(id: int, estoque: EstoqueEditar):
    estoque_editado = estoque_repository.editar(id, estoque)
    return estoque_editado
