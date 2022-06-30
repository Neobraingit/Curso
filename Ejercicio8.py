# Crear una variable mínimo con el valor 20
# Crear una variable máximo con el valor 500
# Recoge un input y almacénalo en la variable dato
# Convierte dato en un número y almacénalo en la variable numero
# Si el número es menor que el valor de mínimo  mostrar el texto "Valor bajo"
# Si el número es mayor que el valor máximo mostrar el texto "valor alto"
# Si el número está entrem el valor mínimo y máximo mostrar "valor medio"

minimo = 20
maximo = 500
dato = input('Introduce un número: ')
numero = int(dato)
if numero <= minimo:
    print ('Valor bajo')
elif numero >= maximo:
    print ('Valor alto')
else:
    numero > minimo and  numero < maximo
    print ('Valor medio')