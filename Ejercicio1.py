#Calcular la letra del DNI Español
def main():
    dni = input("Introduce  los 8 números del DNI: ")
    tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
    valido = False

    while valido == False:
        if dni.isdigit() and len(dni) == 8 :
            dni = int(dni)
            resto = dni % 23
            valido = True
        else :
            dni = input("Introduce un número correcto: ")

    for i in range(len(tabla)) :
        if resto == i:
            resultado = tabla[i]

    print("Tu DNI es: " + str(dni) + str(resultado))