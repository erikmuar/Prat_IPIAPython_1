# learn-sql

## Windows 
```sql
  sqlite3 # donde esté el .exe de sqlite.org
```

```sql
  .open <db>.sqlite3
```

## Mac, Linux
Crear la db:
```bash
  sqlite3 <db>.sqlite3
```
Ver tablas:
```bash
  .tables
```
No saldrá nada la primera vez
Crear una tabla `usuario`:
```sql
  CREATE TABLE usuario (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      email TEXT NOT NULL UNIQUE,
      nombre TEXT, 
      apellido TEXT
  );
```
Insertamos un dato:
```sql
  INSERT INTO usuario (email, nombre) VALUES ('example@example.com', 'Example Name');
```
Mirar todos los datos:
```sql
  SELECT * FROM usuario;
```

## Hacer dump de SQLite3
``` bash
  sqlite3 <db>.sqlite3 .dump > <nombre_del_archivo_dump>.sql
```
## Cargar dump de SQLite3
```bash
  sqlite3 <db>.sqlite3 < <nombre_del_archivo_dumo>.sql
```