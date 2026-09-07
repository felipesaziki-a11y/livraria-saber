from fastapi import APIRouter

from src.schemas.livro import LivroCadastro, LivroEditar
from src.repositories import livro_repository

router = APIRouter()


@router.get("/livros")
def listar_livros():
    return livro_repository.consultar_todos()


@router.get("/livros/{id}")
def consultar_livro(id: int):
    return livro_repository.consultar_por_id(id)


@router.post("/livros")
def cadastrar_livro(livro: LivroCadastro):
    livro_criado = livro_repository.cadastrar(livro)
    return livro_criado


@router.delete("/livros/{id}")
def apagar(id: int):
    livro_repository.apagar(id)


@router.put("/livros/{id}")
def editar(id: int, livro: LivroEditar):
    livro_editado = livro_repository.editar(id, livro)
    return livro_editado
