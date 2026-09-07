from typing import List, Optional

from src.database.conexao import conectar
from src.schemas.genero import Genero, GeneroCadastro

def consultar_todos() -> List[Genero]:
    with conectar() as conexao:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, nome FROM generos")
            registros = cursor.fetchall()

    generos = []
    for registro in registros:
        genero = Genero(id=registro["id"], nome=registro["nome"])
        generos.append(genero)
    return generos

def cadastrar(genero: GeneroCadastro):
    sql = "INSERT INTO generos (nome) VALUES (%s)"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (genero.nome,))
            novo_id = cursor.lastrowid
            conexao.commit()
    return genero(id=novo_id, nome=genero.nome)


def apagar(id: int):
    sql = "DELETE FROM generos WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id,))
            conexao.commit()

def consultar_por_id(id: int) -> Optional[Genero]:
    sql = "SELECT id, nome FROM generos WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()

    if registro:
        return Genero(id=registro["id"], nome=registro["nome"])
    return None

def editar(id: int, genero: GeneroCadastro) -> Optional[Genero]:
    sql = "UPDATE generos SET nome = %s WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (genero.nome, id))
            conexao.commit()
    return genero(id=id, nome=genero.nome)