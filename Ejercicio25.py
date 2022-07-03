# Conectar labase de datos y crear una tabla

import sqlite3

conexion = sqlite3.connect('Biblioteca.db')
cursor = conexion.cursor()
cursor.execute("CREATE TABLE Libros (Título TEXT, Autor TEXT, Editorial TEXTO)")
conexion.commit()
conexion.close()