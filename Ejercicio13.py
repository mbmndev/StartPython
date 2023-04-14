# Crea un algoritmo que calcule el área y volumen de un cubo dado su lado.

def main():
    print("Introduzca el lado del cubo en metros:")
    lado = input()
    lado = int(lado)
    area = lado * lado * 6
    volumen = lado * lado * lado
    print("El área del cubo es de", area, "metros cuadrados")
    print("El volumen del cubo es de", volumen, "metros cúbicos")