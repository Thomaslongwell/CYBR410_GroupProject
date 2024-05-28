CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        password VARCHAR(255)
);

INSERT INTO users(id, name, password) VALUES(1, 'john', 'password123'), (2, 'jane', 'secret');
