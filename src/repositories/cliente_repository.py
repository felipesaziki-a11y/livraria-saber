from typing import List, Optional

from src.database.conexao import conectar
from src.schemas.cliente import Cliente, ClienteCadastro


def consultar_todos() -> List[Cliente]:
    with conectar() as conexao:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, nome, idade, sexo FROM clientes")
            registros = cursor.fetchall()

    clientes = []
    for registro in registros:
        cliente = Cliente(
            id=registro["id"],
            nome=registro["nome"],
            idade=registro["idade"],
            sexo=registro["sexo"],
        )
        clientes.append(cliente)
    return clientes


def cadastrar(cliente: ClienteCadastro) -> Cliente:
    sql = "INSERT INTO clientes (nome, idade, sexo) VALUES (%s, %s, %s)"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (cliente.nome, cliente.idade, cliente.sexo))
            novo_id = cursor.lastrowid
            conexao.commit()
    return Cliente(id=novo_id, nome=cliente.nome, idade=cliente.idade, sexo=cliente.sexo)


def apagar(id: int):
    sql = "DELETE FROM clientes WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id,))
            conexao.commit()


def consultar_por_id(id: int) -> Optional[Cliente]:
    sql = "SELECT id, nome, idade, sexo FROM clientes WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()

    if registro:
        return Cliente(
            id=registro["id"],
            nome=registro["nome"],
            idade=registro["idade"],
            sexo=registro["sexo"],
        )
    return None


def editar(id: int, cliente: ClienteCadastro) -> Optional[Cliente]:
    sql = "UPDATE clientes SET nome = %s, idade = %s, sexo = %s WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (cliente.nome, cliente.idade, cliente.sexo, id))
            conexao.commit()
    return Cliente(id=id, nome=cliente.nome, idade=cliente.idade, sexo=cliente.sexo)
