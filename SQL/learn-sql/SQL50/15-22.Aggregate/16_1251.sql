-- 1251. Average Selling Price
-- https://leetcode.com/problems/average-selling-price/

/*
Escriba una consulta SQL para encontrar el precio medio de venta de cada producto. average_price debe redondearse a 2 decimales.

Devuelva la tabla de resultados en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/

CREATE TABLE IF NOT EXISTS Prices (product_id INT, start_DATE DATE, end_DATE DATE, price INT);
CREATE TABLE IF NOT EXISTS UnitsSold (product_id INT, purchase_DATE DATE, units INT);
TRUNCATE TABLE Prices;
INSERT INTO Prices (product_id, start_DATE, end_DATE, price) VALUES ('1', '2019-02-17', '2019-02-28', '5');
INSERT INTO Prices (product_id, start_DATE, end_DATE, price) VALUES ('1', '2019-03-01', '2019-03-22', '20');
INSERT INTO Prices (product_id, start_DATE, end_DATE, price) VALUES ('2', '2019-02-01', '2019-02-20', '15');
INSERT INTO Prices (product_id, start_DATE, end_DATE, price) VALUES ('2', '2019-02-21', '2019-03-31', '30');
TRUNCATE TABLE UnitsSold;
INSERT INTO UnitsSold (product_id, purchase_DATE, units) VALUES ('1', '2019-02-25', '100');
INSERT INTO UnitsSold (product_id, purchase_DATE, units) VALUES ('1', '2019-03-01', '15');
INSERT INTO UnitsSold (product_id, purchase_DATE, units) VALUES ('2', '2019-02-10', '200');
INSERT INTO UnitsSold (product_id, purchase_DATE, units) VALUES ('2', '2019-03-22', '30');

--------------
-- SOLUCIÓN --
--------------

