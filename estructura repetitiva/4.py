# Solicita al usuario que ingrese un número entero. El valor ingresado se convierte a entero usando int() y se guarda en la variable 'multiplicando'.
multiplicando = int(input('Digite el numero que desea multiplicar: '))

# Imprime un mensaje que indica cuál es la tabla de multiplicar que se va a mostrar
print(f'Tabla de multiplicar del {multiplicando}')

# Inicia un bucle que va a iterar desde 0 hasta 10 (inclusive). La función range(0,11) genera una secuencia de números del 0 al 10.
for i in range(0, 11):
    # Calcula el producto del número ingresado por el usuario ('multiplicando') y el valor actual del iterador 'i'.
    producto = multiplicando * i
    
    # Imprime el resultado de la multiplicación en el formato 'multiplicando x i = producto'
    print(f'{multiplicando} x {i} = {producto}')