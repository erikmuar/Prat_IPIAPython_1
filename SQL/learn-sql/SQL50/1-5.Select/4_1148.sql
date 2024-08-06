-- 1148 https://leetcode.com/problems/article-views-i/
-- Enunciado
/*
Escriba una consulta SQL para encontrar todos los autores que vieron al menos uno de sus propios artículos.
Devuelve la tabla de resultados ordenada por id en orden ascendente.
El formato del resultado de la consulta está en el siguiente ejemplo.
*/

CREATE TABLE IF NOT EXISTS Views (
  article_id INT, 
  author_id INT, 
  viewer_id INT, 
  view_date DATE
  );
TRUNCATE TABLE Views;
INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('1', '3', '5', '2019-08-01');
INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('1', '3', '6', '2019-08-02');
INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('2', '7', '7', '2019-08-01');
INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('2', '7', '6', '2019-08-02');
INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('4', '7', '1', '2019-07-22');
INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('3', '4', '4', '2019-07-21');
INSERT INTO Views (article_id, author_id, viewer_id, view_date) values ('3', '4', '4', '2019-07-21');

--------------
-- SOLUCIÓN --
--------------

SELECT DISTINCT author_id AS `id` FROM `Views` WHERE author_id = viewer_id ORDER BY author_id;