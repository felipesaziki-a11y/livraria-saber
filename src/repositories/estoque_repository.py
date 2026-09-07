from typing import List, Optional

from src.database.conexao import conectar
from src.schemas.estoque import Estoque, EstoqueCadastro


def consultar_todos() -> List[Estoque]:
    with conectar() as conexao:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute(
                "SELECT id, livro_id, quantidade, cliente_id, endereco_id FROM estoque"
            )
            registros = cursor.fetchall()

    itens = []
    for registro in registros:
        item = Estoque(
            id=registro["id"],
            livro_id=registro["livro_id"],
            quantidade=registro["quantidade"],
            cliente_id=registro["cliente_id"],
            endereco_id=registro["endereco_id"],
        )
        itens.append(item)
    return itens


def cadastrar(estoque: EstoqueCadastro) -> Estoque:
    sql = "INSERT INTO estoque (livro_id, quantidade, cliente_id, endereco_id) VALUES (%s, %s, %s, %s)"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                sql,
                (estoque.livro_id, estoque.quantidade, estoque.cliente_id, estoque.endereco_id),
            )
            novo_id = cursor.lastrowid
            conexao.commit()
    return Estoque(
        id=novo_id,
        livro_id=estoque.livro_id,
        quantidade=estoque.quantidade,
        cliente_id=estoque.cliente_id,
        endereco_id=estoque.endereco_id,
    )


def apagar(id: int):
    sql = "DELETE FROM estoque WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id,))
            conexao.commit()


def consultar_por_id(id: int) -> Optional[Estoque]:
    sql = "SELECT id, livro_id, quantidade, cliente_id, endereco_id FROM estoque WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()

    if registro:
        return Estoque(
            id=registro["id"],
            livro_id=registro["livro_id"],
            quantidade=registro["quantidade"],
            cliente_id=registro["cliente_id"],
            endereco_id=registro["endereco_id"],
        )
    return None


def editar(id: int, estoque: EstoqueCadastro) -> Optional[Estoque]:
    sql = "UPDATE estoque SET livro_id = %s, quantidade = %s, cliente_id = %s, endereco_id = %s WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                sql,
                (estoque.livro_id, estoque.quantidade, estoque.cliente_id, estoque.endereco_id, id),
            )
            conexao.commit()
    return Estoque(
        id=id,
        livro_id=estoque.livro_id,
        quantidade=estoque.quantidade,
        cliente_id=estoque.cliente_id,
        endereco_id=estoque.endereco_id,
    )
