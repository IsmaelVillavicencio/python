from Circunferencia import  Circunferencia
class Cilindro(Circunferencia):
    def __init__(self, vX, vY, vradio, valtura):
        #Creamos el atributo de Cilindro
        self.altura = valtura
        #Contruir el Objeto Circunferencia
        Circunferencia.__init__(self, vradio, vX,vY)
    #Lista de metodos GET
    def getAltura(self):
        return self.altura
    #Lista de metodos SET
    def setAltura(self, valtura):
        self.altura = valtura
    #Metodo para calcular el volumen
    def getVolumen(self):
        return Circunferencia.getArea(self) * self.altura
    #Metodo toString
    def toString(arg):
        return "El Cilindro tiene como coordenadas: ",Circunferencia.toString, " y la altura: ", self.altura
