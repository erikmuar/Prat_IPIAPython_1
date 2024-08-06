import sqlite3

def update_list(saldo=0):
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect('<nombre_de_db>.sqlite')
        cur = conn.cursor()

        # Leer el archivo SQL
        with open('updateBulk.sql', 'r') as sql_file:
            sql_query = sql_file.read()

        # Ejecutar la consulta
        cur.execute(sql_query, (saldo, ))

        # Confirmar la transacción
        conn.commit()

    except sqlite3.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

if __name__ == '__main__':
    # Ejemplo de uso
    update_list(saldo=100)
