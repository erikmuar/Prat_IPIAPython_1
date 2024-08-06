-- 1661. Average Time of Process per Machine
-- https://leetcode.com/problems/average-time-of-process-per-machine

/*
Hay un sitio web de una fábrica que tiene varias máquinas, cada una ejecutando el mismo número de procesos. Escribe una consulta SQL para encontrar el tiempo medio que tarda cada máquina en completar un proceso.

El tiempo para completar un proceso es la marca de tiempo 'fin' menos la marca de tiempo 'inicio'. El tiempo medio se calcula dividiendo el tiempo total para completar cada proceso en la máquina por el número de procesos que se ejecutaron.

La tabla resultante debe tener el id_máquina junto con el tiempo medio como tiempo_proceso, que debe redondearse a 3 decimales.

Devuelve la tabla de resultados en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/  

CREATE TABLE IF NOT EXISTS Activity (machine_id INT, process_id INT, activity_type ENUM('start', 'end'), timestamp FLOAT);
TRUNCATE TABLE Activity;
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES ('0', '0', 'start', '0.712');
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES ('0', '0', 'end', '1.52');
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES ('0', '1', 'start', '3.14');
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES ('0', '1', 'end', '4.12');
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES ('1', '0', 'start', '0.55');
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES ('1', '0', 'end', '1.55');
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES ('1', '1', 'start', '0.43');
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES ('1', '1', 'end', '1.42');
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES ('2', '0', 'start', '4.1');
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES ('2', '0', 'end', '4.512');
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES ('2', '1', 'start', '2.5');
INSERT INTO Activity (machine_id, process_id, activity_type, timestamp) VALUES ('2', '1', 'end', '5');

--------------
-- SOLUCIÓN --
--------------

SELECT A.machine_id, ROUND(SUM(B.timestamp - A.timestamp)/COUNT(*), 3) AS processing_time
FROM Activity A, Activity B
WHERE 
  A.process_id = B.process_id 
  AND B.timestamp - A.timestamp > 0
  AND A.machine_id = B.machine_id
GROUP BY machine_id;