#Crea un algoritmo que genere un número aleatorio entre 1 y 100, y le pida al usuario adivinarlo. El algoritmo deberá indicar si el número introducido es mayor o menor que el número aleatorio, hasta que el usuario adivine el número correcto.

def main():
    import random
    x = 0
    nalea = random.randint(1,100)
    print("Inroduce un nuevo número entero entre el 1 y el 100")
    numero = input()
    numero = int(numero)
    while x == 0:
        if numero > nalea:
            print("El número introducido es mayor")
            print("Inroduce un nuevo número entero entre el 1 y el 100")
            numero = input()
            numero = int(numero)
        elif numero < nalea:
            print("El número introducido es menor")
            print("Inroduce un nuevo número entero entre el 1 y el 100")
            numero = input()
            numero = int(numero)
        else:
            x = 1
            print("¡Felicidades!, Has acertado el número")