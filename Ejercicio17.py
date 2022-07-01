# Crea una clase coche con estos atributos: marca, color, combustible
# Crea la funcion __init__ que defina los parámetros de la clase a los atributow
# Crear otra función "mostrar_características" que mediante print muestre los atributos del coche
# Crear un objeto de la clase coche con los atributos  "Opel", "rojo", "gasolina"
# Ejecutar la función "mostrar características" del objeto 

class Coche():
    def __init__(self, marca, color, combustible):
        self.marca = marca
        self.color = color
        self.combustible = combustible



    def caracteristicas(self):
       print ('ESte coche es de la marca {} de color {} y de {}'.format(self.marca, self.color, self.combustible))
       
       
coche1 = Coche('Opel', 'Rojo', 'Gasoil')
print (coche1.marca)
coche1.caracteristicas()
    
    

        