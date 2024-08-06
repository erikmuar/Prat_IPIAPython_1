-- 620. Not Boring Movies
-- https://leetcode.com/problems/not-boring-movies/

/*
Escriba una consulta SQL para informar de las películas con un ID impar y una descripción que no sea "aburrida".

Devuelva la tabla de resultados ordenada por calificación en orden descendente.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/

CREATE TABLE IF NOT EXISTS cinema (id INT, movie VARCHAR(255), description VARCHAR(255), rating FLOAT(2, 1));
TRUNCATE TABLE cinema;
INSERT INTO cinema (id, movie, description, rating) VALUES ('1', 'War', 'great 3D', '8.9');
INSERT INTO cinema (id, movie, description, rating) VALUES ('2', 'Science', 'fiction', '8.5');
INSERT INTO cinema (id, movie, description, rating) VALUES ('3', 'irish', 'boring', '6.2');
INSERT INTO cinema (id, movie, description, rating) VALUES ('4', 'Ice song', 'Fantacy', '8.6');
INSERT INTO cinema (id, movie, description, rating) VALUES ('5', 'House card', 'Interesting', '9.1');

--------------
-- SOLUCIÓN --
--------------
SELECT * FROM Cinema
WHERE 
  MOD(id, 2) = 1 AND
  description != 'boring'
  ORDER BY rating DESC;

-- Explicación
-- Mostrando los ids impares:
SELECT id, MOD(id, 2) FROM Cinema
WHERE MOD(id, 2) = 1;
-- Descartamos descripcion 'boring
-- Ordenamos por rating descendente