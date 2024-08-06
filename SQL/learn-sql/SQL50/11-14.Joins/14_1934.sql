-- 1934. Confirmation Rate
-- https://leetcode.com/problems/confirmation-rate/

/*
La tasa de confirmación de un usuario es el número de mensajes "confirmados" dividido por el número total de mensajes de confirmación solicitados. La tasa de confirmación de un usuario que no solicitó ningún mensaje de confirmación es 0. Redondee la tasa de confirmación a dos decimales.

Escribe una consulta SQL para obtener el porcentaje de confirmación de cada usuario.

Devuelva la tabla de resultados en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/
CREATE TABLE IF NOT EXISTS Signups (user_id INT, time_stamp DATEtime);
CREATE TABLE IF NOT EXISTS Confirmations (user_id INT, time_stamp DATEtime, action ENUM('confirmed','timeout'));
TRUNCATE TABLE Signups;
INSERT INTO Signups (user_id, time_stamp) VALUES ('3', '2020-03-21 10:16:13');
INSERT INTO Signups (user_id, time_stamp) VALUES ('7', '2020-01-04 13:57:59');
INSERT INTO Signups (user_id, time_stamp) VALUES ('2', '2020-07-29 23:09:44');
INSERT INTO Signups (user_id, time_stamp) VALUES ('6', '2020-12-09 10:39:37');
TRUNCATE TABLE Confirmations;
INSERT INTO Confirmations (user_id, time_stamp, action) VALUES ('3', '2021-01-06 03:30:46', 'timeout');
INSERT INTO Confirmations (user_id, time_stamp, action) VALUES ('3', '2021-07-14 14:00:00', 'timeout');
INSERT INTO Confirmations (user_id, time_stamp, action) VALUES ('7', '2021-06-12 11:57:29', 'confirmed');
INSERT INTO Confirmations (user_id, time_stamp, action) VALUES ('7', '2021-06-13 12:58:28', 'confirmed');
INSERT INTO Confirmations (user_id, time_stamp, action) VALUES ('7', '2021-06-14 13:59:27', 'confirmed');
INSERT INTO Confirmations (user_id, time_stamp, action) VALUES ('2', '2021-01-22 00:00:00', 'confirmed');
INSERT INTO Confirmations (user_id, time_stamp, action) VALUES ('2', '2021-02-28 23:59:59', 'timeout');

--------------
-- SOLUCIÓN --
--------------

SELECT 
  S.user_id, 
  ROUND(COALESCE(C.solicitudes_confirmadas, 0) / COALESCE(C.solicitudes_totales, 1), 2) AS confirmation_rate
FROM Signups S
LEFT JOIN (
  SELECT
    user_id,
    COUNT(*) AS solicitudes_totales,
    SUM(action = 'confirmed') AS solicitudes_confirmadas
FROM
    Confirmations
GROUP BY
    user_id
) C ON C.user_id = S.user_id;

-- Explicación: --
-- Este query lista las solicitudes totales y las confirmadas para cada usuario:
SELECT
    user_id,
    COUNT(*) AS solicitudes_totales,
    SUM(action = 'confirmed') AS solicitudes_confirmadas
FROM
    Confirmations
GROUP BY
    user_id;
-- Hacemos un LEFT JOIN con Signups para tener la lista de todos los usuarios:
SELECT 
  S.user_id, 
  C.solicitudes_confirmadas / C.solicitudes_totales AS confirmation_rate
FROM Signups S
LEFT JOIN (
  SELECT
    user_id,
    COUNT(*) AS solicitudes_totales,
    SUM(action = 'confirmed') AS solicitudes_confirmadas
FROM
    Confirmations
GROUP BY
    user_id
) C ON C.user_id = S.user_id; -- el user con id 6 sale NULL
-- Usamos la función COALESCE para colocar valores cuando tengamos NULL para poder dividir:
SELECT 
  S.user_id, 
  COALESCE(C.solicitudes_confirmadas, 0) / COALESCE(C.solicitudes_totales, 1) AS confirmation_rate
FROM Signups S
LEFT JOIN (
  SELECT
    user_id,
    COUNT(*) AS solicitudes_totales,
    SUM(action = 'confirmed') AS solicitudes_confirmadas
FROM
    Confirmations
GROUP BY
    user_id
) C ON C.user_id = S.user_id; -- ahora el NULL del user 6 pasa a 0.0
-- Aplicamos ROUND(..., 2) para redondear a 2 decimales:
SELECT 
  S.user_id, 
  ROUND(COALESCE(C.solicitudes_confirmadas, 0) / COALESCE(C.solicitudes_totales, 1), 2) AS confirmation_rate
FROM Signups S
LEFT JOIN (
  SELECT
    user_id,
    COUNT(*) AS solicitudes_totales,
    SUM(action = 'confirmed') AS solicitudes_confirmadas
FROM
    Confirmations
GROUP BY
    user_id
) C ON C.user_id = S.user_id;
-----------------------------
-- Alternativa de solución:
SELECT
    s.user_id,
    ROUND(COALESCE(c.confirmed_count, 0) / COALESCE(c.total_count, 1), 2) AS confirmation_rate
FROM
    Signups s
LEFT JOIN
    (
        SELECT
            user_id,
            COUNT(*) AS total_count,
            SUM(action = 'confirmed') AS confirmed_count
        FROM
            Confirmations
        GROUP BY
            user_id
    ) c ON s.user_id = c.user_id;
-- Referencia: https://leetcode.com/problems/confirmation-rate/solutions/3608649/mysql-solution-for-confirmation-rate-problem/?envType=study-plan-v2&envId=top-sql-50

