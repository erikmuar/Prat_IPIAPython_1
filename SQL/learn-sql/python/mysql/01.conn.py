# pip install mysql-connector-python

import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        # Establece la conexión con MySQL
        connection = mysql.connector.connect(
            host='localhost',
            port=3306,
            database='<nombre_de_db>',
            user='<usuario_de_db>',
            password='<password_supersafe>'
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Conectado a MySQL Server versión {db_info}")
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print(f"Conectado a la base de datos: {record}")

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Conexión a MySQL cerrada")

if __name__ == "__main__":
    connect_to_mysql()
