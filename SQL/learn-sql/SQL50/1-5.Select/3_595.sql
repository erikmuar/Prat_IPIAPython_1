-- 595 https://leetcode.com/problems/big-countries/
-- Enunciado:
/*
Un país es grande si tiene una superficie de al menos tres millones (es decir, 3_000_000 km2), o
tiene una población de al menos veinticinco millones (es decir, 25_000_000).
Escribe una consulta SQL para obtener el nombre, la población y la superficie de los países grandes.

Devuelva la tabla de resultados en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/

CREATE TABLE IF NOT EXISTS World (
  name VARCHAR(255), 
  continent VARCHAR(255), 
  area INT, 
  population INT, 
  gdp BIGINT);
TRUNCATE TABLE World;
INSERT INTO World (name, continent, area, population, gdp) values ('Afghanistan', 'Asia', '652230', '25500100', '20343000000');
INSERT INTO World (name, continent, area, population, gdp) values ('Albania', 'Europe', '28748', '2831741', '12960000000');
INSERT INTO World (name, continent, area, population, gdp) values ('Algeria', 'Africa', '2381741', '37100000', '188681000000');
INSERT INTO World (name, continent, area, population, gdp) values ('Andorra', 'Europe', '468', '78115', '3712000000');
INSERT INTO World (name, continent, area, population, gdp) values ('Angola', 'Africa', '1246700', '20609294', '100990000000');

--------------
-- SOLUCIÓN --
--------------
SELECT `name`, `population`, `area` FROM World WHERE `area` >= 3000000 OR `population` >= 25000000;