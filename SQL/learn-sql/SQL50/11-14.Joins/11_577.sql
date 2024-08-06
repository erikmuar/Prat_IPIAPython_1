-- 577. Employee Bonus
-- https://leetcode.com/problems/employee-bonus

/*
Escriba una consulta SQL para informar del nombre y el importe de la bonificación de cada empleado con una bonificación inferior a 1000.

Devuelva la tabla de resultados en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/

-- Creamos las tablas:
CREATE TABLE IF NOT EXISTS Employee (empId INT, name VARCHAR(255), supervisor INT, salary INT);
CREATE TABLE IF NOT EXISTS Bonus (empId INT, bonus INT);
TRUNCATE TABLE Employee;
INSERT INTO Employee (empId, name, supervisor, salary) VALUES ('3', 'Brad', NULL, '4000');
INSERT INTO Employee (empId, name, supervisor, salary) VALUES ('1', 'John', '3', '1000');
INSERT INTO Employee (empId, name, supervisor, salary) VALUES ('2', 'Dan', '3', '2000');
INSERT INTO Employee (empId, name, supervisor, salary) VALUES ('4', 'Thomas', '3', '4000');
TRUNCATE TABLE Bonus;
INSERT INTO Bonus (empId, bonus) VALUES ('2', '500');
INSERT INTO Bonus (empId, bonus) VALUES ('4', '2000');

--------------
-- SOLUCIÓN --
--------------

SELECT e.name, b.bonus
FROM Employee e LEFT JOIN Bonus b ON 
e.`empId`=b.`empId`
WHERE b.bonus < 1000 OR b.bonus IS NULL;