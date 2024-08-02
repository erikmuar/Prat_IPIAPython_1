-- SQL

CREATE TABLE IF NOT EXISTS tblUsuarios (
   idx INTEGER PRIMARY KEY AUTOINCREMENT,
   usuario TEXT NOT NULL,
   nombre TEXT NOT NULL,
   sexo TEXT CHECK(sexo IN ('M', 'F')),
   nivel INTEGER CHECK(nivel BETWEEN 0 AND 255),
   email TEXT,
   telefono TEXT,
   marca TEXT,
   compañia TEXT,
   saldo REAL,
   activo INTEGER CHECK(activo IN (0, 1))
);