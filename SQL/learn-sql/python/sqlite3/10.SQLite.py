import sqlite3
# from pathlib import Path

class DBConnector():
    
    # constructor
    # ruta a la db de sqlite
    def __init__(self, ruta_a_db: str) -> None:
        self.database = ruta_a_db
        print("ruta a db:", self.database)
    
    def conectar(self):
        conn = sqlite3.connect(self.database)
        return conn
    
    def desconectar(self, conn) -> None:
        conn.close()
    
    # create table
    def crear_tabla(self, query) -> None:
        conn = self.conectar()
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        self.desconectar(conn)

    # podemos pasarle una fuente de datos como un CSV:
    def seed(self, datos):
        insert_query = '''INSERT INTO tblUsuarios (usuario, nombre, sexo, nivel, email, telefono, marca, compañia, saldo, activo)
        VALUES (?,?,?,?,?,?,?,?,?,?);'''
        conn = self.conectar()
        cur = conn.cursor()
        for dato in datos:
            cur.execute(insert_query, dato)
        conn.commit()
        self.desconectar(conn)
    
    # leer datos
      # order by... 
    def select(id):
        pass
    
    # actualizar
    def update(id):
        pass
    
    # borrar por id
    def delete(id):
        pass
    

if __name__ == '__main__':
    db_conn = DBConnector("db.sqlite3")

    # Create table
    nombre_tabla = "tblUsuarios"
    create_table_query = f'''CREATE TABLE IF NOT EXISTS {nombre_tabla} (
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
        )'''
    db_conn.crear_tabla(create_table_query)

    # Seed
    datos = [
        ('p3p3', 'Pepe', 'H', 3, 'pepe@rana.frog', '123', 'PEPU', 'Le Pepe', -1.0, 1),
        ('jua7', 'Juan', 'M', 2, 'juan@correo.com', '456', 'JUAN', 'La Juan', 0.0, 1)
    ]
    
    db_conn.seed(datos)
