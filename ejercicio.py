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

coche = Coche("azul", 4, 150, 1200)
print(coche)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga= carga
    def __str__(self):
        return super().__str__() + ", {} kg de carga".format(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo= tipo
    def __str__(self):
        return super().__str__() + ", {}".format(self.tipo)

class Motocicleta(Bicicleta):
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
lista =[
    Coche("azul", 4, 150, 1200),
    Camioneta("roja", 4, 240, 1300, 2000),
    Bicicleta("rosa", 2, "montaña"),
    Motocicleta("negra", 2, "ciudad", 120, 800)
]

catalogar(lista)
catalogar(lista, 0)
catalogar(lista, 2)
catalogar(lista, 4)





