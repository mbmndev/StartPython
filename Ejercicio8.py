#Crea un programa en Python que determine si un año es bisiesto o no.

def main():
    año = int(input("Introduce el año para saber si es bisiesto o no: "))

    if (año% 4 == 0) and (año%100 != 0):
        resultado = f"El año {año} es bisiesto"
    elif año%400 == 0:
        resultado = f"El año {año} es bisiesto"
    else:
        resultado = f"El año {año} no es bisiesto"

    print(resultado)