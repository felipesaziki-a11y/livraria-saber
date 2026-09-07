# id INT PRIMARY KEY AUTO_INCREMENT,
#     rua VARCHAR(20),
#     bairro VARCHAR(25),
#     cidade VARCHAR(32),
#     estado VARCHAR(2),
#     cliente_id INT,
#     FOREIGN KEY (cliente_id) REFERENCES clientes(id)

from dataclasses import dataclass
from typing import Optional


@dataclass
class Endereco:
    id: int
    rua: str
    bairro: str
    cidade: str
    estado: str
    cliente_id: Optional[int]

@dataclass
class EnderecoCadastro:
    rua: str
    bairro: str
    cidade: str
    estado: str
    cliente_id: Optional[int]

@dataclass
class EnderecoEditar:
    rua: str
    bairro: str
    cidade: str
    estado: str
    cliente_id: Optional[int]