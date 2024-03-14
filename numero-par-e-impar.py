# Numero par o impar

A = int(input("Ingrese un numero: "))

R = A % 2

if R == 0:
    print("El numero ( ",R," ) es par")
else:
    print("El numero ( ",R," ) es impar")
