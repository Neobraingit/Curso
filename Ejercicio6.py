# Imprimir por pantalla el texto "Introoduce el primer número"
# Crear la variable dato1 con el valor que introduzca el usuario
# Imprimir por pantalla "Introduce el segundo número"
# Crear la variable dato2 con el valor que introduzca el ususario
# Convertir la variable dato1  en una variable numérica llamada numero1
# Crear la variable suma y sumar los datos anteriores
# Crear una variable resultado concatenando el texto " la suma es " y suma
# Imprimir el valor de resultado

print ('Introduce el primer número: ')
dato1 = input()
print ('Introduce el segundo número: ')
dato2 = input()

numero1 = int(dato1)
numero2 = int(dato2)
suma = numero1 + numero2
print (suma)
resultado = suma
print ('El resultado es: {}'.format(resultado))