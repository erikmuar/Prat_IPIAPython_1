-- 1633. Percentage of Users Attended a Contest
-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/
/*

Escribe una consulta SQL para encontrar el porcentaje de usuarios inscritos en cada concurso redondeado a dos decimales.

Devuelve la tabla de resultados ordenada por porcentaje en orden descendente. En caso de empate, ordénalo por contest_id en orden ascendente.

El formato del resultado de la consulta está en el siguiente ejemplo.

*/

CREATE TABLE IF NOT EXISTS Users (user_id INT, user_name VARCHAR(20));
CREATE TABLE IF NOT EXISTS Register (contest_id INT, user_id INT);
TRUNCATE TABLE Users;
INSERT INTO Users (user_id, user_name) VALUES ('6', 'Alice');
INSERT INTO Users (user_id, user_name) VALUES ('2', 'Bob');
INSERT INTO Users (user_id, user_name) VALUES ('7', 'Alex');
TRUNCATE TABLE Register;
INSERT INTO Register (contest_id, user_id) VALUES ('215', '6');
INSERT INTO Register (contest_id, user_id) VALUES ('209', '2');
INSERT INTO Register (contest_id, user_id) VALUES ('208', '2');
INSERT INTO Register (contest_id, user_id) VALUES ('210', '6');
INSERT INTO Register (contest_id, user_id) VALUES ('208', '6');
INSERT INTO Register (contest_id, user_id) VALUES ('209', '7');
INSERT INTO Register (contest_id, user_id) VALUES ('209', '6');
INSERT INTO Register (contest_id, user_id) VALUES ('215', '7');
INSERT INTO Register (contest_id, user_id) VALUES ('208', '7');
INSERT INTO Register (contest_id, user_id) VALUES ('210', '2');
INSERT INTO Register (contest_id, user_id) VALUES ('207', '2');
INSERT INTO Register (contest_id, user_id) VALUES ('210', '7');