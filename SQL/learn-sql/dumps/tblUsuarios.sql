PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE tblUsuarios (
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
INSERT INTO tblUsuarios VALUES(1,'BRE2271','BRENDA','F',2,'brenda@live.com','655-330-5736','SAMSUNG','IUSACELL',100.0,1);
INSERT INTO tblUsuarios VALUES(2,'OSC4677','OSCAR','M',3,'oscar@gmail.com','655-143-4181','LG','TELCEL',0.0,1);
INSERT INTO tblUsuarios VALUES(3,'JOS7086','JOSE','M',3,'francisco@gmail.com','655-143-3922','NOKIA','MOVISTAR',150.0,1);
INSERT INTO tblUsuarios VALUES(4,'LUI6115','LUIS','M',0,'enrique@outlook.com','655-137-1279','SAMSUNG','TELCEL',50.0,1);
INSERT INTO tblUsuarios VALUES(5,'LUI7072','LUIS','M',1,'luis@hotmail.com','655-100-8260','NOKIA','IUSACELL',50.0,0);
INSERT INTO tblUsuarios VALUES(6,'DAN2832','DANIEL','M',0,'daniel@outlook.com','655-145-2586','SONY','UNEFON',100.0,1);
INSERT INTO tblUsuarios VALUES(7,'JAQ5351','JAQUELINE','F',0,'jaqueline@outlook.com','655-330-5514','BLACKBERRY','AXEL',0.0,1);
INSERT INTO tblUsuarios VALUES(8,'ROM6520','ROMAN','M',2,'roman@gmail.com','655-330-3263','LG','IUSACELL',50.0,1);
INSERT INTO tblUsuarios VALUES(9,'BLA9739','BLAS','M',0,'blas@hotmail.com','655-330-3871','LG','UNEFON',100.0,1);
INSERT INTO tblUsuarios VALUES(10,'JES4752','JESSICA','F',1,'jessica@hotmail.com','655-143-6861','SAMSUNG','TELCEL',500.0,1);
INSERT INTO tblUsuarios VALUES(11,'DIA6570','DIANA','F',1,'diana@live.com','655-143-3952','SONY','UNEFON',100.0,0);
INSERT INTO tblUsuarios VALUES(12,'RIC8283','RICARDO','M',2,'ricardo@hotmail.com','655-145-6049','MOTOROLA','IUSACELL',150.0,1);
INSERT INTO tblUsuarios VALUES(13,'VAL6882','VALENTINA','F',0,'valentina@live.com','655-137-4253','BLACKBERRY','AT&T',50.0,0);
INSERT INTO tblUsuarios VALUES(14,'BRE8106','BRENDA','F',3,'brenda2@gmail.com','655-100-1351','MOTOROLA','NEXTEL',150.0,1);
INSERT INTO tblUsuarios VALUES(15,'LUC4982','LUCIA','F',3,'lucia@gmail.com','655-145-4992','BLACKBERRY','IUSACELL',0.0,1);
INSERT INTO tblUsuarios VALUES(16,'JUA2337','JUAN','M',0,'juan@outlook.com','655-100-6517','SAMSUNG','AXEL',0.0,0);
INSERT INTO tblUsuarios VALUES(17,'ELP2984','ELPIDIO','M',1,'elpidio@outlook.com','655-145-9938','MOTOROLA','MOVISTAR',500.0,1);
INSERT INTO tblUsuarios VALUES(18,'JES9640','JESSICA','F',3,'jessica2@live.com','655-330-5143','SONY','IUSACELL',200.0,1);
INSERT INTO tblUsuarios VALUES(19,'LET4015','LETICIA','F',2,'leticia@yahoo.com','655-143-4019','BLACKBERRY','UNEFON',100.0,1);
INSERT INTO tblUsuarios VALUES(20,'LUI1076','LUIS','M',3,'luis2@live.com','655-100-5085','SONY','UNEFON',150.0,1);
INSERT INTO tblUsuarios VALUES(21,'HUG5441','HUGO','M',2,'hugo@live.com','655-137-3935','MOTOROLA','AT&T',500.0,1);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('tblUsuarios',21);
COMMIT;
