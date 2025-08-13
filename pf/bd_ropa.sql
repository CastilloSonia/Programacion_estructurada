-- 🛍️ Base de datos para tienda de ropa

CREATE DATABASE
IF NOT EXISTS tienda_ropa;
USE tienda_ropa;

-- 👥 Tabla Clientes
CREATE TABLE
IF NOT EXISTS clientes
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR
(50) NOT NULL,
    apellido VARCHAR
(50) NOT NULL,
    email VARCHAR
(100) UNIQUE,
    telefono VARCHAR
(20),
    direccion VARCHAR
(100),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 👕 Tabla Productos
CREATE TABLE
IF NOT EXISTS productos
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR
(100) NOT NULL,
    descripcion TEXT,
    categoria ENUM
('camisas', 'pantalones', 'vestidos', 'zapatos', 'accesorios') NOT NULL,
    talla ENUM
('XS', 'S', 'M', 'L', 'XL', 'XXL', 'Única') NOT NULL,
    color VARCHAR
(30) NOT NULL,
    precio DECIMAL
(10, 2) NOT NULL,
    stock INT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 💰 Tabla Ventas
CREATE TABLE
IF NOT EXISTS ventas
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    fecha_venta TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total DECIMAL
(10, 2) NOT NULL,
    metodo_pago ENUM
('efectivo', 'tarjeta', 'transferencia') NOT NULL,
    FOREIGN KEY
(cliente_id) REFERENCES clientes
(id)
);

-- 📝 Tabla Detalle_Venta
CREATE TABLE
IF NOT EXISTS detalle_venta
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    venta_id INT NOT NULL,
    producto_id INT NOT NULL,
    cantidad INT NOT NULL,
    precio_unitario DECIMAL
(10, 2) NOT NULL,
    FOREIGN KEY
(venta_id) REFERENCES ventas
(id),
    FOREIGN KEY
(producto_id) REFERENCES productos
(id)
);

-- 📦 Tabla Inventario
CREATE TABLE
IF NOT EXISTS inventario
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    producto_id INT NOT NULL,
    tipo ENUM
('entrada', 'salida', 'ajuste') NOT NULL,
    cantidad INT NOT NULL,
    motivo VARCHAR
(100) NOT NULL,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario VARCHAR
(50) NOT NULL,
    FOREIGN KEY
(producto_id) REFERENCES productos
(id)
);

-- 👤 Tabla Usuarios (NUEVA - Sistema de autenticación)
CREATE TABLE
IF NOT EXISTS usuarios
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR
(50) UNIQUE NOT NULL,
    password VARCHAR
(100) NOT NULL,
    nombre VARCHAR
(100) NOT NULL,
    rol ENUM
('admin', 'vendedor') DEFAULT 'vendedor',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 🔐 Datos iniciales para usuarios
INSERT IGNORE
INTO usuarios
(username, password, nombre, rol) VALUES
('admin', 'admin123', 'Administrador Principal', 'admin'),
('vendedor1', 'ventas123', 'Vendedor Ejemplo', 'vendedor');

-- 📌 Índices para mejorar rendimiento (NUEVOS)
CREATE INDEX idx_productos_categoria ON productos(categoria);
CREATE INDEX idx_ventas_fecha ON ventas(fecha_venta);
CREATE INDEX idx_inventario_producto ON inventario(producto_id);

-- 🔄 Triggers para gestión de stock (NUEVOS)
DELIMITER //
CREATE TRIGGER after_venta_insert
AFTER
INSERT ON
detalle_venta
FOR
EACH
ROW
BEGIN
    UPDATE productos SET stock = stock - NEW.cantidad WHERE id = NEW.producto_id;
    INSERT INTO inventario
        (producto_id, tipo, cantidad, motivo, usuario)
    VALUES
        (NEW.producto_id, 'salida', NEW.cantidad, 'Venta registrada', 'sistema');
END
//

CREATE TRIGGER after_inventario_insert
AFTER
INSERT ON
inventario
FOR
EACH
ROW
BEGIN
    IF NEW.tipo = 'entrada' THEN
    UPDATE productos SET stock = stock + NEW.cantidad WHERE id = NEW.producto_id;
    ELSEIF NEW.tipo = 'salida' THEN
    UPDATE productos SET stock = stock - NEW.cantidad WHERE id = NEW.producto_id;
END
IF;
END//

DELIMITER ;