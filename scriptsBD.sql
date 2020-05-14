CREATE DATABASE FOCUSTRACKER;

CREATE TABLE usuario(
	ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
	EMAIL varchar(100) not null,
	senha varchar(50) not null,
	token varchar(20),
	expiration datetime
);

ALTER TABLE `usuario` ADD UNIQUE INDEX(`EMAIL`);