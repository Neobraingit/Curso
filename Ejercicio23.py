# Crear una función buscar que mediante una expresion regular indique si una palabra está ebn una frase
import re
def buscar(palabra, texto):
    resultado = re.search(palabra,texto)
    return resultado

texto = ' Esto es una frase de pruebas'
palabra = 'frase'

resultado = buscar(palabra, texto)
resultado
    