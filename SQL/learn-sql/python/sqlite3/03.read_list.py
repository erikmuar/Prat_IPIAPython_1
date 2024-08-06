import sqlite3

def read_list():
    # Conectar a la base de datos
    conn = sqlite3.connect('<nombre_de_db>.sqlite')
    cur = conn.cursor()

    # Leer el archivo SQL
    with open('readList.sql', 'r') as sql_file:
        sql_query = sql_file.read()

    # Ejecutar la consulta
    cur.execute(sql_query)
    results = cur.fetchall()

    # Verificar y mostrar los resultados
    if results:
        print(f"Se obtuvieron {len(results)} registros:")
        for result in results:
            print(result)
    else:
        print("No se encontraron datos.")

    # Cerrar la conexión
    conn.close()

if __name__ == '__main__':
  # Ejemplo de uso
  read_list()
