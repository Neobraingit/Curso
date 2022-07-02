import os
archivo = open('Listado.txt', 'w')
archivo.write('Esto es una linea\n')
archivo.write('Esto es otra linea...')
archivo.close()

archivo = open('Listado.txt', 'r')
print (archivo.read())