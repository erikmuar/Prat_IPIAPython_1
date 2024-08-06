-- 550. Game Play Analysis IV
-- https://leetcode.com/problems/game-play-analysis-iv/
/*
Escriba una consulta SQL para informar de la fracción de jugadores que volvieron a conectarse el día siguiente al día en que se conectaron por primera vez, redondeado a 2 decimales. En otras palabras, debe contar el número de jugadores que iniciaron sesión durante al menos dos días consecutivos a partir de su primera fecha de inicio de sesión y, a continuación, dividir ese número por el número total de jugadores.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/

CREATE TABLE IF NOT EXISTS Activity2 (player_id INT, device_id INT, event_DATE DATE, games_played INT);
TRUNCATE TABLE Activity2;
INSERT INTO Activity2 (player_id, device_id, event_DATE, games_played) VALUES ('1', '2', '2016-03-01', '5');
INSERT INTO Activity2 (player_id, device_id, event_DATE, games_played) VALUES ('1', '2', '2016-03-02', '6');
INSERT INTO Activity2 (player_id, device_id, event_DATE, games_played) VALUES ('2', '3', '2017-06-25', '1');
INSERT INTO Activity2 (player_id, device_id, event_DATE, games_played) VALUES ('3', '1', '2016-03-02', '0');
INSERT INTO Activity2 (player_id, device_id, event_DATE, games_played) VALUES ('3', '4', '2018-07-03', '5');