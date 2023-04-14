#Dada una lista de números enteros, crea un algoritmo que calcule la suma de todos los números pares de la lista.

def main():
    numero = "a"
    suma = 0
    while len(numero)>0:
        print("Introduzca un nuevo número entero:")
        numero = input()
        if len(numero) > 0 and int(numero) % 2 == 0:
            suma += int(numero)
    print("La suma de los numeros pares es de", suma)