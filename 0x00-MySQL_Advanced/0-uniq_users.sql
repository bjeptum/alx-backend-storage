-- Create table users with unique attributes
CREATE DATABASE if not exists users unique_id(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	);
