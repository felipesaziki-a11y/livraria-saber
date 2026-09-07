DROP DATABASE IF EXISTS livraria_saber;

CREATE DATABASE livraria_saber;

USE livraria_saber;

CREATE TABLE generos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(25) NOT NULL
);

INSERT INTO generos (nome) VALUES
('Ação'),
('Aventura'),
('Comédia'),
('Drama'),
('Terror'),
('Ficção Científica'),
('Romance'),
('Suspense');

CREATE TABLE livros(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(50) NOT NULL,
    genero_id INT,
    preco FLOAT NOT NULL,
    presente BOOLEAN NOT NULL DEFAULT(1),
    FOREIGN KEY (genero_id) REFERENCES generos(id)
);

ALTER TABLE livros
ADD COLUMN autor VARCHAR(50) NOT NULL
AFTER nome;

INSERT INTO livros (nome, autor, genero_id, preco) VALUE ('Metamorfose', 'Franz Kafka', 4, 35.99);

SELECT 
    livros.id,
    livros.nome,
    livros.autor,
    generos.nome AS genero,
    livros.preco,
    livros.presente
FROM livros
JOIN generos ON livros.genero_id = generos.id;

CREATE TABLE clientes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(20) NOT NULL,
    idade INT NOT NULL,
    sexo ENUM('F', 'M', 'NB') NOT NULL
);

INSERT INTO clientes (nome, idade, sexo) VALUE ('Pedro', 23, 'M')

CREATE TABLE enderecos(
    id INT PRIMARY KEY AUTO_INCREMENT,
    rua VARCHAR(20),
    bairro VARCHAR(25),
    cidade VARCHAR(32),
    estado VARCHAR(2),
    cliente_id INT,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

INSERT INTO enderecos (rua, bairro, cidade, estado, cliente_id) VALUE ('José Lanznaster', 'Coloninha', 'Gaspar', 'SC', 1);

SELECT 
    enderecos.id,
    enderecos.rua,
    enderecos.bairro,
    enderecos.cidade,
    enderecos.estado,
    clientes.nome AS 'nome do cliente'
FROM enderecos
JOIN clientes ON enderecos.cliente_id = clientes.id;
    
CREATE TABLE estoque(
    id INT PRIMARY KEY AUTO_INCREMENT,
    livro_id INT NOT NULL,
    quantidade INT NOT NULL DEFAULT 0,
    cliente_id INT,
    endereco_id INT,
    FOREIGN KEY (livro_id) REFERENCES livros(id),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (endereco_id) REFERENCES enderecos(id)
);

SELECT 
    estoque.id,
    livros.nome AS livro,
    generos.nome AS genero,
    estoque.quantidade,
    clientes.nome AS cliente,
    enderecos.cidade,
    enderecos.estado
FROM estoque
JOIN livros ON estoque.livro_id = livros.id
JOIN generos ON livros.genero_id = generos.id
LEFT JOIN clientes ON estoque.cliente_id = clientes.id
LEFT JOIN enderecos ON estoque.endereco_id = enderecos.id;

INSERT INTO estoque (livro_id, quantidade, cliente_id, endereco_id) 
VALUES (1, 15, NULL, NULL);

INSERT INTO estoque (livro_id, quantidade, cliente_id, endereco_id) 
VALUES (1, 1, 1, 1);

