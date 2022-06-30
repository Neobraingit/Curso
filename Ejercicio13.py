# Crear una variable  "diccionario"  con los pares siguientes
# Clave = uno  valor = one y así hasta tres
# Mostrar el valor de diccionario
# Añadir un nuevo elemento "cuatro" al diccionario
# Mostrar el valor de diccionario
# Recoger un input y alamacenarlo en dato
# Utilizar dato como clave para recuperar su valor

dic = {'uno' : 'one', 'dos' : 'two', 'tres' : 'three'}
print (dic)
dic['cuatro'] = 'four'
print (dic)
dato = input('Introduce una clave: ')
valor = dic.get(dato)
print (valor)


