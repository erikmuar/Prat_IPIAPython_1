-- 1193. Monthly Transactions I
-- https://leetcode.com/problems/monthly-transactions-i/
/*
Escriba una consulta SQL para encontrar para cada mes y país, el número de transacciones y su importe total, el número de transacciones aprobadas y su importe total.

Devuelve la tabla de resultados en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/

CREATE TABLE IF NOT EXISTS Transactions2 (id INT, country VARCHAR(4), state enum('approved', 'declined'), amount INT, trans_DATE DATE);
TRUNCATE TABLE Transactions2;
INSERT INTO Transactions2 (id, country, state, amount, trans_DATE) VALUES ('121', 'US', 'approved', '1000', '2018-12-18');
INSERT INTO Transactions2 (id, country, state, amount, trans_DATE) VALUES ('122', 'US', 'declined', '2000', '2018-12-19');
INSERT INTO Transactions2 (id, country, state, amount, trans_DATE) VALUES ('123', 'US', 'approved', '2000', '2019-01-01');
INSERT INTO Transactions2 (id, country, state, amount, trans_DATE) VALUES ('124', 'DE', 'approved', '2000', '2019-01-07');