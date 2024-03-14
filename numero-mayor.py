# Pedir dos números
# A y B
# un solo "=" es asignación

A = int(input("ingrese el numero 01: "))
B = int(input("ingrese el numero 02: "))

if A > B:
    M = A
else:
    M = B

print("El mayor es:" + str(M))