#Calcula el área y perímetro de un círculo dado su radio.

def main():
    import math

    radio = float(input("Introduce el radio del circulo: "))
    area= radio ** 2 * math.pi
    perimetro = radio * 2 * math.pi

    print(f"El area del circulo es {area} y el perimetro es {perimetro}")
    