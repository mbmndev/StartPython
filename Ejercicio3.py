#3. Determinar la ruta para llegar a una ciudad por avión. [Con base de datos]
def main():
    origen = ("Madrid", "Washington", "Hong Kong")
    destinosMadrid = ("Lisboa", "Berlin", "Quito", "Lima", "Oslo", "París", "Moscú")
    destinosLima = ("Buenos Aires")
    destinosWashington = ("Bangkok", "Miami", "Los Ángeles")
    destinosHongKong = ("Bangkok", "Tokyo", "Seúl", "Calcuta")
    x = 1
    while x == 1:
        print("Introduzca la ciudad de origen:")
        ciudadOrigen = input()
        if ciudadOrigen in origen:
            x = 0
        else:
            continue
    x = 1
    if ciudadOrigen == "Madrid":
        print("Introduzca la ciudad de destino:")
        ciudadDestino = input()
        if ciudadDestino == "Buenos Aires":
            ciudadEscala = "Lima"
            print("El vuelo tendrá una escala. Volará de", ciudadOrigen,"a", ciudadEscala,". Posteriormente, volará de", ciudadEscala, "a", ciudadDestino, ".")
        elif ciudadDestino in destinosWashington:
            ciudadEscala = "Washington"
            print("El vuelo tendrá una escala. Volará de", ciudadOrigen,"a", ciudadEscala,". Posteriormente, volará de", ciudadEscala, "a", ciudadDestino, ".")
        elif ciudadDestino in destinosHongKong:
            ciudadEscala = "Hong Kong"
            print("El vuelo tendrá una escala. Volará de", ciudadOrigen,"a", ciudadEscala,". Posteriormente, volará de", ciudadEscala, "a", ciudadDestino, ".")
        elif ciudadDestino in destinosMadrid:
            print("El vuelo será directo. Volará de", ciudadOrigen, "a", ciudadDestino,".")
        else:
            print("La ruta seleccionada no existe.")
    if ciudadOrigen == "Washington":
        print("Introduzca la ciudad de destino:")
        ciudadDestino = input()
        if ciudadDestino in destinosWashington:
            print("El vuelo será directo. Volará de", ciudadOrigen, "a", ciudadDestino,".")
        else:
            print("La ruta seleccionada no existe.")
    if ciudadOrigen == "Hong Kong":
        print("Introduzca la ciudad de destino:")
        ciudadDestino = input()
        if ciudadDestino in destinosHongKong:
            print("El vuelo será directo. Volará de", ciudadOrigen, "a", ciudadDestino,".")
        else:
            print("La ruta seleccionada no existe.")