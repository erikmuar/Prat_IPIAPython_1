import sqlite3

def read_one(id):
    # Conectar a la base de datos
    conn = sqlite3.connect('<nombre_de_db>.sqlite')
    cur = conn.cursor()

    # Leer el archivo SQL
    with open('readOne.sql', 'r') as sql_file:
        sql_query = sql_file.read()

    # Ejecutar la consulta con el parámetro id
    cur.execute(sql_query, (id,))
    result = cur.fetchone()

    # Verificar y mostrar el resultado
    if result:
        print(f"Datos obtenidos para ID {id}: {result}")
    else:
        print(f"No se encontraron datos para ID {id}")

    # Cerrar la conexión
    conn.close()

if __name__ == '__main__':
  # Ejemplo de uso
  read_one(1)  # Cambia el valor del id según sea necesario
