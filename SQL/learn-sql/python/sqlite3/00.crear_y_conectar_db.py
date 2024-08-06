import sqlite3

def main():
  # Conectar a la base de datos (crea el archivo si no existe)
  conn = sqlite3.connect('<nombre_de_db>.sqlite') # extensiones habituales son .db o .sqlite / .sqlite3
                                                  # si queréis usar la extensión de VS Code para leer la db (SQLite Viewer), 
                                                  # vale cualquier opción

  # Crear un cursor
  cur = conn.cursor()

  # Crear una tabla
  cur.execute('''
  CREATE TABLE IF NOT EXISTS tblUsuarios (
    idx INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    nombre TEXT NOT NULL,
    sexo TEXT CHECK(sexo IN ('M', 'H')),
    nivel INTEGER CHECK(nivel BETWEEN 0 AND 255),
    email TEXT,
    telefono TEXT,
    marca TEXT,
    compañia TEXT,
    saldo REAL,
    activo INTEGER CHECK(activo IN (0, 1))
  )
  ''')

  # Insertar datos
  cur.execute('''
  INSERT INTO tblUsuarios (usuario, nombre, sexo, nivel, email, telefono, marca, compañia, saldo, activo)
  VALUES ('BRE2271', 'BRENDA', 'M', 2, 'brenda@live.com', '655-330-5736', 'SAMSUNG', 'IUSACELL', 100, 1)
  ''')
  cur.execute('''
  INSERT INTO tblUsuarios (usuario, nombre, sexo, nivel, email, telefono, marca, compañia, saldo, activo)
  VALUES ('OSC4677', 'OSCAR', 'H', 3, 'oscar@gmail.com', '655-143-4181', 'LG', 'TELCEL', 0, 1)
  ''')

  # Confirmar los cambios
  conn.commit()

  # Ejecutar una consulta
  cur.execute('SELECT * FROM tblUsuarios WHERE email NOT LIKE "%@YAHOO%" COLLATE BINARY')

  # Recuperar y mostrar los resultados
  rows = cur.fetchall()
  for row in rows:
      print(row)

  # Cerrar la conexión
  conn.close()

if __name__ == '__main__':
   main()