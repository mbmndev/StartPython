#Crea un algoritmo que determine si un número es positivo, negativo o cero.

def main():
    print("Introduzca un número:")
    numero = input()
    numero = float(numero)
    if numero > 0:
        print("El número es positivo")
    elif numero < 0:
        print("El número es negativo")
    else:
        print("El número es cero")