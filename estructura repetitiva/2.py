# Inicializa el acumulador para la suma de números negativos (convertidos a positivos)
numNegativo = 0

# Inicia un bucle que se repetirá 10 veces
for i in range(0, 10):
    # Solicita al usuario que ingrese un número negativo
    numeros = int(input("Ingrese un numero negativo: "))
    
    # Verifica si el número ingresado es negativo
    if numeros < 0:
        # Si es negativo, se convierte a positivo (multiplicando por -1) y se suma al acumulador
        numNegativo += numeros * -1
    else:
        # Si el número no es negativo, se muestra un mensaje indicando que se deben ingresar números negativos
        print('Escribe numeros negativos')
    
# Imprime la suma total de todos los números negativos convertidos a positivos
print(f'La suma de todos los numeros es {numNegativo}')


        