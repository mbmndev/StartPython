# Dado un número entero, crea un algoritmo que determine si es primo o no.

def main():
    print("Introduce un número entero:")
    numero = input()
    numero = int(numero)
    i = numero - 1
    while i>1:
        if numero % i != 0:
            i-=1
            if i == 1:
                print("El número entero introducido es primo")
            continue
        else:
            print("El número entero introducido no es primo")
            break