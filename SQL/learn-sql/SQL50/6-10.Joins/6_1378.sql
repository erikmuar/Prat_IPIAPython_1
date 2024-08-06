-- Active: 1686067902666@@127.0.0.1@3306@leetcode
-- 1378. Replace Employee ID With The Unique Identifier
-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

/*
Escriba una consulta SQL para mostrar el ID único de cada usuario, Si un usuario no tiene un ID único reemplace simplemente muestre null.

Devuelve la tabla de resultados en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/

CREATE TABLE IF NOT EXISTS Employees (id int, `name` VARCHAR(20));
CREATE TABLE IF NOT EXISTS EmployeeUNI (id INT, unique_id INT);
TRUNCATE TABLE Employees;
INSERT INTO Employees (id, name) VALUES ('1', 'Alice');
INSERT INTO Employees (id, name) VALUES ('7', 'Bob');
INSERT INTO Employees (id, name) VALUES ('11', 'Meir');
INSERT INTO Employees (id, name) VALUES ('90', 'Winston');
INSERT INTO Employees (id, name) VALUES ('3', 'Jonathan');
TRUNCATE TABLE EmployeeUNI;
INSERT INTO EmployeeUNI (id, unique_id) VALUES ('3', '1');
INSERT INTO EmployeeUNI (id, unique_id) VALUES ('11', '2');
INSERT INTO EmployeeUNI (id, unique_id) VALUES ('90', '3');

--------------
-- SOLUCIÓN --
--------------

SELECT u.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI u ON e.id=u.id;