-- Este es otro comentario
/* Este es ooooootro comentario
	El comentario continua */

-- Primera forma de crear una base de datos
CREATE SCHEMA tecsup;
DROP SCHEMA tecsup;

-- Otra forma de crear una base de datos
CREATE DATABASE tecsup;
DROP DATABASE tecsup;

-- Crear una tabla
CREATE TABLE productos (
	productoId INT AUTO_INCREMENT PRIMARY KEY,
    productoNombre VARCHAR(255) NOT NULL,
    productoDescripcion VARCHAR(255) NOT NULL,
    productoPrecio FLOAT NOT NULL,
    estado BOOLEAN,
    created_at DATETIME
);

-- Visualizar todos los datos de una tabla
SELECT*FROM tecsup.productos;

-- Insertar valores en una tabla
INSERT INTO tecsup.productos (productoNombre, productoDescripcion, productoPrecio, estado, created_at)
VALUES ('Zapatos de vestir', 'Zapato para damas', 349.99, TRUE,'2022-08-26 20:20:00');

-- Where
SELECT*FROM tecsup.productos WHERE estado = TRUE;
SELECT*FROM tecsup.productos WHERE estado = FALSE;
SELECT * FROM tecsup.productos WHERE created_at >= '2022-08-26 20:10:00';
SELECT productoNombre FROM tecsup.productos WHERE created_at >= '2022-08-26 20:10:00';