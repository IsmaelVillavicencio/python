"""
Nombre: Operaciones.py
Objetivo: Muestra operaciones selectivas, repetitivas y aritmeticas
Autor: Alejandro Ortiz Figueroa
Fecha: 09/11/2019
"""

def suma(num1,num2):
    res = num1+num2
    return res

def resta(num1,num2):
    res = num1-num2
    return res

def multiplicar(num1,num2):
    res = num1*num2
    return res

def dividir(num1,num2):
    res =num1/num2
    return res

def compare(num1,num2):
    if(num1>num2):
        print("Número uno es el mayor: ",num1,",",num2)
    elif(num2>num1):
        print("Número dos el mayor: ",num1,",",num2)
    else:
        print("Los números son iguales: ",num1,",",num2)

#Funcion para contar de un entero a hasta otro
def contar(num1,num2):
    if(num2>num1):
        #Contar de manera ascendente
        for i in range(num1,num2+1,1):
            print(i)
    elif(num1>num2):
        for i in range(num1,num2-1,-1):
            print(i)
    else:
        print("NO HAY NADA QUE CONTAR")


def main():

    ciclo = "S"
    while ciclo =="S" or ciclo == "s":
        print("---Operaciones Básicas")
        n1=int(input("Introduce el primer número"))
        n2=int(input("Introduce el segundo número"))
        print("La suma es: "+str(suma(n1,n2)))
        print("la resta es: "+str(resta(n1,n2)))
        print("La multiplicación "+str(multiplicar(n1,n2)))
        print("La división: "+str(dividir(n1,n2)))
        compare(n1,n2)
        contar(n1,n2)
        #Preguntar si desea continuar
        ciclo = input("¿Otra operacion(S/N)?")
    else:"*** Fin de programa"

if __name__ == '__main__':
    main()