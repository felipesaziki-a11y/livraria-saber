from typing import List, Optional

from src.database.conexao import conectar
from src.schemas.categoria import Categoria, CategoriaCadastro

def consultar_todos() -> List[Categoria]:
    with conectar() as conexao:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, nome FROM categorias")
            registros = cursor.fetchall()

    categorias = []
    for registro in registros:
        categoria = Categoria(id=registro["id"], nome=registro["nome"])
        categorias.append(categoria)
    return categorias

def cadastrar(categoria: CategoriaCadastro):
    sql = "INSERT INTO categorias (nome) VALUES (%s)"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (categoria.nome,))
            novo_id = cursor.lastrowid
            conexao.commit()
    return Categoria(id=novo_id, nome=categoria.nome)


def apagar(id: int):
    sql = "DELETE FROM categorias WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id,))
            conexao.commit()

def consultar_por_id(id: int) -> Optional[Categoria]:
    sql = "SELECT id, nome FROM categorias WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()

    if registro:
        return Categoria(id=registro["id"], nome=registro["nome"])
    return None

def editar(id: int, categoria: CategoriaCadastro) -> Optional[Categoria]:
    sql = "UPDATE categorias SET nome = %s WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (categoria.nome, id))
            conexao.commit()
    return Categoria(id=id, nome=categoria.nome)