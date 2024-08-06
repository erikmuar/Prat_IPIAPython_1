import sqlite3

def insert_list(lista):
    try:
        # Conectar a la base de datos
        conn = sqlite3.connect('<nombre_de_db>.sqlite')
        cur = conn.cursor()

        # Leer el archivo SQL
        with open('insertBulk.sql', 'r') as sql_file:
            sql_query = sql_file.read()

        # Ejecutar la consulta para cada elemento de la lista:
        for elemento in lista:
            usuario, nombre, sexo, nivel, email, telefono, marca, compañia, saldo, activo = elemento
            cur.execute(sql_query, (usuario, nombre, sexo, nivel, email, telefono, marca, compañia, saldo, activo))

        # Confirmar la transacción
        conn.commit()

    except sqlite3.Error as e:
        print(f"Error al ejecutar la consulta: {e}")
    finally:
        # Cerrar la conexión
        conn.close()

if __name__ == '__main__':
    # Ejemplo de uso
    lista = [
        ('p3p3', 'Pepe', 'H', '3', 'pepe@rana.frog', '123', 'PEPE', 'Le Pepe 1', 0, 1),
        ('p3pu', 'Pepu', 'H', '3', 'pepu@rana.frog', '123', 'PEPU', 'Le Pepe 2', 0, 1)
    ]
    insert_list(lista)
