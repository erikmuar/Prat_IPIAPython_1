-- 1174. Immediate Food Delivery II
-- https://leetcode.com/problems/immediate-food-delivery-ii/
/*
Si la fecha de entrega preferida por el cliente coincide con la fecha del pedido, éste se denomina inmediato; en caso contrario, se denomina programado.

El primer pedido de un cliente es el pedido con la fecha de pedido más temprana que realizó el cliente. Se garantiza que un cliente tiene exactamente un primer pedido.

Escriba una consulta SQL para encontrar el porcentaje de pedidos inmediatos en los primeros pedidos de todos los clientes, redondeado a 2 decimales.

El formato del resultado de la consulta está en el siguiente ejemplo.
*/

CREATE TABLE IF NOT EXISTS Delivery (delivery_id INT, customer_id INT, order_DATE DATE, customer_pref_delivery_DATE DATE);
TRUNCATE TABLE Delivery;
INSERT INTO Delivery (delivery_id, customer_id, order_DATE, customer_pref_delivery_DATE) VALUES ('1', '1', '2019-08-01', '2019-08-02');
INSERT INTO Delivery (delivery_id, customer_id, order_DATE, customer_pref_delivery_DATE) VALUES ('2', '2', '2019-08-02', '2019-08-02');
INSERT INTO Delivery (delivery_id, customer_id, order_DATE, customer_pref_delivery_DATE) VALUES ('3', '1', '2019-08-11', '2019-08-12');
INSERT INTO Delivery (delivery_id, customer_id, order_DATE, customer_pref_delivery_DATE) VALUES ('4', '3', '2019-08-24', '2019-08-24');
INSERT INTO Delivery (delivery_id, customer_id, order_DATE, customer_pref_delivery_DATE) VALUES ('5', '3', '2019-08-21', '2019-08-22');
INSERT INTO Delivery (delivery_id, customer_id, order_DATE, customer_pref_delivery_DATE) VALUES ('6', '2', '2019-08-11', '2019-08-13');
INSERT INTO Delivery (delivery_id, customer_id, order_DATE, customer_pref_delivery_DATE) VALUES ('7', '4', '2019-08-09', '2019-08-09');
