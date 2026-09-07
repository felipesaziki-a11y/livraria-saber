from dataclasses import dataclass


@dataclass
class Livro:
    id: int
    nome: str
    autor: str
    genero_id: int
    preco: float
    presente: bool


@dataclass
class LivroCadastro:
    nome: str
    autor: str
    genero_id: int
    preco: float
    presente: bool = True


@dataclass
class LivroEditar:
    nome: str
    autor: str
    genero_id: int
    preco: float
    presente: bool
