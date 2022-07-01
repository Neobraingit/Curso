class Coche():
    def __init__(self, color, marca):
        self.color = color
        self.marca = marca
        
    def caracteristicas(self):
        print ('Este coche es de la marca {} y del color {}'.format(self.color, self.marca))
        
coche1 = Coche('Seat', 'Amarillo')
    

        
    