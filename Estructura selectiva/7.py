<<<<<<< HEAD
# Solicita al usuario que ingrese la cantidad de llantas compradas y lo convierte a un entero
numeroLlantas = int(input("¿Cuántas llantas compró? "))

# Evalúa la cantidad de llantas para determinar el valor unitario de cada llanta
if numeroLlantas < 5:
    # Si la cantidad de llantas es menor a 5, el valor unitario de cada llanta es 300,000
    valorLlantas = 300000
elif numeroLlantas >= 5 & numeroLlantas == 10:
    # Si la cantidad de llantas está en el rango de 5 a 10 inclusive, el valor unitario de cada llanta es 250,000
    valorLlantas = 250000
else:
    # Si la cantidad de llantas es mayor a 10, el valor unitario de cada llanta es 200,000
    valorLlantas = 200000

# Calcula el valor total de las llantas y lo imprime
print(f"El valor de las llantas es de {valorLlantas * numeroLlantas}")

=======
# Solicita al usuario que ingrese la cantidad de llantas compradas y lo convierte a un entero
numeroLlantas = int(input("¿Cuántas llantas compró? "))

# Evalúa la cantidad de llantas para determinar el valor unitario de cada llanta
if numeroLlantas < 5:
    # Si la cantidad de llantas es menor a 5, el valor unitario de cada llanta es 300,000
    valorLlantas = 300000
elif numeroLlantas >= 5 & numeroLlantas == 10:
    # Si la cantidad de llantas está en el rango de 5 a 10 inclusive, el valor unitario de cada llanta es 250,000
    valorLlantas = 250000
else:
    # Si la cantidad de llantas es mayor a 10, el valor unitario de cada llanta es 200,000
    valorLlantas = 200000

# Calcula el valor total de las llantas y lo imprime
print(f"El valor de las llantas es de {valorLlantas * numeroLlantas}")

>>>>>>> e202adae2eba232c5ee50d165221f050486cdf8d
