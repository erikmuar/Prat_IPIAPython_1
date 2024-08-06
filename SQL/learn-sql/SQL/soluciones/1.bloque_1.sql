/*
Ejercicios: https://parzibyte.me/blog/2018/02/06/ejercicios-resueltos-consultas-sql-mysql/amp/
1. Crear db y tabla: https://gist.github.com/parzibyte/01321b39ce6df361c8917af84c483123
*/

-- Seleccionamos base de datos:
USE pruebas;

-- 1. Listar los nombres de los usuarios
SELECT nombre from tblusuarios;
-- 2. Calcular el saldo máximo de los usuarios de sexo “Mujer”
SELECT MAX(saldo) FROM tblusuarios WHERE sexo = "M"; -- 500
SELECT nombre, saldo, sexo FROM tblusuarios WHERE saldo = 500 AND sexo = 'M' -- JESSICA
-- 3. Listar nombre y teléfono de los usuarios con teléfono NOKIA, BLACKBERRY o SONY
SELECT nombre, telefono FROM tblusuarios WHERE marca = "NOKIA" OR marca = "BLACKBERRY" OR marca = "SONY";
-- Usando IN:
SELECT nombre, telefono 
FROM tblusuarios 
WHERE marca IN ("NOKIA", "BLACKBERRY", "SONY");
-- Si queremos ver la marca:
SELECT nombre, telefono, marca FROM tblusuarios WHERE marca = "NOKIA" OR marca = "BLACKBERRY" OR marca = "SONY";
-- 4. Contar los usuarios sin saldo o inactivos
SELECT idx, nombre, saldo, activo FROM tblusuarios WHERE saldo = 0 OR activo = FALSE; -- vemos que salen usuarios con saldo 0 o activo como 0 (FALSE)
-- Usando COUNT()
SELECT COUNT(*) FROM tblusuarios WHERE saldo = 0 OR activo = FALSE; -- contamos los resultados
-- Como activo es un BOOLEAN pero en realidad se guarda como 0 o 1, también podemos usar NOT:
SELECT idx, nombre, saldo, activo FROM tblusuarios WHERE saldo = 0 OR NOT activo;
-- 5. Listar el login de los usuarios con nivel 1, 2 o 3
SELECT nombre, nivel FROM tblusuarios WHERE nivel < 4 AND nivel > 0; -- Seleccionamos nivel entre 1 y 3
-- Usando BETWEEN:
SELECT nombre, nivel FROM tblusuarios WHERE nivel BETWEEN 1 AND 3; -- incluye los números extremos del intervalo
-- 6. Listar los números de teléfono con saldo menor o igual a 300
SELECT nombre, telefono FROM tblusuarios WHERE saldo <= 300;
-- 7. Calcular la suma de los saldos de los usuarios de la compañia telefónica NEXTEL
SELECT SUM(saldo) FROM tblusuarios WHERE compañia = "NEXTEL";
-- 8. Contar el número de usuarios por compañía telefónica
-- Agrupamos por compañia:
SELECT compañia, COUNT(*) FROM `tblusuarios` GROUP BY compañia;
-- Agrupando por marca:
SELECT compañia, COUNT(*) FROM `tblusuarios` GROUP BY marca;
-- 9. Contar el número de usuarios por nivel
SELECT nivel, COUNT(*) FROM `tblusuarios` GROUP BY nivel;
-- 10. Listar el login de los usuarios con nivel 2
SELECT nombre, email FROM `tblusuarios` WHERE nivel = 2;
-- 11. Mostrar el email de los usuarios que usan gmail
SELECT email FROM `tblusuarios` WHERE email LIKE "%@gmail.com%"; -- Buscamos cualquier_string@gmail.com <> % representa cualquier substring
-- Nota: el segundo % es para permitir caracteres al final, como espacios en blanco
-- 12. Listar nombre y teléfono de los usuarios con teléfono LG, SAMSUNG o MOTOROLA
SELECT nombre, telefono FROM tblusuarios WHERE marca IN ("LG", "SAMSUNG", "MOTOROLA");
