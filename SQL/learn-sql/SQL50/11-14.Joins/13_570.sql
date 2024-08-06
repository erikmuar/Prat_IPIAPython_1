-- 570. Managers with at Least 5 Direct Reports
-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

/*
Escriba una consulta SQL para obtener un informe de los directivos con al menos cinco subordinados directos.

Devuelva la tabla de resultados en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/

-- Cambiamos nombre de tabla de Employee a Employee2 para que podamos ejecutar el query:
CREATE TABLE IF NOT EXISTS Employee2 (id INT, name VARCHAR(255), department VARCHAR(255), managerId INT);
TRUNCATE TABLE Employee2;
INSERT INTO Employee2 (id, name, department, managerId) VALUES ('101', 'John', 'A', NULL);
INSERT INTO Employee2 (id, name, department, managerId) VALUES ('102', 'Dan', 'A', '101');
INSERT INTO Employee2 (id, name, department, managerId) VALUES ('103', 'James', 'A', '101');
INSERT INTO Employee2 (id, name, department, managerId) VALUES ('104', 'Amy', 'A', '101');
INSERT INTO Employee2 (id, name, department, managerId) VALUES ('105', 'Anne', 'A', '101');
INSERT INTO Employee2 (id, name, department, managerId) VALUES ('106', 'Ron', 'B', '101');

--------------
-- SOLUCIÓN --
--------------

SELECT Employee2.name AS manager 
FROM Employee2 
WHERE id IN ((SELECT  
  E1.`managerId`
FROM Employee2 E1, Employee2 E2
WHERE E1.`managerId` = E2.`managerId` AND E1.department = E2.department AND E1.name = E2.name
HAVING COUNT(E2.`managerId`) >= 5));

-- Explicación --
-- El resultado es el nombre del manager con id de usuario 101. Este query nos da ese resultado:
SELECT Employee2.name AS manager 
FROM Employee2 
WHERE id IN (101);
-- Este otro query nos da el id del manager que sale al menos 5 veces:
SELECT  
  E1.`managerId`
FROM Employee2 E1, Employee2 E2
WHERE E1.`managerId` = E2.`managerId` AND E1.department = E2.department AND E1.name = E2.name
HAVING COUNT(E2.`managerId`) >= 5;
-- Se pueden juntar ambos para pasarle un 101 al primer query usando el segundo:
SELECT Employee2.name 
FROM Employee2 
WHERE `id` IN ((SELECT  
  E1.`managerId`
FROM Employee2 E1, Employee2 E2
WHERE E1.`managerId` = E2.`managerId` AND E1.department = E2.department AND E1.name = E2.name
HAVING COUNT(E2.`managerId`) >= 5)); -- colocamos el segundo query dentro de otros paréntesis para que se ejecute devolviendo una lista de resultados y como usamos IN podemos hacer match con cada resultado de la lista (array)
-- Alternativa:
SELECT b.name FROM Employee e1
JOIN (SELECT managerId FROM Employee 
GROUP BY managerID 
HAVING COUNT(*) >= 5) e2 
ON e1.id=e2.managerID