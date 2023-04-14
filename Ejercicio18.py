#Crea un algoritmo que determine si una cadena de texto es un anagrama de otra cadena de texto.

def main():
    print("Introduce una primera cadena de texto:")
    cadena1 = input()
    print("Introduce una segunda cadena de texto:")
    cadena2 = input()
    lista1 = list()
    lista2 = list()
    for letra in cadena1:
        lista1.append(letra)
    for letra in cadena2:
        lista2.append(letra)
    lista1.sort()
    lista2.sort()
    if lista1 == lista2:
        print("Las cadenas de texto son anagramas")
    else:
        print("Las cadenas de texto no son anagramas")