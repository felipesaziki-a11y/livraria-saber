from fastapi import APIRouter

from src.schemas.endereco import EnderecoCadastro, EnderecoEditar
from src.repositories import endereco_repository

router = APIRouter()


@router.get("/enderecos")
def listar_enderecos():
    return endereco_repository.consultar_todos()


@router.get("/enderecos/{id}")
def consultar_endereco(id: int):
    return endereco_repository.consultar_por_id(id)


@router.post("/enderecos")
def cadastrar_endereco(endereco: EnderecoCadastro):
    endereco_criado = endereco_repository.cadastrar(endereco)
    return endereco_criado


@router.delete("/enderecos/{id}")
def apagar(id: int):
    endereco_repository.apagar(id)


@router.put("/enderecos/{id}")
def editar(id: int, endereco: EnderecoEditar):
    endereco_editado = endereco_repository.editar(id, endereco)
    return endereco_editado