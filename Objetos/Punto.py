"""
Nombre: Punto.py
Descripcion: Es la superclase en la jerarquia de herencia
Fecha: 14/11/2019
"""
class Punto(object):
    #metodo constructor
    def __init__(self, valorX, valorY):
        #Cuerpo del constructor
        self.x = valorX
        self.y = valorY

    #lista de metodos get
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    #lista de metodos set
    def setX(self, valorX):
        self.x = valorX

    def setY(self, valorY):
        self.y = valorY

    #metodo ToString
    def toString(self):
        return "LAs coordenadas del punto son: ",str(self.x),",",str(self.y)
