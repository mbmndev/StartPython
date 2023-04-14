#Crea un algoritmo que determine si un número es capicúa o no.

def main():
    print("Introduzca un número entero:")
    num = input()
    i = 0
    while i < len(num):
        if num[i]==num[-i-1]:
            i += 1
            continue
        else:
            print("El número no es capicúa")
            break
    if i == len(num):
        print("El número es capicúa")