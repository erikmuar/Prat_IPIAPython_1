-- 1683 https://leetcode.com/problems/invalid-tweets/
-- Enunciado:
/*

Escribe una consulta SQL para encontrar los ID de los tweets no válidos. 

El tweet es inválido si el número de caracteres utilizados en el contenido del tweet es estrictamente superior a 15.

Devuelva la tabla de resultados en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/

CREATE TABLE IF NOT EXISTS Tweets(
  tweet_id INT, 
  `content` VARCHAR(50)
  );
TRUNCATE TABLE Tweets;
INSERT INTO Tweets (tweet_id, content) VALUES ('1', 'Vote for Biden');
INSERT INTO Tweets (tweet_id, content) VALUES ('2', 'Let us make America great again!');

--------------
-- SOLUCIÓN --
--------------

SELECT tweet_id FROM Tweets WHERE LENGTH(content) > 15;  

