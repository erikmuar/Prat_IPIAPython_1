## Dump

```bash
  sqlite3 <db>.sqlite3 ".dump" > <nombre_del_dump>.sql 

  # nombre_del_dump => dump_ej_02_AGO_16_00.dump
```

## Restaurar db

```bash
  sqlite3 <db>.sqlite3 < <nombre_del_dump>.sql
```

## SQL

- CREATE TABLE IF NOT EXISTS ... 
- INSERT INTO <tabla> ...
- SELECT ...
- UPDATE ... SET ...
- DELETE