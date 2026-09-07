from dataclasses import dataclass
from typing import Optional


@dataclass
class Estoque:
    id: int
    livro_id: int
    quantidade: int
    cliente_id: Optional[int]
    endereco_id: Optional[int]


@dataclass
class EstoqueCadastro:
    livro_id: int
    quantidade: int
    cliente_id: Optional[int] = None
    endereco_id: Optional[int] = None


@dataclass
class EstoqueEditar:
    livro_id: int
    quantidade: int
    cliente_id: Optional[int] = None
    endereco_id: Optional[int] = None
