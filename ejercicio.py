class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.ruedas)
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return Vehiculo.__str__(self) + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

coche = Coche("azul", 150, 4, 1200)
print(coche)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga= carga
    def __str__(self):
        return super().__str__() + ", {} kg de carga".format(self.carga)

class Bicicleta(Coche):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo= tipo
    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)

class Motocicleta(Coche):
    def __init__(self, color, ruedas, tipo, velocidad, cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada= cilindrada
    def __str__(self):
        return super().__str__() + ", {} km/h, {} cc".format(self.velocidad, self.cilindrada)

def catalogar(vehiculos):
    for vehiculo in vehiculos:
        print(type(vehiculo).__name__, vehiculo)
def catalogar(vehiculos, ruedas=None):
    if ruedas !=None:
        contador= 0
        for vehiculo in vehiculos: 
            if vehiculo.ruedas == ruedas:
                contador += 1
        print("\ Se han encontrado {} vehículos con {} ruedas: ".format(contador,ruedas))
    
    for vehiculo in vehiculos: 
        if ruedas == None:
            print(type(vehiculo).__name__, vehiculo)
        else: 
            if vehiculo.ruedas == ruedas:
                print(type(vehiculo).__name__, vehiculo) 





