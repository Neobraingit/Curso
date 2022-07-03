# Insertar varias lineas

import sqlite3

conexion = sqlite3.connect("biblioteca.db")
cursor = conexion.cursor()
lista_personas = [('Pedro', 'Carmona', 'Perez'),
                  ('Maria', 'Lopez', 'Gómez')
                  ]
cursor.executemany("INSERT INTO LIBROS VALUES(?,?,?)", lista_personas)
conexion.commit()
conexion.close()