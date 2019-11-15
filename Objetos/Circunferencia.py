"""
Nombre: Circunferencia.py
Descripcion: Es la superclase en la jerarquia de herencia
Fecha: 14/11/2019
"""
import math
from Punto import Punto
class Circunferencia(Punto):
    def __init__(self, vradio, valorX, valorY):
        #Creamos atributos de la clase Circunferencia
        self.radio = vradio
        #invocar al constructor de la superclase
        Punto.__init__(self, valorX, valorY)
    #Lista de metodos get
    def getRadio(self):
        return self.radio
    #Lista de metodos Set
    def setRadio(self, vradio):
        self.radio = vradio
    def getArea(self):
        return math.pi * math.pow(self.radio,2)

    #Metodo toString
    def toString(self):
        return "La Circunferencia tiene como centro : ",srt(self.getX()),",",srt(self.getY())," y radio igual a: ",str(self.radio)
