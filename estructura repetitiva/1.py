# Inicializa contadores para números positivos, negativos y neutros
positivos = 0
negativos = 0
neutro = 0

# Inicia un bucle que se repetirá 4 veces (para 4 entradas de usuario)
for i in range(0, 4):
    # Solicita al usuario que ingrese un número (puede ser positivo, negativo o neutro)
    numeros = int(input("Digite numero negativo, positivo o neutro: "))
    
    # Verifica si el número es mayor que 1 (se considera positivo)
    if numeros > 1:
        positivos += 1
    # Verifica si el número es menor que 0 (se considera negativo)
    elif numeros < 0:
        negativos += 1
    # Si el número es 0 o 1, se considera neutro
    elif numeros == 0 or numeros == 1:
        neutro += 1

# Imprime el conteo de números positivos, negativos y neutros
print(f"Esta es la cantidad de positivos {positivos} \nEsta es la cantidad de negativos {negativos} \nEsta es la cantidad de neutros {neutro}")

    
