CREATE TABLE USUARIO(
	ID SERIAL PRIMARY KEY,
	EMAIL VARCHAR(100) NOT NULL,
	SENHA VARCHAR(50) NOT NULL,
	TOKEN VARCHAR(50),
	EXPIRATION timestamp,
	NOME VARCHAR(500) NOT NULL,
	DTNASC DATE NOT NULL,
	CEP VARCHAR(10) NOT NULL,
	DIAS int default 30
);

create unique index on usuario (email);

CREATE TABLE DOENCA(
	ID serial PRIMARY KEY,
	NOME VARCHAR(30),
	FOCO int NOT NULL DEFAULT 0
);

INSERT INTO DOENCA (NOME) VALUES ('Corona Vírus');
INSERT INTO DOENCA (NOME) VALUES ('Dengue');
INSERT INTO DOENCA (NOME) VALUES ('Zika');
INSERT INTO DOENCA (NOME, FOCO) VALUES ('Foco Dengue', 1);

CREATE TABLE BAIRRO (
	ID serial PRIMARY KEY,
	NOME VARCHAR(500),
	CEP_INICIAL VARCHAR(10),
	CEP_FINAL VARCHAR(10)
);


CREATE TABLE DENUNCIA(
    ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    CONTROL VARCHAR(50),
    TIPO INT NOT NULL,
    CEP VARCHAR(50) NOT NULL,
    OBSERVACAO VARCHAR(500),
    COORDENADA VARCHAR(50)
);

insert into bairro(id, nome, cep_inicial, cep_final) values (1, 'geral', '1', '99999999');


CREATE TABLE CASO(
	ID serial PRIMARY KEY,
	DOENCA INT NOT NULL,
	CONFIRMADO int NOT NULL DEFAULT 0,
	DESCARTADO int NOT NULL DEFAULT 0,
	CURADO int NOT NULL DEFAULT 0,
	SUSPEITO int NOT NULL DEFAULT 0,
	OBITO int NOT NULL DEFAULT 0,
	OBSERVACAO VARCHAR(500),
	LATITUDE NUMERIC,
	LONGITUDE NUMERIC,
	BAIRRO INT NOT NULL,
	DENUNCIA INT,
	FOREIGN KEY (DOENCA) REFERENCES DOENCA(ID),
	FOREIGN KEY (BAIRRO) REFERENCES BAIRRO(ID),
	FOREIGN KEY (DENUNCIA) REFERENCES DENUNCIA(ID)
);