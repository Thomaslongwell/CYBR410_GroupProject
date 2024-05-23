USE mydatabase;

CREATE TABLE users (
	id INT,
	name VARCHAR(255),
	password VARCHAR(255)
);

INSERT INTO users(id, name, password) VALUES(1, 'john', 'password123'), (2, 'jane', 'secret');


