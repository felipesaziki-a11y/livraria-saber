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
    sobrenome VARCHAR(20) NOT NULL,
);

