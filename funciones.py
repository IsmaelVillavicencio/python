"""
Nombre: Funciones.py
Objetivo: Muestra el formato de las funciones en Python
Autor: Alejandro Ortiz Figueroa
Fecha: 09/11/2019
"""
#Función para imprimir un mensaje
def printMensaje():
    print("Hola soy una función sin parámetros")

def printMensajedos():
    return "Soy la función que regresa una cadena"

#Función que recibe un mensaje y lo imprime
def printMensajetres(cad):
    print("Mensaje Recibido: ",cad)
#Función main
def main():
    printMensaje()
    print("EL mensaje es: ",printMensajedos())
    printMensajetres("Hola")

if __name__=="__main__":
    main()