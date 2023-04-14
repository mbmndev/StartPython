#Dada una lista de números enteros, determina cuál es el mayor y cuál es el menor.

def main():
    num1 = input("Escribe el 1 numero: ")
    num2 = input("Escribe el 2 numero: ")
    num3 = input("Escribe el 3 numero: ")
    num4 = input("Escribe el 4 numero: ")
    num5 = input("Escribe el 5 numero: ")

    arrayNum = [num1, num2, num3, num4, num5]

    condicion = False

    while condicion == False:
        for i in range(5):
            if arrayNum[i].isdigit():
                arrayNum[i] = int(arrayNum[i])
            else:
                arrayNum[i] = input(str(arrayNum[i]) + " no es un numero. Escribe un numero correcto: ")
        condicion = True
    numeroMayor = arrayNum[0]
    numeroMenor = arrayNum[0]
    print("Los numeros son: " + str(arrayNum))

    for i in range(len(arrayNum)):
        if numeroMayor <= arrayNum[i]:
            numeroMayor = arrayNum[i]

    print("El numero más grande de la lista es:  " + str(numeroMayor))

    for i in range(len(arrayNum)):
        if numeroMenor >= arrayNum[i]:
            numeroMenor = arrayNum[i]

    print("El numero más pequeño de la lista es:  " + str(numeroMenor))
    