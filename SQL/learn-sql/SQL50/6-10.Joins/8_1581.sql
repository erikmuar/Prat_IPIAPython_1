-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

/*
Escriba una consulta SQL para encontrar los ID de los usuarios que visitaron sin realizar ninguna transacción y el número de veces que realizaron este tipo de visitas.

Devuelve la tabla de resultados ordenada en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/

CREATE TABLE IF NOT EXISTS Visits(visit_id INT, customer_id INT);
CREATE TABLE IF NOT EXISTS Transactions(transaction_id INT, visit_id INT, amount INT);
TRUNCATE TABLE Visits;
INSERT INTO Visits (visit_id, customer_id) VALUES ('1', '23');
INSERT INTO Visits (visit_id, customer_id) VALUES ('2', '9');
INSERT INTO Visits (visit_id, customer_id) VALUES ('4', '30');
INSERT INTO Visits (visit_id, customer_id) VALUES ('5', '54');
INSERT INTO Visits (visit_id, customer_id) VALUES ('6', '96');
INSERT INTO Visits (visit_id, customer_id) VALUES ('7', '54');
INSERT INTO Visits (visit_id, customer_id) VALUES ('8', '54');
TRUNCATE TABLE Transactions;
INSERT INTO Transactions (transaction_id, visit_id, amount) VALUES ('2', '5', '310');
INSERT INTO Transactions (transaction_id, visit_id, amount) VALUES ('3', '5', '300');
INSERT INTO Transactions (transaction_id, visit_id, amount) VALUES ('9', '5', '200');
INSERT INTO Transactions (transaction_id, visit_id, amount) VALUES ('12', '1', '910');
INSERT INTO Transactions (transaction_id, visit_id, amount) VALUES ('13', '2', '970');

--------------
-- SOLUCIÓN --
--------------

-- Primera columna de customer_id:
SELECT v.customer_id
FROM Visits v 
LEFT JOIN Transactions t 
ON v.visit_id=t.visit_id
WHERE t.transaction_id IS Null
GROUP BY v.customer_id;

-- Ambas columnas:
SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM Visits v LEFT JOIN Transactions t ON v.visit_id=t.visit_id
WHERE t.visit_id IS Null
GROUP BY v.customer_id;

-- También se puede hacer sin JOIN:

-- query con los visit_id en tabla Transactions:
SELECT visit_id FROM Transactions;
-- Solución sin JOIN:
SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY customer_id;

