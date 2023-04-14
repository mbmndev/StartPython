#Calcular el salario de un empleado

def main():
    opcion = "si"

    while opcion == "si":
        salarioBase = int(input("Introduce tu salario base: "))
        horasTrabajadas = int(input("Introduce las horas trabajadas: "))
        percentajeSSocial = int(input("Introduce el percentaje de la seguridad social: "))
        percentajeImpuestos = int(input("Introduce el percentaje de la impuestos: "))

        sueldoBruto = salarioBase * horasTrabajadas
        descuentoSS = (sueldoBruto * percentajeSSocial) / 100
        descuentoIm = (sueldoBruto * percentajeImpuestos) / 100
        sueldoNeto = sueldoBruto - descuentoIm - descuentoSS
        print(f"Tu sueldo neto es: {sueldoNeto: .2f}")

        choose = input("Quieres calcular otro sueldo 'si' o 'no' ?: ")

        opcion = choose.lower()
        