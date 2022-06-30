# Crear una variable "números" con la lista de los números del 1 al 10 
# Mostrar el valor de la variable números
# Recoger un input y almacenarlo en la variable dato
# Convertir dato en número y alamacenarlo en la variable números
# Si el valor de numero está en la lista mostrar si
# Si no está en la lista mostrar no

numeros = [1,2,3,4,5,6,7,8,9,10]
print (numeros)
dato = input('Introduce un número: ')
numero = int(dato)

if numero  in numeros:
    print('Si')
else:
    print ('No')