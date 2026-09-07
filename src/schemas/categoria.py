from dataclasses import dataclass


@dataclass
class Categoria:
    id: int
    nome: str

@dataclass
class CategoriaCadastro:
    nome: str

@dataclass
class CategoriaEditar:
    nome: str