-- 1211. Queries Quality and Percentage
-- https://leetcode.com/problems/queries-quality-and-percentage/

/*
Definimos la calidad de la consulta como:

La media de la relación entre la valoración de la consulta y su posición.

También definimos el porcentaje de consultas deficientes como:

El porcentaje de todas las consultas con una puntuación inferior a 3.

Escriba una consulta SQL para encontrar cada nombre de consulta, la calidad y el porcentaje de consultas deficientes.

Tanto la calidad como el porcentaje de consultas deficientes deben redondearse a 2 decimales.

Devuelve la tabla de resultados en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/

CREATE TABLE IF NOT EXISTS Queries (query_name VARCHAR(30), result VARCHAR(50), position INT, rating INT);
TRUNCATE TABLE Queries;
INSERT INTO Queries (query_name, result, position, rating) VALUES ('Dog', 'Golden Retriever', '1', '5');
INSERT INTO Queries (query_name, result, position, rating) VALUES ('Dog', 'German Shepherd', '2', '5');
INSERT INTO Queries (query_name, result, position, rating) VALUES ('Dog', 'Mule', '200', '1');
INSERT INTO Queries (query_name, result, position, rating) VALUES ('Cat', 'Shirazi', '5', '2');
INSERT INTO Queries (query_name, result, position, rating) VALUES ('Cat', 'Siamese', '3', '3');
INSERT INTO Queries (query_name, result, position, rating) VALUES ('Cat', 'Sphynx', '7', '4');

