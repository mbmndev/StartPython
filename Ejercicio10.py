#Dada una lista de nombres, crea un programa en Python que ordene la lista alfabéticamente.

def main():
    getInputUser = ""
    listaName = []

    def startProgram(getInputUser):
        
        while getInputUser == "":
            getInputUser = input("Introduce nombres: ")
            listaName.append(getInputUser)
            finish=input("¿Desea finalizar el programa? s/n: ")
            if finish== "s":
                listaName.sort()
                print(listaName)
            else:
                getInputUser = ""

    startProgram(getInputUser)