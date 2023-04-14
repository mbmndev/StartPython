#Crea un programa en Python que determine si una cadena de texto es un palíndromo o no.

def main():
    palabra = input("Escribe una palabra de minimo 2 letras: ")
    condicion = False
    palindroma = False

    while condicion == False:
        if not palabra.isdigit() and len(palabra) > 1:
            condicion = True
        else:
            palabra = input("Escribe una palabra de minimo 2 letras: ")


    for i  in range(len(palabra)):
        if palabra[i] == palabra[-i-1]:
            palindroma = True
        else:
            palindroma = False
            exit

    if palindroma == True:
        print("Tu palabra es palindroma")
    else:
        print("Tu palabra no es palindroma")
        