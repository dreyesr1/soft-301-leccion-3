# Condicional simple
# if predicado o condicion:
#       sentencias

# Condicional doble
# if condicion:
#       sentencias
# else
#       sentencias

# Condiocional compuesta
# if condicion:
#       sentencias
# elif:
#       sentencias
# else:
#       sentencias

n = 3

if n % 2 == 0:
    print("n es divisible entre 2")
elif n % 3 == 0:
    print("n es divisible entre 3")
else:
    print("n no es divisible ni entre 2 ni entre 3")


#           BUSCADOR DE LLAVES
# dormitorio, cocina o cualquier otro lugar
    
habitacion = "dormitorio"

if habitacion == "dormitorio":
    print("Las llaves estan en el dormitorio")
elif habitacion == "cocina":
    print("Las llaves estan en la cocina")
elif habitacion == "sala":
    print("Las llaves estan en la sala")
elif habitacion == "cochera":
    print("LLas llaves estan en la cochera")
else:
    print("Las llaves estan en cualquier otro lugar")