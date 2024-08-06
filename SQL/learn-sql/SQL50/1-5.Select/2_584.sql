-- 584 https://leetcode.com/problems/find-customer-referee/
-- Enunciado
/*
Escriba una consulta SQL para reportar los nombres de los clientes que no son referidos por el cliente con id = 2.
Devuelva la tabla de resultados en cualquier orden.
El formato del resultado de la consulta está en el siguiente ejemplo.
*/
-- CREATE TABLE
CREATE TABLE IF NOT EXISTS Customer (id INT, name VARCHAR(25), referee_id INT);
TRUNCATE TABLE Customer;
INSERT INTO Customer (id, name, referee_id) VALUES ('1', 'Will', 'None');
INSERT INTO Customer (id, name, referee_id) VALUES ('2', 'Jane', 'None');
INSERT INTO Customer (id, name, referee_id) VALUES ('3', 'Alex', '2');
INSERT INTO Customer (id, name, referee_id) VALUES ('4', 'Bill', 'None');
INSERT INTO Customer (id, name, referee_id) VALUES ('5', 'Zack', '1');
INSERT INTO Customer (id, name, referee_id) VALUES ('6', 'Mark', '2');

--------------
-- SOLUCIÓN --
--------------

-- Ejercicio: Query para escribir los nombres (name) de los Customer que no están referidos por el referee_id 2
SELECT `name` FROM Customer WHERE referee_id != 2;
-- Usando array:
SELECT `name` FROM Customer WHERE referee_id NOT IN (2);
-- LeetCode:
SELECT `name` FROM Customer WHERE referee_id != 2 OR referee_id IS NULL;