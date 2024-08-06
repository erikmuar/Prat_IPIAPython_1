## Bloque 2

4. Calcular el saldo promedio de los usuarios que tienen teléfono marca NOKIA
  Pista: `AVG`,  se puede usar sum y count...
6. Mostrar el email de los usuarios que no usan yahoo
  Pista: `NOT` + `LIKE`
  ```
    PRAGMA case_sensitive_like=ON;
    PRAGMA case_sensitive_like=OFF;
  ```
9. Listar las diferentes marcas de celular en orden alfabético descendentemente
  Pista: `ORDER BY`
10. Listar las diferentes compañias en orden alfabético aleatorio
  Pista: `RANDOM()`