#Dada una lista de números enteros, crea un algoritmo que calcule la media de la lista.

def main():
    num = "a"
    suma = 0
    i = 0
    media = 0
    while len(num)>0:
        print("Introduzca un nuevo número entero:")
        num = input()
        if len(num)>0:
            suma += int(num)
            i+=1
    media = suma / i
    print("La media de los números enteros introducidos es ", media)