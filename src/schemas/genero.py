from dataclasses import dataclass


@dataclass
class Genero:
    id: int
    nome: str

@dataclass
class GeneroCadastro:
    nome: str

@dataclass
class GeneroEditar:
    nome: str