# Inicializamos la variable multiplicacion en 1. Esta variable se usará para acumular el producto.
multiplicacion = 1

# Bucle que itera sobre los números del 1 al 20 (inclusive)
for i in range(1, 21):  # range(1, 21) genera números del 1 al 20
    multiplicacion *= i  # Multiplica la variable multiplicacion por el valor actual de i

# Imprime el resultado final
print(f'La multiplicacion de los 20 primeros numeros naturales es {multiplicacion}')
