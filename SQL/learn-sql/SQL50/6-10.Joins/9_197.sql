-- 197. Rising Temperature
-- https://leetcode.com/problems/rising-temperature/

/*
Escriba una consulta SQL para encontrar todos los Id de fechas con temperaturas más altas en comparación con sus fechas anteriores (ayer).

Devuelve la tabla de resultados en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/  

CREATE TABLE IF NOT EXISTS Weather (id INT, recordDate DATE, temperature INT);
TRUNCATE TABLE Weather;
INSERT INTO Weather (id, recordDate, temperature) VALUES ('1', '2015-01-01', '10');
INSERT INTO Weather (id, recordDate, temperature) VALUES ('2', '2015-01-02', '25');
INSERT INTO Weather (id, recordDate, temperature) VALUES ('3', '2015-01-03', '20');
INSERT INTO Weather (id, recordDate, temperature) VALUES ('4', '2015-01-04', '30');

--------------
-- SOLUCIÓN --
--------------

SELECT A.id 
FROM Weather A, Weather B
WHERE A.recordDate=DATE_ADD(B.recordDate, INTERVAL 1 DAY)
AND A.temperature > B.temperature; 