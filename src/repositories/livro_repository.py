from typing import List, Optional

from src.database.conexao import conectar
from src.schemas.livro import Livro, LivroCadastro


def consultar_todos() -> List[Livro]:
    with conectar() as conexao:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute(
                "SELECT id, nome, autor, genero_id, preco, presente FROM livros"
            )
            registros = cursor.fetchall()

    livros = []
    for registro in registros:
        livro = Livro(
            id=registro["id"],
            nome=registro["nome"],
            autor=registro["autor"],
            genero_id=registro["genero_id"],
            preco=registro["preco"],
            presente=bool(registro["presente"]),
        )
        livros.append(livro)
    return livros


def cadastrar(livro: LivroCadastro) -> Livro:
    sql = "INSERT INTO livros (nome, autor, genero_id, preco, presente) VALUES (%s, %s, %s, %s, %s)"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                sql, (livro.nome, livro.autor, livro.genero_id, livro.preco, livro.presente)
            )
            novo_id = cursor.lastrowid
            conexao.commit()
    return Livro(
        id=novo_id,
        nome=livro.nome,
        autor=livro.autor,
        genero_id=livro.genero_id,
        preco=livro.preco,
        presente=livro.presente,
    )


def apagar(id: int):
    sql = "DELETE FROM livros WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id,))
            conexao.commit()


def consultar_por_id(id: int) -> Optional[Livro]:
    sql = "SELECT id, nome, autor, genero_id, preco, presente FROM livros WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()

    if registro:
        return Livro(
            id=registro["id"],
            nome=registro["nome"],
            autor=registro["autor"],
            genero_id=registro["genero_id"],
            preco=registro["preco"],
            presente=bool(registro["presente"]),
        )
    return None


def editar(id: int, livro: LivroCadastro) -> Optional[Livro]:
    sql = "UPDATE livros SET nome = %s, autor = %s, genero_id = %s, preco = %s, presente = %s WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                sql,
                (livro.nome, livro.autor, livro.genero_id, livro.preco, livro.presente, id),
            )
            conexao.commit()
    return Livro(
        id=id,
        nome=livro.nome,
        autor=livro.autor,
        genero_id=livro.genero_id,
        preco=livro.preco,
        presente=livro.presente,
    )
