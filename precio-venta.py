# Ejercicio 1

PV = float(input("Ingrese el precio de venta: "))
OPCION = input("Ingrese 'N' para nacional o 'E' para extranjero: ")

if OPCION == "N":
    TOTAL = PV + (PV * .08)
else:
    TOTAL = PV + (PV * .18)

print("El total es: " + str(TOTAL))