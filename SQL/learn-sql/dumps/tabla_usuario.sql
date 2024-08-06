PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE usuario (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      email TEXT NOT NULL UNIQUE,
      nombre TEXT NOT NULL
  );
INSERT INTO usuario VALUES(1,'example@example.com','Example Name');
INSERT INTO usuario VALUES(2,'pepe@larana.com','Pepe Rana');
INSERT INTO usuario VALUES(3,'pepe@thefrog.com','Pep0 Ran0');
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('usuario',3);
COMMIT;
