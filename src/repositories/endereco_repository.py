from typing import List, Optional

from src.database.conexao import conectar
from src.schemas.endereco import Endereco, EnderecoCadastro


def consultar_todos() -> List[Endereco]:
    with conectar() as conexao:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute("SELECT id, rua, bairro, cidade, estado, cliente_id FROM enderecos")
            registros = cursor.fetchall()

    enderecos = []
    for registro in registros:
        endereco = endereco(
            id=registro["id"],
            rua=registro["rua"],
            bairro=registro["bairro"],
            cidade=registro["cidade"],
            estado=registro["estado"],
            cliente_id=registro["cliente"]
        )
        enderecos.append(endereco)
    return enderecos


def cadastrar(endereco: EnderecoCadastro) -> Endereco:
    sql = "ERT INTO enderecos (rua, bairro, cbairro, estado, cliente_id) VALUE (%s, %s, %s, %s, %s)"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (endereco.rua, endereco.bairro, endereco.cidade, endereco.estado, endereco.cliente_id))
            novo_id = cursor.lastrowid
            conexao.commit()
    return endereco(id=novo_id, rua=endereco.rua, bairro=endereco.bairro, cidade=endereco.cidade)


def apagar(id: int):
    sql = "DELETE FROM enderecos WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (id,))
            conexao.commit()


def consultar_por_id(id: int) -> Optional[Endereco]:
    sql = "SELECT id, rua, bairro, cidade, estado, cliente_id FROM enderecos WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor(dictionary=True) as cursor:
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()

    if registro:
        return Endereco(
            id=registro["id"],
            rua=registro["rua"],
            bairro=registro["bairro"],
            cidade=registro["cidade"],
            estado=registro["estado"],
            cliente_id=registro["cliente"]
        )
    return None


def editar(id: int, endereco: EnderecoCadastro) -> Optional[Endereco]:
    sql = "UPDATE enderecos SET rua = %s, bairro = %s, cidade = %s, estado = %s, cliente_id = %s WHERE id = %s;"
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(sql, (endereco.rua, endereco.bairro, endereco.cidade, id))
            conexao.commit()
    return endereco(id=id, rua=endereco.rua, bairro=endereco.bairro, cidade=endereco.cidade, estado=endereco.estado, cliente_id=endereco.cliente_id)
