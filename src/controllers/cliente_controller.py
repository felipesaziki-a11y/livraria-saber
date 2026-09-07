from fastapi import APIRouter

from src.schemas.cliente import ClienteCadastro, ClienteEditar
from src.repositories import cliente_repository

router = APIRouter()


@router.get("/clientes")
def listar_clientes():
    return cliente_repository.consultar_todos()


@router.get("/clientes/{id}")
def consultar_cliente(id: int):
    return cliente_repository.consultar_por_id(id)


@router.post("/clientes")
def cadastrar_cliente(cliente: ClienteCadastro):
    cliente_criado = cliente_repository.cadastrar(cliente)
    return cliente_criado


@router.delete("/clientes/{id}")
def apagar(id: int):
    cliente_repository.apagar(id)


@router.put("/clientes/{id}")
def editar(id: int, cliente: ClienteEditar):
    cliente_editado = cliente_repository.editar(id, cliente)
    return cliente_editado
