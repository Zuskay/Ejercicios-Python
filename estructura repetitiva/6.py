# Solicita al usuario que ingrese el número total de personas en el salón de clases.
nPersonas = int(input("Ingrese el numero de personas de un salon de clases: "))

# Inicializa contadores para el número de hombres y mujeres.
hombres = 0
mujeres = 0

# Inicia un bucle que se repetirá 'nPersonas' veces, donde cada iteración corresponde a una persona.
for i in range(nPersonas):
    # Solicita al usuario que ingrese el género de la persona actual ('H' para hombre o 'M' para mujer).
    genero = input(f'Ingrese el genero de la persona {i+1} (H/M): ')
    
    # Convierte la entrada del género a mayúsculas para asegurar la consistencia en la comparación.
    if genero.upper() == 'H':
        # Si el género es 'H', se incrementa el contador de hombres.
        hombres += 1
    elif genero.upper() == 'M':
        # Si el género es 'M', se incrementa el contador de mujeres.
        mujeres += 1
    else:
        # Opcional: Se puede manejar la entrada no válida si se desea (por ejemplo, mostrar un mensaje de error).
        print('Género no reconocido. Por favor ingrese H o M.')

# Imprime el total de hombres contados.
print(f'Total de hombres: {hombres}')
# Imprime el total de mujeres contadas.
print(f'Total de mujeres: {mujeres}')
# Imprime el total de personas, que es el mismo valor ingresado al principio.
print(f'Total de personas es: {nPersonas}')
