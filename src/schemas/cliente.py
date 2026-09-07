from dataclasses import dataclass
from typing import Literal

Sexo = Literal["F", "M", "NB"]


@dataclass
class Cliente:
    id: int
    nome: str
    idade: int
    sexo: Sexo


@dataclass
class ClienteCadastro:
    nome: str
    idade: int
    sexo: Sexo


@dataclass
class ClienteEditar:
    nome: str
    idade: int
    sexo: Sexo
