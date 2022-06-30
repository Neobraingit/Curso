# Crear una variable llamada "cadena" que contenga el siguiente texto: "Esto es un texto de ejemplo"
# Crear una variable longitud que nos muestre la longitud de la variable "cadena"
# Crear una variable "strLongitud" que contenga el valor de longitud pero convertido a string
# Crear una variable "mayúsculas" que contenga cadena toda en mayúsculas
# Crear una variable resultado que concatene "mayúsculas" con el texto " tiene longitud de " y "strLongitud"

cadena = 'Esto es un texto de prueba'
print (len(cadena))
longitud = len(cadena)
strLongitud = str(longitud)
print (strLongitud)
mayusculas = cadena.upper()
print (mayusculas)
resultado = mayusculas + ' tiene longitud de ' + strLongitud
print (resultado)