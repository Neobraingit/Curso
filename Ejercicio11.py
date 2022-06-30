# Crear una variable que se va a llamar tupla de los siguiente nombres: Antonio, Pedro y María
# Mostrar el valor de la variable tupla
# Recoger un input y almacenarlo en dato
# Si el valor de dato está dentro de tupla mostrar si
# Si el valor de dato no está dentro de tupla mostrar no

tupla = ('Antonio', 'Pedro', 'María')
dato = input('Introduce un nombre: ')
if dato in tupla:
    print ('Si')
else:
    print ('No')
