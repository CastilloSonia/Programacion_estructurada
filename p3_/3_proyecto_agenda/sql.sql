CREATE DATABASE
IF NOT EXISTS bd_agenda;

USE bd_agenda;

CREATE TABLE
IF NOT EXISTS contactos
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR
(50) NOT NULL,
    telefono VARCHAR
(15) NOT NULL,
    email VARCHAR
(50),
    direccion VARCHAR
(100),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);