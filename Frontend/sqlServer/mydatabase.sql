CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(30),
        password VARCHAR(20)
);

INSERT INTO users(id, name, password) VALUES(0, 'admin', 'cybr410pa$$'), (1, 'john', 'password123'), (2, 'jane', 'secret');
