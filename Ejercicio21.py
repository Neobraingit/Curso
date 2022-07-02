# Crear el diccionario frutas
# Grabar esta estructura de datos en un fichero binario 
# Comprobar que sigue siendo un diccinonario con .values()

import pickle

dic = {'manzana' : 'manzano', 'pera' : 'peral', 'naranja' : 'naranjo'}
binario = open('Fichero.pckl', 'wb')
pickle.dump(dic, binario)
binario.close()

 