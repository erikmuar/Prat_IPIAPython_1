import sqlite3

def delete_list(lista):
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect('<nombre_de_db>.sqlite')
        cur = conn.cursor()

        # Leer el archivo SQL
        with open('deleteBulk.sql', 'r') as sql_file:
            sql_query = sql_file.read()

        # Ejecutar la consulta
        for id in lista:
            cur.execute(sql_query, (id, ))

        # Confirmar la transacción
        conn.commit()

    except sqlite3.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

if __name__ == '__main__':
    # Ejemplo de uso
    lista = [2, 5]
    delete_list(lista)
