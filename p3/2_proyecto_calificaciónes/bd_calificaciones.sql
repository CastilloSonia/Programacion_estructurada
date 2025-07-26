CREATE TABLE IF NOT EXISTS alumnos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    calificacion1 DECIMAL(5,2) NOT NULL,
    calificacion2 DECIMAL(5,2) NOT NULL,
    calificacion3 DECIMAL(5,2) NOT NULL
);