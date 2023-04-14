#Crea un programa en Python que calcule el factorial de un número entero.

def main():
    print("Introduzca un número entero:")
    numero = input()
    numero = int(numero)
    cont = 1
    factorial=1
    while cont <=numero:
        factorial *=  cont
        cont += 1
    print("El factorial de", numero, "es", factorial)
