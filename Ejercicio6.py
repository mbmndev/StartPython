#Crea un programa en Python que convierta grados Celsius a Fahrenheit.

def main():
    try:
        cels = float(input("Introduzca los grados celsius: "))
        fahr= (cels*1.8) + 32
        print(f"{cels} grados celsius son {fahr} grados fahrenheit")
        
    except:
        print("Error, introduce un dato correcto")