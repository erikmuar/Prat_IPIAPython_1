import os
import sqlite3

def crear_tabla():
  # Conectar a la base de datos (crea el archivo si no existe)
  conn = sqlite3.connect('<nombre_de_db>.sqlite')

  # Crear un cursor
  cur = conn.cursor()

  # Crear la tabla si no existe
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

  # Confirmar los cambios
  conn.commit()

def confirmar_creacion_de_tabla():
  # Conectar a la base de datos (crea el archivo si no existe)
  conn = sqlite3.connect('<nombre_de_db>.sqlite')
  cur = conn.cursor()

  # Leer y ejecutar el archivo SQL

  # Obtener el directorio actual
  current_directory = os.path.dirname(os.path.abspath(__file__))

  # Construir la ruta completa al archivo
  file_path = os.path.join(current_directory, 'create_table.sql')

  with open(file_path, 'r') as sql_file:
      sql_script = sql_file.read()
      cur.executescript(sql_script)
      conn.commit()

  # Verificar la creación de la tabla
  cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='tblUsuarios';")
  table_exists = cur.fetchone()

  # Confirmar y hacer un print después
  if table_exists:
    print("La tabla 'tblUsuarios' ha sido creada exitosamente.")
  else:
    print("Error: La tabla 'tblUsuarios' no ha sido creada.")

  # Cerrar la conexión
  conn.close()


if __name__ == '__main__':
  crear_tabla()
  confirmar_creacion_de_tabla()
