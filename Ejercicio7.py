#Dado un número entero, crea un programa en Python que determine si es par o impar.

def main():
    num = input("Introduce un numero: ")
    condicion = False
    par = True

    while condicion == False:
        if num.isdigit():
            num = int(num)
            condicion = True
            if num % 2 == 0:
                par = True
            else:
                par = False
        else:
            num = input("Introduce un numero correcto: ")

    print("El numero es par", par)