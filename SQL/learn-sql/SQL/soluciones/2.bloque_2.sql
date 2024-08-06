-- https://parzibyte.me/blog/2018/02/06/ejercicios-resueltos-consultas-sql-mysql/amp/

-- 1. Listar nombre y teléfono de los usuarios con teléfono que no sea de la marca LG o SAMSUNG
SELECT nombre, telefono, marca 
FROM `tblusuarios` 
WHERE marca NOT IN ("LG", "SAMSUNG");

--SELECT nombre, telefono, marca FROM `tblusuarios` WHERE NOT marca = "LG" AND NOT marca = "SAMSUNG";

-- SELECT nombre, telefono, marca FROM `tblusuarios` WHERE marca != "LG" AND marca != "SAMSUNG";

-- 2. Listar el login y teléfono de los usuarios con compañia telefónica IUSACELL
SELECT email, telefono, compañia FROM `tblusuarios` WHERE compañia IN ("IUSACELL");

-- SELECT email, telefono, compañia FROM `tblusuarios` WHERE compañia = "IUSACELL";

-- 3. Listar el login y teléfono de los usuarios con compañia telefónica que no sea TELCEL

-- SELECT email, telefono, compañia FROM `tblusuarios` WHERE compañia NOT IN ("TELCEL");

SELECT email, telefono, compañia FROM `tblusuarios` WHERE compañia != "TELCEL";

-- 4. Calcular el saldo promedio de los usuarios que tienen teléfono marca NOKIA

SELECT AVG(saldo)
FROM tblusuarios
WHERE marca = "NOKIA";
-- COUNT(), SUM(), AVG() devuelven un número
-- Se aplican en columnas numéricas

-- 5. Listar el login y teléfono de los usuarios con compañia telefónica IUSACELL o AXEL

SELECT email, telefono, compañia
FROM tblusuarios
WHERE compañia IN ("IUSACELL", "AXEL");

-- 6. Mostrar el email de los usuarios que no usan yahoo

SELECT email
FROM tblusuarios
WHERE email NOT LIKE "%@yahoo.%";

-- 7. Listar el login y teléfono de los usuarios con compañia telefónica que no sea TELCEL o IUSACELL

SELECT email, telefono, compañia
FROM tblusuarios
WHERE compañia NOT IN ("TELCEL", "IUSACELL");

-- 8. Listar el login y teléfono de los usuarios con compañia telefónica UNEFON

SELECT email, telefono, compañia
FROM tblusuarios
WHERE compañia IN ("UNEFON");

-- 9. Listar las diferentes marcas de celular en orden alfabético descendentemente

SELECT DISTINCT marca
FROM tblusuarios
ORDER BY marca ASC; 
-- por defecto es ascendente, orden alfabético, si queremos orden inverso, DESC
-- Se puede ordenar por cualquier campo en la tabla y no tiene que aparecer en el resultado del query

-- 10. Listar las diferentes compañias en orden alfabético aleatorio

SELECT DISTINCT compañia 
FROM tblusuarios
ORDER BY RAND();

-- 11. Listar el login de los usuarios con nivel 0 o 2

SELECT email, nivel 
FROM tblusuarios
WHERE nivel IN (0,2);

-- 12. Calcular el saldo promedio de los usuarios que tienen teléfono marca LG

SELECT AVG(saldo)
FROM tblusuarios
WHERE marca = "LG";