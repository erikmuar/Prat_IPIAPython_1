-- 1075. Project Employees I
-- https://leetcode.com/problems/project-employees-i/

/* 

Escriba una consulta SQL que informe de la media de años de experiencia de todos los empleados para cada proyecto, redondeada a 2 dígitos.

Devuelva la tabla de resultados en cualquier orden.

El formato del resultado de la consulta está en el siguiente ejemplo.

*/

CREATE TABLE IF NOT EXISTS Project (project_id INT, employee_id INT);
CREATE TABLE IF NOT EXISTS Employee3 (employee_id INT, name VARCHAR(10), experience_years INT);
TRUNCATE TABLE Project;
INSERT INTO Project (project_id, employee_id) VALUES ('1', '1');
INSERT INTO Project (project_id, employee_id) VALUES ('1', '2');
INSERT INTO Project (project_id, employee_id) VALUES ('1', '3');
INSERT INTO Project (project_id, employee_id) VALUES ('2', '1');
INSERT INTO Project (project_id, employee_id) VALUES ('2', '4');
TRUNCATE TABLE Employee3;
INSERT INTO Employee3 (employee_id, name, experience_years) VALUES ('1', 'Khaled', '3');
INSERT INTO Employee3 (employee_id, name, experience_years) VALUES ('2', 'Ali', '2');
INSERT INTO Employee3 (employee_id, name, experience_years) VALUES ('3', 'John', '1');
INSERT INTO Employee3 (employee_id, name, experience_years) VALUES ('4', 'Doe', '2');